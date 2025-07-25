
# DropSniperSMS Aiogram 3 + SQLite Version

This bot integrates with 5sim.net to provide real-time SMS number rental and reading.
It uses Aiogram 3 and a Flask-based dashboard.

## Features
- Aiogram 3.x (async-based)
- SQLite for persistent SMS logs
- Flask-based minimal dashboard
- 5sim.net API integration

## Setup

```bash
pip install -r requirements.txt
python main.py
```

## Files
- `main.py`: Telegram bot logic (Aiogram 3 style)
- `database.py`: SQLite DB logic
- `templates/`: HTML templates for the Flask dashboard
- `README.md`: Setup guide

## Note
Add your 5sim.net API key in `config.py` as:
```python
FIVESIM_API_KEY = "your_real_key_here"
```

