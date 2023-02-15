#INPUT NOMOR HP
phone_number = str(input("Masukkan Nomor Telepon : "))

#POTONG NOMOR HP
angka_akhiran = int(phone_number[-1:])
genap = angka_akhiran % 2
if phone_number[:4] == "0816":
    print("\nAnda menggunakan operator Indosat")
elif phone_number[:4] == "0814":
    print("\nAnda menggunakan operator Telkomsel")

if genap == 0:
    print("Nomor anda berkahiran genap")
else :
    print("Nomor anda berakhiran ganjil")