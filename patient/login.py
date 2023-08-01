from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import information


url = information.first_page["signin"]
service = Service(executable_path='D:\PatientTesting\chromedriver.exe')
driver = webdriver.Chrome(service=service)

driver.get(url)


email_field = driver.find_element("name", "email").get
password_field = driver.find_element("name", "password")

email_field.send_keys(information.patient_account["email"])
password_field.send_keys(information.patient_account["password"])

driver.find_element("id", "kt_sign_in_submit").click()

wait = WebDriverWait(driver, 10)
target_url = "https://patient.test.hemscap.com/#/dashboard"
wait.until(EC.url_to_be(target_url))

if driver.current_url == target_url:
    print("Done!")
