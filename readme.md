# Vinted Scrapper

![GitHub](https://img.shields.io/github/license/DevCode01/Vinted-scrapper)
![Python](https://img.shields.io/badge/python-v3.8-blue)

This project provides a scrapper for Vinted, a popular online marketplace for buying and selling second-hand fashion items. The scrapper is implemented in Python and allows you to extract data from Vinted listings for further analysis or processing.

## Features

- Extracts data from Vinted listings, including item details, prices, descriptions, and seller information.
- Supports searching for specific keywords or categories.
- Provides options for filtering and sorting the extracted data.

## Requirements

- Python 3.8 or higher
- [Requests](https://pypi.org/project/requests/) library
- [Pandas](https://pypi.org/project/pandas/) library

## Installation

1. Clone this repository:

```shell
git clone https://github.com/DevCode01/Vinted-scrapper.git
```

## Usage

1. Get vinted URL (example) :
```shell
https://www.vinted.be/catalog?status_ids[]=6&status_ids[]=2&status_ids[]=1&catalog[]=1206&price_to=500&currency=EUR&brand_id[]=60&brand_id[]=12&brand_id[]=7&brand_id[]=405
```
<br>
2. Paste URL  
On main.py, modify <b>vinted_url</b> to paste the value
<br><br>
3. Get discord webhook URL :  
- Modify the channel (gear icon).
- Go to Integrations.
- Select Webhook.
- Copy the webhook URL.
<br><br>
4. Paste webhook URL  
On main.py, modify <b>discord_url</b> to paste the value  
<br><br>
5. Install dependencies

```shell
pip install -r requirements.txt
```
<br>
6. Execute main.py

```shell
python main.py
```



# Disclaimer
This project is for educational purposes only. Use it responsibly and at your own risk. The author is not responsible for any misuse or damage caused by this software.