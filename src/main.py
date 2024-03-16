import sys
from PyQt5.QtWidgets import *
from components.UnicodeViewer import UnicodeViewer
from components.ButtonTextInput import ButtonTextInput

opcodes = ["punctuation", "identifier", "word", "math", "number"]

class TableCreator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Liblouis Table Creator')

        self.popup = None

        layout = QVBoxLayout()

        self.input_unicode = ButtonTextInput()
        self.input_unicode.input.setReadOnly(True)
        self.input_unicode.input.setPlaceholderText("Select Unicode")
        self.input_unicode.button.setText("Select")
        self.input_unicode.button.clicked.connect(lambda : self.showUnicodePopup())

        self.input_opcode = QTextEdit()
        self.input_braille = QTextEdit()


        layout.addWidget(self.input_unicode)
        layout.addWidget(self.input_opcode)
        layout.addWidget(self.input_braille)

        self.setLayout(layout)

    def showUnicodePopup(self):
        self.popup = UnicodeViewer()
        self.popup.on_select(lambda code : self.input_unicode.input.setText(code) )
        self.popup.show()
    # def openPopup(self):
    #     popup = PopupDialog(self)
    #     popup.setGeometry(self.geometry().center().x() - 150, self.geometry().center().y() - 100, 300, 200)  # Center the popup
    #     popup.add_content(QPushButton("Close", self))
    #     popup.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TableCreator()
    # window.setGeometry(300, 200, 800, 400)
    window.show()
    sys.exit(app.exec_())
