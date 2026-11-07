import sys
from PyQt5.QtWidgets import *


# Dark Theme
DARK_STYLE = """
QMainWindow, QWidget {
    background-color: #2b2b2b;
}

QLabel {
    color: white;
}

QPushButton {
    background-color: #3c3c3c;
    color: white;
    border: 1px solid #555;
    border-radius: 5px;
    padding: 5px;
}

QPushButton:hover {
    background-color: #4a4a4a;
}

QLineEdit, QTextEdit, QComboBox {
    background-color: #3c3c3c;
    color: white;
    border: 1px solid #555;
    border-radius: 3px;
    padding: 5px;
}
"""


# Light Theme
LIGHT_STYLE = """
QMainWindow, QWidget {
    background-color: #f0f0f0;
}

QLabel {
    color: black;
}

QPushButton {
    background-color: #e0e0e0;
    color: black;
    border: 1px solid #aaa;
    border-radius: 5px;
    padding: 5px;
}

QPushButton:hover {
    background-color: #d0d0d0;
}

QLineEdit, QTextEdit, QComboBox {
    background-color: white;
    color: black;
    border: 1px solid #aaa;
    border-radius: 3px;
    padding: 5px;
}
"""


class StyledApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QSS Styling Demo")
        self.setGeometry(300, 300, 400, 300)

        # Widget utama
        central = QWidget()
        self.setCentralWidget(central)

        layout = QVBoxLayout(central)

        # Widget
        self.label = QLabel("This is a styled label")

        self.input = QLineEdit()
        self.input.setPlaceholderText("Enter text here...")

        self.combo = QComboBox()
        self.combo.addItems(
            ["Option 1", "Option 2", "Option 3"]
        )

        self.text_edit = QTextEdit()
        self.text_edit.setPlaceholderText("Multi-line text...")

        self.button = QPushButton("Click Me")
        self.button.clicked.connect(self.on_click)

        # Tombol ganti tema
        self.theme_btn = QPushButton("Switch to Dark Theme")
        self.theme_btn.clicked.connect(self.toggle_theme)

        layout.addWidget(self.label)
        layout.addWidget(self.input)
        layout.addWidget(self.combo)
        layout.addWidget(self.text_edit)
        layout.addWidget(self.button)
        layout.addWidget(self.theme_btn)

        self.is_dark = False

        self.apply_light_theme()

    def on_click(self):
        QMessageBox.information(
            self,
            "Info",
            f"Input: {self.input.text()}\n"
            f"Combo: {self.combo.currentText()}"
        )

    def toggle_theme(self):
        if self.is_dark:
            self.apply_light_theme()
            self.theme_btn.setText("Switch to Dark Theme")
        else:
            self.apply_dark_theme()
            self.theme_btn.setText("Switch to Light Theme")

        self.is_dark = not self.is_dark

    def apply_dark_theme(self):
        self.setStyleSheet(DARK_STYLE)

    def apply_light_theme(self):
        self.setStyleSheet(LIGHT_STYLE)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StyledApp()
    window.show()
    sys.exit(app.exec_())