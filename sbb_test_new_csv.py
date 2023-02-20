from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import time
import pandas as pd 

with open('jobs_SBB.csv', 'w') as file:
    file.write("Job_title \n")

path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get("https://company.sbb.ch/de/jobs-karriere/jobs/offene-stellen.html")
driver.maximize_window()
driver.implicitly_wait(300)

       #douton accepter tous les cookies
cookie =driver.find_element(By.ID, 'onetrust-accept-btn-handler')
try :
    actions = ActionChains(driver)
    actions.click(cookie)
except:
    pass


for k in range(2):
    titles = driver.find_elements(By.CLASS_NAME,'mod_jobfilter_results_link_title')   

      
    title_list = []                                                                                                       
    for title in range(len(titles)):                                            
         title_list.append(titles[title].text)     
    print(title_list)
    
    with open('jobs_SBB.csv', 'a') as file:
        for i in range(len(titles)):
            
            file.write(titles[i].text + "\n")
        
        next=driver.find_element(By.XPATH, '//*[@id="main"]/div[1]/div[2]/div[2]/div[2]/div[4]/ol/li[8]/button')
        actions = ActionChains(driver)
        actions.click(next)
driver.close()
