#PROJECT PERTAMA

print('\n'+5*'='+'PROJECT 1'+5*'=')
nama_random = str(input('masukkan nama random = '))
print(f'\nHallo, salam kenal {nama_random}')

import random
password = random.choice(range(1000,9999))
print('pass anda adalah ', password, ', ingat-ingat!!')

print('\nMasukkan password anda')
password_masuk = int(input('= '))
if password_masuk == password:
    print('Yeeyy!! password yang anda masukkan benar')
    lanjut = str(input("ketik 'lanjut' untuk melanjutkan = "))

while password != password_masuk:
    print('Yahh... Gimana si kok salah. Coba lagi yaa')
    print('\nMasukkan password anda')
    password_masuk = int(input('= '))
    if password == password_masuk:
        print('Yeeyy!! password yang anda masukkan benar')
        lanjut = str(input("ketik 'lanjut' untuk melanjutkan = "))

if lanjut == 'lanjut':
    print('\nMemprediksi Hari dan Umur anda')
else:
    print('Yahh.. gimana sih kok salah\n')

print(5*'='+'PROSES PEMASUKKAN DATA'+5*'=')
import datetime as dt
nama = str(input("nama \t\t= "))
tanggal = int(input('tanggal lahir \t= '))
bulan = int(input('bulan lahir \t= '))
tahun = int(input('tahun lahir \t= '))

print(f'nama anda adalah {nama}')

biodata = dt.date(tahun,bulan,tanggal)
print(f'anda lahir pada {biodata}')

hari_lahir = f'anda lahir pada hari {biodata:%A}'
lower_hari_lahir = hari_lahir.lower()
print(lower_hari_lahir)

hari_ini = dt.date.today()
umur_hari = hari_ini - biodata
print(f'anda hidup sudah {umur_hari.days} hari, atau')
umur_tahun = umur_hari / 365
umur_bulan_sisa = (umur_hari.days % 365) // 30
print(f'umur anda adalah {umur_tahun.days} tahun {umur_bulan_sisa} bulan')

print('Apakah benar? (ya/tidak)')
nilai_prediksi = input('= ')
if nilai_prediksi == 'ya':
    print('Bener dong gueh gitcu lochh..')
else:
    print('Ahh.. masa sih salah, kamu bohong yaa..')


print('\n'+5*'='+'KUIS'+5*'=')
print('Mau bermain kuis? (ya/tidak)')
nilai_kuis = input('= ')

if nilai_kuis == 'ya':
    print('Mari kita mulai...')
    print(input('(enter)'))
else:
    print('Oopss!! Harus mau dong biar pinter...')
    print(input('(enter)'))

inputKuis = float(input('masukkan angka pada interval 0<x<5 atau 10<x<15\n= '))
isAntara1 = (0 < inputKuis < 5)
isAntara2 = (10 < inputKuis < 15)
isIrisan1dan2 = isAntara1 or isAntara2
print(f'Nilai / angka yang anda masukkan bernilai -> {isIrisan1dan2}')

if isIrisan1dan2 == True:
    print('Kamu sangat pintar yaa... nggak nyangka')
else:
    print('Kayaknya kamu ngga lulus sekolah dech...')

print(input('(enter)'))

print('\nMain hitungan lagi yukk')
print(5*'='+'KALKULATOR SEDERHANA'+5*'=')
print('KONSEP --> angka 1 (+,-,x,/) angka 2')
angka_pertama = float(input('masukkan angka pertama = '))
operator = input('masukkan operator (+,-,x,/) --> ')
angka_kedua = float(input('masukkan angka kedua = '))

if operator == '+':
    hasil_jumlah = angka_pertama + angka_kedua
    print(f'Hasil jumlah dari {angka_pertama} {operator} {angka_kedua} adalah {hasil_jumlah}')
elif operator == '-':
    hasil_kurang = angka_pertama - angka_kedua
    print(f'Hasil kurang dari {angka_pertama} {operator} {angka_kedua} adalah {hasil_kurang}')
elif operator == 'x':
    hasil_kali = angka_pertama * angka_kedua
    print(f'Hasil kali dari {angka_pertama} {operator} {angka_kedua} adalah {hasil_kali}')
elif operator == '/':
    hasil_bagi = angka_pertama / angka_kedua
    print(f'Hasil bagi dari {angka_pertama} {operator} {angka_kedua} adalah {hasil_bagi}')
else:
    print('Gimana sih baca yang bener donggs...')

print(input('(enter)'))

print('\n'+5*'='+'AKHIR'+5*'=')
print(f"""
Terimakasih '{nama_random}' alias {nama} sudah berpartisipasi dalam PROJECT 1 ini,
umurmu {umur_tahun.days}, semangat kembangkan dirimu.
Oh ya, masih ingat ngga password kamu tadi berapa?
""")
password_akhir = int(input('= '))

if password_akhir == password:
    print('Woww!! ingatamu boleh juga')
else:
    print('Yahh... ingatamu kureng')

print('\n'+5*'-'+'Sampai Jumpa'+5*'-'+'\n')
