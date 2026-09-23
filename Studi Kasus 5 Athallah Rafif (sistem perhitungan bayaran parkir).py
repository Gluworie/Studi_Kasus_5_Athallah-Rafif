def hitung_biaya_parkir(jenis_kendaraan, lama_parkir):
    if jenis_kendaraan == "Mobil":
        tarif_per_jam = 5000
    elif jenis_kendaraan == "Motor":
        tarif_per_jam = 3000
    else:
        print("Jenis kendaraan tidak dikenali.")
        return 0

    total_biaya = tarif_per_jam * lama_parkir
    return total_biaya

jenis_kendaraan = "Mobil"
jam_masuk = 8
jam_keluar = 13

lama_parkir = jam_keluar - jam_masuk
total_biaya = hitung_biaya_parkir(jenis_kendaraan, lama_parkir)

print("======= Struk Parkir =======")
print("Jenis Kendaraan :", jenis_kendaraan)
print("Jam Masuk       :", jam_masuk)
print("Jam Keluar      :", jam_keluar)
print("Lama Parkir     :", lama_parkir, "jam")
print("Total Biaya     : Rp", total_biaya)