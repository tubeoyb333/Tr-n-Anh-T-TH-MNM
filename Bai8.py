import cv2
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import messagebox

selected_image = None  # Biến toàn cục để lưu ảnh đã chọn

def select_image():
    global selected_image1
    file_path = filedialog.askopenfilename()
    if file_path:
        img1 = cv2.imread(file_path)
        selected_image1 = img1

        # Hiển thị ảnh đã chọn trên giao diện
        image = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(image)
        image = ImageTk.PhotoImage(image)
        image_label.config(image=image)
        image_label.image = image
def edge_detection(ed1, ed2):
    if selected_image1 is not None:
        img = selected_image1
        edges = cv2.Canny(img, ed1, ed2)
        plt.figure(3)
        plt.imshow(edges, cmap='gray')
        plt.title("Edge Detection")
        plt.show()
def get_values2():
    try:
        ed1 = float(ed1_entry.get())
        ed2 = float(ed2_entry.get())
        edge_detection(ed1, ed2)
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ")
root = tk.Tk()
root.title("Tách biên ảnh")

frame = tk.Frame(root)
frame.pack()
ed1_label = tk.Label(frame, text="Enter ed1:")
ed1_label.pack()
ed1_entry = tk.Entry(frame)
ed1_entry.pack()

ed2_label = tk.Label(frame, text="Enter ed2:")
ed2_label.pack()
ed2_entry = tk.Entry(frame)
ed2_entry.pack()
select_button = tk.Button(frame, text="Select Image", command=select_image)
select_button.pack()

image_label = tk.Label(root)
image_label.pack()
edge_button = tk.Button(frame, text="Edge Detection", command=get_values2)
edge_button.pack()

canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

root.mainloop()