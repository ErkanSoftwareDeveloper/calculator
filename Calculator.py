import tkinter as tk  # Tkinter Kütüphanesini ice aktariyoruz

# Pencere oluşturma
root = tk.Tk()
root.title("Calculator")  # Pencere başlığı
root.geometry("400x600")  # pencere boyutu
root.resizable(False, False)  # Pencereyi büyütüp kücültme kapali


# -- Entry (Calculator Display) --
entry = tk.Entry(
    root,
    width=20,
    font=("Arial", 18),
    bd=5,
    relief="ridge",
    justify="right"  # yazilar saga hizali olacak
)
entry.pack(pady=10)  # ekrana ekliyoruz, biraz yukaridan bosluk biraktik

# -- Button (Calculator Buttons) --
button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    ("7", 0, 0), ("8", 0, 1), ("9", 0, 2), ("/", 0, 3),
    ("4", 1, 0), ("5", 1, 1), ("6", 1, 2), ("*", 1, 3),
    ("1", 2, 0), ("2", 2, 1), ("3", 2, 2), ("-", 2, 3),
    ("0", 3, 0), (".", 3, 1), ("=", 3, 2), ("+", 3, 3),
]

for (text, row, col) in buttons:
    btn = tk.Button(
        button_frame, text=text, width=5, height=2, font=("Arial", 14)
    )
    btn.grid(row=row, column=col, padx=5, pady=5)

# -- FUNCTIONS --


def button_click(char):
    current = entry.get()  # ekrandaki mevcut yaziyi al
    entry.delete(0, tk.END)  # ekrani temizle
    entry.insert(0, current + char)  # eski yazinin üstüne yeni karakter ekle


def calculate():
    try:
        # eval fonksiyonu ile matematiksel ifadeyi hesapla
        result = eval(entry.get())
        entry.delete(0, tk.END)  # ekrani temizle
        entry.insert(0, str(result))  # sonucu ekrana yaz
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")  # hata durumunda ekrana "Error" yaz


for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(
            button_frame, text=text, width=5, height=2, font=("Arial", 14),
            # "=" butonuna tiklandiginda calculate fonksiyonu cagrilir
            command=calculate
        )
    else:  # diger butonlar normal calisiyor
        btn = tk.Button(
            button_frame, text=text, width=5, height=2, font=("Arial", 14),
            # her butona tiklandiginda button_click fonksiyonu cagrilir
            command=lambda t=text: button_click(t)
        )
    btn.grid(row=row, column=col, padx=5, pady=5)

clear_btn = tk.Button(root, text="C", width=20, height=2, font=("Arial", 14),
                      # "C" butonuna tiklandiginda ekrani temizle
                      command=lambda: entry.delete(0, tk.END))
clear_btn.pack(pady=10)  # ekrana ekle


def key_press(event):
    char = event.keysym  # basilan tusun karakterini al

    if char in "0123456789":
        button_click(char)  # sayiyi yaz
    elif char in ("plus", "minus", "asterisk", "slash", "period"):
        mapping = {"plus": "+", "minus": "-",
                   "asterisk": "*", "slash": "/", "period": "."}
        button_click(mapping[char])  # isaretleri yaz
    elif char == "Return":
        calculate()  # Enter tusuna basildiginda hesapla
    elif char == "BackSpace":  # geri silme tusu
        current = entry.get()
        entry.delete(0, tk.END)
        entry.insert(0, current[:-1])  # son karakteri sil
    elif char == "Escape":  # temizle
        entry.delete(0, tk.END)  # ekrani temizle


root.bind("<Key>", key_press)  # klavye tuslarina bagla


# uygulama Sürekli calissin diye mainloop
root.mainloop()
