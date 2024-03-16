import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from components.UnicodeSelector import UnicodeSelector
from components.OpcodeSelector import OpcodeSelector
from components.ButtonTextInput import ButtonTextInput

class TableManager(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Liblouis Tables Manager')

        self.popup = None

        layout = QVBoxLayout()


        self.input_opcode = ButtonTextInput()
        self.input_opcode.input.setReadOnly(True)
        self.input_opcode.input.setPlaceholderText("Select Opcode")
        self.input_opcode.button.setText("Select")
        self.input_opcode.button.clicked.connect(lambda : self.showOpcodePopup())

        self.input_unicode = ButtonTextInput()
        self.input_unicode.input.setReadOnly(True)
        self.input_unicode.input.setPlaceholderText("Select Unicode")
        self.input_unicode.button.setText("Select")
        self.input_unicode.button.clicked.connect(lambda : self.showUnicodePopup())

        self.input_braille = QTextEdit()


        layout.addWidget(self.input_opcode)
        layout.addWidget(self.input_unicode)
        layout.addWidget(self.input_braille)

        self.setLayout(layout)

    def showOpcodePopup(self):
        self.popup = OpcodeSelector()
        self.popup.on_select(lambda code : self.input_unicode.input.setText(code) )
        self.popup.show()

    def showUnicodePopup(self):
        self.popup = UnicodeSelector()
        self.popup.on_select(lambda code : self.input_unicode.input.setText(code) )
        self.popup.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = TableManager()
    window.show()

    sys.exit(app.exec_())