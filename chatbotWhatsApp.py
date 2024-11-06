from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

#Colocar opciones
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\\SERVIDOR\\AppData\\Local\\Google\\Chrome\\User Data\\Default")

#Instanciar y dimensionar
driver = webdriver.Chrome(options=options)
driver.set_window_position(0,0)
driver.set_window_size(1024,720)

#Solicitar url especifica
driver.get("https://web.whatsapp.com")
time.sleep(3600)

#//*[@id="pane-side"]/descendant::span[contains(@aria-label,'no leidos')]
#//*[@id="main"]/descendant::div[@role='row']