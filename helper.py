import requests
from gpiozero import Button 
from signal import pause


button = Button(3)

WEBHOOK_URL = "https://nketsia.app.n8n.cloud/webhook-test/1bfa69fd-9017-447b-9c0b-12ac97d7d89d"
def send_email():
    print("Button Pressed")
    requests.get(WEBHOOK_URL)

button.when_pressed = send_email
print("Waiting for button press...") 
pause()   
    