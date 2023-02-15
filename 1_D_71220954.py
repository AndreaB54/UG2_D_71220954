#MENU MAKAN
print("="*15, "MAKANAN", "="*15)
print("1. Telur Bakar\t\t: Rp 7.000", "\n2. Lele Terbang Mas Bhe\t: Rp 10.000", "\n3. Es Coklat Lempu\t: Rp 5.000", "\n4. Es Doger Langensari\t: Rp 13.000")

#PESANAN
print("\n", "="*20, "PESANAN", "="*20)
smoke_egg = int(input("Telur Bakar\t\t\t: "))
leterbang = int(input("Lele Terbang\t\t\t: "))
ice_choco = int(input("Es Coklat\t\t\t: "))
ice_doger = int(input("Es Doger\t\t\t: "))

#DATA HARGA
harga_egg = 7000 * smoke_egg
harga_lele = 10000 * leterbang
harga_es_lempu = 5000 * ice_choco
harga_doger = 13000 * ice_doger
total_bayar = harga_egg + harga_lele + harga_es_lempu + harga_doger

#BAYAR
print("\n", "="*20, "TOTAL", "="*20)
print("TOTAL TELUR BAKAR x", smoke_egg, "\t\t\t: Rp", harga_egg)
print("TOTAL LELE TERBANG x", leterbang, "\t\t\t: Rp", harga_lele)
print("TOTAL ES COKLAT x", ice_choco, "\t\t\t: Rp", harga_es_lempu)
print("TOTAL ES DOGER x", ice_doger, "\t\t\t: Rp", harga_doger)

#TOTAL
print("Jumlah total biaya yang harus dibayar adalah Rp", total_bayar)