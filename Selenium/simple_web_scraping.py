# pip3 install -U selenium
# pip3 install webdriver-manager

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://www.xades.com.mx/')
time.sleep(1)

# Dar click a boton usando Selenium
x = driver.find_element(By.XPATH, '//button[@data-drawer-id="sidebar-menu" and @aria-label="Abrir"]')
x.click()
time.sleep(1)

y = driver.find_element(By.XPATH, '//a[@href="/collections/checo-perez" and @class="Collapsible__Button Heading Link Link--primary u-h6"]')
y.click()
#time.sleep(4)

#
precios = driver.find_elements(By.XPATH, '//span[@class="ProductItem__Price Price Text--subdued"]')

s = [i.text for i in precios]
print(s)


#driver.quit()
