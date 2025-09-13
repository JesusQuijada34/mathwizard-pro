import sys
import sympy as sp
import numpy as np
from PyQt5.QtWidgets import (QApplication, QMainWindow, QTabWidget, QWidget, 
                            QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, 
                            QPushButton, QTextEdit, QGroupBox, QScrollArea,
                            QToolTip, QFrame, QSizePolicy)
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont, QPalette, QColor

class MathMasterPro(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MathMaster Pro - El Arte de Resolver")
        self.setGeometry(100, 100, 1000, 700)
        
        # Estilo dinámico (podría cargarse desde GitHub en una versión más avanzada)
        self.setStyleSheet(self.get_dynamic_styles())
        
        self.init_ui()
        self.set_tooltips()
        
    def get_dynamic_styles(self):
        """Retorna estilos QSS dinámicos con tema moderno"""
        return """
            QMainWindow {
                background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,
                                          stop: 0 #2c3e50, stop: 1 #3498db);
            }
            
            QTabWidget::pane {
                border: 2px solid #34495e;
                background: #ecf0f1;
                border-radius: 8px;
            }
            
            QTabBar::tab {
                background: #95a5a6;
                color: white;
                padding: 10px;
                margin: 2px;
                border-top-left-radius: 8px;
                border-top-right-radius: 8px;
                font-weight: bold;
            }
            
            QTabBar::tab:selected {
                background: #e74c3c;
                color: white;
            }
            
            QTabBar::tab:hover {
                background: #34495e;
            }
            
            QGroupBox {
                font-weight: bold;
                border: 2px solid #7f8c8d;
                border-radius: 8px;
                margin-top: 1ex;
                padding-top: 10px;
                background: rgba(255, 255, 255, 200);
            }
            
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px 0 5px;
                color: #2c3e50;
            }
            
            QPushButton {
                background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                          stop: 0 #3498db, stop: 1 #2980b9);
                border: none;
                color: white;
                padding: 10px;
                border-radius: 6px;
                font-weight: bold;
                min-width: 80px;
            }
            
            QPushButton:hover {
                background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                          stop: 0 #3cb0fd, stop: 1 #3498db);
            }
            
            QPushButton:pressed {
                background: #2c3e50;
            }
            
            QLineEdit {
                padding: 8px;
                border: 2px solid #bdc3c7;
                border-radius: 6px;
                background: white;
                selection-background-color: #3498db;
            }
            
            QLineEdit:focus {
                border: 2px solid #3498db;
            }
            
            QTextEdit {
                background: white;
                border: 2px solid #bdc3c7;
                border-radius: 6px;
                padding: 8px;
                font-family: 'Courier New', monospace;
            }
            
            QLabel {
                color: #2c3e50;
                font-weight: bold;
            }
            
            QScrollArea {
                border: none;
                background: transparent;
            }
        """
    
    def init_ui(self):
        # Widget central y layout principal
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        
        # Título de la aplicación
        title_label = QLabel("🎓 MathMaster Pro - El Arte de Resolver")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("""
            QLabel {
                font-size: 28px;
                font-weight: bold;
                color: white;
                padding: 20px;
                background: rgba(44, 62, 80, 0.8);
                border-radius: 15px;
                margin: 10px;
            }
        """)
        main_layout.addWidget(title_label)
        
        # Widget de pestañas
        self.tabs = QTabWidget()
        main_layout.addWidget(self.tabs)
        
        # Crear las diferentes pestañas
        self.create_basic_math_tab()
        self.create_algebra_tab()
        self.create_polynomials_tab()
        self.create_calculus_tab()
        self.create_advanced_tab()
        
        # Área de resultados
        results_group = QGroupBox("Resultados y Pasos de Solución")
        results_layout = QVBoxLayout()
        
        self.results_text = QTextEdit()
        self.results_text.setReadOnly(True)
        results_layout.addWidget(self.results_text)
        
        results_group.setLayout(results_layout)
        main_layout.addWidget(results_group)
        
    def create_basic_math_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)
        
        # Operaciones básicas
        basic_group = QGroupBox("Operaciones Básicas")
        basic_layout = QVBoxLayout()
        
        # Suma
        sum_layout = QHBoxLayout()
        sum_layout.addWidget(QLabel("Suma (a + b):"))
        self.sum_a = QLineEdit()
        self.sum_a.setPlaceholderText("Ingresa a")
        self.sum_b = QLineEdit()
        self.sum_b.setPlaceholderText("Ingresa b")
        sum_btn = QPushButton("Calcular")
        sum_btn.clicked.connect(self.calculate_sum)
        
        sum_layout.addWidget(self.sum_a)
        sum_layout.addWidget(QLabel("+"))
        sum_layout.addWidget(self.sum_b)
        sum_layout.addWidget(sum_btn)
        basic_layout.addLayout(sum_layout)
        
        # Resta, multiplicación, división (similar pattern)
        # ... (código similar para otras operaciones)
        
        basic_group.setLayout(basic_layout)
        layout.addWidget(basic_group)
        
        self.tabs.addTab(tab, "Básico")
    
    def create_algebra_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)
        
        # Ecuaciones lineales
        linear_group = QGroupBox("Ecuaciones Lineales")
        linear_layout = QVBoxLayout()
        
        eq_layout = QHBoxLayout()
        eq_layout.addWidget(QLabel("Ecuación (ax + b = c):"))
        self.linear_a = QLineEdit()
        self.linear_a.setPlaceholderText("a")
        self.linear_b = QLineEdit()
        self.linear_b.setPlaceholderText("b")
        self.linear_c = QLineEdit()
        self.linear_c.setPlaceholderText("c")
        linear_btn = QPushButton("Resolver")
        linear_btn.clicked.connect(self.solve_linear)
        
        eq_layout.addWidget(self.linear_a)
        eq_layout.addWidget(QLabel("x +"))
        eq_layout.addWidget(self.linear_b)
        eq_layout.addWidget(QLabel("="))
        eq_layout.addWidget(self.linear_c)
        eq_layout.addWidget(linear_btn)
        linear_layout.addLayout(eq_layout)
        
        linear_group.setLayout(linear_layout)
        layout.addWidget(linear_group)
        
        self.tabs.addTab(tab, "Álgebra")
    
    def create_polynomials_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)
        
        # Polinomios
        poly_group = QGroupBox("Polinomios")
        poly_layout = QVBoxLayout()
        
        poly_input_layout = QHBoxLayout()
        poly_input_layout.addWidget(QLabel("Polinomio (ej: x^2 + 2x + 1):"))
        self.poly_input = QLineEdit()
        self.poly_input.setPlaceholderText("Ingresa el polinomio")
        poly_btn = QPushButton("Analizar")
        poly_btn.clicked.connect(self.analyze_polynomial)
        
        poly_input_layout.addWidget(self.poly_input)
        poly_input_layout.addWidget(poly_btn)
        poly_layout.addLayout(poly_input_layout)
        
        poly_group.setLayout(poly_layout)
        layout.addWidget(poly_group)
        
        self.tabs.addTab(tab, "Polinomios")
    
    def create_calculus_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)
        
        # Cálculo
        calculus_group = QGroupBox("Cálculo")
        calculus_layout = QVBoxLayout()
        
        # Derivadas
        deriv_layout = QHBoxLayout()
        deriv_layout.addWidget(QLabel("Derivada de:"))
        self.deriv_input = QLineEdit()
        self.deriv_input.setPlaceholderText("ej: x^2 + sin(x)")
        deriv_btn = QPushButton("Calcular Derivada")
        deriv_btn.clicked.connect(self.calculate_derivative)
        
        deriv_layout.addWidget(self.deriv_input)
        deriv_layout.addWidget(deriv_btn)
        calculus_layout.addLayout(deriv_layout)
        
        calculus_group.setLayout(calculus_layout)
        layout.addWidget(calculus_group)
        
        self.tabs.addTab(tab, "Cálculo")
    
    def create_advanced_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)
        
        # Matemáticas avanzadas
        advanced_group = QGroupBox("Matemáticas Avanzadas")
        advanced_layout = QVBoxLayout()
        
        # Matrices
        matrix_layout = QHBoxLayout()
        matrix_layout.addWidget(QLabel("Matriz (ej: [[1,2],[3,4]]):"))
        self.matrix_input = QLineEdit()
        self.matrix_input.setPlaceholderText("Ingresa la matriz")
        matrix_btn = QPushButton("Calcular Determinante")
        matrix_btn.clicked.connect(self.calculate_determinant)
        
        matrix_layout.addWidget(self.matrix_input)
        matrix_layout.addWidget(matrix_btn)
        advanced_layout.addLayout(matrix_layout)
        
        advanced_group.setLayout(advanced_layout)
        layout.addWidget(advanced_group)
        
        self.tabs.addTab(tab, "Avanzado")
    
    def set_tooltips(self):
        # Tooltips educativos
        self.sum_a.setToolTip("Ingresa el primer número para la suma")
        self.sum_b.setToolTip("Ingresa el segundo número para la suma")
        self.linear_a.setToolTip("Coeficiente de x en la ecuación lineal")
        self.poly_input.setToolTip("Ingresa el polinomio usando notación matemática estándar")
        self.deriv_input.setToolTip("Función para derivar. Usa sin, cos, exp, log, etc.")
        self.matrix_input.setToolTip("Matriz en formato: [[a,b],[c,d]] para 2x2")
    
    def calculate_sum(self):
        try:
            a = float(self.sum_a.text())
            b = float(self.sum_b.text())
            result = a + b
            
            steps = f"""PASOS PARA LA SUMA:
            
1. Identificamos los números: {a} y {b}
2. Aplicamos la operación suma: {a} + {b}
3. Resultado: {result}

💡 Consejo: La suma es conmutativa (a + b = b + a)"""
            
            self.results_text.setHtml(f"<b>Resultado:</b> {result}<br><br>{steps}")
            
        except ValueError:
            self.results_text.setText("❌ Error: Por favor ingresa números válidos")
    
    def solve_linear(self):
        try:
            a = float(self.linear_a.text())
            b = float(self.linear_b.text())
            c = float(self.linear_c.text())
            
            if a == 0:
                self.results_text.setText("❌ Error: 'a' no puede ser cero en una ecuación lineal")
                return
            
            x = (c - b) / a
            
            steps = f"""PASOS PARA RESOLVER ECUACIÓN LINEAL:
            
Ecuación: {a}x + {b} = {c}

1. Restamos {b} en ambos lados: {a}x = {c} - {b}
2. Simplificamos: {a}x = {c - b}
3. Dividimos ambos lados por {a}: x = {c - b} / {a}
4. Resultado: x = {x}

💡 Consejo: Siempre verifica tu solución sustituyendo x en la ecuación original"""
            
            self.results_text.setHtml(f"<b>Solución:</b> x = {x}<br><br>{steps}")
            
        except ValueError:
            self.results_text.setText("❌ Error: Por favor ingresa coeficientes válidos")
    
    def analyze_polynomial(self):
        try:
            expr = self.poly_input.text()
            x = sp.symbols('x')
            poly = sp.sympify(expr)
            
            # Raíces
            roots = sp.solve(poly, x)
            
            # Factorización
            factored = sp.factor(poly)
            
            # Grado
            degree = sp.degree(poly)
            
            steps = f"""ANÁLISIS DEL POLINOMIO:
            
Polinomio: {expr}

1. Grado del polinomio: {degree}
2. Raíces encontradas: {roots}
3. Forma factorizada: {factored}

💡 Consejo: Las raíces son los valores donde el polinomio se hace cero"""
            
            self.results_text.setHtml(f"<b>Análisis Completo:</b><br><br>{steps}")
            
        except Exception as e:
            self.results_text.setText(f"❌ Error: {str(e)}")
    
    def calculate_derivative(self):
        try:
            expr = self.deriv_input.text()
            x = sp.symbols('x')
            f = sp.sympify(expr)
            
            derivative = sp.diff(f, x)
            
            steps = f"""CÁLCULO DE DERIVADA:
            
Función: f(x) = {expr}

1. Aplicamos reglas de derivación
2. Derivada: f'(x) = {derivative}

💡 Consejo: La derivada representa la tasa de cambio instantánea"""
            
            self.results_text.setHtml(f"<b>Derivada:</b> {derivative}<br><br>{steps}")
            
        except Exception as e:
            self.results_text.setText(f"❌ Error: {str(e)}")
    
    def calculate_determinant(self):
        try:
            matrix_str = self.matrix_input.text()
            matrix = sp.Matrix(sp.sympify(matrix_str))
            
            if matrix.rows != matrix.cols:
                self.results_text.setText("❌ Error: La matriz debe ser cuadrada")
                return
            
            det = matrix.det()
            
            steps = f"""CÁLCULO DE DETERMINANTE:
            
Matriz: {matrix_str}

1. Matriz de {matrix.rows}x{matrix.cols}
2. Aplicamos método de cálculo de determinante
3. Determinante: {det}

💡 Consejo: El determinante es cero si la matriz es singular (no invertible)"""
            
            self.results_text.setHtml(f"<b>Determinante:</b> {det}<br><br>{steps}")
            
        except Exception as e:
            self.results_text.setText(f"❌ Error: {str(e)}")

def main():
    app = QApplication(sys.argv)
    
    # Configurar tooltips globales
    QToolTip.setFont(QFont('SansSerif', 10))
    QToolTip.setStyleSheet("""
        QToolTip {
            background-color: #2c3e50;
            color: white;
            border: 2px solid #3498db;
            padding: 5px;
            border-radius: 4px;
            opacity: 200;
        }
    """)
    
    window = MathMasterPro()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()