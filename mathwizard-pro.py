import sys
import sympy as sp
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QWidget, QTabWidget, QVBoxLayout, QLabel,
    QLineEdit, QPushButton, QTextEdit, QHBoxLayout
)
from PyQt5.QtCore import Qt

QSS_STYLE = """
QWidget {
    background: #21222C;
    color: #F8F8F2;
    font-size: 15px;
}
QTabWidget::pane {
    border: 2px solid #44475A;
    border-radius: 6px;
}
QTabBar::tab {
    background: #44475A;
    padding: 8px;
    margin-right: 2px;
    border-top-left-radius: 4px;
    border-top-right-radius: 4px;
}
QTabBar::tab:selected {
    background: #6272A4;
    color: #fff;
}
QLineEdit, QPushButton, QTextEdit {
    background: #282A36;
    border: 1px solid #6272A4;
    border-radius: 4px;
    padding: 5px;
}
QPushButton:hover {
    background: #6272A4;
    color: #fff;
}
"""

def render_steps(steps):
    if isinstance(steps, (list, tuple)):
        return '\n'.join(str(s) for s in steps)
    return str(steps)

class GeneralMathTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Escribe cualquier expresión matemática y pulsa Resolver:")
        self.input = QLineEdit()
        self.button = QPushButton("Resolver")
        self.output = QTextEdit()
        self.output.setReadOnly(True)
        layout.addWidget(self.label)
        layout.addWidget(self.input)
        layout.addWidget(self.button)
        layout.addWidget(self.output)
        self.setLayout(layout)
        self.button.clicked.connect(self.solve_expr)

    def solve_expr(self):
        expr_str = self.input.text()
        self.output.clear()
        try:
            expr = sp.sympify(expr_str)
            result = expr
            evalf = expr.evalf()
            self.output.append(f"Resultado simbólico: {sp.pretty(expr)}")
            if result != evalf:
                self.output.append(f"\nResultado numérico: {evalf}")
        except Exception as e:
            self.output.append(f"Error: {e}")

class EquationSolverTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Escribe una ecuación (usa '='). Ejemplo: 2*x + 3 = 11")
        self.input = QLineEdit()
        self.button = QPushButton("Resolver ecuación")
        self.output = QTextEdit()
        self.output.setReadOnly(True)
        layout.addWidget(self.label)
        layout.addWidget(self.input)
        layout.addWidget(self.button)
        layout.addWidget(self.output)
        self.setLayout(layout)
        self.button.clicked.connect(self.solve_equation)

    def solve_equation(self):
        eq_str = self.input.text()
        self.output.clear()
        try:
            if '=' not in eq_str:
                self.output.append("Debes incluir '=' en la ecuación.")
                return
            lhs, rhs = eq_str.split('=')
            lhs = sp.sympify(lhs)
            rhs = sp.sympify(rhs)
            symbols = list(lhs.free_symbols | rhs.free_symbols)
            if not symbols:
                self.output.append("No se detectaron incógnitas.")
                return
            sol = sp.solve(lhs - rhs, symbols[0])
            self.output.append(f"Solución para {symbols[0]}: {sol}")
            # Pasos (solo para ecuaciones simples, ejemplo educational)
            steps = sp.solve(lhs - rhs, symbols[0], dict=True)
            if steps:
                self.output.append(f"\nPasos simbólicos:\n{steps}")
        except Exception as e:
            self.output.append(f"Error: {e}")

class PolynomialTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Introduce un polinomio (ejemplo: x**3 - 3*x**2 + 4):")
        self.input = QLineEdit()
        self.button_factor = QPushButton("Factorizar")
        self.button_roots = QPushButton("Raíces")
        self.output = QTextEdit()
        self.output.setReadOnly(True)
        btn_layout = QHBoxLayout()
        btn_layout.addWidget(self.button_factor)
        btn_layout.addWidget(self.button_roots)
        layout.addWidget(self.label)
        layout.addWidget(self.input)
        layout.addLayout(btn_layout)
        layout.addWidget(self.output)
        self.setLayout(layout)
        self.button_factor.clicked.connect(self.factor_poly)
        self.button_roots.clicked.connect(self.poly_roots)

    def factor_poly(self):
        self.output.clear()
        try:
            expr = sp.sympify(self.input.text())
            fact = sp.factor(expr)
            self.output.append(f"Factorización:\n{sp.pretty(fact)}")
        except Exception as e:
            self.output.append(f"Error: {e}")

    def poly_roots(self):
        self.output.clear()
        try:
            expr = sp.sympify(self.input.text())
            x = list(expr.free_symbols)[0] if expr.free_symbols else sp.symbols('x')
            roots = sp.solve(expr, x)
            self.output.append(f"Raíces:\n{roots}")
        except Exception as e:
            self.output.append(f"Error: {e}")

class MathWizardPro(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MathWizard Pro - Resolver General")
        self.setGeometry(200, 200, 500, 350)
        tabs = QTabWidget()
        tabs.addTab(GeneralMathTab(), "General")
        tabs.addTab(EquationSolverTab(), "Ecuaciones")
        tabs.addTab(PolynomialTab(), "Polinomios")
        layout = QVBoxLayout()
        layout.addWidget(tabs)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(QSS_STYLE)
    mw = MathWizardPro()
    mw.show()
    sys.exit(app.exec_())