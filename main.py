import asyncio
import aiohttp
import requests

from bs4 import BeautifulSoup as bs


def parse_page(page):
    soup = bs(page, 'lxml')

    pg = soup.find_all('li', 'catalog-grid__cell')
    # print(pg)

    for i in pg:
        print(i.a.img['title'])
        print(i.find('span', 'goods-tile__price-value').string)
        print(i.find('p', 'goods-tile__description goods-tile__description_type_text ng-star-inserted').string)
        print('\n')


async def fetch_connect(session, page):
        async with session.get(
                f'https://rozetka.com.ua/mobile-phones/c80003//page={page}',
                allow_redirects=True) as response:
            html = await response.read()
            parse_page(html)


async def main():
    tasks = []
    async with aiohttp.ClientSession() as session:
        for page in range(1, 67):
            task = asyncio.create_task(fetch_connect(session, page))
            tasks.append(task)
        await asyncio.gather(*tasks, return_exceptions=True)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())