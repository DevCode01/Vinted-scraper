import requests
import pandas as pd


def choose_proxy(number_line):
    # FREE PROXIES
    response = requests.get("https://free-proxy-list.net/")
    proxy_list = pd.read_html(response.text)[0]
    proxy_list["url"] = "http://" + proxy_list["IP Address"] + ":" + proxy_list["Port"].astype(str)
    url_list = proxy_list["url"]
    return url_list[number_line]