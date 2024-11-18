# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 850)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QMainWindow {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, \n"
"                                stop:0 #000000,  /*Top */\n"
"                                stop:0.5 #1C1B1A,   /* Center */\n"
"                                stop:1 #383633);       /* Buttom */\n"
"}")
        MainWindow.setAnimated(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.justPB = QtWidgets.QPushButton(self.centralwidget)
        self.justPB.setEnabled(True)
        self.justPB.setGeometry(QtCore.QRect(40, -50, 320, 400))
        self.justPB.setStyleSheet("QPushButton#justPB {\n"
"    border-radius: 30px;\n"
"    background-color: green; \n"
"    padding: 10px; \n"
"    color: white;\n"
"}")
        self.justPB.setText("")
        self.justPB.setObjectName("justPB")
        self.lbl_CurrentPokemon = QtWidgets.QLabel(self.centralwidget)
        self.lbl_CurrentPokemon.setGeometry(QtCore.QRect(50, 30, 300, 300))
        self.lbl_CurrentPokemon.setText("")
        self.lbl_CurrentPokemon.setPixmap(QtGui.QPixmap("imagesHQ/001.png"))
        self.lbl_CurrentPokemon.setScaledContents(True)
        self.lbl_CurrentPokemon.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_CurrentPokemon.setObjectName("lbl_CurrentPokemon")
        self.lbl_PokemonName = QtWidgets.QLabel(self.centralwidget)
        self.lbl_PokemonName.setGeometry(QtCore.QRect(25, 360, 350, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_PokemonName.setFont(font)
        self.lbl_PokemonName.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.lbl_PokemonName.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_PokemonName.setObjectName("lbl_PokemonName")
        self.btn_Type1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Type1.setGeometry(QtCore.QRect(50, 420, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_Type1.setFont(font)
        self.btn_Type1.setStyleSheet("QPushButton#btn_Type1 {\n"
"    border-radius: 15px;\n"
"    background-color: green; \n"
"    padding: 10px; \n"
"    color: white;\n"
"}")
        self.btn_Type1.setObjectName("btn_Type1")
        self.btn_Type2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Type2.setGeometry(QtCore.QRect(250, 420, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_Type2.setFont(font)
        self.btn_Type2.setStyleSheet("QPushButton#btn_Type2 {\n"
"    border-radius: 15px;\n"
"    background-color: purple; \n"
"    padding: 10px; \n"
"    color: white;\n"
"}")
        self.btn_Type2.setObjectName("btn_Type2")
        self.lbl_PokemonWeight = QtWidgets.QLabel(self.centralwidget)
        self.lbl_PokemonWeight.setGeometry(QtCore.QRect(50, 470, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_PokemonWeight.setFont(font)
        self.lbl_PokemonWeight.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.lbl_PokemonWeight.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_PokemonWeight.setObjectName("lbl_PokemonWeight")
        self.lbl_PokemonHeight = QtWidgets.QLabel(self.centralwidget)
        self.lbl_PokemonHeight.setGeometry(QtCore.QRect(250, 470, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_PokemonHeight.setFont(font)
        self.lbl_PokemonHeight.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.lbl_PokemonHeight.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_PokemonHeight.setObjectName("lbl_PokemonHeight")
        self.le_search = QtWidgets.QLineEdit(self.centralwidget)
        self.le_search.setGeometry(QtCore.QRect(125, 770, 150, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.le_search.setFont(font)
        self.le_search.setObjectName("le_search")
        self.lbl_JustWeight = QtWidgets.QLabel(self.centralwidget)
        self.lbl_JustWeight.setGeometry(QtCore.QRect(50, 505, 100, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_JustWeight.setFont(font)
        self.lbl_JustWeight.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.lbl_JustWeight.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_JustWeight.setObjectName("lbl_JustWeight")
        self.lbl_JustHeight = QtWidgets.QLabel(self.centralwidget)
        self.lbl_JustHeight.setGeometry(QtCore.QRect(250, 505, 100, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_JustHeight.setFont(font)
        self.lbl_JustHeight.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.lbl_JustHeight.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_JustHeight.setObjectName("lbl_JustHeight")
        self.pb_Hp = QtWidgets.QProgressBar(self.centralwidget)
        self.pb_Hp.setGeometry(QtCore.QRect(60, 570, 290, 20))
        self.pb_Hp.setStyleSheet("QProgressBar {\n"
"    border: 1px solid #000;\n"
"    border-radius: 5px;\n"
"    background-color: #E0E0E0; /* Neutral background */\n"
"}\n"
"QProgressBar::chunk {\n"
"    background-color: #FF6B6B; /* Stat color */\n"
"    border-radius: 5px;\n"
"}")
        self.pb_Hp.setMaximum(700)
        self.pb_Hp.setProperty("value", 45)
        self.pb_Hp.setTextVisible(False)
        self.pb_Hp.setFormat("")
        self.pb_Hp.setObjectName("pb_Hp")
        self.pb_Attack = QtWidgets.QProgressBar(self.centralwidget)
        self.pb_Attack.setGeometry(QtCore.QRect(60, 600, 290, 20))
        self.pb_Attack.setStyleSheet("QProgressBar {\n"
"    border: 1px solid #000;\n"
"    border-radius: 5px;\n"
"    background-color: #E0E0E0; /* Neutral background */\n"
"}\n"
"QProgressBar::chunk {\n"
"    background-color: #F9A825; /* Stat color */\n"
"    border-radius: 5px;\n"
"}")
        self.pb_Attack.setMaximum(460)
        self.pb_Attack.setProperty("value", 49)
        self.pb_Attack.setTextVisible(False)
        self.pb_Attack.setFormat("")
        self.pb_Attack.setObjectName("pb_Attack")
        self.lbl_JustHp = QtWidgets.QLabel(self.centralwidget)
        self.lbl_JustHp.setGeometry(QtCore.QRect(10, 570, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_JustHp.setFont(font)
        self.lbl_JustHp.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.lbl_JustHp.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbl_JustHp.setObjectName("lbl_JustHp")
        self.lbl_JustAtk = QtWidgets.QLabel(self.centralwidget)
        self.lbl_JustAtk.setGeometry(QtCore.QRect(10, 600, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_JustAtk.setFont(font)
        self.lbl_JustAtk.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.lbl_JustAtk.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbl_JustAtk.setObjectName("lbl_JustAtk")
        self.pb_Defense = QtWidgets.QProgressBar(self.centralwidget)
        self.pb_Defense.setGeometry(QtCore.QRect(60, 630, 290, 20))
        self.pb_Defense.setStyleSheet("QProgressBar {\n"
"    border: 1px solid #000;\n"
"    border-radius: 5px;\n"
"    background-color: #E0E0E0; /* Neutral background */\n"
"}\n"
"QProgressBar::chunk {\n"
"    background-color: #42A5F5; /* Stat color */\n"
"    border-radius: 5px;\n"
"}")
        self.pb_Defense.setMaximum(460)
        self.pb_Defense.setProperty("value", 49)
        self.pb_Defense.setTextVisible(False)
        self.pb_Defense.setFormat("")
        self.pb_Defense.setObjectName("pb_Defense")
        self.pb_SpAttack = QtWidgets.QProgressBar(self.centralwidget)
        self.pb_SpAttack.setGeometry(QtCore.QRect(60, 660, 290, 20))
        self.pb_SpAttack.setStyleSheet("QProgressBar {\n"
"    border: 1px solid #000;\n"
"    border-radius: 5px;\n"
"    background-color: #E0E0E0; /* Neutral background */\n"
"}\n"
"QProgressBar::chunk {\n"
"    background-color: #AB47BC; /* Stat color */\n"
"    border-radius: 5px;\n"
"}")
        self.pb_SpAttack.setMaximum(460)
        self.pb_SpAttack.setProperty("value", 65)
        self.pb_SpAttack.setTextVisible(False)
        self.pb_SpAttack.setFormat("")
        self.pb_SpAttack.setObjectName("pb_SpAttack")
        self.pb_SpDefense = QtWidgets.QProgressBar(self.centralwidget)
        self.pb_SpDefense.setGeometry(QtCore.QRect(60, 690, 290, 20))
        self.pb_SpDefense.setStyleSheet("QProgressBar {\n"
"    border: 1px solid #000;\n"
"    border-radius: 5px;\n"
"    background-color: #E0E0E0; /* Neutral background */\n"
"}\n"
"QProgressBar::chunk {\n"
"    background-color: #66BB6A; /* Stat color */\n"
"    border-radius: 5px;\n"
"}")
        self.pb_SpDefense.setMaximum(460)
        self.pb_SpDefense.setProperty("value", 65)
        self.pb_SpDefense.setTextVisible(False)
        self.pb_SpDefense.setFormat("")
        self.pb_SpDefense.setObjectName("pb_SpDefense")
        self.pb_Speed = QtWidgets.QProgressBar(self.centralwidget)
        self.pb_Speed.setGeometry(QtCore.QRect(60, 720, 290, 20))
        self.pb_Speed.setStyleSheet("QProgressBar {\n"
"    border: 1px solid #000;\n"
"    border-radius: 5px;\n"
"    background-color: #E0E0E0; /* Neutral background */\n"
"}\n"
"QProgressBar::chunk {\n"
"    background-color: #FF7043; /* Stat color */\n"
"    border-radius: 5px;\n"
"}")
        self.pb_Speed.setMaximum(460)
        self.pb_Speed.setProperty("value", 45)
        self.pb_Speed.setTextVisible(False)
        self.pb_Speed.setFormat("")
        self.pb_Speed.setObjectName("pb_Speed")
        self.lbl_JustDef = QtWidgets.QLabel(self.centralwidget)
        self.lbl_JustDef.setGeometry(QtCore.QRect(10, 630, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_JustDef.setFont(font)
        self.lbl_JustDef.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.lbl_JustDef.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbl_JustDef.setObjectName("lbl_JustDef")
        self.lbl_JustSpAtk = QtWidgets.QLabel(self.centralwidget)
        self.lbl_JustSpAtk.setGeometry(QtCore.QRect(10, 660, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_JustSpAtk.setFont(font)
        self.lbl_JustSpAtk.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.lbl_JustSpAtk.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbl_JustSpAtk.setObjectName("lbl_JustSpAtk")
        self.lbl_JustSpDef = QtWidgets.QLabel(self.centralwidget)
        self.lbl_JustSpDef.setGeometry(QtCore.QRect(10, 690, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_JustSpDef.setFont(font)
        self.lbl_JustSpDef.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.lbl_JustSpDef.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbl_JustSpDef.setObjectName("lbl_JustSpDef")
        self.lbl_JustSpeed = QtWidgets.QLabel(self.centralwidget)
        self.lbl_JustSpeed.setGeometry(QtCore.QRect(10, 720, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_JustSpeed.setFont(font)
        self.lbl_JustSpeed.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.lbl_JustSpeed.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbl_JustSpeed.setObjectName("lbl_JustSpeed")
        self.lbl_Hp = QtWidgets.QLabel(self.centralwidget)
        self.lbl_Hp.setGeometry(QtCore.QRect(360, 570, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_Hp.setFont(font)
        self.lbl_Hp.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.lbl_Hp.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbl_Hp.setObjectName("lbl_Hp")
        self.lbl_Atk = QtWidgets.QLabel(self.centralwidget)
        self.lbl_Atk.setGeometry(QtCore.QRect(360, 600, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_Atk.setFont(font)
        self.lbl_Atk.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.lbl_Atk.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbl_Atk.setObjectName("lbl_Atk")
        self.lbl_Def = QtWidgets.QLabel(self.centralwidget)
        self.lbl_Def.setGeometry(QtCore.QRect(360, 630, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_Def.setFont(font)
        self.lbl_Def.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.lbl_Def.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbl_Def.setObjectName("lbl_Def")
        self.lbl_SpAtk = QtWidgets.QLabel(self.centralwidget)
        self.lbl_SpAtk.setGeometry(QtCore.QRect(360, 660, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_SpAtk.setFont(font)
        self.lbl_SpAtk.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.lbl_SpAtk.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbl_SpAtk.setObjectName("lbl_SpAtk")
        self.lbl_SpDef = QtWidgets.QLabel(self.centralwidget)
        self.lbl_SpDef.setGeometry(QtCore.QRect(360, 690, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_SpDef.setFont(font)
        self.lbl_SpDef.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.lbl_SpDef.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbl_SpDef.setObjectName("lbl_SpDef")
        self.lbl_Speed = QtWidgets.QLabel(self.centralwidget)
        self.lbl_Speed.setGeometry(QtCore.QRect(360, 720, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_Speed.setFont(font)
        self.lbl_Speed.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.lbl_Speed.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbl_Speed.setObjectName("lbl_Speed")
        self.lbl_PokemonID = QtWidgets.QLabel(self.centralwidget)
        self.lbl_PokemonID.setGeometry(QtCore.QRect(60, 0, 81, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_PokemonID.setFont(font)
        self.lbl_PokemonID.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.lbl_PokemonID.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbl_PokemonID.setObjectName("lbl_PokemonID")
        self.lbl_JustSearchLabel = QtWidgets.QLabel(self.centralwidget)
        self.lbl_JustSearchLabel.setGeometry(QtCore.QRect(100, 750, 200, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_JustSearchLabel.setFont(font)
        self.lbl_JustSearchLabel.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.lbl_JustSearchLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_JustSearchLabel.setObjectName("lbl_JustSearchLabel")
        self.btn_Seach = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Seach.setGeometry(QtCore.QRect(150, 800, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_Seach.setFont(font)
        self.btn_Seach.setStyleSheet("QPushButton {\n"
"    border-radius: 9px;\n"
"    background-color: yellow; \n"
"    padding: 10px; \n"
"    color: black;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: blue; \n"
"    color: white;\n"
"}\n"
"")
        self.btn_Seach.setObjectName("btn_Seach")
        self.btn_Prev = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Prev.setGeometry(QtCore.QRect(40, 770, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.btn_Prev.setFont(font)
        self.btn_Prev.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: gray; \n"
"    padding: 10px; \n"
"    color: black;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: blue; \n"
"    color: white;\n"
"}\n"
"")
        self.btn_Prev.setObjectName("btn_Prev")
        self.btn_Next = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Next.setGeometry(QtCore.QRect(300, 770, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.btn_Next.setFont(font)
        self.btn_Next.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: gray; \n"
"    padding: 10px; \n"
"    color: black;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: blue; \n"
"    color: white;\n"
"}\n"
"")
        self.btn_Next.setObjectName("btn_Next")
        self.lbl_JustHp_2 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_JustHp_2.setGeometry(QtCore.QRect(10, 540, 60, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_JustHp_2.setFont(font)
        self.lbl_JustHp_2.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.lbl_JustHp_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbl_JustHp_2.setObjectName("lbl_JustHp_2")
        self.lbl_JustHp_3 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_JustHp_3.setGeometry(QtCore.QRect(75, 540, 300, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_JustHp_3.setFont(font)
        self.lbl_JustHp_3.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.lbl_JustHp_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbl_JustHp_3.setObjectName("lbl_JustHp_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pokedex API by KennyNeutron"))
        self.lbl_PokemonName.setText(_translate("MainWindow", "Bulbasaur"))
        self.btn_Type1.setText(_translate("MainWindow", "GRASS"))
        self.btn_Type2.setText(_translate("MainWindow", "POISON"))
        self.lbl_PokemonWeight.setText(_translate("MainWindow", "6.9Kg"))
        self.lbl_PokemonHeight.setText(_translate("MainWindow", "0.7M"))
        self.lbl_JustWeight.setText(_translate("MainWindow", "Weight"))
        self.lbl_JustHeight.setText(_translate("MainWindow", "Height"))
        self.lbl_JustHp.setText(_translate("MainWindow", "HP"))
        self.lbl_JustAtk.setText(_translate("MainWindow", "Atk"))
        self.lbl_JustDef.setText(_translate("MainWindow", "Def"))
        self.lbl_JustSpAtk.setText(_translate("MainWindow", "SP Atk"))
        self.lbl_JustSpDef.setText(_translate("MainWindow", "SP Def"))
        self.lbl_JustSpeed.setText(_translate("MainWindow", "Speed"))
        self.lbl_Hp.setText(_translate("MainWindow", "45"))
        self.lbl_Atk.setText(_translate("MainWindow", "49"))
        self.lbl_Def.setText(_translate("MainWindow", "49"))
        self.lbl_SpAtk.setText(_translate("MainWindow", "65"))
        self.lbl_SpDef.setText(_translate("MainWindow", "65"))
        self.lbl_Speed.setText(_translate("MainWindow", "45"))
        self.lbl_PokemonID.setText(_translate("MainWindow", "#001"))
        self.lbl_JustSearchLabel.setText(_translate("MainWindow", "Enter Pokemon Name or ID"))
        self.btn_Seach.setText(_translate("MainWindow", "SEARCH"))
        self.btn_Prev.setText(_translate("MainWindow", "PREV"))
        self.btn_Next.setText(_translate("MainWindow", "NEXT"))
        self.lbl_JustHp_2.setText(_translate("MainWindow", "Abilities:"))
        self.lbl_JustHp_3.setText(_translate("MainWindow", "overgrow, chlorophyl"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())