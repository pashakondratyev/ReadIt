import requests

import readit.config as cfg


# Need to obfuscate API key
def new_pushover_message(message, url):
    user_data = {
        "token": cfg.pushover["api_key"],
        "user": cfg.pushover["user_key"],
        "message": message,
        "url": url
    }
    response = requests.post("https://api.pushover.net/1/messages.json", data=user_data)
    print(response)


if __name__ == '__main__':
    new_pushover_message("Hi mom!")
