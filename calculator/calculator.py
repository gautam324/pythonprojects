import tkinter as tk
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Resizable Calculator")
        self.root.configure(bg="#222222") 
        
        self.entry = tk.Entry(root, width=35, borderwidth=5, bg="#444444", fg="white", font=("Arial", 40, "bold"))  
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

      
        button_dimensions = {'width': 9, 'height': 3, 'relief': 'flat', 'bg': "#333333", 'fg': 'white', 'font': ("Arial", 12, "bold")}  
        # Simple calculator buttons
        buttons_simple = [
            ('7', lambda: self.show('7')),
            ('8', lambda: self.show('8')),
            ('9', lambda: self.show('9')),
            ('/', lambda: self.show('/')),
            ('4', lambda: self.show('4')),
            ('5', lambda: self.show('5')),
            ('6', lambda: self.show('6')),
            ('*', lambda: self.show('*')),
            ('1', lambda: self.show('1')),
            ('2', lambda: self.show('2')),
            ('3', lambda: self.show('3')),
            ('-', lambda: self.show('-')),
            ('0', lambda: self.show('0')),
            ('.', lambda: self.show('.')),
            ('=', self.solve),
            ('C', self.clear)
        ]

        # Scientific calculator buttons
        buttons_scientific = [
            ("sin", lambda: self.calculate(math.sin)),
            ("cos", lambda: self.calculate(math.cos)),
            ("tan", lambda: self.calculate(math.tan)),
            ("sqrt", lambda: self.calculate(math.sqrt)),
            ("log", lambda: self.calculate(math.log10)),
            ("ln", lambda: self.calculate(math.log)),
            ("π", lambda: self.calculate(math.pi)),
            ("e", lambda: self.calculate(math.e)),
            ("^", lambda: self.show('^')),
        ]

        # Create simple calculator buttons
        for i, (text, command) in enumerate(buttons_simple):
            tk.Button(root, **button_dimensions, text=text, command=command).grid(row=1 + i // 4, column=i % 4, padx=5, pady=5, sticky="ew")

        # Create scientific calculator buttons
        for i, (text, command) in enumerate(buttons_scientific):
            tk.Button(root, **button_dimensions, text=text, command=command).grid(row=5 + i // 3, column=i % 3, padx=5, pady=5, sticky="ew")

        # Make columns and rows resizable
        for i in range(4):
            root.columnconfigure(i, weight=1)
        for i in range(6):
            root.rowconfigure(i, weight=1)

    def show(self, value):
        current = self.entry.get()
        self.entry.delete(0, tk.END)
        self.entry.insert(0, str(current) + str(value))

    def solve(self):
        expression = self.entry.get()
        try:
            result = eval(expression)
            self.entry.delete(0, tk.END)
            self.entry.insert(0, result)
        except Exception as e:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Error")

    def clear(self):
        self.entry.delete(0, tk.END)

    def calculate(self, func=None):
        expression = self.entry.get()
        try:
            if func:
                result = func(float(expression))
            else:
                result = eval(expression)
            self.entry.delete(0, tk.END)
            self.entry.insert(0, result)
        except Exception as e:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Error")

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()
