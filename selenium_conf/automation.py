from selenium import webdriver
import time
import os


def ChromeBrowser(sent_number, received_number, message):

  options = webdriver.ChromeOptions ()
  options.add_argument(f"user-data-dir={os.path.expanduser('~')}\\AppData\\Local\\Chrome\\Whatsapp Mk\\sent_number\\{str(sent_number)}")
  driver = webdriver.Chrome(executable_path=f"{os.path.abspath(os.getcwd())}\\selenium_conf\\webdriver\\chromedriver.exe", options=options)
  
  url = f'https://web.whatsapp.com/send?phone={str(received_number)}&text={str(message)}'
  driver.get(url)
  
  while True:
    try:
      time.sleep(2)
      driver.find_element_by_css_selector("button._4sWnG").click()
      break
    except:
       time.sleep(1)
  time.sleep(4)
  driver.quit()


