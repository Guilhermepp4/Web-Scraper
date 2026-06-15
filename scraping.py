import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import os
import json

output_folder = "data"
output_folder_iamges = "images"
os.makedirs(output_folder, exist_ok=True)
os.makedirs(output_folder_iamges, exist_ok=True)

url_base = "https://casamariomachado.pt/284-artigos-de-latao-para-pichelaria"
final_images = []

def extract_data(html_page, page_number):
    soup = BeautifulSoup(html_page.text, 'html.parser')
    images_ul = soup.find("ul", class_="product_list grid row")

    images = images_ul.find_all("li")

    for image in images:
        image_url = image.find("img")["data-original"] or image.find("img")["src"]
        image_name = image.find("h5").text.strip()
        final_images.append({"url": image_url, 
                            "name": image_name.replace(" ", "_").replace("/", "_"),
                            "page": page_number})

def prepare_url():
    for i in range(1,8):
        try:
        
            print(f"Extracting content from page {i}...")
            url = f"{url_base}?p={i}"
            html_page = requests.get(url)
            extract_data(html_page, i)
            print(f"Page {i} extracted successfully.")
        
        except Exception as e:
            print(f"Error extracting page {i}: {e}")
            continue

def extract_imgs(final_images):
    for item in final_images:
        image_url = item["url"]
        image_name = item["name"]

        try:
            response = requests.get(image_url, timeout=10)
            response.raise_for_status()

            img = Image.open(BytesIO(response.content))
            
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGBA")
                background = Image.new("RGB", img.size, (255, 255, 255))
                background.paste(img, mask=img.split()[3])
                img = background
            else:
                img = img.convert("RGB")

            img = img.resize((300, 300))

            path = os.path.join(output_folder_iamges, f"{image_name}.jpg")
            img.save(path, "JPEG", quality=90)

            print(f"Downloaded and saved {image_name} successfully.")
        except Exception as e:
            print(f"Error downloading {image_name}: {e}")
            continue

def main():
    prepare_url()

    f_out = open("data/images.json", "w")
    json.dump(final_images, f_out, indent=4, ensure_ascii=False)
    f_out.close()

    extract_imgs(final_images)

if __name__ == "__main__":
    main()