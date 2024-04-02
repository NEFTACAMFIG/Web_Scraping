# Install selenium "pip install -U selenium"
# Install webdriver manager "pip install webdriver-manager"
# Install wget "pip install wget"

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import random

# Timing in which pages will be changed
tiempo = [0.54, .73, 0.98]
# Driver to acess LinkedIn page
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://www.linkedin.com/home')
time.sleep(5)

#  Click button for Login
x = driver.find_element(By.XPATH, '//a[@class="nav__button-secondary btn-md btn-secondary-emphasis"]')
x.click()
time.sleep(random.choice(tiempo))

# Username and Password
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='session_key']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='session_password']")))

username.clear()
password.clear()

username.send_keys("Your User Name")
time.sleep(random.choice(tiempo))
password.send_keys("Your Password")
time.sleep(random.choice(tiempo))

# Click for start session
log_in = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
time.sleep(random.choice(tiempo))

# Profile list Example
profile_list =['List of profiles names that you want to scrape']

# Create an empty list for collect all the data
profiles_final_list = []

# Iteration through all the list of profiles
for profile in profile_list:
    profiless = []
    profile_url = f'https://www.linkedin.com/in/{profile}/' # Access to profiles using URL
    driver.get(profile_url)
    time.sleep(random.choice(tiempo))

    name_p = {} # Obtain the name using in LinkedIn
    name_p['name'] = driver.find_element(By.XPATH, '//h1[@class="text-heading-xlarge inline t-24 v-align-middle break-words"]').text
    profiless.append(name_p)
    #print(name_p)
    time.sleep(random.choice(tiempo))

    start = time.time() # Scrolling all the page to charge all data
    initialScroll = 0
    finalScroll = 1000

    while True:
        driver.execute_script(f"window.scrollTo({initialScroll}, {finalScroll})")

        initialScroll = finalScroll
        finalScroll += 1000

        time.sleep(random.choice(tiempo))
        end = time.time()

        if round(end - start) > 20:
            break
    # Obtaining the URL profile of the person
    prof_url = {}
    prof_url['url'] = str(driver.current_url)
    profiless.append(prof_url)
    #print(prof_url)

    exp = {key:[] for key in ['job', 'company', 'date', 'location', 'description']} # Creating a list to divide the data
    jobs = driver.find_elements(By.CSS_SELECTOR, 'section:has(#experience)>div>ul>li') # Finding experience section
    for job in jobs:
        try:
            exp['job'] += [job.find_element(By.CSS_SELECTOR, 'span[class="mr1 t-bold"] span').text]
        except Exception as e:
            exp['job'] += ['*missing value*']

        try:
            exp['company'] += [job.find_element(By.CSS_SELECTOR, 'span[class="t-14 t-normal"] span').text]
        except Exception as e:
            exp['company'] += ['*missing value*']

        try:
            exp['date'] += [job.find_element(By.CSS_SELECTOR, 'span[class="t-14 t-normal t-black--light"] span').text]
        except Exception as e:
            exp['date'] += ['*missing value*']

        try:
            exp['location'] += [job.find_element(By.CSS_SELECTOR, 'span[class="t-14 t-normal t-black--light"]:nth-child(4) span').text]
        except Exception as e:
            exp['location'] += ['*missing value*']

        try:
            exp['description'] += [job.find_element(By.CSS_SELECTOR, 'ul li ul span[aria-hidden=true]').text]
        except Exception as e:
            exp['description'] += ['*missing value*']

    #print(exp)
    profiless.append(exp)
    time.sleep(random.choice(tiempo))

    # Education section same process than experience section
    education = {key: [] for key in ['university', 'grade', 'date_u', 'activities', 'description_u']}
    edu = driver.find_elements(By.CSS_SELECTOR, 'section:has(#education)>div>ul>li')
    for ed in edu:
        try:
            education['university'] += [ed.find_element(By.CSS_SELECTOR, 'span[class="mr1 hoverable-link-text t-bold"] span').text]
        except Exception as e:
            education['university'] += ['*missing value*']

        try:
            education['grade'] += [ed.find_element(By.CSS_SELECTOR, 'span[class="t-14 t-normal"] span').text]
        except Exception as e:
            education['grade'] += ['*missing value*']

        try:
            education['date_u'] += [ed.find_element(By.CSS_SELECTOR, 'span[class="t-14 t-normal t-black--light"] span').text]
        except Exception as e:
            education['date_u'] += ['*missing value*']

        try:
            education['activities'] += [ed.find_element(By.CSS_SELECTOR, 'span[class="t-14 t-normal t-black--light"]:nth-child(4) span').text]
        except Exception as e:
            print('education --> activites', e)
            education['activities'] += ['*missing value*']
        try:
            education['description_u'] += [ed.find_element(By.CSS_SELECTOR, 'ul li ul span[aria-hidden=true]').text]
        except Exception as e:
            print('education --> description', e)
            education['description_u'] += ['*missing value*']
    #print(education)
    profiless.append(education)
    profiles_final_list.append(profiless) # Adding all data in one list
    time.sleep(random.choice(tiempo))

#print(len(profiles_final_list))

# Obtaining the data in a .json format and exporting to the computer
with open('datos_profiles.json', 'w') as f:
    json.dump(profiles_final_list, f)

