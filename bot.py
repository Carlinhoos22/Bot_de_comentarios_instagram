from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(executable_path=r'/home/jenniffer/Documentos/PASTA-WESLLEY-PROGRAMAS/Bot_Comentario_Instagram/chromedriver') # CAMINHO DO PATH DRIVER QUE CONTROLA O NAVEGADOR, NECESSARIO BAIXALO DE ACORDO COM A VERSÃO E O TIPO DO NAVEGADOR...

    def login(self):
        driver = self.driver
        driver.get('https://www.instagram.com/')
        sleep(6)

        #input aria-label="Telefone, nome de usuário ou email" aria-required="true" autocapitalize="none" autocorrect="off" maxlength="75" name="username" type="text" class="_2hvTZ pexuQ zyHYP" value=""
        #//input[@name="username"]

        input_username = driver.find_element_by_name('//input[@name="username"')
        driver.find_
        input_password = driver.find_element_by_xpath('//select[@name="password"]')

        input_username.click()
        input_username.clear()
        input_username.send_keys(self.username)



meuBot = InstagramBot('SEU_NOME_DE_USUARIO_LOGIN', 'SUA_SENHA_DE_LOGIN')
meuBot.login()
