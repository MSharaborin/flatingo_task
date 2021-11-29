import asyncio

import aiohttp
from bs4 import BeautifulSoup as bs


def parse_page(page):
    soup = bs(page, 'html.parser')

    pg = soup.find_all('li', 'catalog-grid__cell')
    # print(pg)

    for i in pg:
        print(i.a.img['title'])
        print(i.a.img['src'])
        print(i.img('ng-star-inserted'))
        # print(i.p['goods-tile__description'])
        print(i.find('span', 'goods-tile__price-value'))
        print(i.find('p', 'goods-tile__description goods-tile__description_type_text ng-star-inserted'))
        print('\n')

    # print(soup.find('ul', 'catalog-grid ng-star-inserted'))
    # for i in soup.find('ul', 'catalog-grid ng-star-inserted'):
    #     print(i.a)



async def fetch_connect(session):
        async with session.get('https://rozetka.com.ua/mobile-phones/c80003/') as response:

            html = await response.text()
            parse_page(html)


async def main():
    tasks = []
    async with aiohttp.ClientSession() as session:
        task = asyncio.create_task(fetch_connect(session))
        tasks.append(task)
        await asyncio.gather(*tasks, return_exceptions=True)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())