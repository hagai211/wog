import sys

from selenium import webdriver
import chromedriver_autoinstaller
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from time import sleep

# configures Chrome browser
opt = webdriver.ChromeOptions()
chromedriver_autoinstaller.install()
driver = webdriver.Chrome(options=opt)


def test_scores_service(url):
    if not url.startswith("http://"):
        url = "http://" + url
    driver.get(url)
    try:
        score = int(driver.find_element(By.XPATH, '//*[@id="score"]').text)
    except NoSuchElementException:
        print("Score value not found")
        return False
    if 1 <= score <= 1000:
        return True
    else:
        return False


def main_function(url):
    if test_scores_service(url):
        sys.exit(0)
    else:
        sys.exit(1)


