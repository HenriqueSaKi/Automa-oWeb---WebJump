#Exercício para Automação Web - WebJump

#Bibliotecas
from selenium import webdriver
import time


driver = webdriver.Chrome(executable_path='chromedriver')
driver.get("https://wejump-automation-test.github.io/qa-test/")
driver.maximize_window()

#Clica e verifica existência dos botões do Box Buttons
class ButtonsBox ():
    def __init__(self):
        pass

    def ClicaBotao (self):
        botaoOne = driver.find_element_by_xpath("//div[@id='panel_body_one']//button[contains(text(),'One')]")
        botaoOne.click()
        botaoTwo = driver.find_element_by_xpath("//div[@id='panel_body_one']//button[contains(text(),'Two')]")
        botaoTwo.click()
        botaoFour = driver.find_element_by_xpath("//div[@id='panel_body_one']//button[contains(text(),'Four')]")
        botaoFour.click()


BB = ButtonsBox()
BB.ClicaBotao()
time.sleep(5)