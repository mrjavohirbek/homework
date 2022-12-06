import requests
import json


headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    "X-Is-Ajax-Request": "X-Is-Ajax-Request",
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}


def get_data():
    url = 'https://roscarservis.ru/catalog/legkovye/?form_id=catalog_filter_form&filter_mode=params&sort=asc&filter_type=tires&arCatalogFilter_458_1500340406=Y&set_filter=Y&arCatalogFilter_463=668736523&PAGEN_1=1'

    r = requests.get(url=url, headers=headers)
    # with open('index.html', 'w', encoding='utf-8') as file:
    #     file.write(r.text)
    # print(r.json())
    # with open('r.json', 'w', encoding='utf-8') as file:
    # json.dump(r.json(), file, indent=4, ensure_ascii=False)

    pages_count = r.json()['pagesCount']
    data_list = []
    for page in range(1, pages_count+1):
        url = f'https://roscarservis.ru/catalog/legkovye/?form_id=catalog_filter_form&filter_mode=params&sort=asc&filter_type=tires&arCatalogFilter_458_1500340406=Y&set_filter=Y&arCatalogFilter_463=668736523&PAGEN_1={page}'

        r = requests.get(url=url, headers=headers)
        data = r.json()
        items = data['items']
        possible_stores = ['discountStores', 'externalStores', 'commonStores']
        for item in items:
            total_amount = 0

            item_name = item['name']
            item_price = item['price']
            item_img = f"https://roscarservis.ru{item['imgSrc']}"
            item_url = f"https://roscarservis.ru{item['url']}"

            stores = []
            for ps in possible_stores:
                if ps in item:
                    if item[ps] is None or len(item[ps]) < 1:
                        continue
                    else:
                        for store in item[ps]:
                            store_name = store['STORE_NAME']
                            store_price = store['PRICE']
                            store_amount = store['AMOUNT']
                            total_amount += int(store['AMOUNT'])
                        stores.append(
                            {
                                'store_name': store_name,
                                'store_price': store_price,
                                'store_amount': store_amount,
                            }
                        )
            data_list.append(
                {
                    'name': item_name,
                    'price': item_price,
                    'img': item_img,
                    'url': item_url,
                    'stores': stores,
                    'total_amount': total_amount
                }
            )
    with open('data.json', 'a', encoding='utf-8') as file:
        json.dump(data_list, file, indent=4, ensure_ascii=False)


get_data()
