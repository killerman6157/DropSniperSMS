import json
from os.path import exists

OTP_FILE = "otp_log.json"
USER_MAP_FILE = "user_map.json"

def load_json(path, default):
    return json.load(open(path)) if exists(path) else default

def save_json(path, data):
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)

def assign_number_to_user(user_id, number):
    user_map = load_json(USER_MAP_FILE, {})
    if user_id in user_map:
        return user_map[user_id]
    user_map[user_id] = number
    save_json(USER_MAP_FILE, user_map)
    return number

def get_user_status(user_id):
    user_map = load_json(USER_MAP_FILE, {})
    otp_log = load_json(OTP_FILE, {})
    number = user_map.get(user_id)
    if not number:
        return None, None
    otps = otp_log.get(number, [])
    return number, otps

def receive_otp(number, otp):
    otp_log = load_json(OTP_FILE, {})
    user_map = load_json(USER_MAP_FILE, {})

    otp_log.setdefault(number, []).append(otp)
    save_json(OTP_FILE, otp_log)

    for uid, num in user_map.items():
        if num == number:
            return uid
    return None