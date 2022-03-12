from conf import *
from spider import *

import os
import json

curr_dir = os.getcwd()
chromedriver_dir = os.path.join(curr_dir, 'selenium_webdriver', 'chromedriver.exe')

spider = my_spider(chromedriver_dir)
all_assets = []

# navigate through the given urls and scrap the content
print('Starting chromedriver....\n')
for url in URLS:
    asset_info = spider.crawl_start(url)
    all_assets.append(asset_info)
# cleanup selenium
print('Closing chromedriver....\n')
spider.close_driver()

# write the extracted data to json file
with open('data.json', 'w') as file:
    json.dump(all_assets, file, indent=2)
