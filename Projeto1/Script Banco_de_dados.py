import tkinter as tk
import sqlite3 
import pandas as pd

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