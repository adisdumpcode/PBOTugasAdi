import tkinter as tk
from tkinter import ttk, messagebox, Radiobutton

class Classification:
    def __init__(self, root):
        self.root = root
        self.root.title("Klasifikasi Motor")
        self.root.geometry("500x500")
        
        #Variabel untuk menyimpan Pilihan 
        self.moto_option = tk.StringVar(value="") # Untuk CC
        self.jenis_var = tk.StringVar(value="") #Untuk Jenis
        self.widget_create()

    def widget_create(self):
        title_label = tk.Label(text="Klasifikasi Motor", font=("Arial", 20, "bold"))
        title_label.pack(pady=10)

        #Nama Motor
        name_label = tk.Label(text="Merk Motor: ")
        name_label.pack()
        self.name_entry = tk.Entry(self.root,width=35)
        self.name_entry.pack(pady=5)

        #pilih cc motor
        cc_label = tk.Label(text="Masukkan CC Motor: ")
        cc_label.pack()
        #Radio Buttons
        tk.Radiobutton(root, text='110-150', variable=self.moto_option, value='110-150').pack(anchor=tk.W)
        tk.Radiobutton(root, text='250-300', variable=self.moto_option, value='250-300').pack(anchor=tk.W)
        tk.Radiobutton(root, text='600-1000', variable=self.moto_option, value='600-1000').pack(anchor=tk.W)

        #daftar motor
        motor_label = tk.Label(self.root, text="Daftar CC Motor")
        motor_label.pack()

        self.motor_table = ttk.Treeview(self.root, columns=("Merk Motor", "CC Motor", "Jenis Motor"), show="headings")
        self.motor_table.heading("Merk Motor", text="Merk Motor")
        self.motor_table.heading("CC Motor", text="CC Motor")
        self.motor_table.heading("Jenis Motor", text="Jenis Motor")
        self.motor_table.pack()

        add_motor_button = tk.Button(self.root, text="Tambah Motor", command=self.add_motor)
        add_motor_button.pack(pady=10)

        #clear tabel
        clear_button = tk.Button(self.root, text="Clear Table", command=self.clear_data)
        clear_button.pack()

    def klasifikasi(self, cc):
        """Klasifikasi motor berdasarkan CC."""
        if cc == "110-150":
            return "Motor Bebek/Scooter"
        elif cc == "250-300":
            return "Motor Semi Gede"
        elif cc == "600-1000":
            return "Motor Gede"
        else:
            return "Unknown"

    def add_motor(self):
        name = self.name_entry.get()
        motor_cc = self.moto_option.get()
        jenis = self.klasifikasi(motor_cc)

        if name and motor_cc and jenis:
            self.motor_table.insert("", tk.END, values=(name, motor_cc, jenis))
            self.name_entry.delete(0, tk.END)
            self.moto_option.set("")
            self.jenis_var.set("")
        else:
            messagebox.showerror("showerror", "Isi semua tabel dengan benar!")

    def clear_data(self):
        confirm = messagebox.askquestion("confirmation","Yakin ingin Menghapus?")

        if confirm:
            for item in self.motor_table.get_children():
                self.motor_table.delete(item)

if __name__ == '__main__':
    root = tk.Tk()
    app = Classification(root)
    root.mainloop()