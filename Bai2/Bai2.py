import tkinter as tk
from tkinter import messagebox
from sympy import symbols, sympify, diff, integrate
import numpy as np
import matplotlib.pyplot as plt

expression = None
derivative = None

def calculate_derivative():
    global expression, derivative

    degree = degree_entry.get()
    coefficients = coefficients_entry.get()
    variable = variable_entry.get()
    try:
        x = symbols(variable)
        degree = int(degree)
        coefficients = [float(coeff) for coeff in coefficients.split(",")]

        # Tạo biểu thức dựa trên bậc và hệ số
        expression = 0
        for i in range(0, degree+1):
            expression += coefficients[i] * x ** (degree - i)

        # Tính đạo hàm
        derivative = diff(expression, x)

        result_label.config(text=f"Phương trình gốc: {expression}\nĐạo hàm: {derivative}")

    except Exception as e:
        messagebox.showerror("Lỗi", f"Lỗi trong quá trình tính toán: {str(e)}")
        result_label.config(text="Phương trình gốc: \nĐạo hàm: ")

def calculate_integral():
    lower_limit = lower_limit_entry.get()
    upper_limit = upper_limit_entry.get()
    coefficients = coefficients_entry.get()
    variable = variable_entry.get()
    try:
        x = symbols(variable)
        lower_limit = float(lower_limit)
        upper_limit = float(upper_limit)
        if lower_limit >= upper_limit:
            messagebox.showerror("Lỗi", f"Hệ số trên phải lớn hơn hệ số dưới")
        else:
            coefficients = [float(coeff) for coeff in coefficients.split(",")]

            # Tạo biểu thức dựa trên bậc và hệ số
            expression = 0
            for i in range(0, len(coefficients)):
                expression += coefficients[i] * x ** (len(coefficients) - i - 1)

            # Tính tích phân
            integral = integrate(expression, (x, lower_limit, upper_limit))

            result_label.config(text=f"Phương trình gốc: {expression}\nTích phân từ {lower_limit} đến {upper_limit}: {integral}")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Lỗi trong quá trình tính toán: {str(e)}")
        result_label.config(text="Phương trình gốc: \nTích phân: ")

def plot_expression():
    if expression is not None and derivative is not None:
        x = symbols(variable_entry.get())
        x_values = np.linspace(-10, 10, 400)
        y_expression = [expression.subs(x, val) for val in x_values]
        y_derivative = [derivative.subs(x, val) for val in x_values]

        fig, axes = plt.subplots(1, 2, figsize=(10, 5))

        axes[0].plot(x_values, y_expression, label="Phương trình gốc")
        axes[0].set_xlabel(variable_entry.get())
        axes[0].set_ylabel("Giá trị")
        axes[0].legend()

        axes[1].plot(x_values, y_derivative, label="Đạo hàm")
        axes[1].set_xlabel(variable_entry.get())
        axes[1].set_ylabel("Giá trị")
        axes[1].legend()

        plt.tight_layout()
        plt.show()
    else:
        messagebox.showerror("Lỗi", "Vui lòng tính đạo hàm trước khi vẽ biểu đồ.")

# Tạo cửa sổ giao diện
root = tk.Tk()
root.title("Tính Đạo Hàm và Tích Phân Của Phương Trình")

# Nhãn hướng dẫn
degree_label = tk.Label(root, text="Bậc của phương trình:")
degree_label.pack()

# Ô nhập liệu cho bậc
degree_entry = tk.Entry(root)
degree_entry.pack()

# Nhãn hướng dẫn
coefficients_label = tk.Label(root, text="Hệ số (các hệ số cách nhau bằng dấu phẩy từ bậc cao đến bậc thấp):")
coefficients_label.pack()

# Ô nhập liệu cho hệ số
coefficients_entry = tk.Entry(root)
coefficients_entry.pack()

# Nhãn hướng dẫn
variable_label = tk.Label(root, text="Tên biến:")
variable_label.pack()

# Ô nhập liệu cho biến
variable_entry = tk.Entry(root)
variable_entry.pack()

# Nhãn hướng dẫn
lower_limit_label = tk.Label(root, text="Hệ số dưới tích phân:")
lower_limit_label.pack()

# Ô nhập liệu cho hệ số đầu
lower_limit_entry = tk.Entry(root)
lower_limit_entry.pack()

# Nhãn hướng dẫn
upper_limit_label = tk.Label(root, text="Hệ số trên tích phân:")
upper_limit_label.pack()

# Ô nhập liệu cho hệ số cuối
upper_limit_entry = tk.Entry(root)
upper_limit_entry.pack()

# Nút tính đạo hàm
calculate_derivative_button = tk.Button(root, text="Tính Đạo Hàm", command=calculate_derivative)
calculate_derivative_button.pack()

# Nút tính tích phân
calculate_integral_button = tk.Button(root, text="Tính Tích Phân", command=calculate_integral)
calculate_integral_button.pack()

# Nút vẽ biểu đồ
plot_expression_button = tk.Button(root, text="Vẽ Biểu Đồ", command=plot_expression)
plot_expression_button.pack()

# Nhãn kết quả
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
