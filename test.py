# from BaseReuests.Base_Requests import Base

# base = Base()
# filters = dict(user_id=1)
# params = dict(user_id=1, times=13131, balance=3)
# a = base.creater(filters, params)
# print(a)
import pyppeteer
import asyncio
from pyppeteer import launch
from PIL import Image
import io












async def main():
    browser = await launch({'headless': False})
    page = await browser.newPage()
    await page.setViewport({"width": 1600, "height": 900})
    await page.goto('https://genius.com/Lyalka-fuck-lyrics')
    paths = '#lyrics-root > div:nth-child(3)'
    page = await page.waitForSelector(paths)
    s = await page.screenshot({'encoding': "binary"})
    photo = io.BytesIO(s)
    img = Image.open(photo)
    img.show()





async def mains():
    browser = await launch({'headless': False, "args": ["--start-maximized"]})
    page = await browser.newPage()
    await page.setViewport({"width": 1600, "height": 900})
    await page.goto('https://vk.com/')
    paths = '#index_email'
    entry_box = await page.querySelector(paths)
    await entry_box.type('+375291520804')
    await page.keyboard.press("Enter")
    password_paths = '#root > div > div > div > div > div.vkc__AuthRoot__col.vkc__AuthRoot__contentCol.vkuiSplitCol > div > div > div > form > div:nth-child(1) > div.vkc__Password__Wrapper > div:nth-child(1) > div > input'
    await page.waitForSelector(password_paths)
    passwort_type = await page.querySelector(password_paths)
    await passwort_type.type('fjyA4376')
    await page.keyboard.press("Enter")
    await page.waitForSelector('#l_pr > a > span.left_label.inl_bl')
    await page.click('#l_pr > a > span.left_label.inl_bl')
    await page.waitFor(10000)
    await page.waitForSelector('#post_field')
    new_type = await page.querySelector('#post_field')
    await new_type.type('Запись которую написал бот!')
    await page.waitFor(10000)
    await page.click('#send_post > span > span')
    await page.waitFor(10000)
    await browser.close()
    



    # photo = io.BytesIO(s)
    # img = Image.open(photo)
    # img.show()

print("Starting...")
asyncio.get_event_loop().run_until_complete(main())
print("Screenshot has been taken")