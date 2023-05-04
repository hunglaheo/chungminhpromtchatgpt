from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import json

driver = webdriver.Chrome()

driver.maximize_window()
with open('listCauhoi.json', 'r',encoding='utf8') as f:
    data=json.loads(f.readline())


driver.get('https://chungminh.com/wp-admin/')
driver.find_element(By.XPATH,'/html/body/div[1]/form/p[1]/input').send_keys("admin")
driver.find_element(By.XPATH,'/html/body/div[1]/form/div/div/input').send_keys("mXl5e&X&FT")
driver.find_element(By.XPATH,'/html/body/div[1]/form/p[3]/input[1]').click()
driver.execute_script("window.scrollTo(0, 0);")
driver.find_element(By.CSS_SELECTOR,'#menu-posts-al_product > a > div.wp-menu-name').click()

for x in data:
    tieude = x["name"]
    with open('data/'+x["filename"]+'.txt','r',encoding='utf8') as f:
        noidung = f.readlines()
        for y in noidung:
            if y == "\n":
                noidung.remove(y)
        for y in noidung:
            if y == "\n":
                noidung.remove(y)

        driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/ul/li[10]/ul/li[3]/a').click()# Add item
        sleep(2)
        driver.find_element(By.CSS_SELECTOR,'#title').send_keys(tieude)
        sleep(2)
        driver.find_element(By.CSS_SELECTOR,'#content').send_keys(noidung)
        sleep(2)
        driver.execute_script("window.scrollTo(0, 0);")
        sleep(2)
        driver.find_element(By.CSS_SELECTOR,'#publish').click()
        sleep(2)



driver.quit()