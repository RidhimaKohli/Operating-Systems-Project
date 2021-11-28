from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from datetime import datetime
from os import system
import re
from webdriver_manager.chrome import ChromeDriverManager

def validate_text(regex,inp):
	if not re.match(regex,inp):
		return False
	return True

print("Enter Your Email : " , end="")
email = input()
while not(validate_text(r"^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$",email)):
        system("clear")
        print("Invalid Email")
        print("Enter Email Again")
        email = input()
system('clear')
print("Enter Your Password : " , end="")
psswd = input()
system('clear')    
print("Enter Meeting Code Without Any Special-Character : " , end="")
code = input()
while not(validate_text(r"^[a-zA-Z0-9]*$",code)):
        system("clear")
        print("Invalid GMeet Code, Try Again")
        print("Without Special Character")
        code = input()
system('clear')


now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)
print("Time To Join Class [ Format = HH:MM:SS ] eg. 01:59:20")
start_time = input()
while not(validate_text(r"\d\d:\d\d:\d\d",start_time)):
        system("clear")
        print("Enter In Correct Format [ HH:MM:SS ] ")
        print("Time To Join Class [ Format = HH:MM:SS ] eg. 01:59:20")
        start_time = input()


while current_time != (start_time):
    system("clear")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time , " , Start at : " , start_time)
    sleep(1)

if current_time == (start_time):
    path = "chromedriver.exe"
    opt = Options()
    # Open With maximized Screen
    opt.add_argument("start-maximized")
    # Add Permission for Microphone , Camera and Notificaion 
    opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1, 
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.notifications": 1 
    })

    driver = webdriver.Chrome(ChromeDriverManager().install(),options=opt)
    driver.get("https://meet.google.com/new")
    #Email Passed
    search = driver.find_element_by_name("identifier")
    search.send_keys(email)
    search.send_keys(Keys.RETURN)
    driver.implicitly_wait(5)
    #password Passed 
    search = driver.find_element_by_name("password")
    print(search)
    search.send_keys(psswd)
    search.send_keys(Keys.RETURN)

    #Open Google Meet With Your Code
    sleep(3)
    driver.get("https://meet.google.com/lookup/" + code)
    sleep(3)

    
    try:
      # Turn OFF  Video and Audio 
#       driver.find_element_by_xpath("/html/body/div[1]/c-wiz/div/div/div[9]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[4]/div[1]/div/div/div").click()# Turn OFF Video By Default
#       driver.find_element_by_xpath("/html/body/div[1]/c-wiz/div/div/div[9]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[4]/div[2]/div/div").click()
      sleep(8)
      turn_off_mic_action = ActionChains(driver)
      turn_off_mic_action.key_down(Keys.CONTROL).send_keys("d").key_up(Keys.CONTROL).perform();
      turn_off_camera_action = ActionChains(driver)
      turn_off_camera_action.key_down(Keys.CONTROL).send_keys("e").key_up(Keys.CONTROL).perform();
        
#       driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[4]/div[1]/div/div/div').click()
    # turn off camera
#       driver.find_element_by_css_selector('div.U26fgb.JRY2Pb.mUbCce.kpROve.yBiuPb.y1zVCf.HNeRed.M9Bg4d').click()
      sleep(1)
#       driver.find_element_by_css_selector('div.U26fgb.JRY2Pb.mUbCce.kpROve.yBiuPb.y1zVCf.HNeRed.M9Bg4d').click()
#       sleep(10)
#       driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[4]/div[2]/div/div').click()
      # Join Class
      driver.find_element_by_css_selector('div.uArJ5e.UQuaGc.Y5sE8d.uyXBBb.xKiqt').click()
#       driver.find_element_by_xpath("/html/body/div[1]/c-wiz/div/div/div[9]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/span").click()
      sleep(20)
    except:
        print("Can't Join, Try Again")
    

    if current_time == end_time:
        driver.find_element_by_css_selector('div.VfPpkd.Bz112c.LgbsSe.yHy1rc.eT1oJ.tWDL4c.jh0Tpd.Gt6sbf.QQrMi.ftJPW').click()
        system("clear")
        print("Left Meet")
        driver.close()
