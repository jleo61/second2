from test.test_data import TestLocators
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.parametrize("num1,num2", [("ma","ja"),
                                        ("ka","fa"),
                                        ("Admin","admin123")])
def test_login(num1,num2):
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(3)

    driver.find_element(By.XPATH, "//input[@placeholder = 'Username']").send_keys(num1)
    driver.find_element(By.XPATH, "//input[@placeholder = 'Password']").send_keys(num2)
    time.sleep(3)

    driver.find_element(By.XPATH, "//button[@type = 'submit']").click()
    time.sleep(3)
    # invld = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p")
    # element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p")))




    print(driver.title)

    assert driver.title == "OrangeHRM"

    driver.close()




