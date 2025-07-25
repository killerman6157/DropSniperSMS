import json

def show_dashboard():
    try:
        with open("user_map.json", "r") as f:
            user_map = json.load(f)
        with open("otp_log.json", "r") as f:
            otp_log = json.load(f)

        print("\n📊 FluxSMS Dashboard")
        print("="*30)
        print(f"🔢 Total Users: {len(user_map)}")
        for user_id, number in user_map.items():
            otps = otp_log.get(number, [])
            print(f"👤 User: {user_id} | 📱 Number: {number} | 📩 OTPs: {len(otps)}")
        print("="*30)
    except Exception as e:
        print("❌ Error loading dashboard:", e)

if __name__ == '__main__':
    show_dashboard()