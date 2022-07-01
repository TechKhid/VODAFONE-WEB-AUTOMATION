# This application is to automate signups of back locks on the Instant Schools platform
# Data to be used will be loaded from an excel sheet

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
import datetime as dt 
# from passw_gen import *

## URLS
instantSchools = "https://instantschools.vodafone.com.gh"
signup = "https://instantschools.vodafone.com.gh/en/user/#/create_account"

PATH = r"C:\Users\Samuel Mensah\OneDrive\Desktop\VODAFONE_WEBAUTO_PROJECT\chromedriver.exe"
ser = Service(PATH)
try:
   driver = webdriver.Chrome(service=ser)
   print("Chrome browser has been launched successfully")

except:
   print("Chrome browser lauch failed!")


# df = pd.read_excel (r'C:\Users\Samuel Mensah\OneDrive\Desktop\IS_Database\St. Elisabeth Primary.xlsx')
df = pd.read_excel (r'C:\Users\Samuel Mensah\OneDrive\Desktop\VODAFONE_WEBAUTO_PROJECT\learners_database.xlsx')
names = []
phones = []

#Funtion for logging out
def logout():
   driver.get("https://instantschools.vodafone.com.gh/en/logout/")
   print("logged out!")

def log_reg(name):
   try:
     
      with open('regist_log.txt', 'r+') as f:
         data = f.readlines()
         name_list = []
         for line in data:
            entry = line.split(',')
            name_list.append(entry[0])
         if name not in name_list:
               date_ = dt.date.today()
               time_ = dt.datetime.today().time().strftime("%H:%M:%S")
               f.writelines(f'\n{name} registered at [{str(date_.strftime("%A-%B-%d-%Y"))}, {time_}]')
   except:
      print("Logging failed")   
      pass

# Function for checking signup success
def confirm_signUp(num, pass_, stud_):
   try:
      driver.get(instantSchools)
      time.sleep(3)
      phone_n = driver.find_element_by_xpath('//*[@id="username"]/div/div/label/input')
      phone_n.click()
      num = str(num)
      phone_n.send_keys(num)
      time.sleep(2)

      passwor_ = driver.find_element_by_xpath('//*[@id="password"]/div/div/label/input')
      passwor_.click()
      passwor_.send_keys(pass_)
      time.sleep(2)

      Sign_in = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div[1]/div/div/form/div[4]/button')
      Sign_in.click()
      time.sleep(5)
      print(f"Done registering {stud_}")
      log_reg(stud_)
      time.sleep(2)
      logout()
   except:
      pass

#function for signing new entries 
def new_signup(name, phone):
   driver.get(signup)
   print("Now at signup screen")

   time.sleep(2)
   
   Full_Name = driver.find_element_by_xpath('//*[@id="name"]/div/div/label/input')
   Full_Name.click()
   Full_Name.send_keys(name)
   time.sleep(2)

   # Select and insert phone number
   Phone_Number = driver.find_element_by_xpath('//*[@id="username"]/div/div/label/input')
   Phone_Number.click()
   phone = str(phone)
   Phone_Number.send_keys(phone)
   time.sleep(2)

   # Select password field
   Password = driver.find_element_by_xpath('//*[@id="password"]/div/div/label/input')
   Password.click()
   
   password = phone 
   Password.send_keys(password, Keys.TAB, password)
   time.sleep(2)

  
   Agree = driver.find_element_by_xpath('//*[@id="terms-agreement-checkbox"]/div/label')
   Agree.click()
   time.sleep(2)

   Finish = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/form/p[2]/button')
   Finish.click()
   time.sleep(5)
   confirm_signUp(phone, password, name)
   time.sleep(2)






if __name__ == "__main__":
#Iterating through excel file and fetching name and corresponding number
   with open('regist_log.txt', 'r+') as f:
         f.truncate(0)
         time.sleep(1)
         f.close()

   for stud_ in range(len(df)):
      name = df["NAME"][stud_]
      phone = df["NUMBER"][stud_]
      print(name, phone)
      names.append(name)
      phones.append(phone)

      driver.get(instantSchools)#open home(signin page)
      print("Open Instant")
      time.sleep(10)
      print("Waiting for next command...")
      driver.get(signup)#switching to signup page
      print("Now at signup screen")

      time.sleep(2)
      #Error Handling sequence
      try:
         # Select and insert fullname
         Full_Name = driver.find_element_by_xpath('//*[@id="name"]/div/div/label/input')
         Full_Name.click()
         Full_Name.send_keys(name)
         time.sleep(2)

         # Select and insert phone number
         Phone_Number = driver.find_element_by_xpath('//*[@id="username"]/div/div/label/input')
         Phone_Number.click()
         phone = str(phone)
         Phone_Number.send_keys(phone)
         time.sleep(2)

         # Select password field and enter password
         Password = driver.find_element_by_xpath('//*[@id="password"]/div/div/label/input')
         Password.click()
         password = phone 
         Password.send_keys(password, Keys.TAB, password)
         time.sleep(2)

         #Select and check 'Agree' checkbox
         Agree = driver.find_element_by_xpath('//*[@id="terms-agreement-checkbox"]/div/label')
         Agree.click()
         time.sleep(2)

         #Select and click "Finish"
         Finish = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/form/p[2]/button')
         Finish.click()
         time.sleep(5)
         confirm_signUp(phone, password, name)
         time.sleep(2)
      except:
         print("Can't find Signup page, so I")
         logout()
         time.sleep(2)

   print("Done registering...:)")
   driver.close()