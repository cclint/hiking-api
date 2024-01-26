from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from chromedriver_py import binary_path
import pytest
import time

@pytest.fixture(scope="module")
def browser_session():
    svc = Service(binary_path)
    browser = webdriver.Chrome(service=svc)
    browser.implicitly_wait(1)
    yield browser
    browser.quit()

@pytest.mark.parametrize("input_name, input_location, input_description", [
    ("Hatcher's Pass", "Palmer, AK", "Super Fun"),
    ("Thunderbird Falls", "Chugiak, AK", "The waterfalls are really neat LOL"),
    ("Kincaid Park", "Anchorage, AK", "You could walk to Fire Island when the tide is down but you might die LOL"),
    ("FlatTop Trail", "Anchorage, AK", "Flattop Trail is the best trail in Anchorage. Well treaded. Very public"),
    ("Byron Glacier Trail", "Portage, AK", "Easy walk to some ice caves ooh la la!"),
    ("Portage Glacier Trail", "Portage, AK", "Ha literally have to get here from Whittier and it depends on the weather LOL")
    ])
def test_submit_a_trail(browser_session, input_name, input_location, input_description):
    browser=browser_session

    browser.get('http://127.0.0.1:5000/add')

    name_input = browser.find_element(By.ID,"inputName")
    location_input = browser.find_element(By.ID, "inputLocation")
    description_input = browser.find_element(By.ID, "inputDescription")
    submit_button = browser.find_element(By.TAG_NAME, "button")
    
    name_input.send_keys(input_name)
    location_input.send_keys(input_location)
    description_input.send_keys(input_description)
    submit_button.click()

    success_message = browser.find_element(By.ID, "statusmessage")

    assert success_message is not None, "Trail Information Not Submitted Successfully"