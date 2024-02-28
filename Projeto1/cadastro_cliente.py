import tkinter as tk
import sqlite3 
import pandas as pd
import openpyxl


janela = tk.Tk()
janela.title('Cadastro de Clientes')
janela. geometry("330x350")

#Função para cadastrar clientes no Banco
def cadastrar_cliente():
    conexao = sqlite3.connect('cliente.db')
    c = conexao.cursor()

    #Inserir dados na tabela:
    c.execute("INSERT INTO clientes VALUES (:nome,:sobrenome,:telefone,:email,:profissao)",
              {
			            'nome':entry_nome.get(),
                        'sobrenome': entry_sobrenome.get(),
                        'telefone':entry_telefone.get(),
                        'email': entry_email.get(),
                        'profissao': entry_profissao.get()
              })


    # Commit as mudanças:
    conexao.commit()

    # Fechar o banco de dados:
    conexao.close()

    # #Apaga os valores das caixas de entrada
    entry_nome.delete(0,"end")
    entry_sobrenome.delete(0,"end")
    entry_telefone.delete(0,"end")
    entry_email.delete(0,"end")
    entry_profissao.delete(0,"end")

    
#Função para exportar excel
def exporta_clientes():
    conexao = sqlite3.connect('cliente.db')
    c = conexao.cursor()

    # Inserir dados na tabela:
    c.execute("SELECT *, oid FROM clientes")
    clientes_cadastrados = c.fetchall()
    # print(clientes_cadastrados)
    clientes_cadastrados=pd.DataFrame(clientes_cadastrados,columns=['nome','sobrenome','telefone','email','profissao','Id_banco'])
    clientes_cadastrados.to_excel('clientes.xlsx')

    # Commit as mudanças:
    conexao.commit()

    # Fechar o banco de dados:
    conexao.close()




label_nome = tk.Label(janela, text='Nome')
label_nome.grid(row=1,column=0, padx=10, pady=10)

label_sobrenome = tk.Label(janela, text="Sobrenome")
label_sobrenome.grid(row=2, column=0, padx=10, pady=10)

label_telefone = tk.Label(janela, text="Telefone")
label_telefone.grid(row=3, column=0, padx=10, pady=10)

label_email = tk.Label(janela, text='E-mail')
label_email.grid(row=4, column=0 , padx=10, pady=10)

label_profissao = tk.Label(janela, text='Profissão')
label_profissao.grid(row=5, column=0 , padx=10, pady=10)


entry_nome = tk.Entry(janela , width =35)
entry_nome.grid(row=1,column=1, padx=10, pady=10)

entry_sobrenome = tk.Entry(janela, width =35)
entry_sobrenome.grid(row=2, column=1, padx=10, pady=10)

entry_telefone = tk.Entry(janela, width=35)
entry_telefone.grid(row=3, column=1, padx=10, pady=10)

entry_email = tk.Entry(janela, width =35)
entry_email.grid(row=4, column=1 , padx=10, pady=10)

entry_profissao = tk.Entry(janela, width =35)
entry_profissao.grid(row=5, column=1 , padx=10, pady=10)

#botões


# Botão de Cadastrar

botao_cadastrar = tk.Button(text='Cadastrar Cliente', command=cadastrar_cliente)
botao_cadastrar.grid(row=7, column=0,columnspan=2, padx=10, pady=10 , ipadx = 50)

# Botão de Exportar

botao_exportar = tk.Button(text='Exportar para Excel', command=exporta_clientes)
botao_exportar.grid(row=8, column=0,columnspan=2, padx=10, pady=10 , ipadx = 50)


janela.mainloop()
