import random
import requests
from discordwebhook import Discord
from free_proxy.f_proxy import choose_proxy


def send_discord_notification(title, description, link, image_url, discord_url):
    webhook_url = discord_url
    discord = Discord(url=webhook_url)

    ########################################
    # PROXY SETUP #
    ########################################

    generate_random_number_proxy = random.randint(0, 299)
    # PROXY URL
    proxy = "f" + str(choose_proxy(generate_random_number_proxy))

    payload = {
        "embeds": [
            {
                "title": title,
                "description": description,
                "url": link,
                "image": {
                    "url": image_url
                }
            }
        ]
    }

    response = requests.post(webhook_url, json=payload, proxies={
        'http': proxy
    })

    if response.status_code == 204:
        print('Successfully sent.')
    else:
        print(f'Error : {response.status_code}')