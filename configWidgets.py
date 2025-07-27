from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class createConfigWidgets:
    def Slider(self, currentIndex, context):
        customSlider = QSlider(context)
        customSlider.setOrientation(Qt.Horizontal)
        customSlider.setValue(currentIndex)
        customSlider.setFixedWidth(480)
        return customSlider

    def Button(self, text, context):
        customButton = QPushButton(text, context)
        customButton.setFixedWidth(480)
        customButton.setFixedHeight(35)
        return customButton

class configWidgets:
    def multipierLabel(self, context, multipierValue):
        multipierLabel = QLabel('\nMultiplier: x{}'.format(multipierValue), context)
        return multipierLabel
