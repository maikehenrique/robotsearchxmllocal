from glob import glob
from datetime import datetime
import time

class BotBuscaChavesNFCE:

    chaveslista = []
    chavesVLidas = []
    chavesXLidas = []
    chavesVxml = []
    chavesXxml = []
    datahorasInicio = ""
    datahorasTerminio = ""

    achadosLidos = []
    achadosXML = []
    localizados = []
    
    def inicio(self):
        self.menu()
        chave = ''
        
        print("Digite as chaves a serem procuradas")
        while chave != '0':
            chave = input("")
            chave = str(chave.rstrip())
            self.chaveslista.append(chave)

        self.chaveslista.remove('0')
        #print(self.chaveslista)
        self.busca()
    def relatorio(self):
        print("Gerando Relatório")
        try:
            datahorastring = datetime.now().strftime('%d/%m/%Y %H:%M')
            texto = "----------------Relatório de busca XML -------------------\n\n"
            texto+="Chaves Lidas comparando com Pasta:\n"

            texto+="Localizadas:\n"
            
            for var1 in range(len(self.achadosLidos)):
                if self.achadosLidos[var1]:
                    texto+="V "+str(self.chaveslista[var1])+"\n"
                    
            texto+="Não Localizadas:\n"     
            for var1 in range(len(self.achadosLidos)):
                if self.achadosLidos[var1] == 0:
                    texto+="X "+str(self.chaveslista[var1])+"\n"

            texto+="\n\n\n Pasta XML com Chaves Lidas:\n"

            texto+="Localizadas:\n"
            for var1 in range(len(self.achadosXML)):
                if self.achadosXML[var1]:
                    texto+="V "+str(self.localizados[var1])+"\n"

            texto+="Não Localizadas:\n"    
            for var1 in range(len(self.achadosXML)):
                if self.achadosXML[var1] == 0:
                    texto+="X "+str(self.localizados[var1])+"\n"

            arquivo = open('./Relatorio.txt','w', encoding="utf8")

            with open("./Relatorio.txt","a+") as arquivo:
                arquivo.read()
                arquivo.write(texto)
                
        except Exception as e:
                print("Erro ao Gerar Relatório !!!!!!!!!!!!!!!",e)

        self.datahorasTerminio = datetime.now().strftime('%d/%m/%Y %H:%M')
        print("Iniciou Busca as :"+self.datahorasInicio)
        print("Terminou Busca as :"+self.datahorasTerminio)
                
    def busca(self):
        
        self.datahorasInicio = datetime.now().strftime('%d/%m/%Y %H:%M')
        print("Iniciando Busca as :"+self.datahorasInicio)
        print("-------------------------------------------------")
           
        print("Comparação entre Chaves lidas e Pasta XML")  
        self.localizados = glob('**/*.xml', recursive=True)

        for var1 in range(len(self.chaveslista)):
            self.achadosLidos.append(0)

        for var2 in range(len(self.localizados)):
            self.achadosXML.append(0)

        for i in range(len(self.localizados)):
            for j in range(len(self.chaveslista)):
                if self.chaveslista[j] in self.localizados[i]:
                    self.achadosLidos[j] = 1
                    self.achadosXML[i] = 1

        self.relatorio()
        input("-------Terminado--------")
        

    def menu(self):
        print("----------- BOT DE BUSCA DE XML PYTHON ------------")
        print("Desenvolvido por : Maike Henrique"                  )
        print("--------------------V 2.0--------------------------\n")
        
bot = BotBuscaChavesNFCE()
bot.inicio()
