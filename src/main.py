import sys
from utils.view import clearLayout
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

        self.form = QVBoxLayout()

        self.input_opcode = ButtonTextInput()
        self.input_opcode.input.setReadOnly(True)
        self.input_opcode.input.setPlaceholderText("Select Opcode")
        self.input_opcode.button.setText("Select")
        self.input_opcode.button.clicked.connect(lambda : self.showOpcodePopup())

        # self.input_unicode = ButtonTextInput()
        # self.input_unicode.input.setReadOnly(True)
        # self.input_unicode.input.setPlaceholderText("Select Unicode")
        # self.input_unicode.button.setText("Select")
        # self.input_unicode.button.clicked.connect(lambda : self.showUnicodePopup())

        # self.input_braille = QTextEdit()

        layout.addWidget(self.input_opcode)
        # layout.addWidget(self.input_unicode)
        # layout.addWidget(self.input_braille)

        layout.addLayout(self.form)

        self.setLayout(layout)

    def showOpcodePopup(self):
        def on_select(opcode):
            self.input_opcode.input.setText(opcode["code"])
            self.generateForm(opcode["fields"])

        self.popup = OpcodeSelector()
        self.popup.on_select(lambda code : on_select(code))
        self.popup.show()

    def generateForm(self, fields):
        clearLayout(self.form)
        for field in fields:
            if field == "characters":
                inp = QTextEdit()
                inp.setPlaceholderText("add characters (string)")
                self.form.addWidget(inp)

            if field == "unicode":
                inp = ButtonTextInput()
                inp.input.setReadOnly(True)
                inp.input.setPlaceholderText("Select Unicode")
                inp.button.setText("Select")
                i = inp.input
                def open_popup():
                    self.popup = UnicodeSelector()
                    self.popup.on_select(lambda code : i.setText(code))
                    self.popup.show()
                inp.button.clicked.connect(lambda : open_popup())
                self.form.addWidget(inp)

            if field == "dots":
                inp = QTextEdit()
                inp.setPlaceholderText("Enter Dots")
                self.form.addWidget(inp)
            

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = TableManager()
    window.show()

    sys.exit(app.exec_())