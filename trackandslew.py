
# pip install requests
import requests, time

ALPACA_HOST = "http://127.0.0.1:11111"   # change to your Alpaca endpoint
DEVICE_NUM = 0                            # telescope device number

def put(path, **params):
    r = requests.put(f"{ALPACA_HOST}/api/v1/telescope/{DEVICE_NUM}/{path}", params=params, timeout=5)
    r.raise_for_status()
    return r.json()

def get(path, **params):
    r = requests.get(f"{ALPACA_HOST}/api/v1/telescope/{DEVICE_NUM}/{path}", params=params, timeout=5)
    r.raise_for_status()
    return r.json()

# 1) Connect
put("connected", Connected=True)

# 2) Ensure tracking on and mount is aligned/site set in driver
put("tracking", Tracking=True)

# 3) Slew to RA/Dec (hours/degrees). Example: Jupiter from step (1)
# Replace with values you print from script (1).
target_ra_hours  = 0.0    # e.g., 2.345
target_dec_deg   = 0.0    # e.g., +12.34

put("slewtocoordinates", RightAscension=target_ra_hours, Declination=target_dec_deg)

# 4) Poll until Slewing false
while True:
    if not get("isslewing")["Value"]:
        break
    time.sleep(1)

print("On target & tracking.")