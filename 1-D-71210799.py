def ganti_kata(kalimat, cari, ganti):
    kata_kalimat = kalimat.split()

    for i in range(len(kata_kalimat)):
        if kata_kalimat[i] == cari:
            kata_kalimat[i] = ganti

    return " ".join(kata_kalimat)
     

kalimat = input("Masukkan kalimat: ")
cari    = input("Kata yang dicari: ")
ganti   = input("Diganti menjadi: ")

hasil   = ganti_kata(kalimat, cari, ganti)
print("Kalimat baru:", hasil)
