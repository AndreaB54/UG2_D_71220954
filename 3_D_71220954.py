#LIST BARANG YANG MAU DIBELI
beli_barang = str(input("Masukkan brand apa saja yang hendak dibeli (pisahkan dengan koma): "))
bagi_barang = beli_barang.split(',')

#TANYA HARGA BARANG SATU PER SATU
# for barang in bagi_barang:
#     barang 
#     for tanya in barang :
#         harga = int(input(f"Berapa harga barang {barang} ?: "))
#         print(f"Harga {barang}\t\tRp. {harga}\tDiskon Rp. ")

#RUMUS BARU
barang = 0
while barang < len(bagi_barang):
    harga = int(input(f"Berapa harga barang {bagi_barang[barang]} ?: "))
    if harga >= 10000000 and harga < 25000000:
        diskon_10 = (harga*0.1)
        print(f"Harga {bagi_barang[barang]}\t\tRp. {harga}\tDiskon Rp. {diskon_10}")
    elif harga >= 25000000:
        diskon_25 = (harga*0.25)
        print(f"Harga {bagi_barang[barang]}\t\tRp. {harga}\tDiskon Rp. {diskon_25}")
    else:
        print(f"Harga {bagi_barang[barang]}\t\tRp. {harga}\tDiskon Rp. 0")
    barang += 1

print("Total uang yang harus anda bayarkan adalah Rp. ", barang)