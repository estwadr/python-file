print("\n"+5*"="+"PENILAIAN MAHASISWA"+5*"=")
nama = str(input(f"Masukkan nama mahasiswa = "))
matkul1 = float(input(f"Nilai matkul 1 = "))
matkul2 = float(input(f"Nilai matkul 2 = "))
matkul3 = float(input(f"Nilai matkul 3 = "))
matkul4 = float(input(f"Nilai matkul 4 = "))

rata_rata = (matkul1 + matkul2 + matkul3 + matkul4) / 4

print(f"Mahasiswa dengan nama {nama}")
print(f"punya rata-rata nilai yaitu {rata_rata}")
if rata_rata >= 90:
    print(f"dan punya kategori prestasi 'Sangat Baik'")
elif 70 <= rata_rata < 90:
    print(f"dan punya kategori prestasi 'Baik'")
elif 50 <= rata_rata < 70:
    print(f"dan punya kategori prestasi 'Cukup'")
else:
    print(f'Kategori prestasi dibawah manusia normal')
