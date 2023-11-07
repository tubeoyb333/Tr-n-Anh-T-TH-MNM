import tkinter as tk

import numpy as np
from tkinter import messagebox

def solve_equation():
    # Lấy giá trị n và m từ ô nhập liệu
    try:
        n = int(num_eqn_entry.get())
        m = int(num_vars_entry.get())
    except ValueError:
        messagebox.showinfo("Thông báo !",
                            "Số lượng phương trình hoặc số lượng ẩn không hợp lệ. Vui lòng nhập một số nguyên.")
        return

    # Kiểm tra số lượng phương trình và ẩn
    if n != m or n <= 0 or m <= 0 :
        messagebox.showinfo("Thông báo", "Hệ phương trình không tuyến tính vui lòng nhập lại !")
        return
    else:
        # Tạo cửa sổ giao diện cho việc nhập ma trận A và vector B
        input_window = tk.Toplevel(root)
        input_window.title("Nhập Ma Trận A và Vector B")

        # Tạo ma trận A và vector B
        A = np.zeros((n, m))
        B = np.zeros(n)
    def submit_input():
        try:
            # Nhập ma trận A và vector B từ các ô nhập liệu
            for i in range(n):
                for j in range(m):
                    value = matrix_entries[i][j].get()
                    if not value:
                        messagebox.showinfo("Thông báo","Bạn chưa nhập dữ liệu cho ma trận A. Vui lòng nhập lại.")
                        return
                    A[i][j] = float(value)

            for i in range(n):
                value = vector_entries[i].get()
                if not value:
                    messagebox.showinfo("Thông báo","Bạn chưa nhập dữ liệu cho vector B. Vui lòng nhập lại.")
                    return
                B[i] = float(value)
        except ValueError:
            messagebox.showinfo("Thông báo","Dữ liệu nhập không hợp lệ. Vui lòng nhập số vào các ô nhập liệu.")
            return
        # Giải hệ phương trình
        augmented_matrix = np.column_stack((A, B))
        rank_A = np.linalg.matrix_rank(A)
        rank_augmented = np.linalg.matrix_rank(augmented_matrix)

        if rank_A == rank_augmented == m:
            X = np.linalg.solve(A, B)
            result_label.config(text='Nghiệm của hệ phương trình:')
            result_text = []
            for i in range(m):
                result_text.append(f'x{i + 1} = {X[i]:.2f}')
            result_label2.config(text='\n'.join(result_text))
        elif rank_A == rank_augmented < m:
            result_label.config(text='Vô số nghiệm.')
        else:
            result_label.config(text='Vô nghiệm.')
    def reset_input():
        # Xóa dữ liệu nhập trong ô nhập liệu
        for i in range(n):
            for j in range(m):
                matrix_entries[i][j].delete(0, tk.END)

        for i in range(n):
            vector_entries[i].delete(0, tk.END)

        result_label.config(text='')
        result_label2.config(text='')
        num_eqn_entry.delete(0, tk.END)
        num_vars_entry.delete(0, tk.END)

    # Tạo giao diện cho việc nhập ma trận A và vector B
    matrix_entries = []
    vector_entries = []

    for i in range(n):
        row_entries = []
        for j in range(m):
            entry = tk.Entry(input_window)
            entry.grid(row=i, column=j)
            row_entries.append(entry)
        matrix_entries.append(row_entries)

    for i in range(n):
        entry = tk.Entry(input_window)
        entry.grid(row=i, column=m)
        vector_entries.append(entry)

    submit_button = tk.Button(input_window, text="Xác nhận", command=submit_input)
    submit_button.grid(row=n, columnspan=m+1)
    reset_button = tk.Button(input_window, text="Reset", command=reset_input)
    reset_button.grid(row=n+1, columnspan=m+1)

# Tạo cửa sổ giao diện chính
root = tk.Tk()
root.title("Giải Hệ Phương Trình Tuyến Tính")

# Nhập số lượng phương trình và số lượng ẩn
num_eqn_label = tk.Label(root, text="Số lượng phương trình:")
num_eqn_label.pack()
num_eqn_entry = tk.Entry(root)
num_eqn_entry.pack()

num_vars_label = tk.Label(root, text="Số lượng ẩn:")
num_vars_label.pack()
num_vars_entry = tk.Entry(root)
num_vars_entry.pack()

solve_button = tk.Button(root, text="Giải Hệ Phương Trình", command=solve_equation)
solve_button.pack()

# Nhãn để hiển thị kết quả
result_label = tk.Label(root, text="")
result_label.pack()
result_label2 = tk.Label(root, text="")
result_label2.pack()
error_label = tk.Label(root, text="")
error_label.pack()

root.mainloop()
