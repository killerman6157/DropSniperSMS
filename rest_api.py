import requests

API_KEY = "PUT_YOUR_5SIM_API_KEY_HERE"
BASE_URL = "https://5sim.net/v1/user/buy/activation/any/any"

def fetch_number(country_code="ng"):
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }
    try:
        response = requests.get(BASE_URL, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data.get("phone")
        else:
            print("API Error:", response.status_code, response.text)
            return None
    except Exception as e:
        print("Exception while calling 5sim API:", e)
        return None