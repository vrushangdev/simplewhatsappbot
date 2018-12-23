from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import socket
import time
handl=open('message.txt','r', encoding="utf8")
message_text=handl.read()
messages=message_text.split('\n')
print(messages)
no_of_message=1 
filename='contacts.txt'

handle = open(filename,'r')

moblie_no_list=list() # list of phone number can be of any length
for number in handle:
    if len(number)==12:
        moblie_no_list.append(number)
    elif len(number)==13:
        moblie_no_list.append(number.replace('+',''))
    elif len(number) ==10:
        number='91'+number
        moblie_no_list.append(number)
    else:
        pass 
               

def element_presence(by,xpath,time):
    element_present = EC.presence_of_element_located((By.XPATH, xpath))
    WebDriverWait(driver, time).until(element_present)
 
def is_connected():
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        socket.create_connection(("www.google.com", 80))
        return True
    except :
        is_connected()
driver = webdriver.Firefox()
driver.get("http://web.whatsapp.com")
time.sleep(10) #wait time to scan the code in second
 
def send_whatsapp_msg(phone_no,text):
    driver.get("https://web.whatsapp.com/send?phone={}&source=&data=#".format(phone_no))
    try:
        driver.switch_to_alert().accept()
    except:
        pass
 
    try:
        element_presence(By.XPATH,'//*[@id="main"]/footer/div[1]/div[2]/div/div[2]',30)
        txt_box=driver.find_element(By.XPATH , '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        global messages
        for message in messages:
            txt_box.send_keys(message)
            txt_box.send_keys(Keys.SHIFT,'\n')
        txt_box.send_keys("\n")
 
    except :
        print("invailid phone no :"+str(phone_no))
for moblie_no in moblie_no_list:
    try:
        send_whatsapp_msg(moblie_no,message_text)
 
    except Exception as e:
        time.sleep(10)
        is_connected()