from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


class my_spider:
    def __init__(self, chromedriver_dir):
        # set headers
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
        # setting up driver options
        chr_service = Service(chromedriver_dir)
        self.options = webdriver.ChromeOptions()
        self.options.headless = True
        self.options.add_argument(f'user-agent={user_agent}')
        self.driver = webdriver.Chrome(service=chr_service, options=self.options)

    def crawl_start(self, url):
        chrome = self.driver
        wait = WebDriverWait(chrome, 10)
        asset_info = {
            'product-name': '',
            'product-price': '',
            'product-selected-color': '',
            'product-sizes': ''
        }

        # start and redirect chrome to the given url
        chrome.get(url)

        # wait until element is visible
        wait.until(ec.visibility_of_element_located((By.XPATH, '//h1[@itemprop="name"]')))

        # get asset name
        asset_name = chrome.find_element(By.XPATH, '//h1[@itemprop="name"]')
        asset_name = asset_name.get_attribute('innerHTML')
        asset_info['product-name'] = asset_name

        # get asset price
        asset_price = chrome.find_element(By.XPATH, '//meta[@itemprop="price"]')
        asset_price = asset_price.get_attribute('content')
        asset_info['product-price'] = float(asset_price)

        # get selected color
        asset_color = chrome.find_element(By.XPATH, '//div[@class="color-container color-container--selected"]')
        asset_color = asset_color.get_attribute('aria-label')
        if ' selected' in asset_color.lower():
            asset_color = asset_color.replace(' selected', '')
        asset_info['product-selected-color'] = asset_color

        # get product sizes
        asset_size = []
        search = chrome.find_element(By.XPATH, '//div[@class="selector-list"]')
        search = search.find_elements(By.XPATH, './child::*')
        for size in search:
            asset_size.append(size.get_attribute('data-size'))
        asset_info['product-sizes'] = asset_size

        return asset_info

    def close_driver(self):
        chrome = self.driver
        chrome.close()
