# Import necessary modules for environment variables, async operations, and Telegram handling
import os
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from motor.motor_asyncio import AsyncIOMotorClient

# Fetch credentials from environment variables set in Koyeb/Render
API_ID = int(os.environ.get("API_ID", 0))
API_HASH = os.environ.get("API_HASH", "")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
MONGO_URI = os.environ.get("MONGO_URI", "")

# Initialize Pyrogram client and MongoDB client
app = Client("MultiUserFileBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
db_client = AsyncIOMotorClient(MONGO_URI)
db = db_client["multi_user_file_bot"]
settings_col = db["group_settings"]
files_col = db["files"]

# Handle /start command in private chat with inline buttons and instructions
@app.on_message(filters.command("start") & filters.private)
async def start_handler(client, message: Message):
    bot_info = await client.get_me()
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("➕ Add Me To Your Group", url=f"http://t.me/{bot_info.username}?startgroup=true")],
        [InlineKeyboardButton("⚙️ Help & Commands", callback_data="help_callback")]
    ])
    await message.reply_text(
        "👋 **Welcome to File Checker & Auto-Uploader Bot!**\n\n"
        "Main aapke public group aur private channel ko manage karne me madad karta hoon. "
        "Jab koi user group me file name ya year bhejega, toh bot check karega ki file database me hai ya nahi!\n\n"
        "**Quick Setup Steps:**\n"
        "1️⃣ Mujhe apne **Public Group** me add karein aur Admin banayein.\n"
        "2️⃣ Group me command dalein: `/setchannel -100xxxxxxxxxx` (Aapka Private Channel ID).\n"
        "3️⃣ Bot ready ho jayega!",
        reply_markup=keyboard
    )

# Handle /setchannel command in groups to link a private channel to that specific public group
@app.on_message(filters.command("setchannel") & filters.group)
async def set_channel(client, message: Message):
    chat_id = message.chat.id
    try:
        user = await client.get_chat_member(chat_id, message.from_user.id)
        if user.status not in ["administrator", "creator"]:
            return await message.reply_text("❌ Sirf Group Admins hi channel set kar sakte hain!")
    except Exception:
        pass
    
    args = message.text.split(" ")
    if len(args) < 2:
        return await message.reply_text("❌ Sahi format use karein:\n`/setchannel -100xxxxxxxxxx`")
    
    try:
        channel_id = int(args[1])
    except ValueError:
        return await message.reply_text("❌ Channel ID numeric honi chahiye (e.g., `-1001234567890`)!")

    # Update or insert group configuration into MongoDB
    await settings_col.update_one(
        {"group_id": chat_id},
        {"$set": {"channel_id": channel_id}},
        upsert=True
    )
    await message.reply_text(f"✅ **Success!** Private Channel ID successfully set ho gayi hai:\n`{channel_id}`")

# Listen to incoming messages in public groups and check the database for files
@app.on_message(filters.group & (filters.document | filters.video | filters.text))
async def check_files(client, message: Message):
    group_id = message.chat.id
    settings = await settings_col.find_one({"group_id": group_id})
    if not settings or "channel_id" not in settings:
        return

    query = message.text or message.caption
    if not query:
        return

    # Check if the file exists in the database for the configured channel
    existing = await files_col.find_one({"channel_id": settings["channel_id"], "name": {"$regex": query, "$options": "i"}})

    if existing:
        await message.reply_text(f"✅ **File Already Uploaded!**\n\n🔗 **Link:** {existing['link']}")
    else:
        await message.reply_text("⏳ **File available nahi hai, database me upload ho rahi hai...**")

app.run()

