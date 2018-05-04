from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import urls
import config

driver = webdriver.Firefox()
wait = WebDriverWait(driver, 10)

def doLogin(driver):
    driver.get(urls.LOGIN)
    username = driver.find_element_by_name("j_username")
    password = driver.find_element_by_name("j_password")


    username.send_keys(config.USERNAME)
    password.send_keys(config.PASSWORD)
    driver.find_element_by_tag_name("form").submit()
    wait.until(
        EC.presence_of_element_located((By.XPATH, "//a[@title='Sair']"))
    )



def doDiarios(driver):
    driver.get(urls.DIARIOS)
    wait.until(
        EC.presence_of_element_located((By.XPATH, "//span[text()='Selecionar Turma']"))
    )
    select = Select(driver.find_element_by_xpath("//select/option[text()='Selecione uma Turma']/.."))
    texts = []
    for i, option in enumerate(select.options):
        if i > 0:
            print(option.text)
            print(option.get_attribute("value"))
            texts.append(option.text)

    return texts


def doDiario(driver, text):
    driver.get(urls.DIARIOS)
    #wait.until(
    #    EC.presence_of_element_located((By.XPATH, "//span[text()='Selecionar Turma']"))
    #)
    element = wait.until(
        EC.presence_of_element_located((By.XPATH, "//label[text()='Selecione uma Turma']"))
    )
    #element = driver.find_element_by_xpath("//label[text()='Selecione uma Turma']")
    element.click()
    li = driver.find_element_by_xpath("//li[text()='{}']".format(text))
    li.click()



def doTable(driver):
    rows = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@id='corpo:academicos_content']//table")
                )
            )
    print(rows)




doLogin(driver)
#disciplinas = doDiarios(driver)
doDiario(driver, "13257 - Trabalho de conclusão de curso I - Ciência da Computação - 7ª Fase - Matutino - 2016/1")
doTable(driver)
#for d in disciplinas:
#    doDiario(driver, d)
#doDiario(driver, disciplinas[1])

#button.click()
#elem.send_keys(Keys.RETURN)
#assert "No results found." not in driver.page_source
#driver.close()
