from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from pyqt_switch import PyQtSwitch
import sys
import os
import qdarktheme
import toml
from configWidgets import *
from gamelistDialogComponents import *

gameNameList = [""]
texturescaleValueList = [1]
multiplierList = [1]
perfmodeList = [""]

def dbArrayClear():
    gameNameList.clear()
    texturescaleValueList.clear()
    multiplierList.clear()
    perfmodeList.clear()

class Window(QMainWindow):
    def createGameItems(self):
        with open('{}/.config/lsfg-vk/conf.toml'.format(os.path.expanduser("~")), 'r') as f:
            config = toml.load(f)

        for game_ in config['game']:
            exeValue = game_['exe']
            multiplierValue = game_['multiplier']
            texturescaleValue = game_['flow_scale']
            perfmodeValue = game_['performance_mode']
            gameNameList.append(exeValue)
            texturescaleValueList.append(texturescaleValue)
            multiplierList.append(multiplierValue)
            perfmodeList.append(perfmodeValue)
            hbox = QHBoxLayout(self)
            widget = QWidget()
            widget.setLayout(hbox)
            appButton = QPushButton('{}'.format(exeValue), self)
            appButton.clicked.connect(lambda: self.createGameConfig())
            appButton.setFixedHeight(70)
            appButton.setFixedWidth(750)
            hbox.addWidget(appButton)
            self.vbox.addWidget(widget)

    def loadUi(self):
        dbArrayClear()
        self.vbox = QVBoxLayout(self)
        self.vbox.setAlignment(Qt.AlignCenter)
        self.scroll = QScrollArea()
        self.widget = QWidget()
        self.widget.setMinimumHeight(450)
        self.widget.setLayout(self.vbox)

        try:
            self.createGameItems()
        except:
            print("No games configured")

        os.system("./gamesdb.sh")

        self.scroll.setWidget(self.widget)
        self.scroll.setAlignment(Qt.AlignHCenter)
        self.setCentralWidget(self.scroll)

        self.show()

    def createToolbarActions(self):
        self.newdirectorySession = QAction('&Add New Game', self)
        self.newdirectorySession.setShortcut('Ctrl+A')
        self.newdirectorySession.triggered.connect(self.gamelistSessionDialog)
        self.configMenu.addAction(self.newdirectorySession)

        self.versionSession = QAction('&Version', self)
        self.versionSession.setShortcut('Ctrl+V')
        self.versionSession.triggered.connect(self.versionSessionDialog)
        self.aboutMenu.addAction(self.versionSession)

        self.bugReportSession = QAction('&Bug Report', self)
        self.bugReportSession.setShortcut('Ctrl+B')
        self.bugReportSession.triggered.connect(self.pullRequestSessionDialog)
        self.aboutMenu.addAction(self.bugReportSession)

        self.pullRequestSession = QAction('&Pull Request', self)
        self.pullRequestSession.setShortcut('Ctrl+P')
        self.pullRequestSession.triggered.connect(self.bugReportSessionDialog)
        self.aboutMenu.addAction(self.pullRequestSession)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lsfg-Gui")
        self.setFixedSize(800, 500)
        self.setStyleSheet(qdarktheme.load_stylesheet(theme="dark"))

        self.makeConfigWidgets = createConfigWidgets()
        self.uiConfigWidgets = configWidgets()

        self.menuToolbar = self.menuBar()
        self.configMenu = self.menuToolbar.addMenu('&Config')
        self.aboutMenu = self.menuToolbar.addMenu('&About')

        self.createToolbarActions()
        self.loadUi()

    def perfModeClick(self):
        if(perfmodeList[self.nameIndex] == True):
            perfmodeList[self.nameIndex] = False
            self.perfModeButton.setText("Performance Mode: {}".format(perfmodeList[self.nameIndex]))
        else:
            perfmodeList[self.nameIndex] = True
            self.perfModeButton.setText("Performance Mode: {}".format(perfmodeList[self.nameIndex]))

    def perfModeArea(self):
        self.perfModeButton = self.makeConfigWidgets.Button("Performance Mode: {}".format(perfmodeList[self.nameIndex]), self)
        self.perfModeButton.clicked.connect(self.perfModeClick)
        self.vbox.addWidget(self.perfModeButton)

    def sliderTextureValueChanged(self):
        self.textureLabel.setText("\nTexture: {}%".format(self.textureSlider.value()))

    def textureArea(self):
        self.textureSlider = self.makeConfigWidgets.Slider(int(texturescaleValueList[self.nameIndex] * 100), self)
        self.textureSlider.setRange(25, 100)
        self.textureSlider.valueChanged.connect(self.sliderTextureValueChanged)

        self.textureLabel = QLabel("\nTexture: {}%".format(self.textureSlider.value()))

        self.vbox.addWidget(self.textureSlider)
        self.vbox.addWidget(self.textureLabel)

    def saveChanges(self):
        os.system("./remove.sh {}".format(self.senderButton))
        if(perfmodeList[self.nameIndex] == True):
            os.system("./input.sh {} {} true {}".format(self.senderButton, self.multiplierSlider.value(), float(self.textureSlider.value() / 100)))
            print("{} {} {}".format(self.senderButton, self.multiplierSlider.value(), float(self.textureSlider.value() / 100)))
        else:
            os.system("./input.sh {} {} false {}".format(self.senderButton, self.multiplierSlider.value(), float(self.textureSlider.value() / 100)))
            print("{} {} {}".format(self.senderButton, self.multiplierSlider.value(), float(self.textureSlider.value() / 100)))

        self.loadUi()

    def backButtonWrapper(self):
        backButton = self.makeConfigWidgets.Button("Back", self)
        backButton.clicked.connect(self.saveChanges)
        self.vbox.addWidget(backButton)

    def multiplierArea(self):
        self.multiplierSlider = self.makeConfigWidgets.Slider(multiplierList[self.nameIndex], self)
        self.multiplierSlider.setRange(2,4)
        multiplierLabel = self.uiConfigWidgets.multipierLabel(self, self.multiplierSlider.value())

        def sliderMutiplierValueChanged():
            multiplierLabel.setText("\nMultiplier: x{}".format(self.multiplierSlider.value()))

        self.multiplierSlider.valueChanged.connect(sliderMutiplierValueChanged)
        self.vbox.addWidget(self.multiplierSlider)
        self.vbox.addWidget(multiplierLabel)

    def createGameConfig(self):
        self.senderButton = self.sender().text()
        self.nameIndex = gameNameList.index(self.senderButton)

        def clear_():
            for i in reversed(range(self.vbox.count())):
                self.vbox.itemAt(i).widget().close()

        clear_()

        self.vbox.addStretch()
        self.vbox.setDirection(QBoxLayout.Direction.BottomToTop)
        self.perfModeArea()
        self.vbox.addWidget(QLabel(''))
        self.multiplierArea()
        self.textureArea()
        self.backButtonWrapper()

    def versionSessionDialog(self):
        os.system("xdg-open https://github.com/Skyghost090/Lsfg-Gui")

    def pullRequestSessionDialog(self):
        os.system("xdg-open https://github.com/Skyghost090/Lsfg-Gui/pulls")

    def bugReportSessionDialog(self):
        os.system("xdg-open https://github.com/Skyghost090/Lsfg-Gui/issues")

    def confirmAddButtonClick(self):
        os.system("./input.sh {} 4 true 1.0".format(self.gameCommand.text()))
        self.addGamedialog.close()
        self.dialog.close()
        self.loadUi()

    def confirmRemoveButtonClick(self):
        os.system("./remove.sh {}".format(self.itemName))
        self.addGamedialog.close()
        self.dialog.close()
        self.loadUi()

    def addGameDialog(self):
        self.addGamedialog = createDialog.create(self, self)
        self.addGamedialog.setWindowTitle("Add Game")
        self.gameCommand = QLineEdit("Please Type Game Command", self.addGamedialog)
        self.gameCommand.setGeometry(15,20,370,30)

        addGameButton = QPushButton("Add", self.addGamedialog)
        addGameButton.setGeometry(310, 65, 75, 35)
        addGameButton.clicked.connect(self.confirmAddButtonClick)
        self.addGamedialog.exec_()

    def removeGameDialog(self):
        self.addGamedialog = createDialog.create(self, self)
        self.addGamedialog.setWindowTitle("Remove Game")
        label = QLabel("Do you want remove game?", self.addGamedialog)
        label.setGeometry(15,25,370,30)

        confirmButton = QPushButton("Yes", self.addGamedialog)
        confirmButton.setGeometry(15,75,70,30)
        confirmButton.clicked.connect(self.confirmRemoveButtonClick)
        self.addGamedialog.exec_()

    def gamelistSessionDialog(self):
        self.dialog = createDialog.create(self, self)
        listWidget = QListWidget(self.dialog)
        scroll = QScrollArea(self.dialog)
        scroll.setWidget(listWidget)

        def listClick():
            self.itemName = listWidget.currentItem().text()
            if (self.itemName == "Add Game"):
                self.addGameDialog()
            else:
                self.removeGameDialog()

        listWidget.setGeometry(0,0,400,300)
        listWidget.addItem(QListWidgetItem("Add Game"))
        listWidget.clicked.connect(listClick)
        dirsFile = open('games.txt', 'r')

        for line in dirsFile:
            listWidget.addItem(QListWidgetItem("{}".format(line).rstrip()))

        self.dialog.setWindowTitle("Game Directory")
        self.dialog.exec_()

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
