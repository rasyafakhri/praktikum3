import math

def hitung_luas(r):
    return math.pi * r**2

def hitung_keliling(r):
    return 2 * math.pi * r

def main():
    radius = float(input("Masukkan jari-jari lingkaran: "))
    
    luas = hitung_luas(radius)
    keliling = hitung_keliling(radius)
    
    print(f"Luas lingkaran: {luas:.2f}")
    print(f"Keliling lingkaran: {keliling:.2f}")

if __name__ == "__main__":
    main()
