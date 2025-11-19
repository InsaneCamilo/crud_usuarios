from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout,
    QTableWidget, QTableWidgetItem, QLineEdit, QLabel, QMessageBox
)
from api import listar_usuarios, crear_usuario, actualizar_usuario, eliminar_usuario
import sys

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("CRUD Usuarios - PyQt5 + Django")
        self.resize(600, 400)

        # --- Widgets ---
        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["Código", "Nombre"])
        self.table.setColumnWidth(0, 100)
        self.table.setColumnWidth(1, 300)

        self.input_codigo = QLineEdit()
        self.input_nombre = QLineEdit()

        self.btn_cargar = QPushButton("Refrescar")
        self.btn_agregar = QPushButton("Agregar")
        self.btn_actualizar = QPushButton("Actualizar")
        self.btn_eliminar = QPushButton("Eliminar")

        # --- Layouts ---
        form = QHBoxLayout()
        form.addWidget(QLabel("Código:"))
        form.addWidget(self.input_codigo)
        form.addWidget(QLabel("Nombre:"))
        form.addWidget(self.input_nombre)

        buttons = QHBoxLayout()
        buttons.addWidget(self.btn_cargar)
        buttons.addWidget(self.btn_agregar)
        buttons.addWidget(self.btn_actualizar)
        buttons.addWidget(self.btn_eliminar)

        layout = QVBoxLayout()
        layout.addWidget(self.table)
        layout.addLayout(form)
        layout.addLayout(buttons)

        self.setLayout(layout)

        # --- Eventos ---
        self.btn_cargar.clicked.connect(self.cargar_datos)
        self.btn_agregar.clicked.connect(self.agregar_usuario)
        self.btn_actualizar.clicked.connect(self.actualizar_usuario)
        self.btn_eliminar.clicked.connect(self.eliminar_usuario)
        self.table.cellClicked.connect(self.cargar_campos)

        # Cargar al inicio
        self.cargar_datos()

    def cargar_datos(self):
        datos = listar_usuarios()
        self.table.setRowCount(len(datos))

        for i, usuario in enumerate(datos):
            self.table.setItem(i, 0, QTableWidgetItem(str(usuario["codigo"])))
            self.table.setItem(i, 1, QTableWidgetItem(usuario["nombre"]))

    def cargar_campos(self, row, col):
        codigo = self.table.item(row, 0).text()
        nombre = self.table.item(row, 1).text()
        self.input_codigo.setText(codigo)
        self.input_nombre.setText(nombre)

    def agregar_usuario(self):
        codigo = self.input_codigo.text()
        nombre = self.input_nombre.text()

        if crear_usuario(codigo, nombre):
            QMessageBox.information(self, "OK", "Usuario creado")
            self.cargar_datos()
        else:
            QMessageBox.warning(self, "Error", "No se pudo crear usuario")

    def actualizar_usuario(self):
        codigo = self.input_codigo.text()
        nombre = self.input_nombre.text()

        if actualizar_usuario(codigo, nombre):
            QMessageBox.information(self, "OK", "Usuario actualizado")
            self.cargar_datos()
        else:
            QMessageBox.warning(self, "Error", "No se pudo actualizar usuario")

    def eliminar_usuario(self):
        codigo = self.input_codigo.text()

        if eliminar_usuario(codigo):
            QMessageBox.information(self, "OK", "Usuario eliminado")
            self.cargar_datos()
        else:
            QMessageBox.warning(self, "Error", "No se pudo eliminar usuario")

# --- MAIN ---
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())
