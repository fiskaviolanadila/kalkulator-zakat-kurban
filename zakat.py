import tkinter as tk
from tkinter import messagebox

def hitung_zakat():
    try:
        emas = float(entry_emas.get())
        nisab_emas = 85  # Nisab zakat emas dalam gram
        zakat_emas = 0.025 * emas if emas >= nisab_emas else 0
        label_zakat_emas.config(text=f"Zakat Emas: {zakat_emas:.2f} gram")

        perak = float(entry_perak.get())
        nisab_perak = 595  # Nisab zakat perak dalam gram
        zakat_perak = 0.025 * perak if perak >= nisab_perak else 0
        label_zakat_perak.config(text=f"Zakat Perak: {zakat_perak:.2f} gram")
    except ValueError:
        messagebox.showerror("Kesalahan Input", "Masukkan jumlah emas dan perak dalam bentuk angka")

def hitung_qurban():
    try:
        berat_hidup = float(entry_berat_hidup.get())
        jenis_hewan = var_jenis_hewan.get()
        
        if jenis_hewan == "Kambing":
            total_berat = berat_hidup * 0.482
        elif jenis_hewan in ["Sapi", "Kerbau", "Unta"]:
            total_berat = berat_hidup * 0.55  # Ubah faktor menjadi 0.55 untuk Sapi, Kerbau, dan Unta
        else:
            total_berat = 0
        
        label_total_qurban.config(text=f"Total Berat Qurban: {total_berat:.2f} kg")
    except ValueError:
        messagebox.showerror("Kesalahan Input", "Masukkan berat hidup hewan dalam bentuk angka")

# Membuat jendela utama
root = tk.Tk()
root.title("Kalkulator Zakat dan Qurban")
root.geometry("400x400")
root.configure(bg="#E0F7FA")

# Membuat dan menempatkan widget untuk menghitung zakat
frame_zakat = tk.LabelFrame(root, text="Kalkulator Zakat", bg="#E0F7FA", padx=10, pady=10)
frame_zakat.grid(row=0, column=0, padx=10, pady=10)

tk.Label(frame_zakat, text="Emas (gram):", bg="#E0F7FA").grid(row=0, column=0, padx=5, pady=5)
entry_emas = tk.Entry(frame_zakat)
entry_emas.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_zakat, text="Perak (gram):", bg="#E0F7FA").grid(row=1, column=0, padx=5, pady=5)
entry_perak = tk.Entry(frame_zakat)
entry_perak.grid(row=1, column=1, padx=5, pady=5)

tk.Button(frame_zakat, text="Hitung Zakat", command=hitung_zakat, bg="#4CAF50", fg="white", width=15).grid(row=2, column=0, columnspan=2, padx=5, pady=5)

label_zakat_emas = tk.Label(frame_zakat, text="Zakat Emas:", bg="#E0F7FA")
label_zakat_emas.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

label_zakat_perak = tk.Label(frame_zakat, text="Zakat Perak:", bg="#E0F7FA")
label_zakat_perak.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Membuat dan menempatkan widget untuk menghitung qurban
frame_qurban = tk.LabelFrame(root, text="Kalkulator Qurban", bg="#E0F7FA", padx=10, pady=10)
frame_qurban.grid(row=1, column=0, padx=10, pady=10)

tk.Label(frame_qurban, text="Jenis Hewan:", bg="#E0F7FA").grid(row=0, column=0, padx=5, pady=5)
var_jenis_hewan = tk.StringVar(value="Kambing")
jenis_hewan_options = ["Kambing", "Sapi", "Kerbau", "Unta"]
jenis_hewan_menu = tk.OptionMenu(frame_qurban, var_jenis_hewan, *jenis_hewan_options)
jenis_hewan_menu.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_qurban, text="Berat Hidup (kg):", bg="#E0F7FA").grid(row=1, column=0, padx=5, pady=5)
entry_berat_hidup = tk.Entry(frame_qurban)
entry_berat_hidup.grid(row=1, column=1, padx=5, pady=5)

tk.Button(frame_qurban, text="Hitung Qurban", command=hitung_qurban, bg="#2196F3", fg="white", width=15).grid(row=2, column=0, columnspan=2, padx=5, pady=5)

label_total_qurban = tk.Label(frame_qurban, text="Total Berat Qurban:", bg="#E0F7FA")
label_total_qurban.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Memulai event loop utama
root.mainloop()
