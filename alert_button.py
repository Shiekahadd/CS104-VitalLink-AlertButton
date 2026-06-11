import time
import requests
import RPi.GPIO as GPIO

BOT_TOKEN = "8863593979:AAH-p8PnPZrawNqtIARssVlb8FWa6pl_65M"
CHAT_ID = "8975704418"

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

button_pressed = False

def send_telegram_message():
    url = f"https://api.telegram.org/bot8863593979:AAH-p8PnPZrawNqtIARssVlb8FWa6pl_65M/sendMessage"
    data = {
        "chat_id": "8975704418",
        "text": "Someone pressed the alert button!"
    }
    requests.post(url, json=data)

while True:
    if GPIO.input(7) == GPIO.HIGH and not button_pressed:
        print("Someone pressed the alert button!")
        send_telegram_message()
        button_pressed = True

    elif GPIO.input(7) == GPIO.LOW:
        button_pressed = False

    time.sleep(0.1)
