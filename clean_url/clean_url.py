def clean_url(url):
    index_point_interrogation = url.find('?')
    url_params = url[index_point_interrogation + 1:].split('&')
    param_dict = {}
    for param in url_params:
        key, value = param.split('=')
        key = key.replace('[]', '')
        param_dict.setdefault(key, set()).add(value)
    unique_params = []
    for key, values in param_dict.items():
        unique_params.append(key + '=' + ','.join(values))

    cleaned_url = "https://www.vinted.be/api/v2/catalog/items?" + '&'.join(unique_params) + "&is_for_swap=0&material_ids=&video_game_rating_ids="
    return cleaned_url.replace('[', '').replace(']', '').replace('catalog=', 'catalog_ids=').replace('brand_id=', 'brand_ids=')

