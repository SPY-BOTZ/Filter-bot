import os
from pyrogram import Client, filters

# Environment variables se credentials lein
API_ID = int(os.environ.get("API_ID", "0"))
API_HASH = os.environ.get("API_HASH", "")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

bot = Client(
    "filter_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@bot.on_message(filters.command("start"))
async def start_command(client, message):
    await message.reply_text("👋 Hello! Bot is successfully running.")

if __name__ == "__main__":
    print("Bot started successfully...")
    bot.run()
    
