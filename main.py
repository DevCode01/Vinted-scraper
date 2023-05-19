from alert_bot.bot import discord_alert_vinted_bot

discord_url = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
vinted_url = "https://www.vinted.fr/catalog?status_ids[]=6&status_ids[]=2&status_ids[]=1&status_ids[]=3&status_ids[]=4&catalog[]=1242&order=newest_first&brand_id[]=53"

discord_alert_vinted_bot(vinted_url, discord_url)

