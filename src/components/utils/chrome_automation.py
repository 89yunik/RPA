from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from .error_handler import error_handler

class ChromeAutomation:
    def __init__(self):
        self.driver:None = None
        
    @error_handler()
    def start_browser(self, driver_path:str, wait_time:int=10) -> str: 
        self.driver:WebDriver = webdriver.Chrome(service=Service(driver_path))
        self.driver.implicitly_wait(wait_time)

        start_browser_log = 'Browser started'
        return start_browser_log

    @error_handler()
    def open_url(self, url:str) -> str: 
        self.driver.get(url)

        open_url_log = 'URL opened'
        return open_url_log

    @error_handler()
    def quit_browser(self) -> str:
        if self.driver: 
            self.driver.quit()

            quit_browser_log = 'Browser closed'
            return quit_browser_log

    @error_handler()
    def control_elements_by_xpath(self, xpath_values:dict) -> str:
        for xpath, value in xpath_values.items():
            web_element:WebElement = self.driver.find_element(By.XPATH, xpath)
            web_element_tag_name:str = web_element.tag_name.lower()
            if web_element_tag_name=='select': Select(web_element).select_by_value(value)
            elif web_element_tag_name=='input': web_element.clear(); web_element.send_keys(value)
            elif web_element_tag_name=='a' or web_element_tag_name=='button': web_element.click()
        
        control_elements_by_xpath_log = 'Element control finished'
        return control_elements_by_xpath_log