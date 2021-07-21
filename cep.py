import requests
import json
import PySimpleGUI as sg


class TelaPython:
    def __init__(self):

        layout = [
                [sg.Text('cep'),sg.Input(size = (25,0), key='CEP')],
                [sg.Button('Buscar')],
                [sg.Output(size=(30,10))]
        ]


        self.tela = sg.Window('Buscar CEP',layout)
        



    def consultacep(self,cep):

        url = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
        if url.status_code == 200:
        	print('Sucesso')
        elif url.status_code == 400:
        	print('Erro 400')

        endereco = url.json()

        return endereco


    def start_window(self):
        while True:
                
            self.button , self.values = self.tela.Read()
          
            try:    
                valores = self.consultacep(self.values['CEP'])
                for k, v in valores.items():
                    print(k.upper() , ':' ,v)
               
            except:
                print('Name Error, funcao não definida')
                

jn = TelaPython()
jn.start_window()
