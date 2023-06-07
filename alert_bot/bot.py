import calendar
import random
import requests
import time
import discord_notification.notification as notif
from clean_url.clean_url import clean_url
from free_proxy.f_proxy import choose_proxy, choose_proxy_with_previous_proxy


def discord_alert_vinted_bot(urlvinted, discord_url):
    vinted_url = clean_url(urlvinted)
    print(vinted_url)

########################################
            # PROXY SETUP #
########################################

    generate_random_number_proxy = random.randint(0, 299)
    # PROXY URL
    proxy = "f"+str(choose_proxy(generate_random_number_proxy))

########################################
         # USER-AGENT SETUP#
########################################

    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0",
        "Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
        'Mozilla/5.0 (Linux; Android 10; SM-G996U Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 10; SM-G980F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.96 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 9; SM-G973U Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 6.0; HTC One X10 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.98 Mobile Safari/537.36',
        'Mozilla/5.0 (iPhone14,6; U; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/19E241 Safari/602.1',
        'Mozilla/5.0 (iPhone14,3; U; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/19A346 Safari/602.1',
        'Mozilla/5.0 (iPhone13,2; U; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/15E148 Safari/602.1',
        'Mozilla/5.0 (Linux; Android 12; SM-X906C Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246',
        'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9',
    ]

    # RANDOM USER AGENT
    random_user_agent = random.choice(user_agents)

    languages = [
        "en-US",
        "fr-FR",
        "es-ES",
        "de-DE",
        "ja-JP"
    ]

    # RANDOM LANGUAGES
    random_languages = random.choice(languages)

    cache_controls = [
        "no-cache",
        "max-age=3600",
        "no-store",
        "public, max-age=86400",
        "private, must-revalidate"
    ]

    # RANDOM CACHE CONTROLS
    random_cache_controls = random.choice(cache_controls)

    #RANDOM HEADERS
    headers = {
        'User-Agent': random_user_agent,
        'accept-encoding': 'gzip, deflate, br',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': random_languages,
        'cache-control': random_cache_controls,
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-request': "1",
        'DNT': '1',
        'Connection': 'keep-alive',
        'TE': 'Trailers',
    }


    # GET SESSION
    session = requests.Session()
    session.headers.update(headers)
    session2 = session.get('https://www.vinted.be/catalog?search_text=nike')
    # GET COOKIE
    cookie_vinted = session2.cookies.get_dict().get('_vinted_fr_session', "")
    # SET COOKIE
    session.cookies.set('_vinted_fr_session', cookie_vinted)
    # REQUEST with proxy
    response = session.get(vinted_url,headers=headers, proxies = {'http': proxy})
    # GET ITEMS
    items_found = response.json().get('items')
    previous_items = set(item['id'] for item in items_found)
    default_timestamp = calendar.timegm(time.gmtime())


    ########################################
                # LOOP (dirty) #
    ########################################
    while True:
        time.sleep(3)

    ########################################
            # PROXY SETUP (again) #
    ########################################

        generate_random_number_proxy = random.randint(0, 299)
        # PROXY URL
        proxy = "f" + str(choose_proxy_with_previous_proxy(generate_random_number_proxy, proxy))

        # NEW SESSION
        session = requests.Session()
        session.headers.update(headers)
        session2 = session.get(urlvinted)
        # GET COOKIE
        cookie_vinted = session2.cookies.get_dict().get('_vinted_fr_session', "")
        # SET COOKIE
        session.cookies.set('_vinted_fr_session', cookie_vinted)

        random_user_agent = random.choice(user_agents)
        headers = {
            'User-Agent': random_user_agent,
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en',
            'DNT': '1',
            'Connection': 'keep-alive',
            'TE': 'Trailers',
        }

        response = session.get(
            vinted_url,
            headers=headers, proxies={
                'http': proxy
            }, verify=False)

        items_found = response.json().get('items')


        ################################################################################
         # GET ITEMS AND SEND NOTIFICATION IS THE PUBLICATION IS LESS THAN 60 SECONDS #
        ################################################################################

        if items_found is not None:
            # SORT TIMESTAMPS
            timestamps = [item['photo']['high_resolution']['timestamp'] for item in items_found if item is not None and 'photo' in item and item['photo'] is not None and 'high_resolution' in item['photo'] and 'timestamp' in item['photo']['high_resolution'] and item['photo']['high_resolution']['timestamp'] > default_timestamp]
            timestamps = [timestamp for timestamp in timestamps if timestamp > default_timestamp and timestamp - calendar.timegm(time.gmtime()) >= -55]
            timestamps.sort()
            # IF TIMESTAMP > LAST_TIMESTAMP AND TIMESTAMP-NOW <= 60 seconds
            for timestamp in timestamps:
                print("TIMESTAMP")
                print(timestamp - calendar.timegm(time.gmtime()))
                for item in items_found:
                    if item and item['photo'] and item['photo']['high_resolution'] and item['photo']['high_resolution']['timestamp'] == timestamp:
                        item_id = item['id']
                        if item_id not in previous_items:
                            default_timestamp = timestamp
                            previous_items.add(item_id)
                            # GET TITLE
                            title = item['title']
                            # GET BRAND TITLE LIKE NIKE, ADIDAS, ...
                            marque = item['brand_title']
                            # GET CLOTHING SIZE
                            taille = item['size_title']
                            # GET FIRST IMAGE
                            url_image = item['photo']['url'] if 'photo' in item and item[
                                'photo'] is not None and 'url' in item['photo'] else ""
                            #GET PRODUCT URL
                            url_link = item['url']
                            # GET SELLER INFORMATIONS TO GET MARK, ...
                            vendeur = item['user']['login']
                            mark_seller = item['user']['id']
                            # GET STARS USERS
                            userURL = "https://www.vinted.be/api/v2/users/" + str(mark_seller) + "?localize=false"

                            # GET USER INFORMATIONS
                            j = session.get(userURL)
                            reputation = j.json()['user']['feedback_reputation']
                            reputation = 5 * reputation if reputation > 0 else "Aucune evaluation"
                            feedback_count = j.json()['user']['feedback_count']

                            # SET NOTIFICATION INFORMATIONS
                            notification_title = title
                            notification_description = "\n💵 Prix : " + item['price'] + "€\n\n" + "📏 Taille : " + taille + "\n\n :shirt: Marque : " + marque + "\n\n" + "👤 Vendeur : " + vendeur + "\n\n:star: Note vendeur : " + str(reputation) + " (" + str(feedback_count) + " avis)" + "\n\n📅 Publié " + "<t:" + str(timestamp) + ":R>\n\n"
                            notification_link = url_link
                            notification_image_url = url_image

                            # DISCORD NOTIFICATION
                            notif.send_discord_notification(notification_title, notification_description, notification_link, notification_image_url, discord_url)