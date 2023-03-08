def hitung_mobil():
    mobil = {}
    while True:
        asal = input("Masukkan asal mobil (ketik 'done' untuk keluar): ")
        if asal == "Done":
         break
    mobil[asal] = mobil.get(asal, 0) + 1

    for k, v in mobil.items():
     print(f"Jumlah Mobil {k}: {v}")
     
     
hitung_mobil()