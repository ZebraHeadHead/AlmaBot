import tkinter as tk
from tkinter import messagebox
import webScraper  # Import your script function


def run_script():
    user_input = entry.get()
    item_list = webScraper.namesIntoLinks(
        webScraper.findItemNames(user_input, output_label))

    for widget in output_frame.winfo_children():
        widget.destroy()
    row_num = 0

    for i in item_list:
        output = webScraper.getList(i)
        col_num = 0
        for item in output:
            label = tk.Label(output_frame, text=item)
            label.grid(row=row_num, column=col_num)
            col_num += 1
        row_num += 1


# Create the main window
root = tk.Tk()
root.title("Material Finder")
root.geometry("1300x500")


# Input field
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Run button
run_button = tk.Button(root, text="Run Script", command=run_script)
run_button.pack(pady=5)

# Output label
output_label = tk.Label(root, text="", wraplength=250)
output_label.pack(pady=10)
# Frame to hold the dynamically created labels (rows and columns)
output_frame = tk.Frame(root)
output_frame.pack(pady=10)

for i in range(10):
    output_frame.grid_rowconfigure(i, weight=1)

# Run the application
root.mainloop()
