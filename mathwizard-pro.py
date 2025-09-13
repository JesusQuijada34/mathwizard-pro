import sys
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5.QtWidgets import (QApplication, QMainWindow, QTabWidget, QWidget, 
                            QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, 
                            QPushButton, QTextEdit, QGroupBox, QScrollArea,
                            QToolTip, QFrame, QSizePolicy, QMessageBox)
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
        self.create_graphing_tab()
        
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
        
        # Resta
        sub_layout = QHBoxLayout()
        sub_layout.addWidget(QLabel("Resta (a - b):"))
        self.sub_a = QLineEdit()
        self.sub_a.setPlaceholderText("Ingresa a")
        self.sub_b = QLineEdit()
        self.sub_b.setPlaceholderText("Ingresa b")
        sub_btn = QPushButton("Calcular")
        sub_btn.clicked.connect(self.calculate_subtraction)
        
        sub_layout.addWidget(self.sub_a)
        sub_layout.addWidget(QLabel("-"))
        sub_layout.addWidget(self.sub_b)
        sub_layout.addWidget(sub_btn)
        basic_layout.addLayout(sub_layout)
        
        # Multiplicación
        mul_layout = QHBoxLayout()
        mul_layout.addWidget(QLabel("Multiplicación (a × b):"))
        self.mul_a = QLineEdit()
        self.mul_a.setPlaceholderText("Ingresa a")
        self.mul_b = QLineEdit()
        self.mul_b.setPlaceholderText("Ingresa b")
        mul_btn = QPushButton("Calcular")
        mul_btn.clicked.connect(self.calculate_multiplication)
        
        mul_layout.addWidget(self.mul_a)
        mul_layout.addWidget(QLabel("×"))
        mul_layout.addWidget(self.mul_b)
        mul_layout.addWidget(mul_btn)
        basic_layout.addLayout(mul_layout)
        
        # División
        div_layout = QHBoxLayout()
        div_layout.addWidget(QLabel("División (a ÷ b):"))
        self.div_a = QLineEdit()
        self.div_a.setPlaceholderText("Ingresa a")
        self.div_b = QLineEdit()
        self.div_b.setPlaceholderText("Ingresa b")
        div_btn = QPushButton("Calcular")
        div_btn.clicked.connect(self.calculate_division)
        
        div_layout.addWidget(self.div_a)
        div_layout.addWidget(QLabel("÷"))
        div_layout.addWidget(self.div_b)
        div_layout.addWidget(div_btn)
        basic_layout.addLayout(div_layout)
        
        # Potenciación
        pow_layout = QHBoxLayout()
        pow_layout.addWidget(QLabel("Potenciación (a^b):"))
        self.pow_a = QLineEdit()
        self.pow_a.setPlaceholderText("Base")
        self.pow_b = QLineEdit()
        self.pow_b.setPlaceholderText("Exponente")
        pow_btn = QPushButton("Calcular")
        pow_btn.clicked.connect(self.calculate_power)
        
        pow_layout.addWidget(self.pow_a)
        pow_layout.addWidget(QLabel("^"))
        pow_layout.addWidget(self.pow_b)
        pow_layout.addWidget(pow_btn)
        basic_layout.addLayout(pow_layout)
        
        # Raíz cuadrada
        sqrt_layout = QHBoxLayout()
        sqrt_layout.addWidget(QLabel("Raíz cuadrada (√a):"))
        self.sqrt_a = QLineEdit()
        self.sqrt_a.setPlaceholderText("Ingresa el número")
        sqrt_btn = QPushButton("Calcular")
        sqrt_btn.clicked.connect(self.calculate_sqrt)
        
        sqrt_layout.addWidget(self.sqrt_a)
        sqrt_layout.addWidget(sqrt_btn)
        basic_layout.addLayout(sqrt_layout)
        
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
        
        # Ecuaciones cuadráticas
        quadratic_group = QGroupBox("Ecuaciones Cuadráticas")
        quadratic_layout = QVBoxLayout()
        
        quad_layout = QHBoxLayout()
        quad_layout.addWidget(QLabel("Ecuación (ax² + bx + c = 0):"))
        self.quad_a = QLineEdit()
        self.quad_a.setPlaceholderText("a")
        self.quad_b = QLineEdit()
        self.quad_b.setPlaceholderText("b")
        self.quad_c = QLineEdit()
        self.quad_c.setPlaceholderText("c")
        quad_btn = QPushButton("Resolver")
        quad_btn.clicked.connect(self.solve_quadratic)
        
        quad_layout.addWidget(self.quad_a)
        quad_layout.addWidget(QLabel("x² +"))
        quad_layout.addWidget(self.quad_b)
        quad_layout.addWidget(QLabel("x +"))
        quad_layout.addWidget(self.quad_c)
        quad_layout.addWidget(QLabel("= 0"))
        quad_layout.addWidget(quad_btn)
        quadratic_layout.addLayout(quad_layout)
        
        quadratic_group.setLayout(quadratic_layout)
        layout.addWidget(quadratic_group)
        
        # Sistema de ecuaciones
        system_group = QGroupBox("Sistema de Ecuaciones Lineales")
        system_layout = QVBoxLayout()
        
        sys_layout = QHBoxLayout()
        sys_layout.addWidget(QLabel("Sistema 2x2:"))
        self.sys_a1 = QLineEdit()
        self.sys_a1.setPlaceholderText("a1")
        self.sys_b1 = QLineEdit()
        self.sys_b1.setPlaceholderText("b1")
        self.sys_c1 = QLineEdit()
        self.sys_c1.setPlaceholderText("c1")
        sys_btn = QPushButton("Resolver Sistema")
        sys_btn.clicked.connect(self.solve_system)
        
        sys_layout.addWidget(self.sys_a1)
        sys_layout.addWidget(QLabel("x +"))
        sys_layout.addWidget(self.sys_b1)
        sys_layout.addWidget(QLabel("y ="))
        sys_layout.addWidget(self.sys_c1)
        sys_layout.addWidget(sys_btn)
        system_layout.addLayout(sys_layout)
        
        # Segunda ecuación del sistema
        sys2_layout = QHBoxLayout()
        self.sys_a2 = QLineEdit()
        self.sys_a2.setPlaceholderText("a2")
        self.sys_b2 = QLineEdit()
        self.sys_b2.setPlaceholderText("b2")
        self.sys_c2 = QLineEdit()
        self.sys_c2.setPlaceholderText("c2")
        
        sys2_layout.addWidget(self.sys_a2)
        sys2_layout.addWidget(QLabel("x +"))
        sys2_layout.addWidget(self.sys_b2)
        sys2_layout.addWidget(QLabel("y ="))
        sys2_layout.addWidget(self.sys_c2)
        system_layout.addLayout(sys2_layout)
        
        system_group.setLayout(system_layout)
        layout.addWidget(system_group)
        
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
        
        # Integrales
        integral_layout = QHBoxLayout()
        integral_layout.addWidget(QLabel("Integral de:"))
        self.integral_input = QLineEdit()
        self.integral_input.setPlaceholderText("ej: x^2 + cos(x)")
        integral_btn = QPushButton("Calcular Integral")
        integral_btn.clicked.connect(self.calculate_integral)
        
        integral_layout.addWidget(self.integral_input)
        integral_layout.addWidget(integral_btn)
        calculus_layout.addLayout(integral_layout)
        
        # Límites
        limit_layout = QHBoxLayout()
        limit_layout.addWidget(QLabel("Límite de:"))
        self.limit_input = QLineEdit()
        self.limit_input.setPlaceholderText("ej: sin(x)/x")
        self.limit_point = QLineEdit()
        self.limit_point.setPlaceholderText("punto (ej: 0, oo)")
        limit_btn = QPushButton("Calcular Límite")
        limit_btn.clicked.connect(self.calculate_limit)
        
        limit_layout.addWidget(self.limit_input)
        limit_layout.addWidget(QLabel("cuando x →"))
        limit_layout.addWidget(self.limit_point)
        limit_layout.addWidget(limit_btn)
        calculus_layout.addLayout(limit_layout)
        
        # Series de Taylor
        taylor_layout = QHBoxLayout()
        taylor_layout.addWidget(QLabel("Serie de Taylor de:"))
        self.taylor_input = QLineEdit()
        self.taylor_input.setPlaceholderText("ej: exp(x)")
        self.taylor_point = QLineEdit()
        self.taylor_point.setPlaceholderText("punto (ej: 0)")
        self.taylor_order = QLineEdit()
        self.taylor_order.setPlaceholderText("orden (ej: 5)")
        taylor_btn = QPushButton("Calcular Taylor")
        taylor_btn.clicked.connect(self.calculate_taylor)
        
        taylor_layout.addWidget(self.taylor_input)
        taylor_layout.addWidget(QLabel("en x ="))
        taylor_layout.addWidget(self.taylor_point)
        taylor_layout.addWidget(QLabel("orden"))
        taylor_layout.addWidget(self.taylor_order)
        taylor_layout.addWidget(taylor_btn)
        calculus_layout.addLayout(taylor_layout)
        
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
        matrix_group = QGroupBox("Operaciones con Matrices")
        matrix_layout = QVBoxLayout()
        
        # Determinante
        det_layout = QHBoxLayout()
        det_layout.addWidget(QLabel("Matriz (ej: [[1,2],[3,4]]):"))
        self.matrix_input = QLineEdit()
        self.matrix_input.setPlaceholderText("Ingresa la matriz")
        det_btn = QPushButton("Calcular Determinante")
        det_btn.clicked.connect(self.calculate_determinant)
        
        det_layout.addWidget(self.matrix_input)
        det_layout.addWidget(det_btn)
        matrix_layout.addLayout(det_layout)
        
        # Inversa
        inv_layout = QHBoxLayout()
        inv_layout.addWidget(QLabel("Matriz Inversa:"))
        self.matrix_inv_input = QLineEdit()
        self.matrix_inv_input.setPlaceholderText("Ingresa la matriz")
        inv_btn = QPushButton("Calcular Inversa")
        inv_btn.clicked.connect(self.calculate_inverse)
        
        inv_layout.addWidget(self.matrix_inv_input)
        inv_layout.addWidget(inv_btn)
        matrix_layout.addLayout(inv_layout)
        
        matrix_group.setLayout(matrix_layout)
        advanced_layout.addWidget(matrix_group)
        
        # Estadísticas
        stats_group = QGroupBox("Estadísticas")
        stats_layout = QVBoxLayout()
        
        # Estadísticas descriptivas
        stats_data_layout = QHBoxLayout()
        stats_data_layout.addWidget(QLabel("Datos (separados por comas):"))
        self.stats_input = QLineEdit()
        self.stats_input.setPlaceholderText("ej: 1,2,3,4,5")
        stats_btn = QPushButton("Calcular Estadísticas")
        stats_btn.clicked.connect(self.calculate_statistics)
        
        stats_data_layout.addWidget(self.stats_input)
        stats_data_layout.addWidget(stats_btn)
        stats_layout.addLayout(stats_data_layout)
        
        stats_group.setLayout(stats_layout)
        advanced_layout.addWidget(stats_group)
        
        # Trigonometría
        trig_group = QGroupBox("Trigonometría")
        trig_layout = QVBoxLayout()
        
        # Funciones trigonométricas
        trig_func_layout = QHBoxLayout()
        trig_func_layout.addWidget(QLabel("Función trigonométrica:"))
        self.trig_input = QLineEdit()
        self.trig_input.setPlaceholderText("ej: sin(pi/2), cos(0)")
        trig_btn = QPushButton("Evaluar")
        trig_btn.clicked.connect(self.evaluate_trig)
        
        trig_func_layout.addWidget(self.trig_input)
        trig_func_layout.addWidget(trig_btn)
        trig_layout.addLayout(trig_func_layout)
        
        trig_group.setLayout(trig_layout)
        advanced_layout.addWidget(trig_group)
        
        # Conversión de unidades
        units_group = QGroupBox("Conversión de Unidades")
        units_layout = QVBoxLayout()
        
        # Conversión de ángulos
        angle_layout = QHBoxLayout()
        angle_layout.addWidget(QLabel("Ángulo:"))
        self.angle_input = QLineEdit()
        self.angle_input.setPlaceholderText("ej: 90")
        self.angle_from = QLineEdit()
        self.angle_from.setPlaceholderText("desde (deg/rad)")
        self.angle_to = QLineEdit()
        self.angle_to.setPlaceholderText("hacia (deg/rad)")
        angle_btn = QPushButton("Convertir")
        angle_btn.clicked.connect(self.convert_angle)
        
        angle_layout.addWidget(self.angle_input)
        angle_layout.addWidget(QLabel("de"))
        angle_layout.addWidget(self.angle_from)
        angle_layout.addWidget(QLabel("a"))
        angle_layout.addWidget(self.angle_to)
        angle_layout.addWidget(angle_btn)
        units_layout.addLayout(angle_layout)
        
        units_group.setLayout(units_layout)
        advanced_layout.addWidget(units_group)
        
        advanced_group.setLayout(advanced_layout)
        layout.addWidget(advanced_group)
        
        self.tabs.addTab(tab, "Avanzado")
    
    def create_graphing_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)
        
        # Gráficos de funciones
        graph_group = QGroupBox("Gráficos de Funciones")
        graph_layout = QVBoxLayout()
        
        # Función a graficar
        func_layout = QHBoxLayout()
        func_layout.addWidget(QLabel("Función f(x) ="))
        self.graph_input = QLineEdit()
        self.graph_input.setPlaceholderText("ej: x^2, sin(x), exp(x)")
        self.x_min = QLineEdit()
        self.x_min.setPlaceholderText("x min")
        self.x_max = QLineEdit()
        self.x_max.setPlaceholderText("x max")
        graph_btn = QPushButton("Graficar")
        graph_btn.clicked.connect(self.plot_function)
        
        func_layout.addWidget(self.graph_input)
        func_layout.addWidget(QLabel("x ∈ ["))
        func_layout.addWidget(self.x_min)
        func_layout.addWidget(QLabel(","))
        func_layout.addWidget(self.x_max)
        func_layout.addWidget(QLabel("]"))
        func_layout.addWidget(graph_btn)
        graph_layout.addLayout(func_layout)
        
        # Múltiples funciones
        multi_func_layout = QHBoxLayout()
        multi_func_layout.addWidget(QLabel("Múltiples funciones (separadas por ;):"))
        self.multi_graph_input = QLineEdit()
        self.multi_graph_input.setPlaceholderText("ej: x^2; sin(x); cos(x)")
        multi_graph_btn = QPushButton("Graficar Múltiples")
        multi_graph_btn.clicked.connect(self.plot_multiple_functions)
        
        multi_func_layout.addWidget(self.multi_graph_input)
        multi_func_layout.addWidget(multi_graph_btn)
        graph_layout.addLayout(multi_func_layout)
        
        graph_group.setLayout(graph_layout)
        layout.addWidget(graph_group)
        
        # Gráficos paramétricos
        param_group = QGroupBox("Gráficos Paramétricos")
        param_layout = QVBoxLayout()
        
        param_layout_inner = QHBoxLayout()
        param_layout_inner.addWidget(QLabel("x(t) ="))
        self.param_x = QLineEdit()
        self.param_x.setPlaceholderText("ej: cos(t)")
        param_layout_inner.addWidget(self.param_x)
        param_layout_inner.addWidget(QLabel("y(t) ="))
        self.param_y = QLineEdit()
        self.param_y.setPlaceholderText("ej: sin(t)")
        param_layout_inner.addWidget(self.param_y)
        param_layout_inner.addWidget(QLabel("t ∈ [0, 2π]"))
        param_btn = QPushButton("Graficar Paramétrico")
        param_btn.clicked.connect(self.plot_parametric)
        
        param_layout_inner.addWidget(param_btn)
        param_layout.addLayout(param_layout_inner)
        
        param_group.setLayout(param_layout)
        layout.addWidget(param_group)
        
        # Gráficos polares
        polar_group = QGroupBox("Gráficos Polares")
        polar_layout = QVBoxLayout()
        
        polar_layout_inner = QHBoxLayout()
        polar_layout_inner.addWidget(QLabel("r(θ) ="))
        self.polar_input = QLineEdit()
        self.polar_input.setPlaceholderText("ej: 1 + cos(θ)")
        polar_btn = QPushButton("Graficar Polar")
        polar_btn.clicked.connect(self.plot_polar)
        
        polar_layout_inner.addWidget(self.polar_input)
        polar_layout_inner.addWidget(polar_btn)
        polar_layout.addLayout(polar_layout_inner)
        
        polar_group.setLayout(polar_layout)
        layout.addWidget(polar_group)
        
        self.tabs.addTab(tab, "Gráficos")
    
    def set_tooltips(self):
        # Tooltips educativos
        self.sum_a.setToolTip("Ingresa el primer número para la suma")
        self.sum_b.setToolTip("Ingresa el segundo número para la suma")
        self.sub_a.setToolTip("Ingresa el minuendo (número del que se resta)")
        self.sub_b.setToolTip("Ingresa el sustraendo (número que se resta)")
        self.mul_a.setToolTip("Ingresa el primer factor")
        self.mul_b.setToolTip("Ingresa el segundo factor")
        self.div_a.setToolTip("Ingresa el dividendo (número que se divide)")
        self.div_b.setToolTip("Ingresa el divisor (número por el que se divide)")
        self.pow_a.setToolTip("Ingresa la base de la potencia")
        self.pow_b.setToolTip("Ingresa el exponente de la potencia")
        self.sqrt_a.setToolTip("Ingresa el radicando (número del que se extrae la raíz)")
        self.linear_a.setToolTip("Coeficiente de x en la ecuación lineal")
        self.quad_a.setToolTip("Coeficiente de x² en la ecuación cuadrática")
        self.quad_b.setToolTip("Coeficiente de x en la ecuación cuadrática")
        self.quad_c.setToolTip("Término independiente en la ecuación cuadrática")
        self.sys_a1.setToolTip("Coeficiente de x en la primera ecuación")
        self.sys_b1.setToolTip("Coeficiente de y en la primera ecuación")
        self.sys_c1.setToolTip("Término independiente de la primera ecuación")
        self.sys_a2.setToolTip("Coeficiente de x en la segunda ecuación")
        self.sys_b2.setToolTip("Coeficiente de y en la segunda ecuación")
        self.sys_c2.setToolTip("Término independiente de la segunda ecuación")
        self.poly_input.setToolTip("Ingresa el polinomio usando notación matemática estándar")
        self.deriv_input.setToolTip("Función para derivar. Usa sin, cos, exp, log, etc.")
        self.integral_input.setToolTip("Función para integrar. Usa sin, cos, exp, log, etc.")
        self.limit_input.setToolTip("Función para calcular límite")
        self.limit_point.setToolTip("Punto hacia el cual tiende x (usa 'oo' para infinito)")
        self.taylor_input.setToolTip("Función para expandir en serie de Taylor")
        self.taylor_point.setToolTip("Punto alrededor del cual expandir")
        self.taylor_order.setToolTip("Orden de la serie de Taylor")
        self.matrix_input.setToolTip("Matriz en formato: [[a,b],[c,d]] para 2x2")
        self.matrix_inv_input.setToolTip("Matriz para calcular inversa: [[a,b],[c,d]]")
        self.stats_input.setToolTip("Datos numéricos separados por comas")
        self.trig_input.setToolTip("Función trigonométrica: sin(x), cos(x), tan(x), etc.")
        self.angle_input.setToolTip("Valor del ángulo a convertir")
        self.angle_from.setToolTip("Unidad origen: 'deg' para grados, 'rad' para radianes")
        self.angle_to.setToolTip("Unidad destino: 'deg' para grados, 'rad' para radianes")
    
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
    
    def calculate_subtraction(self):
        try:
            a = float(self.sub_a.text())
            b = float(self.sub_b.text())
            result = a - b
            
            steps = f"""PASOS PARA LA RESTA:
            
1. Identificamos los números: {a} y {b}
2. Aplicamos la operación resta: {a} - {b}
3. Resultado: {result}

💡 Consejo: La resta NO es conmutativa (a - b ≠ b - a)"""
            
            self.results_text.setHtml(f"<b>Resultado:</b> {result}<br><br>{steps}")
            
        except ValueError:
            self.results_text.setText("❌ Error: Por favor ingresa números válidos")
    
    def calculate_multiplication(self):
        try:
            a = float(self.mul_a.text())
            b = float(self.mul_b.text())
            result = a * b
            
            steps = f"""PASOS PARA LA MULTIPLICACIÓN:
            
1. Identificamos los números: {a} y {b}
2. Aplicamos la operación multiplicación: {a} × {b}
3. Resultado: {result}

💡 Consejo: La multiplicación es conmutativa (a × b = b × a)"""
            
            self.results_text.setHtml(f"<b>Resultado:</b> {result}<br><br>{steps}")
            
        except ValueError:
            self.results_text.setText("❌ Error: Por favor ingresa números válidos")
    
    def calculate_division(self):
        try:
            a = float(self.div_a.text())
            b = float(self.div_b.text())
            
            if b == 0:
                self.results_text.setText("❌ Error: No se puede dividir por cero")
                return
            
            result = a / b
            
            steps = f"""PASOS PARA LA DIVISIÓN:
            
1. Identificamos los números: {a} y {b}
2. Verificamos que b ≠ 0: ✓
3. Aplicamos la operación división: {a} ÷ {b}
4. Resultado: {result}

💡 Consejo: La división NO es conmutativa (a ÷ b ≠ b ÷ a)"""
            
            self.results_text.setHtml(f"<b>Resultado:</b> {result}<br><br>{steps}")
            
        except ValueError:
            self.results_text.setText("❌ Error: Por favor ingresa números válidos")
    
    def calculate_power(self):
        try:
            a = float(self.pow_a.text())
            b = float(self.pow_b.text())
            result = a ** b
            
            steps = f"""PASOS PARA LA POTENCIACIÓN:
            
1. Identificamos base: {a} y exponente: {b}
2. Aplicamos la operación potenciación: {a}^{b}
3. Resultado: {result}

💡 Consejo: a^0 = 1 para cualquier a ≠ 0"""
            
            self.results_text.setHtml(f"<b>Resultado:</b> {result}<br><br>{steps}")
            
        except ValueError:
            self.results_text.setText("❌ Error: Por favor ingresa números válidos")
    
    def calculate_sqrt(self):
        try:
            a = float(self.sqrt_a.text())
            
            if a < 0:
                self.results_text.setText("❌ Error: No se puede calcular la raíz cuadrada de un número negativo")
                return
            
            result = a ** 0.5
            
            steps = f"""PASOS PARA LA RAÍZ CUADRADA:
            
1. Identificamos el número: {a}
2. Verificamos que a ≥ 0: ✓
3. Aplicamos la operación raíz cuadrada: √{a}
4. Resultado: {result}

💡 Consejo: √a × √a = a para cualquier a ≥ 0"""
            
            self.results_text.setHtml(f"<b>Resultado:</b> {result}<br><br>{steps}")
            
        except ValueError:
            self.results_text.setText("❌ Error: Por favor ingresa un número válido")
    
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
    
    def solve_quadratic(self):
        try:
            a = float(self.quad_a.text())
            b = float(self.quad_b.text())
            c = float(self.quad_c.text())
            
            if a == 0:
                self.results_text.setText("❌ Error: 'a' no puede ser cero en una ecuación cuadrática")
                return
            
            # Discriminante
            discriminant = b**2 - 4*a*c
            
            if discriminant > 0:
                x1 = (-b + discriminant**0.5) / (2*a)
                x2 = (-b - discriminant**0.5) / (2*a)
                solutions = f"x₁ = {x1}, x₂ = {x2}"
                nature = "Dos soluciones reales diferentes"
            elif discriminant == 0:
                x = -b / (2*a)
                solutions = f"x = {x}"
                nature = "Una solución real (raíz doble)"
            else:
                real_part = -b / (2*a)
                imag_part = abs(discriminant)**0.5 / (2*a)
                solutions = f"x₁ = {real_part} + {imag_part}i, x₂ = {real_part} - {imag_part}i"
                nature = "Dos soluciones complejas conjugadas"
            
            steps = f"""RESOLUCIÓN DE ECUACIÓN CUADRÁTICA:
            
Ecuación: {a}x² + {b}x + {c} = 0

1. Identificamos coeficientes: a={a}, b={b}, c={c}
2. Calculamos discriminante: Δ = b² - 4ac = {b}² - 4({a})({c}) = {discriminant}
3. Naturaleza de las soluciones: {nature}
4. Soluciones: {solutions}

💡 Fórmula cuadrática: x = (-b ± √Δ) / (2a)"""
            
            self.results_text.setHtml(f"<b>Soluciones:</b> {solutions}<br><br>{steps}")
            
        except ValueError:
            self.results_text.setText("❌ Error: Por favor ingresa coeficientes válidos")
    
    def solve_system(self):
        try:
            a1 = float(self.sys_a1.text())
            b1 = float(self.sys_b1.text())
            c1 = float(self.sys_c1.text())
            a2 = float(self.sys_a2.text())
            b2 = float(self.sys_b2.text())
            c2 = float(self.sys_c2.text())
            
            # Determinante del sistema
            det = a1 * b2 - a2 * b1
            
            if det == 0:
                self.results_text.setText("❌ El sistema no tiene solución única (determinante = 0)")
                return
            
            # Solución por regla de Cramer
            x = (c1 * b2 - c2 * b1) / det
            y = (a1 * c2 - a2 * c1) / det
            
            steps = f"""RESOLUCIÓN DE SISTEMA DE ECUACIONES:
            
Sistema:
{a1}x + {b1}y = {c1}
{a2}x + {b2}y = {c2}

1. Calculamos determinante: Δ = a₁b₂ - a₂b₁ = {a1}×{b2} - {a2}×{b1} = {det}
2. Aplicamos regla de Cramer:
   x = (c₁b₂ - c₂b₁)/Δ = ({c1}×{b2} - {c2}×{b1})/{det} = {x}
   y = (a₁c₂ - a₂c₁)/Δ = ({a1}×{c2} - {a2}×{c1})/{det} = {y}

💡 Verificación: Sustituye x e y en ambas ecuaciones"""
            
            self.results_text.setHtml(f"<b>Solución:</b> x = {x}, y = {y}<br><br>{steps}")
            
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
    
    def calculate_integral(self):
        try:
            expr = self.integral_input.text()
            x = sp.symbols('x')
            f = sp.sympify(expr)
            
            integral = sp.integrate(f, x)
            
            steps = f"""CÁLCULO DE INTEGRAL:
            
Función: f(x) = {expr}

1. Aplicamos reglas de integración
2. Integral indefinida: ∫f(x)dx = {integral}

💡 Consejo: La integral es la operación inversa de la derivada"""
            
            self.results_text.setHtml(f"<b>Integral:</b> {integral}<br><br>{steps}")
            
        except Exception as e:
            self.results_text.setText(f"❌ Error: {str(e)}")
    
    def calculate_limit(self):
        try:
            expr = self.limit_input.text()
            point = self.limit_point.text()
            x = sp.symbols('x')
            f = sp.sympify(expr)
            
            # Convertir punto especial
            if point.lower() in ['oo', 'inf', 'infinity']:
                limit_point = sp.oo
            elif point.lower() in ['-oo', '-inf', '-infinity']:
                limit_point = -sp.oo
            else:
                limit_point = float(point)
            
            limit_result = sp.limit(f, x, limit_point)
            
            steps = f"""CÁLCULO DE LÍMITE:
            
Función: f(x) = {expr}
Punto: x → {point}

1. Evaluamos el límite
2. Resultado: {limit_result}

💡 Consejo: Los límites describen el comportamiento de una función cerca de un punto"""
            
            self.results_text.setHtml(f"<b>Límite:</b> {limit_result}<br><br>{steps}")
            
        except Exception as e:
            self.results_text.setText(f"❌ Error: {str(e)}")
    
    def calculate_taylor(self):
        try:
            expr = self.taylor_input.text()
            point = float(self.taylor_point.text())
            order = int(self.taylor_order.text())
            x = sp.symbols('x')
            f = sp.sympify(expr)
            
            taylor_series = sp.series(f, x, point, order).removeO()
            
            steps = f"""SERIE DE TAYLOR:
            
Función: f(x) = {expr}
Punto: x = {point}
Orden: {order}

1. Calculamos derivadas sucesivas en x = {point}
2. Construimos la serie de Taylor
3. Resultado: {taylor_series}

💡 Consejo: La serie de Taylor aproxima una función mediante un polinomio"""
            
            self.results_text.setHtml(f"<b>Serie de Taylor:</b> {taylor_series}<br><br>{steps}")
            
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
    
    def calculate_inverse(self):
        try:
            matrix_str = self.matrix_inv_input.text()
            matrix = sp.Matrix(sp.sympify(matrix_str))
            
            if matrix.rows != matrix.cols:
                self.results_text.setText("❌ Error: La matriz debe ser cuadrada")
                return
            
            if matrix.det() == 0:
                self.results_text.setText("❌ Error: La matriz es singular (determinante = 0), no tiene inversa")
                return
            
            inverse = matrix.inv()
            
            steps = f"""CÁLCULO DE MATRIZ INVERSA:
            
Matriz: {matrix_str}

1. Verificamos que la matriz es cuadrada: ✓
2. Calculamos el determinante: {matrix.det()}
3. Como det ≠ 0, la matriz tiene inversa
4. Aplicamos método de cálculo de inversa
5. Matriz inversa: {inverse}

💡 Consejo: A × A⁻¹ = I (matriz identidad)"""
            
            self.results_text.setHtml(f"<b>Matriz Inversa:</b><br>{inverse}<br><br>{steps}")
            
        except Exception as e:
            self.results_text.setText(f"❌ Error: {str(e)}")
    
    def calculate_statistics(self):
        try:
            data_str = self.stats_input.text()
            data = [float(x.strip()) for x in data_str.split(',')]
            
            if len(data) < 2:
                self.results_text.setText("❌ Error: Se necesitan al menos 2 datos")
                return
            
            # Estadísticas básicas
            mean_val = np.mean(data)
            median_val = np.median(data)
            std_val = np.std(data)
            var_val = np.var(data)
            min_val = np.min(data)
            max_val = np.max(data)
            range_val = max_val - min_val
            
            steps = f"""ESTADÍSTICAS DESCRIPTIVAS:
            
Datos: {data}

1. Media (promedio): {mean_val:.4f}
2. Mediana: {median_val:.4f}
3. Desviación estándar: {std_val:.4f}
4. Varianza: {var_val:.4f}
5. Mínimo: {min_val:.4f}
6. Máximo: {max_val:.4f}
7. Rango: {range_val:.4f}

💡 Consejo: La desviación estándar mide la dispersión de los datos"""
            
            self.results_text.setHtml(f"<b>Estadísticas:</b><br><br>{steps}")
            
        except Exception as e:
            self.results_text.setText(f"❌ Error: {str(e)}")
    
    def evaluate_trig(self):
        try:
            expr = self.trig_input.text()
            x = sp.symbols('x')
            f = sp.sympify(expr)
            
            # Evaluar en algunos puntos comunes
            points = [0, sp.pi/6, sp.pi/4, sp.pi/3, sp.pi/2, sp.pi, 2*sp.pi]
            results = []
            
            for point in points:
                try:
                    value = f.subs(x, point).evalf()
                    results.append(f"f({point}) = {value}")
                except:
                    pass
            
            steps = f"""EVALUACIÓN TRIGONOMÉTRICA:
            
Función: f(x) = {expr}

Evaluaciones en puntos clave:
{chr(10).join(results)}

💡 Consejo: Usa pi para π, sin/cos/tan para funciones trigonométricas"""
            
            self.results_text.setHtml(f"<b>Evaluación:</b><br><br>{steps}")
            
        except Exception as e:
            self.results_text.setText(f"❌ Error: {str(e)}")
    
    def convert_angle(self):
        try:
            angle = float(self.angle_input.text())
            from_unit = self.angle_from.text().lower()
            to_unit = self.angle_to.text().lower()
            
            if from_unit == to_unit:
                result = angle
            elif from_unit in ['deg', 'degree', 'degrees'] and to_unit in ['rad', 'radian', 'radians']:
                result = angle * sp.pi / 180
            elif from_unit in ['rad', 'radian', 'radians'] and to_unit in ['deg', 'degree', 'degrees']:
                result = angle * 180 / sp.pi
            else:
                self.results_text.setText("❌ Error: Unidades no reconocidas. Usa 'deg' o 'rad'")
                return
            
            steps = f"""CONVERSIÓN DE ÁNGULOS:
            
Valor: {angle} {from_unit}

1. Fórmula de conversión:
   - De grados a radianes: rad = deg × π/180
   - De radianes a grados: deg = rad × 180/π

2. Conversión: {angle} {from_unit} = {result:.6f} {to_unit}

💡 Consejo: 180° = π radianes"""
            
            self.results_text.setHtml(f"<b>Resultado:</b> {result:.6f} {to_unit}<br><br>{steps}")
            
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