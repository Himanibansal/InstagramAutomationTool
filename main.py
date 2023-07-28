from selenium import webdriver
import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
#open instagram
browser.get("https://www.instagram.com")
#wait for 3 sec to fully load the page
time.sleep (1)
browser.maximize_window()
#identify user field and send username
browser.find_element(By.CSS_SELECTOR,"input[name='username']").send_keys("create_own_idea")
# username_input = browser.find_element_by_css_selector("input[name='username']").send_keys("create_own_idea")

#identify password field and send password
browser.find_element(By.CSS_SELECTOR,"input[name='password']").send_keys("create@@himi")
# password_input = browser.find_element_by_css_selector("input[name='password']").send_keys("create@@himi")

#find and click submit
browser.find_element(By.XPATH,"//button[@type='submit']").click()
# login_button = browser.find_element_by_xpath("//button[@type='submit']")
# login_button.click()

# click on notNow button
time.sleep(2)
notNowButton = WebDriverWait(browser, 15).until(
    lambda d: d.find_element(By.XPATH,'//button[text()="Not Now"]'))
notNowButton.click()
time.sleep(2)

# click on notNow button
notNowButton = WebDriverWait(browser, 15).until(
    lambda d: d.find_element(By.XPATH,'//button[text()="Not Now"]'))
notNowButton.click()
time.sleep(2)

 # go to profile
browser.find_element(By.CSS_SELECTOR,"#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.ctQZg.KtFt3 > div > div:nth-child(6) > span").click()
time.sleep(2)
browser.find_element(By.CSS_SELECTOR,'#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.ctQZg.KtFt3 > div > div:nth-child(6) > div.poA5q > div.uo5MA._2ciX.tWgj8.XWrBI > div._01UL2 > a:nth-child(1)').click()
time.sleep(4)
# browser.find_element(By.CSS_SELECTOR,'#react-root > section > main > div > header > section > div.XBGH5 > div.qF0y9.Igw0E.IwRSH.eGOV_.ybXk5.ui_ht.bPdm3 > div > a').click()


## serch
browser.find_element(By.CSS_SELECTOR,"#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.QY4Ed.P0xOK > input").send_keys("narendramodi")
# browser.find_element(By.CSS_SELECTOR,'#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.QY4Ed.P0xOK > div.yPP5B > div > div._01UL2 > div > ul > div').click()
# # browser.find_element(By.CSS_SELECTOR,'#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.QY4Ed.P0xOK > div.yPP5B > div > div._01UL2 > div > ul > div > a > div > div.qF0y9.Igw0E.IwRSH.YBx95.vwCYk').click()
#
# # browser.find_element(By.CSS_SELECTOR,"#f32f15cb1c0180c > div > div").click()
# # # browser.find_element(By.XPATH,'//button[text()="Follow"]')
# # profile_button = browser.find_element_by_xpath("//button[//*[@id="react-root"]]")
# # profile_button.click()
#
# # loop
# # for i in range (5):
# #     browser.find_element_by_xpath('//*[@id="react-root"]/section/main/section/div[3]/div[2]/div[2]/div/div/div/div[1]/div[3]/button').click()
# #     browser.refresh()
# #     time.sleep(3)