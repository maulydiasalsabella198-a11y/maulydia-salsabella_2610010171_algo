
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QListWidgetItem
from PyQt5.QtCore import Qt
from PyQt5 import uic


class TodoApp(QWidget):
    def __init__(self):
        super().__init__()

        # Memuat desain dari Qt Designer
        uic.loadUi("to_do_list.ui", self)

        # Menghubungkan tombol dengan fungsi
        self.add_btn.clicked.connect(self.add_task)
        self.complete_btn.clicked.connect(self.complete_task)
        self.delete_btn.clicked.connect(self.delete_task)

        # Menekan Enter juga menambahkan tugas
        self.task_input.returnPressed.connect(self.add_task)

    # Fungsi menambahkan tugas
    def add_task(self):
        task = self.task_input.text().strip()

        if task:
            self.task_list.addItem(task)
            self.task_input.clear()

    # Fungsi menandai tugas selesai
    def complete_task(self):
        item = self.task_list.currentItem()

        if item:
            if not item.text().startswith("✓ "):
                item.setText("✓ " + item.text())

            item.setForeground(Qt.green)

    # Fungsi menghapus tugas
    def delete_task(self):
        row = self.task_list.currentRow()

        if row >= 0:
            self.task_list.takeItem(row)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TodoApp()
    window.show()
    sys.exit(app.exec_())