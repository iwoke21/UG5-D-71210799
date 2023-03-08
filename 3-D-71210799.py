
import math

while True: 
        jarak_awal_input = input("Masukkan jarak awal (dalam meter): ")

        if jarak_awal_input.lower() == "berhenti":
            print("Program dihentikan")
        break

try:
    jarak_awal = float(jarak_awal_input)
    sudut_elevasi_pertama = float(input("Masukkan sudut elevasi pada menit ke-5 (dalam derajat): "))
    sudut_elevasi_kedua = float(input("Masukkan sudut elevasi pada menit ke-6 (dalam derajat): "))

    sudut_elevasi_pertama_rad = math.radians(sudut_elevasi_pertama)
    sudut_elevasi_kedua_rad = math.radians(sudut_elevasi_kedua)

    ketinggian_benda = (jarak_awal * math.tan(sudut_elevasi_kedua_rad)) - (jarak_awal * math.tan(sudut_elevasi_pertama_rad))

    print(f"Ketinggian drone pada menit ke-5 adalah {ketinggian_benda} meter\n")

except ValueError:
    print("Input yang dimasukkan tidak valid\n")



