import tkinter as tk
import clustering as cs

# Create tkinter window
window_main = tk.Tk(className='ALGORITMA K-MEANS')
window_main.geometry("300x350")
window_main.title("ALGORITMA K-MEANS")

# Title label
label_title = tk.Label(window_main, text="ALGORITMA K-MEANS", font=("Arial", 14, "bold"))
label_title.pack(pady=10)

# Button data
button_data = [
    ("Figure Peminjam", cs.peminjam),
    ("Figure Titik Awal Centroid", cs.titikAwal),
    ("Hasil Clustering", cs.hasil)
]

# Create buttons for menu
for text, command in button_data:
    button = tk.Button(window_main, text=text, command=command, width=20, height=2)
    button.pack(pady=5)

# Run tkinter event loop
window_main.mainloop()
