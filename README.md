# DropSniperSMS Telegram Bot (5sim.net Integration + GUI)

A Telegram bot that fetches real phone numbers using [5sim.net](https://5sim.net) and logs OTPs. Includes a CLI dashboard to monitor usage.

## 🚀 Features

- Integrates with 5sim.net REST API
- Fetches real phone numbers per user request
- Stores OTPs and user data in local JSON files
- CLI Dashboard (`gui.py`) to view OTP logs and number usage

---

## 🧠 Requirements

- Python 3.8+
- Telegram bot token
- 5sim.net API Key

Install dependencies:

```bash
pip install aiogram requests


---

🔐 Setup

1. Replace YOUR_BOT_TOKEN in main.py with your actual bot token.


2. Replace YOUR_5SIM_API_KEY in rest_api.py with your 5sim.net API key.



# rest_api.py
API_KEY = "YOUR_5SIM_API_KEY"

You can get a 5sim API key here: https://5sim.net/dashboard


---

▶️ Running the Bot

Run this in your terminal:

python main.py


---

🖥 CLI Dashboard (GUI)

This bot includes a command-line GUI to track user OTP submissions.

Run it with:

python gui.py

It shows:

Total OTPs received

Active users

Number ↔ User mappings



---

📁 Files

File	Purpose

main.py	Telegram bot logic
rest_api.py	Fetch numbers from 5sim.net
db.py	Handles storage in JSON
gui.py	Terminal-based GUI dashboard
otp_log.json	Stores OTPs per user
user_map.json	Stores user ↔ number links



---

📬 Example Bot Commands

/get_number — Get a real number

/submit_otp — Submit OTP after receiving

/dashboard — Admin command to view live logs



---

🛡 Disclaimer

This bot is for educational and private testing purposes only. Do not use on public groups or spam platforms. You are responsible for your own use.


---

👤 Author

Developed by Bashir Rabiu — 🇳🇬 Kano, Nigeria
