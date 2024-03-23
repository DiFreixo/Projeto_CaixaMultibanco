# This Python file uses the following encoding: utf-8
from PySide6.QtCore import Qt, QTimer
from PySide6 import QtGui
from PySide6.QtWidgets import*
from ui_caixaMultibanco import Ui_form_Multibanco
#import warnings
#warnings.filterwarnings("ignore", "\nPyarrow", DeprecationWarning)
import pandas
import datetime

class CaixaMultibanco(QWidget, Ui_form_Multibanco):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # atributos da classe 'CaixaMultibanco'
        self.saldo = 1000
        self.nome = "Maria dos Santos"
        self.contaNum = "000123456789"
        self.pinNum = "1111"

        # estado inicial da interface
        self.lblMultibanco.setPixmap(QtGui.QPixmap("imagens/Marcar Código.png"))
        self.lblMultibanco.setScaledContents(True)

        # ativar botões 'Confirmar', 'Anular', 'Corrigir' e numéricos ao click
        self.btnMultibanco_confirmar.clicked.connect(self.verificar_pin)
        self.btnMultibanco_anular.clicked.connect(self.anular)
        self.btnMultibanco_corrigir.clicked.connect(self.corrigir)
        self.btnMultibanco_0.clicked.connect(self.insert0)
        self.btnMultibanco_00.clicked.connect(self.insert00)
        self.btnMultibanco_1.clicked.connect(self.insert1)
        self.btnMultibanco_2.clicked.connect(self.insert2)
        self.btnMultibanco_3.clicked.connect(self.insert3)
        self.btnMultibanco_4.clicked.connect(self.insert4)
        self.btnMultibanco_5.clicked.connect(self.insert5)
        self.btnMultibanco_6.clicked.connect(self.insert6)
        self.btnMultibanco_7.clicked.connect(self.insert7)
        self.btnMultibanco_8.clicked.connect(self.insert8)
        self.btnMultibanco_9.clicked.connect(self.insert9)
        self.btnMultibanco_ponto.clicked.connect(self.insertPonto)
        #desativar botões
        self.btnMultibanco_levantamentos.setEnabled(False)
        self.btnMultibanco_depositos.setEnabled(False)
        self.btnMultibanco_codigo.setEnabled(False)
        self.btnMultibanco_consultas.setEnabled(False)
        self.btnMultibanco_pagamentos.setEnabled(False)
        self.btnMultibanco_seta1.setEnabled(False)
        self.btnMultibanco_consultarIBAN.setEnabled(False)
        self.btnMultibanco_seta3.setEnabled(False)


        # caixa de texto para inserir o pin
        self.txtPin = QLineEdit(self)
        self.txtPin.setEchoMode(QLineEdit.Password)
        self.txtPin.resize(100,30)
        self.txtPin.move(455,270)
        self.txtPin.setMaxLength(4)
        # atribuir uma cor de fundo à caixa de texto e aumentar o tamanho da fonte
        self.txtPin.setStyleSheet("QLineEdit {background-color: blue;border: 3px blue;font-size: 25px;font-weight: bold;}")
        self.txtPin.setVisible(True)

        # caixa de texto para inserir o montante
        self.txtQuantia = QLineEdit(self)
        self.txtQuantia.resize(95,30)
        self.txtQuantia.move(287,237)
        self.txtQuantia.setMaxLength(5)
        # atribuir uma cor de fundo à caixa de texto e aumentar o tamanho da fonte
        self.txtQuantia.setStyleSheet("QLineEdit {background-color: blue;border: 3px blue;font-size: 25px;font-weight: bold;}")
        self.txtQuantia.setVisible(False)

        # caixa de texto para inserir o novo pin
        self.txtNovoPin = QLineEdit(self)
        self.txtNovoPin.setEchoMode(QLineEdit.Password)
        self.txtNovoPin.resize(95,30)
        self.txtNovoPin.move(449,260)
        self.txtNovoPin.setMaxLength(4)
        # atribuir uma cor de fundo à caixa de texto e aumentar o tamanho da fonte
        self.txtNovoPin.setStyleSheet("QLineEdit {background-color: blue;border: 3px blue;font-size: 25px;font-weight: bold;}")
        self.txtNovoPin.setVisible(False)

        # criar uma tabela para apresentar os dados
        self.tabelaDados = QTableWidget(self)
        self.tabelaDados.move(96, 61)
        self.tabelaDados.resize(491, 341)
        self.tabelaDados.setStyleSheet("QTableWidget {background-color: rgb(254, 251, 246);}")
        self.tabelaDados.verticalHeader().setVisible(False)
        self.tabelaDados.horizontalHeader().setVisible(False)
        self.tabelaDados.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tabelaDados.setShowGrid(False)
        self.tabelaDados.verticalScrollBar().hide()
        self.tabelaDados.horizontalScrollBar().hide()
        self.tabelaDados.setLayoutDirection(Qt.LeftToRight)
        self.tabelaDados.setVisible(False)
#------------------------------------------------------------------------------------------------------

    # Verificar se o código digitado está correto
    def verificar_pin(self):
        self.txtQuantia.setVisible(False)
        self.txtPin.setVisible(False)
        self.txtNovoPin.setVisible(False)
        self.txtNovoPin.clear()
        self.txtQuantia.clear()

        #obter o valor digitado no campo 'txtPin' e armazenar na variável 'pin'
        pin = self.txtPin.text()
        if(pin == self.pinNum):
            #imagem menuInicial
            self.lblMultibanco.setPixmap(QtGui.QPixmap("imagens/menuInicial.png"))
            self.lblMultibanco.setScaledContents(True)

            # Se o pin estiver correto ativar os botões
            self.btnMultibanco_levantamentos.setEnabled(True)
            self.btnMultibanco_depositos.setEnabled(True)
            self.btnMultibanco_codigo.setEnabled(True)
            self.btnMultibanco_consultas.setEnabled(True)
            self.btnMultibanco_pagamentos.setEnabled(True)
            self.btnMultibanco_seta1.setEnabled(True)
            self.btnMultibanco_consultarIBAN.setEnabled(True)
            self.btnMultibanco_seta3.setEnabled(True)

            self.btnMultibanco_levantamentos.clicked.connect(lambda checked=False: self.botao_clicked(self.btnMultibanco_levantamentos))
            self.btnMultibanco_depositos.clicked.connect(lambda checked=False: self.botao_clicked(self.btnMultibanco_depositos))
            self.btnMultibanco_codigo.clicked.connect(lambda checked=False: self.botao_clicked(self.btnMultibanco_codigo))
            self.btnMultibanco_consultas.clicked.connect(self.consultar_conta)
            self.btnMultibanco_pagamentos.clicked.connect(self.pagamentos)

        else:
            self.lblMultibanco.setText("Pin incorreto...")
            QTimer.singleShot(3000, self.anular)
#------------------------------------------------------------------------------------------------------

    # Botão 'Corrigir'
    def corrigir(self):
        self.txtPin.clear()
        self.txtQuantia.clear()
        self.txtNovoPin.clear()
#------------------------------------------------------------------------------------------------------

    # Botão 'Anular'
    def anular(self):
        self.txtPin.setVisible(False)
        self.txtQuantia.setVisible(False)
        self.txtNovoPin.setVisible(False)
        self.txtPin.clear()
        self.txtQuantia.clear()
        self.txtNovoPin.clear()
        self.lblMultibanco.setText("Operação anulada!\nPor favor retire o seu cartão...")
        # Define um temporizador para chamar reset_interface após 3 segundos
        QTimer.singleShot(3000, self.reset_interface)  # 3000 ms = 3 segundos
#------------------------------------------------------------------------------------------------------

    # Verificar qual botão foi pressionado
    def botao_clicked(self, btn):
        # Desconecta todos os slots conectados anteriormente ao sinal clicked do botão 'Confirmar'
        self.btnMultibanco_confirmar.clicked.disconnect()
        self.btn = btn
        if self.btn == self.btnMultibanco_levantamentos:
            self.lblMultibanco.setPixmap(QtGui.QPixmap("imagens/introduzaMontante.png"))
            self.txtQuantia.setVisible(True)
            # conecta o novo slot
            self.btnMultibanco_confirmar.clicked.connect(self.levantar_dinheiro)
            # desativar botões
            self.btnMultibanco_levantamentos.setEnabled(True)
            self.btnMultibanco_depositos.setEnabled(False)
            self.btnMultibanco_codigo.setEnabled(False)
            self.btnMultibanco_consultas.setEnabled(False)
            self.btnMultibanco_pagamentos.setEnabled(False)
            self.btnMultibanco_seta1.setEnabled(False)
            self.btnMultibanco_consultarIBAN.setEnabled(False)
            self.btnMultibanco_seta3.setEnabled(False)

        elif self.btn == self.btnMultibanco_depositos:
            self.lblMultibanco.setPixmap(QtGui.QPixmap("imagens/introduzaMontante.png"))
            self.txtQuantia.setVisible(True)
            # conecta o novo slot
            self.btnMultibanco_confirmar.clicked.connect(self.depositar_dinheiro)
            # desativar botões
            self.btnMultibanco_levantamentos.setEnabled(False)
            self.btnMultibanco_depositos.setEnabled(True)
            self.btnMultibanco_codigo.setEnabled(False)
            self.btnMultibanco_consultas.setEnabled(False)
            self.btnMultibanco_pagamentos.setEnabled(False)
            self.btnMultibanco_seta1.setEnabled(False)
            self.btnMultibanco_consultarIBAN.setEnabled(False)
            self.btnMultibanco_seta3.setEnabled(False)

        elif self.btn == self.btnMultibanco_codigo:
            self.lblMultibanco.setPixmap(QtGui.QPixmap("imagens/novoCodigo.png"))
            self.txtNovoPin.setVisible(True)
            # conecta o novo slot
            self.btnMultibanco_confirmar.clicked.connect(self.alterar_pin)
            # desativar botões
            self.btnMultibanco_levantamentos.setEnabled(False)
            self.btnMultibanco_depositos.setEnabled(False)
            self.btnMultibanco_codigo.setEnabled(True)
            self.btnMultibanco_consultas.setEnabled(False)
            self.btnMultibanco_pagamentos.setEnabled(False)
            self.btnMultibanco_seta1.setEnabled(False)
            self.btnMultibanco_consultarIBAN.setEnabled(False)
            self.btnMultibanco_seta3.setEnabled(False)
 #------------------------------------------------------------------------------------------------------

    # Depósitos
    def depositar_dinheiro(self):
        self.txtQuantia.setVisible(False)
        self.txtPin.setVisible(False)
        self.txtNovoPin.setVisible(False)
        self.txtPin.clear()
        self.txtNovoPin.clear()
        try:
            # Obter o valor digitado no campo 'txtQuantia' e armazenar na variável 'quantia_str'
            self.quantia_str = self.txtQuantia.text()
            # Remover espaços em branco e verificar se a string não está vazia
            self.quantia_str = self.quantia_str.strip()
            if self.quantia_str == "":
                # caso a string estiver vazia, avisar o utilizador
                self.lblMultibanco.setText("Por favor, insira o montante a depositar.")
                QTimer.singleShot(3000, self.return_menuInicial)
            else:
                # Tentar converter a string para float
                self.quantia = float(self.quantia_str)
                self.saldo = self.saldo + self.quantia
                self.lblMultibanco.setText(f"Depósito de {self.quantia} Euros\n efetuado com sucesso!")
                QTimer.singleShot(4000, self.return_menuInicial)

        except ValueError:
            # Se a conversão para float falhar, avisar o utilizador
            self.lblMultibanco.setText("O montante inserido não é um número válido.")
            QTimer.singleShot(3000, self.anular)
#------------------------------------------------------------------------------------------------------

    # Levantamentos
    def levantar_dinheiro(self):
        self.txtQuantia.setVisible(False)
        self.txtPin.setVisible(False)
        self.txtNovoPin.setVisible(False)
        self.txtPin.clear()
        self.txtNovoPin.clear()

        try:
            # Obter o valor digitado no campo 'txtQuantia' e armazenar na variável 'quantia_str'
            self.quantia_str = self.txtQuantia.text()
            # Remover espaços em branco e verificar se a string não está vazia
            self.quantia_str = self.quantia_str.strip()
            if self.quantia_str == "":
                # caso a string estiver vazia, avisar o utilizador
                self.lblMultibanco.setText("Por favor, insira o montante a levantar.")
                QTimer.singleShot(3000, self.return_menuInicial)
            else:
                # Tentar converter a string para float
                self.quantia = float(self.quantia_str)
                if self.quantia > self.saldo:
                    self.lblMultibanco.setText("Saldo insuficiente!")
                    QTimer.singleShot(3000, self.return_menuInicial)
                else:
                    self.saldo = self.saldo - self.quantia
                    self.lblMultibanco.setText(f"Levantamento de {self.quantia} Euros\n Por favor retire o seu dinheiro")
                    QTimer.singleShot(4000, self.return_menuInicial)
        except ValueError:
            # Se a conversão para float falhar, avisar o utilizador
            self.lblMultibanco.setText("O montante inserido não é um número válido.")
            QTimer.singleShot(3000, self.anular)
 #------------------------------------------------------------------------------------------------------

    # Pagamentos
    def pagamentos(self):
        self.txtPin.setVisible(False)
        self.txtQuantia.setVisible(False)
        self.txtNovoPin.setVisible(False)
        self.lblMultibanco.setPixmap(QtGui.QPixmap("imagens/pagamentos.png"))
        # desativar botões
        self.btnMultibanco_levantamentos.setEnabled(False)
        self.btnMultibanco_depositos.setEnabled(False)
        self.btnMultibanco_codigo.setEnabled(False)
        self.btnMultibanco_consultas.setEnabled(False)
        self.btnMultibanco_pagamentos.setEnabled(True)
        self.btnMultibanco_seta1.setEnabled(False)
        self.btnMultibanco_consultarIBAN.setEnabled(False)
        self.btnMultibanco_seta3.setEnabled(False)
        QTimer.singleShot(4000, self.anular)
#------------------------------------------------------------------------------------------------------

    # Alterar Código Secreto
    def alterar_pin(self):
        self.txtQuantia.setVisible(False)
        self.txtPin.setVisible(False)
        self.txtNovoPin.setVisible(False)
        self.txtPin.clear()
        self.txtQuantia.clear()

        # Obter o valor digitado no campo 'txtNovoPin' e armazenar na variável 'novoPin'
        novoPin = self.txtNovoPin.text()
        # verificar se a variável não está vazia
        if novoPin == "":
            # caso a string estiver vazia, avisar o utilizador
            self.lblMultibanco.setText("Por favor, insira o novo código secreto.")
            QTimer.singleShot(3000, self.return_menuInicial)
        else:
            self.pinNum = novoPin
            self.lblMultibanco.setText("Código secreto alterado com sucesso!")
            QTimer.singleShot(4000, self.return_menuInicial)
#------------------------------------------------------------------------------------------------------

    # Consultas
    def consultar_conta(self):
        self.txtQuantia.setVisible(False)
        self.txtPin.setVisible(False)
        self.txtNovoPin.setVisible(False)
        self.txtPin.clear()
        self.txtQuantia.clear()
        self.txtNovoPin.clear()
        self.lblMultibanco.setPixmap(QtGui.QPixmap("imagens/consultas.png"))
        # desativar botões
        self.btnMultibanco_levantamentos.setEnabled(False)
        self.btnMultibanco_depositos.setEnabled(False)
        self.btnMultibanco_codigo.setEnabled(False)
        self.btnMultibanco_consultas.setEnabled(True)
        self.btnMultibanco_pagamentos.setEnabled(False)
        self.btnMultibanco_seta1.setEnabled(False)
        self.btnMultibanco_consultarIBAN.setEnabled(True)
        self.btnMultibanco_seta3.setEnabled(False)
        # desconecta o slot conectado anteriormente ao sinal clicked do botão 'Consultas'
        self.btnMultibanco_consultas.clicked.disconnect()
        # conecta o novo slot ao do botão 'Consultas'
        self.btnMultibanco_consultas.clicked.connect(self.consultar_saldo)
        self.btnMultibanco_consultarIBAN.clicked.connect(self.consultar_IBAN)
#------------------------------------------------------------------------------------------------------

    # Consultar Saldo da conta
    def consultar_saldo(self):
        self.txtQuantia.setVisible(False)
        self.txtPin.setVisible(False)
        self.txtNovoPin.setVisible(False)
        self.txtPin.clear()
        self.txtQuantia.clear()
        self.txtNovoPin.clear()
        self.btnMultibanco_consultarIBAN.setEnabled(True)
        dataHoje = datetime.datetime.now().strftime('%d/%m/%y - %H:%M')

        # limpar a tabela
        self.tabelaDados.setRowCount(0)
        # configuração das linhas e colunas da tabela
        self.tabelaDados.setRowCount(4)
        self.tabelaDados.setColumnCount(2)
        # preenchimento da tabela com os dados
        self.tabelaDados.setItem(0, 0, QTableWidgetItem("Data:"))
        self.tabelaDados.setItem(0, 1, QTableWidgetItem(dataHoje))
        self.tabelaDados.setItem(1, 0, QTableWidgetItem("Conta:"))
        self.tabelaDados.setItem(1, 1, QTableWidgetItem(self.contaNum))
        self.tabelaDados.setItem(2, 0, QTableWidgetItem("Cliente:"))
        self.tabelaDados.setItem(2, 1, QTableWidgetItem(self.nome))
        self.tabelaDados.setItem(3, 0, QTableWidgetItem("Saldo:"))
        self.tabelaDados.setItem(3, 1, QTableWidgetItem(str(self.saldo)+ " Euros"))

        # adicionar uma linha e uma coluna ao início da tabela
        self.tabelaDados.insertRow(0)
        self.tabelaDados.insertColumn(0)
        # unir a primeira linha da tabela
        self.tabelaDados.setSpan(0, 1, 1, self.tabelaDados.columnCount())
        # atribuir uma largura  a uma coluna específica da tabela
        self.tabelaDados.setColumnWidth(2,200)
        # atribuir uma altura a uma linha específica da tabela
        self.tabelaDados.setRowHeight(0,50)
        # atribuir uma imagem à primeira linha da tabela
        headerItem = QLabel()
        headerItem.setPixmap(QtGui.QPixmap("imagens/multibanco.jpg"))
        headerItem.setScaledContents(True)
        self.tabelaDados.setCellWidget(0, 1, headerItem)
        # exibir a tabela
        self.tabelaDados.show()

        # chamar o método para exportar o saldo
        self.exportarCSV()
        # após 4 segundos retonar ao menu inicial
        QTimer.singleShot(4000, self.return_menuInicial)

    # exportar saldo da conta (usar módulo Pandas para exportar dados)
    def exportarCSV(self):
        rowCount = self.tabelaDados.rowCount()
        columnCount = self.tabelaDados.columnCount()

        data = []
        for row in range(rowCount):
            rowData = []
            for column in range(columnCount):
                widgetItem = self.tabelaDados.item(row, column)
                if widgetItem and widgetItem.text:
                    rowData.append(widgetItem.text())
                else:
                    rowData.append('NULL')
            data.append(rowData)

        dataframe = pandas.DataFrame(data)
        dataframe.to_csv('files/ConsultarSaldo.csv', header=False, index=False)
        #print('Ficheiro CSV exportado!')
#------------------------------------------------------------------------------------------------------

    # Consultar IBAN da conta
    def consultar_IBAN(self):
        self.txtQuantia.setVisible(False)
        self.txtPin.setVisible(False)
        self.txtNovoPin.setVisible(False)
        self.txtPin.clear()
        self.txtQuantia.clear()
        self.txtNovoPin.clear()
        self.btnMultibanco_consultas.setEnabled(False)
        self.lblMultibanco.hide()
        # chama o método responsável pela importação dos dados
        QTimer.singleShot(0, self.importarCSV)

    # importar os dados da conta
    def importarCSV(self):
        # usar módulo Pandas para importar os dados
        fileName = "files/ConsultarIBAN.csv"
        dados = pandas.read_csv(fileName, sep=';')
        # limpar a tabela
        self.tabelaDados.setRowCount(0)
        # configuração das linhas e colunas com base no DataFrame
        self.tabelaDados.setRowCount(dados.shape[0])
        self.tabelaDados.setColumnCount(dados.shape[1])

        # preenchimento da tabela com os dados importados
        for row_index, row in dados.iterrows():
            for col_index, item in enumerate(row):
                self.tableItem = QTableWidgetItem(str(item))
                self.tabelaDados.setItem(row_index, col_index,self.tableItem)
                # alinhar o texto das colunas
                if col_index == 0:
                    self.tableItem.setTextAlignment(Qt.AlignLeft)
                else:
                    self.tableItem.setTextAlignment(Qt.AlignRight)

        # adicionar uma linha e uma coluna ao início da tabela
        self.tabelaDados.insertRow(0)
        self.tabelaDados.insertColumn(0)
        # unir a primeira linha da tabela
        self.tabelaDados.setSpan(0, 1, 1, self.tabelaDados.columnCount())
        # atribuir uma largura  a uma coluna específica da tabela
        self.tabelaDados.setColumnWidth(2,200)
        # atribuir uma altura a uma linha específica da tabela
        self.tabelaDados.setRowHeight(0,50)
        # atribuir uma imagem à primeira linha da tabela
        headerItem = QLabel()
        headerItem.setPixmap(QtGui.QPixmap("imagens/multibanco.jpg"))
        headerItem.setScaledContents(True)
        self.tabelaDados.setCellWidget(0, 1, headerItem)

        # exibir a tabela para apresentação dos dados importados
        self.tabelaDados.show()
        # após 4 segundos retonar ao menu inicial
        QTimer.singleShot(4000, self.return_menuInicial)
#------------------------------------------------------------------------------------------------------

    # Retornar ao menu inicial
    def return_menuInicial(self):
        self.txtQuantia.clear()
        self.txtNovoPin.clear()
        self.tabelaDados.setVisible(False)
        # desconecta o slot conectado anteriormente ao sinal clicked do botão 'Consultas'
        self.btnMultibanco_consultas.clicked.disconnect()
        #imagem menuInicial 
        self.lblMultibanco.setPixmap(QtGui.QPixmap("imagens/menuInicial.png"))
        self.lblMultibanco.setScaledContents(True)
        self.lblMultibanco.show()
        # ativar botões
        self.btnMultibanco_levantamentos.setEnabled(True)
        self.btnMultibanco_depositos.setEnabled(True)
        self.btnMultibanco_codigo.setEnabled(True)
        self.btnMultibanco_consultas.setEnabled(True)
        self.btnMultibanco_pagamentos.setEnabled(True)
        self.btnMultibanco_seta1.setEnabled(True)
        self.btnMultibanco_consultarIBAN.setEnabled(True)
        self.btnMultibanco_seta3.setEnabled(True)

        self.btnMultibanco_levantamentos.clicked.connect(lambda checked=False: self.botao_clicked(self.btnMultibanco_levantamentos))
        self.btnMultibanco_depositos.clicked.connect(lambda checked=False: self.botao_clicked(self.btnMultibanco_depositos))
        self.btnMultibanco_codigo.clicked.connect(lambda checked=False: self.botao_clicked(self.btnMultibanco_codigo))
        self.btnMultibanco_consultas.clicked.connect(self.consultar_conta)
        self.btnMultibanco_pagamentos.clicked.connect(self.pagamentos)
#------------------------------------------------------------------------------------------------------

    # Restaurar o estado inicial da interface, tal como estava quando a aplicação foi iniciada
    def reset_interface(self):
        self.txtPin.setVisible(True)
        self.txtQuantia.setVisible(False)
        self.txtNovoPin.setVisible(False)
        self.txtPin.clear()
        self.txtQuantia.clear()
        self.txtNovoPin.clear()

        self.lblMultibanco.setPixmap(QtGui.QPixmap("imagens/Marcar Código.png"))
        self.lblMultibanco.setScaledContents(True)

        #desativar botões
        self.btnMultibanco_levantamentos.setEnabled(False)
        self.btnMultibanco_depositos.setEnabled(False)
        self.btnMultibanco_codigo.setEnabled(False)
        self.btnMultibanco_consultas.setEnabled(False)
        self.btnMultibanco_pagamentos.setEnabled(False)
        self.btnMultibanco_seta1.setEnabled(False)
        self.btnMultibanco_consultarIBAN.setEnabled(False)
        self.btnMultibanco_seta3.setEnabled(False)
        # Desconecta todos os slots conectados anteriormente ao sinal clicked do botão 'Confirmar'
        self.btnMultibanco_confirmar.clicked.disconnect()
        # conecta o novo slot
        self.btnMultibanco_confirmar.clicked.connect(self.verificar_pin)
 #------------------------------------------------------------------------------------------------------

    #Atribuir valores ao botões
    def insert0(self):
        self.btnMultibanco_0 = 0
        self.txtPin.insert(str(self.btnMultibanco_0))
        self.txtQuantia.insert(str(self.btnMultibanco_0))
        self.txtNovoPin.insert(str(self.btnMultibanco_0))
    def insert00(self):
        self.btnMultibanco_00 = '00'
        self.txtPin.insert(str(self.btnMultibanco_00))
        self.txtQuantia.insert(str(self.btnMultibanco_00))
        self.txtNovoPin.insert(str(self.btnMultibanco_00))
    def insert1(self):
        self.btnMultibanco_1 = 1
        self.txtPin.insert(str(self.btnMultibanco_1))
        self.txtQuantia.insert(str(self.btnMultibanco_1))
        self.txtNovoPin.insert(str(self.btnMultibanco_1))
    def insert2(self):
        self.btnMultibanco_2 = 2
        self.txtPin.insert(str(self.btnMultibanco_2))
        self.txtQuantia.insert(str(self.btnMultibanco_2))
        self.txtNovoPin.insert(str(self.btnMultibanco_2))
    def insert3(self):
        self.btnMultibanco_3 = 3
        self.txtPin.insert(str(self.btnMultibanco_3))
        self.txtQuantia.insert(str(self.btnMultibanco_3))
        self.txtNovoPin.insert(str(self.btnMultibanco_3))
    def insert4(self):
        self.btnMultibanco_4 = 4
        self.txtPin.insert(str(self.btnMultibanco_4))
        self.txtQuantia.insert(str(self.btnMultibanco_4))
        self.txtNovoPin.insert(str(self.btnMultibanco_4))
    def insert5(self):
        self.btnMultibanco_5 = 5
        self.txtPin.insert(str(self.btnMultibanco_5))
        self.txtQuantia.insert(str(self.btnMultibanco_5))
        self.txtNovoPin.insert(str(self.btnMultibanco_5))
    def insert6(self):
        self.btnMultibanco_6 = 6
        self.txtPin.insert(str(self.btnMultibanco_6))
        self.txtQuantia.insert(str(self.btnMultibanco_6))
        self.txtNovoPin.insert(str(self.btnMultibanco_6))
    def insert7(self):
        self.btnMultibanco_7 = 7
        self.txtPin.insert(str(self.btnMultibanco_7))
        self.txtQuantia.insert(str(self.btnMultibanco_7))
        self.txtNovoPin.insert(str(self.btnMultibanco_7))
    def insert8(self):
        self.btnMultibanco_8 = 8
        self.txtPin.insert(str(self.btnMultibanco_8))
        self.txtQuantia.insert(str(self.btnMultibanco_8))
        self.txtNovoPin.insert(str(self.btnMultibanco_8))
    def insert9(self):
        self.btnMultibanco_9 = 9
        self.txtPin.insert(str(self.btnMultibanco_9))
        self.txtQuantia.insert(str(self.btnMultibanco_9))
        self.txtNovoPin.insert(str(self.btnMultibanco_9))
    def insertPonto(self):
        self.btnMultibanco_ponto = '.'
        self.txtPin.insert(str(self.btnMultibanco_ponto))
        self.txtQuantia.insert(str(self.btnMultibanco_ponto))
#------------------------------------------------------------------------------------------------------
