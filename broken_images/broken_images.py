from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from urllib.parse import urljoin

def test_broken_images():
    driver = webdriver.Chrome()
    
    try:
        driver.get("https://the-internet.herokuapp.com/broken_images")
        
        images = driver.find_elements(By.TAG_NAME, "img")
        
        broken_images = 0
        
        for image in images:
            img_url = image.get_attribute("src")
            
            response = requests.get(img_url)
            
            if response.status_code != 200:
                broken_images += 1
                print(f"Broken image found: {img_url}")
        
        print(f"Total images checked: {len(images)}")
        print(f"Number of broken images: {broken_images}")
        
        assert broken_images > 0, "No broken images found, but the page should have some"
        
    finally:
        driver.quit()

if __name__ == "__main__":
    test_broken_images()