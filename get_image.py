"""get_image.py"""

import requests
import aiohttp
import asyncio

def download_image_requests(url):
    r = requests.get(url)
    return r

async def download_image_aiohttp(session, url, index):
    async with session.get(url, ssl=False) as response:
        content = await response.read()
        with open(f"async_images/image{index}.jpg", "wb") as f:
            f.write(content)

async def main(url):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(10):
            folder_name = f"image_folder_{i+1}"
            task = download_image_aiohttp(session, url, i+1)
            tasks.append(task)
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    URL = "https://picsum.photos/200/300"
    
    for i in range(10):
        with open(f"images/image{i+1}.jpg", 'wb') as f:
            f.write(download_image_requests(URL).content)
    
    asyncio.run(main(URL))