import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QListWidget, QListWidgetItem, QLabel, QLineEdit

class UnicodeViewer(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Unicode Viewer')
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()

        # Create a QLineEdit for inputting Unicode code points or characters
        self.search_bar = QLineEdit()
        self.search_bar.textChanged.connect(self.search)  # Connect to textChanged signal
        layout.addWidget(self.search_bar)

        # Create a QListWidget to display Unicode code points and characters
        self.list_widget = QListWidget()
        self.list_widget.itemDoubleClicked.connect(self.showCharacterDetails)
        layout.addWidget(self.list_widget)

        # Create a QLabel to display selected character details
        self.character_details_label = QLabel()
        layout.addWidget(self.character_details_label)

        self.setLayout(layout)

        self.populateList()

    def populateList(self):
        # Populate QListWidget with Unicode code points and characters
        for code_point in range(0x0000, 0xFFFF):
            char = chr(code_point)
            item = QListWidgetItem(f"{char} (U+{code_point:04X})")
            item.setData(1, code_point)  # Store the code point as item data
            self.list_widget.addItem(item)

    def search(self):
        # Clear previous search results
        self.list_widget.clear()

        # Get the search query from the search bar
        query = self.search_bar.text().strip()

        # Search by character
        for code_point in range(0x0000, 0xFFFF):
            char = chr(code_point)
            if query.lower() in char.lower():
                item = QListWidgetItem(f"{char} (U+{code_point:04X})")
                item.setData(1, code_point)  # Store the code point as item data
                self.list_widget.addItem(item)

        # Search by Unicode code point
        for code_point in range(0x0000, 0xFFFF):
            if query.lower() in f"U+{code_point:04X}".lower():
                char = chr(code_point)
                item = QListWidgetItem(f"{char} (U+{code_point:04X})")
                item.setData(1, code_point)  # Store the code point as item data
                self.list_widget.addItem(item)

    def showCharacterDetails(self, item):
        # Show details of the selected character
        code_point = item.data(1)
        char = chr(code_point)
        self.character_details_label.setText(f"Character: {char}\n"
                                              f"Unicode Code Point: U+{code_point:04X}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = UnicodeViewer()
    window.show()
    sys.exit(app.exec_())
