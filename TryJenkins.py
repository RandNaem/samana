# driver configuration
from behave import given, then, when
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import random
import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.microsoft import EdgeChromiumDriverManager
chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
chrome_options.add_argument('--lang=eng')
chrome_services = Service(EdgeChromiumDriverManager().install())
driver = webdriver.Edge(service=chrome_services, options=chrome_options)
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/#top")
# DEALING WITH ALERTS
driver.find_element(By.XPATH, "//input[@id='name']").send_keys("Tom")
driver.find_element(By.XPATH, "//input[@id='alertbtn']").click()
alert = Alert(driver)
print(alert.text)
time.sleep(5)
alert.accept() # alert.dismiss()
