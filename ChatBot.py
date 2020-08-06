from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

class WhatsappBot:
    def __init__(self):
        # Parte 1 - A mensagem que você quer enviar
        self.mensagem = "O JOGO"
        # Parte 2 - Nome dos grupos ou pessoas a quem você deseja enviar a mensagem
        self.grupos_ou_pessoas = ["Nerds Geeks"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(
        executable_path=r'./chromedriver', chrome_options=options)

    def EnviarMensagens(self):


        # <div tabindex="-1" class="_3uMse">
        # <div tabindex="-1" class="_2FVVk _2UL8j">
        # <div class="_2FbwG" style="visibility: visible;">Digite uma mensagem</div><div class="_3FRCZ copyable-text selectable-text" contenteditable="true" data-tab="1" dir="ltr" spellcheck="true"></div></div></div>
        self.driver.get('https://web.whatsapp.com')
        for i in range(20):
            print(i)
            time.sleep(1)
        for grupo_ou_pessoa in self.grupos_ou_pessoas:
            for i in range(50):
                campo_grupo = self.driver.find_element_by_xpath(f"//span[@title='{grupo_ou_pessoa}']")
                # time.sleep(3)
                campo_grupo.click()
                chat_box = self.driver.find_element_by_class_name('_3uMse')
                # time.sleep(3)
                chat_box.click()
                chat_box.send_keys(self.mensagem)
                botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
                # time.sleep(3)
                botao_enviar.click()
                # time.sleep(5)


bot = WhatsappBot()

bot.EnviarMensagens()
print("fim")