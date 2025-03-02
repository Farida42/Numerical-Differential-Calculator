import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

class NumericalDifferentiationCalculator:
    def _init_(self, master):
        self.master = master
        self.master.title("Numerical Differentiation Calculator")

        # Input Function
        self.function_label = tk.Label(self.master, text="Enter Function:")
        self.function_label.grid(row=0, column=0, sticky="E")

        self.function_entry = tk.Entry(self.master)
        self.function_entry.grid(row=0, column=1, columnspan=2, sticky="WE")

        # Point
        self.point_label = tk.Label(self.master, text="Enter Point:")
        self.point_label.grid(row=1, column=0, sticky="E")

        self.point_entry = tk.Entry(self.master)
        self.point_entry.grid(row=1, column=1, columnspan=2, sticky="WE")

        # Step Size
        self.step_label = tk.Label(self.master, text="Enter Step Size:")
        self.step_label.grid(row=2, column=0, sticky="E")

        self.step_entry = tk.Entry(self.master)
        self.step_entry.grid(row=2, column=1, columnspan=2, sticky="WE")

        # Method Selection
        self.method_label = tk.Label(self.master, text="Select Method:")
        self.method_label.grid(row=3, column=0, sticky="E")

        self.method_combobox = ttk.Combobox(self.master, values=["Forward Difference", "Backward Difference", "Central Difference"])
        self.method_combobox.grid(row=3, column=1, columnspan=2, sticky="WE")
        self.method_combobox.set("Forward Difference")

        # Calculate Button
        self.calculate_button = tk.Button(self.master, text="Calculate", command=self.calculate)
        self.calculate_button.grid(row=4, column=0, columnspan=3, pady=10)

        # Result Display
        self.result_label = tk.Label(self.master, text="")
        self.result_label.grid(row=5, column=0, columnspan=3)

        # Graph
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.master)
        self.canvas.get_tk_widget().grid(row=0, column=3, rowspan=6, padx=10)

    def calculate(self):
        try:
            function_str = self.function_entry.get()
            point = float(self.point_entry.get())
            step_size = float(self.step_entry.get())
            method = self.method_combobox.get()

            function = lambda x: eval(function_str)

            if method == "Forward Difference":
                derivative = (function(point + step_size) - function(point)) / step_size
            elif method == "Backward Difference":
                derivative = (function(point) - function(point - step_size)) / step_size
            elif method == "Central Difference":
                derivative = (function(point + step_size) - function(point - step_size)) / (2 * step_size)
            else:
                raise ValueError("Invalid differentiation method")

            self.result_label.config(text=f"Estimated Derivative: {derivative}")

            x_values = np.linspace(point - 2, point + 2, 100)
            y_values = function(x_values)

            self.ax.clear()
            self.ax.plot(x_values, y_values, label="Function")
            self.ax.scatter(point, function(point), color="red", label="Point of Interest")
            self.ax.legend()

            tangent_line = derivative * (x_values - point) + function(point)
            self.ax.plot(x_values, tangent_line, label="Tangent Line", linestyle="--")

            self.canvas.draw()

        except Exception as e:
            self.result_label.config(text=f"Error: {str(e)}")

if _name_ == "_main_":
    root = tk.Tk()
    app = NumericalDifferentiationCalculator(root)
    root.mainloop()