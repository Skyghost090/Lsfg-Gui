from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import qdarktheme

class createDialog:
    def create(self, context):
        customDialog = QDialog(context)
        customDialog.setFixedSize(405,305)
        customDialog.setStyleSheet(qdarktheme.load_stylesheet(theme="dark"))
        return customDialog
