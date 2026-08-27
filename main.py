import os
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
    app.run(host="0.0.0.0", port=port)

# --- Pyrogram Bot Setup ---
# Apni details yahan environment variables se le raha hai (Koyeb Env Variables me set karein)
API_ID = int(os.environ.get("API_ID", "123456"))  # Apna API ID yahan ya Env me dalein
API_HASH = os.environ.get("API_HASH", "your_api_hash")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8367187334:AAEeQv1GtML3AHIovZD-pNWHAhpgo6XIfAg")

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
    # Aap yahan apna filter/database logic add kar sakte hain
    pass

def run_bot():
    bot.run()

# --- Main Execution ---
if __name__ == "__main__":
    # Flask ko background thread me start karein
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()
    
    print("Starting Telegram Bot...")
    # Bot ko main thread me chalayein
    run_bot()
  
