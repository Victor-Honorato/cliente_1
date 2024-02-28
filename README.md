# Cadastro de Clientes

Cadastro de Clientes
Este é um simples aplicativo de cadastro de clientes usando Tkinter e SQLite em Python.

Pré-requisitos
Antes de executar o aplicativo, certifique-se de ter instalado os seguintes pacotes:

tkinter: Biblioteca para criar interfaces gráficas.
pandas: Biblioteca para manipulação e análise de dados.
openpyxl: Biblioteca para trabalhar com arquivos Excel.

Configuração do Banco de Dados
O aplicativo utiliza um banco de dados SQLite para armazenar os dados dos clientes. Antes de executar o aplicativo, você precisa criar a tabela necessária no banco de dados. Execute o seguinte código para criar a tabela:

import sqlite3

conexao = sqlite3.connect('cliente.db')
cursor = conexao.cursor()

cursor.execute('''CREATE TABLE clientes(
            Nome text,
            Sobrenome text,
            Telefone text,
            Email text,               
            Profissão text)''')

conexao.commit()
conexao.close()

Executando o Aplicativo
Para executar o aplicativo, basta rodar o script cadastro_cliente.py

O aplicativo abrirá uma interface gráfica onde você pode cadastrar clientes e exportar os dados para um arquivo Excel.

Funcionalidades
Cadastrar Cliente: Preencha os campos de nome, sobrenome, telefone, e-mail e profissão e clique no botão "Cadastrar Cliente" para adicionar um novo cliente ao banco de dados.

Exportar para Excel: Clique no botão "Exportar para Excel" para gerar um arquivo Excel contendo todos os clientes cadastrados.

Observações
Certifique-se de ter as permissões adequadas para escrever no diretório onde o script está localizado. O aplicativo criará ou atualizará os arquivos cliente.db (banco de dados SQLite) e clientes.xlsx (arquivo Excel de exportação) no mesmo diretório do script.









