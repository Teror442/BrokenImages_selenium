import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from urllib.parse import urljoin

class TestBrokenImages(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://the-internet.herokuapp.com/broken_images")
        
    def tearDown(self):
        self.driver.quit()
        
    def test_images_status(self):
        images = self.driver.find_elements(By.TAG_NAME, "img")
        broken_images = 0
        working_images = 0
        
        for image in images:
            img_url = image.get_attribute("src")
            response = requests.get(img_url)
            
            if response.status_code == 200:
                working_images += 1
                print(f"Working image found: {img_url}")
            else:
                broken_images += 1
                print(f"Broken image found: {img_url}")
        
        print(f"Total images checked: {len(images)}")
        print(f"Working images: {working_images}")
        print(f"Broken images: {broken_images}")

if __name__ == "__main__":
    unittest.main()