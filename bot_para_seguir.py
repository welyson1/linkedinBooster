from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time
from dotenv import load_dotenv
import os
# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

def main():
    # Obtém as credenciais do ambiente
    email = os.getenv("EMAIL")
    senha = os.getenv("SENHA")

    service = Service(ChromeDriverManager().install())
    navegador = webdriver.Chrome(service=service)

    navegador.maximize_window()

    navegador.get("https://www.linkedin.com/home")
    time.sleep(random.uniform(0, 15))
    navegador.find_element('xpath', '//*[@id="session_key"]').send_keys(email) #Seu email
    time.sleep(random.uniform(0, 15))
    navegador.find_element('xpath', '//*[@id="session_password"]').send_keys(senha) #Sua senha
    time.sleep(random.uniform(0, 15))
    navegador.find_element('xpath', '//*[@id="main-content"]/section[1]/div/div/form/div[2]/button').click()
    time.sleep(20)  
    
    tempo_limite = 10
    tempo_limite_pop_UP = 1
    
    for page in range(1, 100):
        navegador.get('https://www.linkedin.com/search/results/people/?activelyHiring=%22true%22&keywords=power%20platform&network=%5B%22F%22%2C%22S%22%5D&origin=FACETED_SEARCH&page=' + str(page) + '&sid=cE%40')
        
        WebDriverWait(navegador, tempo_limite).until(EC.visibility_of_element_located((By.CLASS_NAME, 'reusable-search__result-container')))
        
        divElements = navegador.find_elements(By.CLASS_NAME ,'reusable-search__result-container')
        
        for elemento in divElements:
            WebDriverWait(elemento, tempo_limite).until(EC.visibility_of_element_located((By.CLASS_NAME, 'artdeco-button__text')))
            
            profileStatus = elemento.find_element(By.CLASS_NAME, 'artdeco-button__text')
            print(profileStatus.text)
            
            if(profileStatus.text == "Seguir"):
                profileDiv = elemento.find_element(By.CLASS_NAME, 'entity-result__actions')
                if(profileDiv):
                    profileButton = profileDiv.find_element(By.TAG_NAME, 'button')
                    if(profileButton):
                        profileButton.click()
                        time.sleep(random.uniform(0, 15))
                else:
                    print("Não encontrou a div") 
            else: 
                print("Não é possível conectar")
    
    
if __name__ == "__main__":
    startTime = time.time()
    main()
    
    endTime = time.time()
    
    durationTime = endTime - startTime
    durationTime = round(durationTime, 2)
    
    print("Tempo de execução: ", durationTime, " segundos")