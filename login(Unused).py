# This application is to automate logins on the Instant Schools platform
# Data to be used will be loaded from an excel sheet

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# Variables
number = "0543030620"
password = "myschool"
# number = "0203887623"
# password = "richPhil"


## URLS
instantSchools = "https://instantschools.vodafone.com.gh"
sigin = "https://instantschools.vodafone.com.gh/en/user/#/signin"
# signup = "https://instantschools.vodafone.com.gh/en/user/#/create_account"

## Chrome Driver location
PATH = r"C:\Users\Samuel Mensah\OneDrive\Desktop\IS_Database\chromedriver.exe"


# STEP 2 - Lunch browser and open Instant Schools
ser = Service(PATH)
driver = webdriver.Chrome(service=ser)
driver.get(sigin)
time.sleep(15)


# STEP 3 - Fill Forms
Phone_Number = driver.find_element_by_xpath('//*[@id="username"]/div/div/label/input')
Phone_Number.click()
Phone_Number.send_keys(number)
time.sleep(2)

Password = driver.find_element_by_xpath('//*[@id="password"]/div/div/label/input')
Password.click()
Password.send_keys(password)
time.sleep(2)

Sign_in = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div[1]/div/div/form/div[4]/button')
Sign_in.click()
time.sleep(2)

# STEP 4 - Select Profile
# Select_Profile = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div[1]/table/tr[1]/td[2]/button')
# Select_Profile.click()
