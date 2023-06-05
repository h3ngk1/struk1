# DATA
Member = (input("Masukkan Nama Member Anda : "))
Nama_Barang1 = str(input("Masukkan nama item pertama yang dibeli : "))
Qty_Barang1 = int(input("Masukkan Jumlah Pembelian : "))
Nama_Barang2 = str(input("Masukkan nama item kedua yang dibeli : "))
Qty_Barang2 = int(input("Masukkan Jumlah Pembelian : "))
Nama_Barang3 = str(input("Masukkan nama item ketiga yang dibeli : "))
Qty_Barang3 = int(input("Masukkan Jumlah Pembelian : "))

# DATA BARANG
Harga_Barang1 = 10000
Harga_Barang2 = 20000
Harga_Barang3 = 25000
Total_Harga_Barang1 = int(Qty_Barang1 * 10000)
Total_Harga_Barang2 = int(Qty_Barang2 * 20000)
Total_Harga_Barang3 = int(Qty_Barang3 * 25000)

# PROSES
Total_Harga = int(Total_Harga_Barang1 + Total_Harga_Barang2 + Total_Harga_Barang3)
Diskon = int(Total_Harga * (5/100))
# PPh = int( * (11/100))
PPh_Final = int(Total_Harga * (11/100))
Grand_Total = int(Total_Harga - Diskon + PPh_Final)

# OUTPUT
print(' ')
print('--------------------------------------------------')
print('------------------Fashion_Week--------------------')
print("Jl. KS Tubun No. 1, Slipi, Palmerah, Jakarta Barat\n            Nomor NPWP : 21.367.668.5841            ")
print(' ')
print("Nama Member : ", Member)
import datetime
Sekarang = datetime.datetime.now()
print(Sekarang.strftime("%A, %d-%m-%Y %H:%M"))
print('--------------------------------------------------')

print(Nama_Barang1) 
print(Harga_Barang1,                    'x', Qty_Barang1)
print(' = ', Total_Harga_Barang1)
print(Nama_Barang2)
print(Harga_Barang2,                    'x', Qty_Barang2)
print(' = ', Total_Harga_Barang2)
print(Nama_Barang3)
print(Harga_Barang3,                    'x', Qty_Barang3)
print(' = ', Total_Harga_Barang3)

print('------------------------------------------')
print("Total",       "      :", "Rp. ", int(Total_Harga))
print("Diskon",      "     :", "Rp. ", int(Diskon))
print( str("PPh         : 11%"))
print("Grand Total", ":", "Rp. ", int(Grand_Total))

print('==========================================')
print(' ')
print("Terima kasih telah berbelanja di Fashion_Week\nSelamat datang kembali")

print(' ')
print("Customer care : 021 1230123")
print(' ')
