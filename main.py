# Referencia: https://www.callmebot.com/blog/free-api-whatsapp-messages/
from dotenv import load_dotenv
import requests
import os 

load_dotenv()

API_KEY = os.getenv("APIKEY")
PHONE_NUMBER = os.getenv("PHONENUMBER")
MESSAGE = "Hello World!"

requests.post(f"https://api.callmebot.com/whatsapp.php?phone={PHONE_NUMBER}&text={MESSAGE}&apikey={API_KEY}")

