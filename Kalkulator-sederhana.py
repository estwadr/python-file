print("\n"+5*"="+"KALKULATOR SEDERHANA"+5*"=")
print('KONSEP --> angka 1, operasi(+,-,x,/), angka 2')
angka_pertama = float(input(f"Angka pertama = "))
operasi = input(f"Operasi(+,-,x,/) = ")
angka_kedua = float(input(f"Angka kedua = "))
if operasi == '+':
    hasil_jumlah = angka_pertama + angka_kedua
    print(f"Hasil penjumlahan dari {angka_pertama} + {angka_kedua} = {hasil_jumlah}")
elif operasi == '-':
    hasil_kurang = angka_pertama - angka_kedua
    print(f"Hasil pengurangan dari {angka_pertama} - {angka_kedua} = {hasil_kurang}")
elif operasi == 'x' or operasi == '*':
    hasil_kali = angka_pertama * angka_kedua
    print(f"Hasil perkalian dari {angka_pertama} x {angka_kedua} = {hasil_kali}")
elif operasi == '/':
    hasil_bagi = angka_pertama / angka_kedua
    print(f"Hasil pembagian dari {angka_pertama} / {angka_kedua} = {hasil_bagi}")
else:
    print(f"Input yang anda masukkan salah!!!")
