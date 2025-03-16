import requests
import time
from Config import BOT_TOKEN

api_url = "https://api.telegram.org/bot"


run = True

offset = -2
chat_id: int

while run:
    print(offset)
    updates = requests.get(f"{api_url}{BOT_TOKEN}/getUpdates?offset={offset+1}").json()
    if updates["result"]:
        for result in updates["result"]:
            offset = result["update_id"]
            chat_id = result["message"]["from"]["id"]
            PHOTO = requests.get("https://api.thecatapi.com/v1/images/search").json()
            requests.get(f"{api_url}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={PHOTO[0]['url']}")


    time.sleep(1)
