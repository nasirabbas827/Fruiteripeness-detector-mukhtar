import tkinter as tk
from tkinter import filedialog, Label, Button, Frame, Canvas
from tkinter import ttk
from PIL import Image, ImageTk
import numpy as np
import cv2
from tensorflow.keras.models import load_model

# Load trained CNN model
model = load_model("fruit_ripeness_cnn_model.h5")
ripeness_classes = ['Unripe', 'Ripe', 'Overripe']
IMG_SIZE = (128, 128)

# Tkinter window
root = tk.Tk()
root.title("Fruit Ripeness Detector")
root.geometry("900x650")
root.resizable(True, True)

# Create a canvas for gradient background
canvas = Canvas(root, width=600, height=650, highlightthickness=0)
canvas.pack(fill="both", expand=True)

# Create a gradient effect (light green to white)
def create_gradient(canvas, width, height):
    limit = height
    for i in range(limit):
        r = int(220 - (i / limit) * 100)  # Red component
        g = int(245 - (i / limit) * 50)   # Green component
        b = int(220 - (i / limit) * 100)  # Blue component
        color = f'#{r:02x}{g:02x}{b:02x}'
        canvas.create_line(0, i, width, i, fill=color)

create_gradient(canvas, 600, 650)

# Configure ttk style for modern look
style = ttk.Style()
style.theme_use('clam')

# Custom button style with rounded effect and hover
style.configure('Custom.TButton', 
                font=('Helvetica', 12, 'bold'),
                padding=10,
                background='#4CAF50',
                foreground='white',
                borderwidth=0)
style.map('Custom.TButton',
          background=[('active', '#45a049'), ('!active', '#4CAF50')],
          foreground=[('active', 'white'), ('!active', 'white')])

# Frame to hold all widgets (centered with padding)
main_frame = Frame(canvas, bg='white', bd=5, relief='ridge')
main_frame.place(relx=0.5, rely=0.5, anchor='center', width=500, height=550)

# Title label
title_label = Label(main_frame, 
                    text="Fruit Ripeness Detector", 
                    font=("Helvetica", 20, "bold"), 
                    bg='white', 
                    fg='#2E7D32')
title_label.pack(pady=20)

# Label to display image with a border
image_frame = Frame(main_frame, bg='white', bd=3, relief='solid')
image_frame.pack(pady=10)
image_label = Label(image_frame, bg='white')
image_label.pack()

# Label to display prediction
result_label = Label(main_frame, 
                     text="", 
                     font=("Helvetica", 14), 
                     bg='white', 
                     fg='#1B5E20')
result_label.pack(pady=20)

def predict_ripeness():
    # Open file dialog
    file_path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.jpg *.jpeg *.png")]
    )
    if not file_path:
        return
    
    # Load and display image
    img = Image.open(file_path)
    img_resized = img.resize((250, 250))
    img_tk = ImageTk.PhotoImage(img_resized)
    image_label.configure(image=img_tk)
    image_label.image = img_tk

    # Preprocess image for model
    img_array = cv2.imread(file_path)
    img_array = cv2.cvtColor(img_array, cv2.COLOR_BGR2RGB)
    img_array = cv2.resize(img_array, IMG_SIZE)
    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Predict
    preds = model.predict(img_array)
    pred_class = ripeness_classes[np.argmax(preds)]
    confidence = np.max(preds) * 100

    # Display result
    result_label.config(text=f"Predicted: {pred_class} ({confidence:.2f}%)")

# Button to select image and predict
select_button = ttk.Button(main_frame, 
                          text="Select Image", 
                          command=predict_ripeness, 
                          style='Custom.TButton')
select_button.pack(pady=20)


root.mainloop()