from selenium import webdriver
from selenium.webdriver.chrome.service import Service

import information

url = information.first_page['patient_signup']

service = Service(executable_path='D:\PatientTesting\chromedriver.exe')
driver = webdriver.Chrome(service=service)

driver.get(url)


first_name = driver.find_element("name", "first_name")
last_name = driver.find_element("name", "last_name")
birthday = driver.find_element("name", "birthday")
height_foot = driver.find_element("name", "userHeightFeet")
height_inch = driver.find_element("name", "userHeight")
weight = driver.find_element("name", "userWeight")
occupation = driver.find_element("name", "occupation")
employed = driver.find_element("id", "currentlyEmployedStatus")
employer_name = driver.find_element("name", "employer_name")
insurance_provider = driver.find_element("name", "insuranceProvider")
insurance_id = driver.find_element("name", "insuranceId")
home_cell_phone_number = driver.find_element("name", "homeCellPhoneNumber")
email = driver.find_element("name", "email")
state = driver.find_element("name", "state")
city = driver.find_element("name", "city")
zip_code = driver.find_element("name", "zip_code")
user_name = driver.find_element("name", "user_name")
password = driver.find_element("name", "password")
confirm_password = driver.find_element("name", "password_confirmation")
agree = driver.find_element("name", "toc")
submit = driver.find_element("id", "kt_sign_up_submit")
