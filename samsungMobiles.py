from urllib import request
from urllib.request import Request
from bs4 import BeautifulSoup
import json

MyPhone = []
phone = []
price = []
ram_rom = []
rating = []
display = []
camera = []
battery = []

b_url = 'https://www.flipkart.com/search?q=samsung+smartphone+5g&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page='
for i in range(1, 8):

    url = b_url + str(i)
    request_site = Request(url, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Referer": "https://www.flipkart.com/"})
    html = request.urlopen(request_site)
    soup = BeautifulSoup(html, 'html.parser')
    # print(soup)
    # link = soup.find('a', class_='_1LKTO3').get('href')
    # allLink = 'https://www.flipkart.com/' + link
    # url = allLink

    #
    name = soup.find_all('div', {'class': '_4rR01T'})
    prices = soup.find_all('div', {'class': '_30jeq3 _1_WHN1'})
    ram = soup.find_all('li', {'class': 'rgWa7D'})
    ratings = soup.find_all('div', {'class': '_3LWZlK'})
    boxes = soup.find_all('li', {'class': 'rgWa7D'})
    for box in boxes:
        text = box.get_text().lower()
        if 'camera' in text:
            camera.append(box.get_text())
        elif 'battery' in text:
            battery.append(box.get_text())
        elif 'display' in text:
            display.append(box.get_text())

    for i in name:
        name = i.text
        phone.append(name)
    for i in prices:
        prices = i.text
        price.append(prices)
    for i in ram:
        ram = i.text
        ram_rom.append(ram)
    for i in ratings:
        ratings = i.text
        rating.append(ratings)
    #
    #
    # y={ 'Mob Name':phone,
    #         'Price':price,}
    for phn, prices, cam, ram, rat, dsply, btry in zip(phone, price, camera, ram_rom, rating, display, battery):
        AllPhones = {
            'Mob Name': phn,
            'Price': prices,
            'Camera': cam,
            'Ram&Rom': ram,
            'Rating': rat,
            'Display': dsply,
            'Battery': btry
        }
        MyPhone.append(AllPhones)
print(MyPhone)
# # print(AllPhones)
# jsonfile = open("samsung_Mobiles.json","w")
# json.dump(MyPhone,jsonfile)
