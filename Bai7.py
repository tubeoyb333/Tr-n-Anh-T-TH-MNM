import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import matplotlib.pyplot as plt

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

def lammin_image():
    if selected_image is not None:
        x, y, width, height = 100, 270, 150, 150
        image = selected_image.copy()
        roi = image[y:y+height, x:x+width]
        ksize = (21, 21)
        sigma = 0
        blurred_roi = cv2.GaussianBlur(roi, ksize, sigma)
        image[y:y+height, x:x+width] = blurred_roi

        # Hiển thị ảnh đã làm mịn ra figure
        plt.figure(figsize=(6, 6))
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        plt.title("Ảnh đã làm mịn")
        plt.axis('off')  # Tắt trục của biểu đồ
        plt.show()

# Tạo cửa sổ giao diện
root = tk.Tk()
root.title("Làm mịn ảnh")

frame = tk.Frame(root)
frame.pack()

select_button = tk.Button(frame, text="Chọn ảnh", command=select_image)
select_button.pack()

image_label = tk.Label(root)
image_label.pack()

minify_button = tk.Button(frame, text="Làm mịn", command=lammin_image)
minify_button.pack()

root.mainloop()
