import os
import argparse
import change_wallpaper
import settings
import climage
from colorama import Fore, Back, Style, init
import aiohttp
import asyncio
from concurrent.futures import ThreadPoolExecutor

# Initialize colorama
init(autoreset=True)


async def download_image(url, output):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            with open(output, 'wb') as f:
                f.write(await response.read())
    return output


async def fetch_image_url():
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://api.nasa.gov/planetary/apod?api_key={settings.NASA_APOD}") as response:
            data = await response.json()
            return data['hdurl'] if 'hdurl' in data else data['url']


def convert_and_set_wallpaper(image_path):
    image_terminal = climage.convert(image_path, width=50)
    change_wallpaper.change_wallpaper(image_path)
    print(Fore.GREEN + image_terminal)
    print(Fore.YELLOW + f"Wallpaper saved and changed.")

def action(args):
    if args.wallpaper == "apod":
        try:
            
            image_url = asyncio.run(fetch_image_url())
            title = "Astronomy Picture of the Day"
            image_path = os.path.join(os.getcwd(), f"{title}.png")

            
            asyncio.run(download_image(image_url, image_path))

            
            with ThreadPoolExecutor() as executor:
                executor.submit(convert_and_set_wallpaper, image_path)

            print(Fore.CYAN + Style.BRIGHT + f"Wallpaper Saved: {title}")
            os.remove(image_path)
        except Exception as e:
            print(Fore.RED + f"Error: {str(e)}")


parser = argparse.ArgumentParser(
    prog='wallpaper-apod',
    description='Changes the wallpaper to NASA APOD',
    epilog='Text at the bottom of help'
)

parser.add_argument('wallpaper', action='store', help='The wallpaper action to change to NASA APOD')

args = parser.parse_args()

action(args)
