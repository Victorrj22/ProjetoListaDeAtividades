from kivy.app import App
from kivy.lang import Builder 
import requests
import random
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager

class Adm(ScreenManager):
    pass
class Inicio(Screen):
    def on_start(self):
        drink = self.ids["atividades"].text = self.nova_atividade()

    def nova_atividade(self):
        lnk = "https://www.boredapi.com/api/activity"
        requisicao = requests.get(lnk)
        dic_requisicao = requisicao.json()
        cotacao = dic_requisicao["activity"]
        return cotacao
class Tela(App):
    def build(self):
        return Adm()

Tela().run()