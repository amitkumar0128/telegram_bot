
# 🤖 Amit Telegram Bot

A powerful, modular Telegram bot built with Python & [Telethon](https://github.com/LonamiWebs/Telethon).  
This bot packs three core features: OpenAI integration, YouTube downloader, and Wikipedia search — all through simple Telegram commands.

---

## 🚀 Features

### 🧠 OpenAI Chat
Chat with an AI powered by OpenAI's GPT model directly in Telegram.  
Use it for quick answers, code help, ideas, or just fun convos.

**Command Example:**
```
/ask What is the difference between Docker and a virtual machine?
```

---

### 📥 YouTube Audio Downloader
Download YouTube videos as MP3 files and receive them straight in your chat.

**Command Example:**
```
/download a <youtube-url> # For only audio
/download v <youtube-url> # For video download
```

---

### 📚 Wikipedia Search
Search Wikipedia and get summarized answers directly in Telegram.

**Command Example:**
```
/wiki Elon Musk
```

---

## 🔧 Setup Instructions

### 1. Clone this repo

```bash
git clone https://github.com/amitkumar0128/telegram_bot.git
cd telegram_bot
```

### 2. Create a virtual environment

```bash
sudo apt install python3-venv  # for ubuntu
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure `.env` file

Configure `.env` file in the project root:

```
API_ID=your_telegram_api_id
API_HASH=your_telegram_api_hash
BOT_TOKEN=your_bot_token
OPENAI_API_KEY=your_openai_api_key
BOT_USERNAME=your_bot_username
```

> 📌 You can get your API ID and hash from https://my.telegram.org and your bot token from [@BotFather](https://t.me/BotFather).

---

### 5. Run the bot

```bash
cd ..
python3 -m telegram_bot
```

---

## 📁 Project Structure

```
telegram_bot/
├── plugins/            # Plugin files: chatgpt, yt.dl, wiki
│    ├── chatgpt.py
│    ├── start.py
│    ├── wiki.py
│    └── yt.dl.py
├── utils/              # Plugin loader
├── __init__.py         # Bot initialization
├── __main__.py         # Main entry point
├── .env                # Environment variables
├── requirements.txt
└── README.md
```

---

## Screenshots

<p align="center">
<img src="https://github.com/user-attachments/assets/c1e030a8-b790-4b99-8505-4c66da6eda16" alt="Screenshot" width="500"/>
<img src="https://github.com/user-attachments/assets/6b3f52d3-829f-4516-8d95-f3fe90ec910a" alt="Screenshot" width="500"/>
<img src="https://github.com/user-attachments/assets/63397207-a39a-4a2c-b0bd-86da8e4b6fd0" alt="Screenshot" width="500"/>
<img src="https://github.com/user-attachments/assets/017e9065-6025-43ab-8767-574548421eaf" alt="Screenshot" width="500"/>
<img src="https://github.com/user-attachments/assets/b6104614-9faf-4b48-be40-f36c0fe6e535" alt="Screenshot" width="500"/>
</p>

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you’d like to change.

---

## ⚠️ Disclaimer

This bot is for educational purposes only. Download responsibly and respect copyright laws.

---

## 📜 License

GPL-3.0 License
