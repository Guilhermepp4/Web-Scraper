import requests
from bs4 import BeautifulSoup
import json


url_base = "https://casamariomachado.pt/284-artigos-de-latao-para-pichelaria"

def extract_data(html_page, page_number):
    soup = BeautifulSoup(html_page.text, 'html.parser')
    images_ul = soup.find("ul", class_="product_list grid row")

    images = images_ul.find_all("li")

    for image in images:
        image_url = image.find("img")["src"]
        image_name = image.find("h5").text.strip()
        final_images.append({"url": image_url, 
                            "name": image_name, 
                            "page": page_number})

final_images = []

for i in range(1,8):
    url = f"{url_base}?p={i}"
    html_page = requests.get(url)
    extract_data(html_page, i)

f_out = open("data/images.json", "w")
json.dump(final_images, f_out, indent=4, ensure_ascii=False)
f_out.close()