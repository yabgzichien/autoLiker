from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH  = "C:/Users/User/Desktop/Selenium/chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get('https://www.instagram.com/')
driver.maximize_window()
time.sleep(2)

username = driver.find_element_by_name("username")
username.send_keys("username")

password = driver.find_element_by_name("password")
password.send_keys("password12345")
password.send_keys(Keys.RETURN)
time.sleep(3)

search = driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input")
search.send_keys("#keyboard")
time.sleep(1)
search.send_keys(Keys.RETURN)
time.sleep(1)
search.send_keys(Keys.RETURN)
time.sleep(6)

posts = driver.find_elements_by_class_name("_9AhH0")

def like ():   
    time.sleep(3)
    like = driver.find_element_by_xpath("/html/body/div[6]/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button")
    like.click()

def close():
    close = driver.find_element_by_xpath("/html/body/div[6]/div[3]/button")
    close.click()

def comment():
    c = driver.find_element_by_xpath("/html/body/div[6]/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea")
    c.click()
    time.sleep(1)
    c1 = driver.find_element_by_class_name("Ypffh")
    c1.send_keys("nice keyboard")
    c1.send_keys(Keys.RETURN)
    time.sleep(2)

for post in posts:
    time.sleep(2)
    post.click()
    like()
    comment()
    close()


    driver.execute_script("window.scrollTo(0, 5);")

