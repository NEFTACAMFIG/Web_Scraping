# Instalar selenium pip install -U selenium
# Instalar webdriver manager pip install webdriver-manager
# Instalar wget pip install wget
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import os
import wget


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://www.instagram.com/')
time.sleep(3)

# Presionar command + f para abrir el buscador de XPATH
x = driver.find_element(By.XPATH, '//button[@class="_a9-- _a9_1"]')
x.click()
time.sleep(300)

# Agregar username
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

username.clear()
password.clear()

username.send_keys("Your user")
time.sleep(2)
password.send_keys("Your Password")
time.sleep(2)

log_in = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
time.sleep(2)

ahora_no = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Ahora no')]"))).click()
time.sleep(2)
ahora_no2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Ahora no')]"))).click()
time.sleep(3)

y = driver.find_element(By.XPATH, '(//a[@href="#"])[1]')
y.click()
time.sleep(3)


searchbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Buscar']")))
searchbox.clear()
keyword1 = "#Europe"
searchbox.send_keys(keyword1)
time.sleep(2)
searchbox.send_keys(Keys.ENTER)
time.sleep(2)
searchbox.send_keys(Keys.ENTER)
time.sleep(8)

driver.execute_script("window.scrollTo(0,4000);")
time.sleep(3)

images = driver.find_elements(By.TAG_NAME, "img")
time.sleep(3)

images = [image.get_attribute("src") for image in images]
images = images[2:-1]
#print(images)

path = os.getcwd()
path = os.path.join(path, keyword1[1:] + "s")

os.mkdir(path)
#print(path)

counter = 0
for image in images:
    save_as = os.path.join(path, keyword1[1:] + str(counter) + '.jpg')
    wget.download(image, save_as)
    counter += 1

