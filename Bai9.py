import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog, simpledialog
from PIL import Image, ImageTk

selected_image = None  # Biến toàn cục để lưu ảnh đã chọn

def select_image():
    global selected_image
    file_path = filedialog.askopenfilename()
    if file_path:
        img = cv2.imread(file_path)
        selected_image = img

        # Hiển thị ảnh đã chọn trên giao diện
        image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(image)
        image = ImageTk.PhotoImage(image)
        image_label.config(image=image)
        image_label.image = image

def smooth_image(x,y):
    global selected_image
    if selected_image is not None:
        kernel_sharpen_1 = np.array([[x, x, x], [x, x, x], [x, x, x]])
        # applying different kernels to the input image
        output_1 = cv2.filter2D(selected_image, -1, kernel_sharpen_1)
        kernel = np.array([[0, -y, 0],
                           [-y, 1 + 4 * y, -y],
                           [0, -y, 0]])

        # Áp dụng kernel lên ảnh gốc
        output_2 = cv2.filter2D(output_1, -1, kernel)

        # Hiển thị ảnh đã chỉnh độ nét

        cv2.imshow('Sharpening', output_2)
def get_values1():
    x = float(x_entry.get())
    y = float(y_entry.get())
    smooth_image(x,y)

root = tk.Tk()
root.title("Smooth Image App")

frame = tk.Frame(root)
frame.pack()

x_label = tk.Label(frame, text="Điền độ sáng (0 - 5):")
x_label.pack()
x_entry = tk.Entry(frame)
x_entry.pack()

y_label = tk.Label(frame, text="Điền tương phản(0 - 5):")
y_label.pack()
y_entry = tk.Entry(frame)
y_entry.pack()

select_button = tk.Button(frame, text="Select Image", command=select_image)
select_button.pack()

select_button = tk.Button(frame, text="Smooth Image", command=get_values1)
select_button.pack()

image_label = tk.Label(root)
image_label.pack()

canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

root.mainloop()
