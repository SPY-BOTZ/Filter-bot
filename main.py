import os
import asyncio
import threading
from flask import Flask
from pyrogram import Client, filters

# --- Flask Web Server (Koyeb Health Check ke liye) ---
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is alive and running!", 200

def run_flask():
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port, use_reloader=False)

# --- Pyrogram Telegram Bot Setup ---
API_ID = int(os.environ.get("API_ID", "0"))  # Apni API_ID environment variable se lein
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
    await message.reply_text("👋 Hello! Bot is successfully running and connected.")

@bot.on_message(filters.text & ~filters.command)
async def handle_text(client, message):
    pass

def run_bot():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    bot.run()

# --- Main Execution ---
if __name__ == "__main__":
    # Flask ko background thread me start karein taaki Koyeb health check pass ho
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()
    
    print("Starting Telegram Bot...")
    # Telegram bot ko alag thread me chalayein
    bot_thread = threading.Thread(target=run_bot)
    bot_thread.start()
    bot_thread.join()
    
