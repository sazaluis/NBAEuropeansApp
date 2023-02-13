import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QApplication

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Jugadores por continente")
        self.resize(300, 300)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)
        self.botones = []
        self.crear_botones()

    def crear_botones(self):
        continentes = ['NULL', 'Europe', 'United States', 'South America', 'Asia', 'Africa']
        for continente in continentes:
            boton = QPushButton(continente)
            boton.clicked.connect(lambda: self.mostrar_jugadores(continente))
            self.layout.addWidget(boton)

    def mostrar_jugadores(self, continente):
        jugadores = {
            'sam-hauser': {'ciudad': 'Stevens Point, WI', 'continente': 'US'},
            'jd-davison': {'ciudad': 'Letohatchee, AL', 'continente': 'NULL'},

        }
        print("Jugadores de", continente)
        for nombre, info in jugadores.items():
            if info['continente'] == continente:
                print(nombre)


class TablaJugadores(QWidget):
    def __init__(self, jugadores, parent=None):
        super().__init__(parent)
        self.jugadores = jugadores

        # Configuración de la tabla
        self.tabla = QTableWidget(len(jugadores), 2)
        self.tabla.setHorizontalHeaderLabels(["Jugador", "País"])
        for i, jugador in enumerate(jugadores):
            nombre = QTableWidgetItem(jugador[0])
            pais = QTableWidgetItem(jugador[1])
            self.tabla.setItem(i, 0, nombre)
            self.tabla.setItem(i, 1, pais)

        # Botón Atrás
        self.atras_btn = QPushButton("Atrás")
        self.atras_btn.clicked.connect(self.close)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.tabla)
        layout.addWidget(self.atras_btn)
        self.setLayout(layout)

def ver_jugadores(self, continente):
    jugadores = []
    for jugador, datos in self.datos.items():
        if datos[1] == continente:
            jugadores.append((jugador, datos[0]))
    tabla_jugadores = TablaJugadores(jugadores, self)
    tabla_jugadores.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec_())