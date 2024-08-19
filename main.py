import numpy as np
import matplotlib.pyplot as plt

def gambar_grafik(fungsi, x_min, x_max):
    # Menghasilkan nilai x dari x_min hingga x_max
    x = np.linspace(x_min, x_max, 400)
    # Menghitung nilai y berdasarkan fungsi yang diberikan
    y = fungsi(x)
    
    # Membuat grafik
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label=f"y = {fungsi.__name__}(x)")
    plt.title("Grafik Fungsi Matematika")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    plt.show()

def fungsi_sin(x):
    return np.sin(x)

def fungsi_cos(x):
    return np.cos(x)

def fungsi_parabola(x):
    return x**2

def main():
    print("Selamat datang di aplikasi grafik fungsi matematika!")
    print("Pilih fungsi yang ingin digambar:")
    print("1. Sinus (sin(x))")
    print("2. Kosinus (cos(x))")
    print("3. Parabola (x^2)")
    
    pilihan = input("Masukkan nomor pilihan (1/2/3): ")
    
    if pilihan == "1":
        fungsi = fungsi_sin
    elif pilihan == "2":
        fungsi = fungsi_cos
    elif pilihan == "3":
        fungsi = fungsi_parabola
    else:
        print("Pilihan tidak valid.")
        return
    
    x_min = float(input("Masukkan nilai x minimum: "))
    x_max = float(input("Masukkan nilai x maksimum: "))
    
    gambar_grafik(fungsi, x_min, x_max)

if __name__ == "__main__":
    main()
