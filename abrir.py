import random
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep
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
    sleep(2)
    navegador.find_element('xpath', '//*[@id="session_key"]').send_keys(email) #Seu email
    sleep(2)
    navegador.find_element('xpath', '//*[@id="session_password"]').send_keys(senha) #Sua senha
    sleep(2)
    navegador.find_element('xpath', '//*[@id="main-content"]/section[1]/div/div/form/div[2]/button').click()
    sleep(20)    

    tempo_limite = 10

    for page in range(1, 100):
        navegador.get('https://www.linkedin.com/search/results/people/?activelyHiring=%22true%22&keywords=power%20platform&origin=FACETED_SEARCH&page=' + str(page) + '&sid=cE%40')
        WebDriverWait(navegador, tempo_limite).until(EC.visibility_of_element_located((By.CLASS_NAME, 'reusable-search__result-container')))
        divElements = navegador.find_elements(By.CLASS_NAME ,'reusable-search__result-container')

        for elemento in divElements:
            WebDriverWait(elemento, tempo_limite).until(EC.visibility_of_element_located((By.CLASS_NAME, 'app-aware-link')))
            profileLink = elemento.find_element(By.CLASS_NAME, 'app-aware-link').get_attribute('href')
            print("Abrindo perfil:", profileLink)
            navegador.execute_script("window.open('" + profileLink + "');")  # Abrir o perfil em uma nova aba
            sleep(random.uniform(1, 5))  # Tempo de espera aleatório entre 5 e 10 segundos
            handles = navegador.window_handles
            navegador.switch_to.window(handles[-1])  # Trocar para a última aba aberta
            sleep(random.uniform(2, 6))  # Tempo de espera aleatório para a rolagem entre 3 e 7 segundos
            # Rolagem para baixo
            for _ in range(random.randint(2, 4)):
                navegador.execute_script("window.scrollBy(0, " + str(random.randint(300, 500)) + ");")
                sleep(random.uniform(0.5, 3))
            sleep(random.uniform(3, 7))  # Tempo de espera aleatório após a rolagem entre 2 e 5 segundos
            # Rolagem para cima
            for _ in range(random.randint(2, 4)):
                navegador.execute_script("window.scrollBy(0, -" + str(random.randint(300, 500)) + ");")
                sleep(random.uniform(0.5, 1.5))
            sleep(random.uniform(1, 4))  # Tempo de espera aleatório após a rolagem entre 2 e 5 segundos
            # Fechar o perfil
            navegador.close()
            # Trocar para a aba principal
            navegador.switch_to.window(handles[0])
            sleep(random.uniform(2, 5))  # Tempo de espera aleatório após fechar o perfil entre 2 e 5 segundos

if __name__ == "__main__":
    startTime = time.time()
    main()
    endTime = time.time()
    durationTime = endTime - startTime
    durationTime = round(durationTime, 2)
    print("Tempo de execução: ", durationTime, " segundos")
