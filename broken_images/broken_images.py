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
        
    def test_broken_images_count(self):
        images = self.driver.find_elements(By.TAG_NAME, "img")
        broken_images = 0
        
        for image in images:
            img_url = image.get_attribute("src")
            response = requests.get(img_url)
            
            if response.status_code != 200:
                broken_images += 1
                print(f"Broken image found: {img_url}")
        
        print(f"Total images checked: {len(images)}")
        print(f"Number of broken images: {broken_images}")
        
        self.assertGreater(broken_images, 0, "No broken images found, but the page should have some")
        
    def test_all_images_loaded(self):
        images = self.driver.find_elements(By.TAG_NAME, "img")
        
        for image in images:
            img_url = image.get_attribute("src")
            response = requests.get(img_url)
            
            self.assertEqual(response.status_code, 200, 
                           f"Image {img_url} returned status code {response.status_code}")

if __name__ == "__main__":
    unittest.main()