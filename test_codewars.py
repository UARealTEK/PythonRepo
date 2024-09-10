import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture()
def browser():
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser
    browser.quit()

def test_login(browser):
    #opening the browser and clicking on the button
    browser.get("https://www.codewars.com/")
    login_button = browser.find_element(By.XPATH,"/html/body/div/div[3]/div[1]/div/nav/div[2]/a[1]")
    login_button.click()
    assert browser.current_url == "https://www.codewars.com/users/sign_in", f"Expected: https://www.codewars.com/users/sign_in, but was {browser.current_url}"

    #Inserting users log in
    user_log_in = browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/main/div[2]/form/div[3]/div[1]/input")
    user_log_in.click()
    user_log_in.send_keys("uarealtek1994@gmail.com")

    #inserting users password
    user_password = browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/main/div[2]/form/div[3]/div[2]/input")
    user_password.click()
    user_password.send_keys("Lolipop99")

    #clicking on the button and checking for successful log in
    submit_login = browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/main/div[2]/form/button[2]")
    submit_login.click()
    assert browser.current_url == "https://www.codewars.com/dashboard", f"Expected https://www.codewars.com/dashboard, but was {browser.current_url}"

    #check the response code
    response = requests.get(browser.current_url)
    assert response.status_code == 200, f"Expected - 200, but was {response.status_code}"