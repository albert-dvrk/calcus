"""
Калькулятор с графическим интерфейсом (tkinter) — точка входа.

Файл состоит из двух частей:
  1) CalculatorEngine — логика калькулятора (без окон), она вызывает функции
     из operations.py и методы памяти из memory.py;
  2) CalculatorApp — окно с кнопками, оно только передаёт нажатия в движок.

Кто добавляет новую операцию в operations.py, дописывает сюда:
  1) импорт функции
  2) кнопку в нужный список (BINARY_OPS или UNARY_OPS)
"""

import tkinter as tk
from operations import (
    add, subtract, multiply, divide, mod, power,
    sin_deg, cos_deg, sqrt, floor_value, ceil_value,
)
from memory import Memory

class CalculatorEngine:
    """Логика калькулятора: что показано на экране и что делает каждая кнопка."""
    def __init__(self):
        self.memory = Memory()
        self.display = "0"      # текст на экране
        self.status = ""        # сообщение под экраном (ошибки)
        self.accumulator = None  # первое число, ждущее второго
        self.pending_op = None   # операция, ждущая второго числа
        self.fresh = True        # следующая цифра начнёт ввод заново

    def press_digit(self, digit):
        self.status = ""
        if self.fresh or self.display == "0":
            self.display = digit
        else:
            self.display += digit
        self.fresh = False
    def press_dot(self):
        self.status = ""
        if self.fresh:
            self.display = "0."
            self.fresh = False
        elif "." not in self.display:
            self.display += "."
    def negate(self):
        if self.display == "0":
            return
        if self.display.startswith("-"):
            self.display = self.display[1:]
        else:
            self.display = "-" + self.display
    def backspace(self):
        if self.fresh:
            return
        self.display = self.display[:-1]
        if self.display in ("", "-"):
            self.display = "0"
    def clear(self):
        self.display = "0"
        self.status = ""
        self.accumulator = None
        self.pending_op = None
        self.fresh = True

    def current_value(self):
        return float(self.display)
    def show_result(self, value):
        """Выводит результат на экран; None (функция ещё не написана) и ошибки — в статус."""
        if value is None:
            self.fail("операция ещё не реализована")
            return False
        value = round(float(value), 10)
        self.display = format(value, ".12g")
        self.fresh = True
        return True
    def fail(self, message):
        self.display = "0"
        self.status = f"Ошибка: {message}"
        self.accumulator = None
        self.pending_op = None
        self.fresh = True
    def apply_binary(self):
        """Выполняет отложенную операцию над accumulator и текущим числом."""
        if self.pending_op is None:
            return True
        try:
            result = self.pending_op(self.accumulator, self.current_value())
        except (ValueError, ZeroDivisionError, OverflowError) as e:
            self.fail(str(e) or "некорректная операция")
            return False
        self.pending_op = None
        self.accumulator = None
        return self.show_result(result)
    def press_binary(self, func):
        """Кнопки двух чисел: +, −, ×, ÷, mod, xʸ."""
        self.status = ""
        if self.pending_op is not None and not self.fresh:
            if not self.apply_binary():  # цепочка: 2 + 3 + 4
                return
        self.accumulator = self.current_value()
        self.pending_op = func
        self.fresh = True
    def press_equals(self):
        self.status = ""
        if self.pending_op is not None:
            self.apply_binary()
    def press_unary(self, func):
        """Кнопки одного числа: sin, cos, √, floor, ceil."""
        self.status = ""
        try:
            result = func(self.current_value())
        except (ValueError, OverflowError) as e:
            self.fail(str(e) or "некорректная операция")
            return
        self.show_result(result)

    def memory_add(self):
        self.memory.madd(self.current_value())
        self.fresh = True
    def memory_subtract(self):
        self.memory.msubtract(self.current_value())
        self.fresh = True
    def memory_recall(self):
        self.show_result(self.memory.mrecall())
    def memory_clear(self):
        self.memory.mclear()
    def memory_store(self):
        self.memory.mstore(self.current_value())
        self.fresh = True
    def memory_in_use(self):
        return self.memory.mrecall() != 0

class CalculatorApp:
    """Окно калькулятора: рисует кнопки и передаёт нажатия в CalculatorEngine."""
    def __init__(self, root):
        self.root = root
        self.engine = CalculatorEngine()
        root.title("Калькулятор")
        root.resizable(False, False)
        self.display_var = tk.StringVar()
        self.status_var = tk.StringVar()
        tk.Label(root, textvariable=self.display_var, anchor="e",
                 font=("Arial", 26), bg="white", relief="sunken",
                 padx=8, pady=8).grid(row=0, column=0, columnspan=5,
                                      sticky="ew", padx=6, pady=(6, 2))
        tk.Label(root, textvariable=self.status_var, anchor="w",
                 fg="red", font=("Arial", 10)).grid(row=1, column=0,
                                                    columnspan=5, sticky="ew", padx=8)
        e = self.engine
        # (текст кнопки, действие). None — пустая клетка.
        layout = [
            [("MC", e.memory_clear), ("MR", e.memory_recall), ("MS", e.memory_store),
             ("M+", e.memory_add), ("M-", e.memory_subtract)],
            [("sin", lambda: e.press_unary(sin_deg)), ("cos", lambda: e.press_unary(cos_deg)),
             ("√", lambda: e.press_unary(sqrt)),
             ("floor", lambda: e.press_unary(floor_value)),
             ("ceil", lambda: e.press_unary(ceil_value))],
            [("7", lambda: e.press_digit("7")), ("8", lambda: e.press_digit("8")),
             ("9", lambda: e.press_digit("9")), ("÷", lambda: e.press_binary(divide)),
             ("C", e.clear)],
            [("4", lambda: e.press_digit("4")), ("5", lambda: e.press_digit("5")),
             ("6", lambda: e.press_digit("6")), ("×", lambda: e.press_binary(multiply)),
             ("⌫", e.backspace)],
            [("1", lambda: e.press_digit("1")), ("2", lambda: e.press_digit("2")),
             ("3", lambda: e.press_digit("3")), ("−", lambda: e.press_binary(subtract)),
             ("xʸ", lambda: e.press_binary(power))],
            [("0", lambda: e.press_digit("0")), (".", e.press_dot),
             ("±", e.negate), ("+", lambda: e.press_binary(add)),
             ("mod", lambda: e.press_binary(mod))],
        ]
        for r, row in enumerate(layout, start=2):
            for c, (text, action) in enumerate(row):
                self.add_button(text, action, r, c)
        self.add_button("=", e.press_equals, len(layout) + 2, 0, columnspan=5)
        self.bind_keyboard()
        self.refresh()
    def add_button(self, text, action, row, col, columnspan=1):
        tk.Button(self.root, text=text, width=6, height=2, font=("Arial", 12),
                  command=lambda: self.on_press(action)
                  ).grid(row=row, column=col, columnspan=columnspan,
                         sticky="ew", padx=2, pady=2)
    def on_press(self, action):
        action()
        self.refresh()
    def refresh(self):
        self.display_var.set(self.engine.display)
        mem = "M  " if self.engine.memory_in_use() else ""
        self.status_var.set(mem + self.engine.status)
    def bind_keyboard(self):
        e = self.engine
        for d in "0123456789":
            self.root.bind(d, lambda ev, d=d: self.on_press(lambda: e.press_digit(d)))
        self.root.bind(".", lambda ev: self.on_press(e.press_dot))
        self.root.bind("+", lambda ev: self.on_press(lambda: e.press_binary(add)))
        self.root.bind("-", lambda ev: self.on_press(lambda: e.press_binary(subtract)))
        self.root.bind("*", lambda ev: self.on_press(lambda: e.press_binary(multiply)))
        self.root.bind("/", lambda ev: self.on_press(lambda: e.press_binary(divide)))
        self.root.bind("<Return>", lambda ev: self.on_press(e.press_equals))
        self.root.bind("=", lambda ev: self.on_press(e.press_equals))
        self.root.bind("<BackSpace>", lambda ev: self.on_press(e.backspace))
        self.root.bind("<Escape>", lambda ev: self.on_press(e.clear))

def main():
    root = tk.Tk()
    CalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()