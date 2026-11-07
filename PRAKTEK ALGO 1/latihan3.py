
import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QVBoxLayout
)


class TemperatureConverter(QWidget):
    def __init__(self):
        super().__init__()

        # Pengaturan jendela
        self.setWindowTitle("Konverter Suhu")
        self.setGeometry(300, 300, 300, 180)

        # Membuat layout
        layout = QVBoxLayout()

        # Input Celsius
        self.label_c = QLabel("Celsius:")
        self.input_c = QLineEdit()
        self.input_c.setPlaceholderText(
            "Masukkan suhu Celsius"
        )

        # Output Fahrenheit
        self.label_f = QLabel("Fahrenheit:")
        self.output_f = QLabel("0 °F")
        self.output_f.setStyleSheet(
            "font-size: 12px; font-weight: bold;"
        )

        # Memasukkan widget ke layout
        layout.addWidget(self.label_c)
        layout.addWidget(self.input_c)
        layout.addWidget(self.label_f)
        layout.addWidget(self.output_f)

        self.setLayout(layout)

        # Signal dan slot
        self.input_c.textChanged.connect(self.convert)

    def convert(self):
        try:
            celsius = float(self.input_c.text())
            fahrenheit = (celsius * 9 / 5) + 32

            self.output_f.setText(
                f"{fahrenheit:.2f} °F"
            )

        except ValueError:
            if self.input_c.text().strip() == "":
                self.output_f.setText("0 °F")
            else:
                self.output_f.setText("Invalid input")


def main():
    app = QApplication(sys.argv)
    window = TemperatureConverter()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()