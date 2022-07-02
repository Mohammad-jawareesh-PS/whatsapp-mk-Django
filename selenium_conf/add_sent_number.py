from selenium import webdriver
import time
import os
from random import randint

def add_number(sent_number):
  driver = webdriver.Chrome(executable_path=f"{os.path.abspath(os.getcwd())}\\selenium_conf\\webdriver\\chromedriver.exe")
  
  url = 'https://web.whatsapp.com/'
  driver.get(url)

  path = f'{os.path.abspath(os.getcwd())}\\static\\confirm_numbers\\QR\\{sent_number}'
  if not os.path.exists(path):
    os.makedirs(path)
  while True:
    # file_name = randint(10000,90000)
    img_path = os.path.join(path, 'QRCODE.JPG')
    time.sleep(10)
    try:
      with open(img_path, 'wb') as file:
        file.write(driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div[1]/div/div[2]/div').screenshot_as_png)
    except:
      pass

  time.sleep(120)
  driver.quit()

# add_number('test')

# media/confirm_numbers/QR/test/QRCODE.JPG