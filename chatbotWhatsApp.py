from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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

#Cambiamos
while (True):
    
    #Expresiones xpath
    #//*[@id="pane-side"]/descendant::span[contains(@aria-label,'no leidos')]
    #//*[@id="main"]/descendant::div[@role='row']
    #//div/div/div[1]/div[1]/div[1]/div/div[1]/div/span[1]/span
    #//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div/div[1]

    #Recuperamos nuevos mensajes
    new_message =driver.find_element(By.XPATH,'//*[@id="pane-side"]/descendant::span[contains(@aria-label\'no leidos\')]')
    new_message.click()
    
    #Obtener los mensajes del usuario
    last_messages =driver.find_elements(By.XPATH,'//*[@id="main"]/descendant::div[@role=\'row\']')
    last_message = last_messages[-1]
    
    #Mostrar mensaje seleccionado
    last_message_text = last_message.find_element(By.XPATH, '//div/div/div[1]/div[1]/div[1]/div/div[1]/div/span[1]/span')
    print(f'user message:{last_message.text}')
   
    

