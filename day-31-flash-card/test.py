import tkinter as tk
import tkinter.font as tkfont


def update_canvas():
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()

    # Define text and font
    text = "안녕하세요, 세계!"  # Korean text
    font = tkfont.Font(family='Arial', size=24)

    # Get font metrics
    ascent = font.metrics("ascent")
    descent = font.metrics("descent")
    linespace = font.metrics("linespace")

    # Calculate text width and height
    text_id = canvas.create_text(
        canvas_width / 2, canvas_height / 2,
        text=text,
        font=font,
        anchor='center'
    )

    bbox = canvas.bbox(text_id)  # Get bounding box of the text
    if bbox:
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
    else:
        text_width = text_height = 0

    # Add padding around the text
    padding = 20
    canvas.config(width=text_width + 2 * padding, height=text_height + 2 * padding)

    # Update the position of the text
    canvas.delete(text_id)  # Remove previous text
    canvas.create_text(
        canvas_width / 2, canvas_height / 2,
        text=text,
        font=font,
        anchor='center'
    )


root = tk.Tk()

# Create a Canvas widget
canvas = tk.Canvas(root, bg='white')
canvas.pack(fill=tk.BOTH, expand=True)

# Initial update
update_canvas()

# Update text position and size when the canvas is resized
canvas.bind("<Configure>", lambda event: update_canvas())

root.mainloop()