# Filter-bot
# README.md

# Multi-User File Checker & Auto-Uploader Bot

Ek advanced Telegram bot jo public groups ke messages ko read karke private channels / database se files match karta hai aur automatic links provide karta hai.

## Features
- **Multi-user / Multi-group support**: Koi bhi admin apne group me bot add karke apna private channel link kar sakta hai.
- **MongoDB Integration**: Fast file searching aur data management ke liye.
- **Interactive Start Message**: Inline buttons aur clear instructions ke sath.

## Deployment on Koyeb

1. **GitHub Repository Banayein:** Upar di gayi saari files (`bot.py`, `requirements.txt`, `runtime.txt`, `Procfile`, `README.md`) ko apne GitHub repo me push kar dein.
2. **Koyeb Dashboard:** 
   - New App par click karein aur apna GitHub repository select karein.
   - **Builder:** Python
   - **Run Command:** `python bot.py`
3. **Environment Variables Add Karein:**
   - `API_ID`: Aapka Telegram API ID
   - `API_HASH`: Aapka Telegram API Hash
   - `BOT_TOKEN`: BotFather se mila hua token
   - `MONGO_URI`: MongoDB Atlas connection string
4. **Deploy:** Deploy button par click karein. Bot bina kisi error ke live ho jayega!
5. 
