from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLocators:
    base_url = "https://rahulshettyacademy.com/AutomationPractice/"

    name_input = "//input[@class = 'form-control ng-touched ng-dirty ng-invalid']"

    hide_item = "//input[@id='hide-textbox']"

    radio_button = "//div[@id = 'radio-btn-example']/fieldset/label"


