from PyQt5.QtWidgets import *

class UnicodeViewer(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.setWindowTitle('Unicode Viewer')

        layout = QVBoxLayout()

        search = QLineEdit()
        search.setPlaceholderText("Search for Unicode / Character")

        label = QLabel("Double click code to select")

        self.unicodes_list = QListWidget()
        self.unicodes_list.itemClicked.connect(lambda x : search.setText(x.text()))

        for code in range(0x0000, 0xFFFF):
            txt = f"{chr(code)} (U+{code:04X})"
            item = QListWidgetItem(txt)
            item.setToolTip(f"Select {txt}")
            self.unicodes_list.addItem(item)

        layout.addWidget(search)
        layout.addWidget(label)
        layout.addWidget(self.unicodes_list)

        self.setLayout(layout)

    def on_select(self, cb):
        def callback(code):
            cb(code)
            self.hide()
        self.unicodes_list.itemDoubleClicked.connect(lambda x : callback(x.text()))