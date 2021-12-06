from sqlite3.dbapi2 import Error
from PyQt5 import uic, QtWidgets
import sqlite3
import math

def listar_dados():
    banco = sqlite3.connect('banco_cadastro.db') 
    cursor = banco.cursor()
    cursor.execute("SELECT * FROM dados")
    dados_lidos = cursor.fetchall()
    tela.tableWidget.setRowCount(len(dados_lidos))
    tela.tableWidget.setColumnCount(4)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 4):
           tela.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
    
    banco.close()

def salvar_dados():
    nome = tela.lineEdit.text()
    altura = float(tela.lineEdit_2.text())
    peso = float(tela.lineEdit_3.text())

    imc = 0
    imc = peso/(altura**2)

    tela.label_6.setText(str(round(imc, 2)))

    try:
        banco = sqlite3.connect('banco_cadastro.db')
        cursor = banco.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS dados (nome TEXT, altura DECIMAL, peso DECIMAL, imc DECIMAL);")
        cursor.execute(
            f"INSERT INTO dados VALUES('{nome}', {altura}, {peso}, {imc});")
        banco.commit()
        banco.close()
        print("Dados cadastrados com sucesso!")

    except sqlite3.Error as erro:
        print("Erro ao inserir dados: ", erro)


app = QtWidgets.QApplication([])
tela = uic.loadUi("janela.ui")
tela.pushButton.clicked.connect(salvar_dados)
tela.pushButton_2.clicked.connect(listar_dados)

tela.show()
app.exec()
