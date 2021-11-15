menu_utama = ['menabung', 'transfer', 'tarik tunai']
penerima = ['derryl', 'dedi', 'sigit', ]
menu_tarik = [50000, 100000, 150000, 200000, 250000]
saldo = 0
print('======== Selamat Datang Di ATM Serba Bisa ========')
nama = input('Masukkan nama Anda :')
while True:
    for index in range(0, len(menu_utama)):
        print(f'{index +1}. {menu_utama[index]}')
    pilihan_menu = int(input('Silahkan Pilih Menu :'))
    if pilihan_menu <= 0 or pilihan_menu > len(menu_tarik):
        print('Silahkan Pilih Menu Dengan benar')
        continue
    else:
        print(f'------ {menu_utama[pilihan_menu-1]} ------')
        if pilihan_menu == 1:
            nabung = int(input('Silahkan Masukkan Jumlah Money :'))
            saldo += nabung
            print(f'Nama  : {nama}')
            print(f'Saldo : {saldo}')
        elif pilihan_menu == 2:
            for index_penerima in range(0, len(penerima)):
                print(f'{index_penerima+1}. {penerima[index_penerima]}')
            nerima = int(input('Pilih Penerima :'))
            if nerima < 0 or nerima > len(penerima):
                print('Silahkan Pilih Menu Dengan benar')
            else:
                transfer = int(input('Mau Transfer Berapa nich :'))
                if saldo < transfer:
                    print('Maaf Saldo Anda Kurang Memadai')
                else:
                    saldo -= transfer
                    print(
                        f'Saldo sebesar {transfer} Telah Dikirim ke {penerima[nerima]}')
                    print(f'Nama  : {nama}')
                    print(f'Saldo : {saldo}')
        elif pilihan_menu == 3:
            for index_tarik in range(0, len(menu_tarik)):
                print(f'{index_tarik+1}. {menu_tarik[index_tarik]}')
            nominal = int(input('Silahkan Masukkan Jumlah Penarikan :'))
            if saldo < menu_tarik[nominal]:
                print('Maaf Saldo Anda Kurang Memadai ya beb')
            else:
                print('Penarikan Sedang Di proses keep smile')

    transaksi_lain = input('Apakah Mau Transaksi Lainya :')
    if transaksi_lain == 'y' or transaksi_lain == 'Y':
        continue
    else:
        print('======== Terimakasih Telah Menggunakan ATM ========')
        break
