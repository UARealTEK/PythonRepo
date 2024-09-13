from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture()
def driver():
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser

def test_open(driver):
    try:
        driver.get('https://www.youtube.com/')
        element = driver.find_element(By.LINK_TEXT, "Підписки")
        element.click()
        youtube_link = driver.current_url
        expected_youtube_link = "https://www.youtube.com/feed/subscriptions"
        assert youtube_link == expected_youtube_link, f"Expected: {expected_youtube_link} but got {driver.current_url}"
    finally:
        driver.quit()