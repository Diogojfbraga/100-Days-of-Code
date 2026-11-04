
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

logo_path = None
image_path = None
result_image = None


# Select background image
def open_file():
    global image_path

    image_path = filedialog.askopenfilename(
        title="Select Background Image",
        filetypes=[
            ("Image files", ("*.png", "*.jpg", "*.jpeg")),
            ("All files", "*.*")
        ]
    )


# Select watermark logo
def open_filelogo():
    global logo_path

    logo_path = filedialog.askopenfilename(
        title="Select Logo",
        filetypes=[
            ("Image files", ("*.png", "*.jpg", "*.jpeg")),
            ("All files", "*.*")
        ]
    )


# Add watermark
def watermark():
    global result_image

    if not image_path or not logo_path:
        messagebox.showwarning(
            "Missing Image",
            "Please select a background image and a logo."
        )
        return

    # Open images
    background_image = Image.open(image_path).convert("RGBA")
    logo_image = Image.open(logo_path).convert("RGBA")

    background_width, background_height = background_image.size
    logo_width, logo_height = logo_image.size

    # Resize logo to 20% of background width
    new_logo_width = int(background_width * 0.2)
    new_logo_height = int(
        logo_height * (new_logo_width / logo_width)
    )

    logo_image = logo_image.resize(
        (new_logo_width, new_logo_height),
        Image.Resampling.LANCZOS
    )

    # Set logo transparency to 50%
    alpha = logo_image.getchannel("A")
    alpha = alpha.point(lambda p: int(p * 0.5))
    logo_image.putalpha(alpha)

    # Position logo at bottom-right
    margin = 20

    logo_x = background_width - new_logo_width - margin
    logo_y = background_height - new_logo_height - margin

    # Create result image
    result_image = background_image.copy()

    result_image.paste(
        logo_image,
        (max(0, logo_x), max(0, logo_y)),
        logo_image
    )

    # Display result in a new Tkinter window
    preview_window = tk.Toplevel(window)
    preview_window.title("Watermarked Image")

    preview_image = result_image.copy()
    preview_image.thumbnail((700, 500))

    photo = ImageTk.PhotoImage(preview_image)

    label = tk.Label(preview_window, image=photo)
    label.image = photo
    label.pack(padx=10, pady=10)


# Save watermarked image
def save_image():

    if result_image is None:
        messagebox.showwarning(
            "No Image",
            "Please create a watermarked image first."
        )
        return

    save_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[
            ("PNG files", "*.png"),
            ("JPEG files", "*.jpg")
        ]
    )

    if save_path:

        if save_path.lower().endswith((".jpg", ".jpeg")):
            result_image.convert("RGB").save(save_path)
        else:
            result_image.save(save_path)

        messagebox.showinfo(
            "Saved",
            "Watermarked image saved successfully!"
        )


# Main application
window = tk.Tk()
window.title("Watermark App")
window.geometry("500x400")

label = tk.Label(
    window,
    text="Watermark Application",
    font=("Arial", 25)
)
label.pack(pady=20)

button1 = tk.Button(
    window,
    text="Select Image",
    command=open_file
)
button1.pack(pady=10)

button2 = tk.Button(
    window,
    text="Select Logo",
    command=open_filelogo
)
button2.pack(pady=10)

button3 = tk.Button(
    window,
    text="Show Watermarked Image",
    command=watermark
)
button3.pack(pady=10)

button4 = tk.Button(
    window,
    text="Save Image",
    command=save_image
)
button4.pack(pady=10)

window.mainloop()
