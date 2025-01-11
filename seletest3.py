from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.exceptions import TimeoutException

from dotenv import load_dotenv
import os


load_dotenv()

email = os.getenv('LINKEDIN_EMAIL')

profile_name = os.getenv('LINKEDIN_PROFILE_NAME')

password = os.getenv('LINKEDIN_PASSWORD')

driver = webdriver.Firefox()
#driver.implicitly_wait(10)
driver.get("https://www.linkedin.com/login")

#print(f"email : {email}")

username_elem = driver.find_element(By.NAME, "session_key")
username_elem.send_keys(email)
username_elem.send_keys(Keys.RETURN)

password_elem = driver.find_element(By.NAME, "session_password")
password_elem.send_keys(password)
password_elem.send_keys(Keys.RETURN)

#myElem = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'theme--mercado .share-box-feed-entry__trigger--v2)))')))
#driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)
post_elem = wait.until(EC.presence_of_element_located((By.ID, "ember48")))
post_elem.send_keys(Keys.RETURN)

#cancel_elem = wait.until(EC.presence_of_element_located((By.XPATH, "TODO")))

text_elem = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".ql-editor.ql-blank")))
text_elem.send_keys("Bonjour à tous")

""" publish_elem = wait.until(EC.presence_of_element_located((By.ID, "ember198")))
publish_elem.send_keys(Keys.RETURN) """

button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".share-actions__primary-action.artdeco-button--primary")))
button.send_keys(Keys.RETURN)


""" assert "Python" in driver.title
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source

driver.close() """