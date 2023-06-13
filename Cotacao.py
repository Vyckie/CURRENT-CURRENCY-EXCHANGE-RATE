import requests
import customtkinter

def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''

    texto_cotações = customtkinter.CTkLabel(janela, text=texto)
    texto_cotações.grid(column=0, row=2, padx=0, pady=0)

customtkinter.set_appearance_mode("Dark")
janela = customtkinter.CTk()
janela.title("COTAÇÃO ATUAL DAS MOEDAS")
janela.geometry("360x300")
#janela.iconbitmap("cifrao.png") 
janela.resizable(False, False)

texto_orientação = customtkinter.CTkLabel(janela, text="CLIQUE ABAIXO PARA VIZUALIZAR AS COTAÇÕES", font=("Oswald", 14))
texto_orientação.grid(column=0, row=0, padx=15, pady=20)

botao = customtkinter.CTkButton(janela, text="BUSCAR COTAÇÕES", command=pegar_cotacoes)
botao.grid(column=0, row=1 ,padx=12, pady=15)

texto_versao = customtkinter.CTkLabel(janela, text="@vyckie.2023", font=("Courier New", 10))
texto_versao.grid(column=0, row=3, padx=15, pady=10)

janela.mainloop()