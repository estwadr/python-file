print("\nPROGRAM KONVERENSI SUHU\n")

print("====CELCIUS====")
#konferensi celcius ke satuan lain
celcius = float(input("Masukkan suhu = "))
print("Suhu yang dimasukkan adalah", celcius, "Celcius")
#celcius ke reamur
reamur = (4/5) * celcius
print("Suhu dalam reamur adalah ", reamur, "Reamur")
#celcius ke fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("Suhu dalam fehrenheit adalah ", fahrenheit, "Fahrenheit")
#celcius ke kelvin
kelvin = celcius + 273
print("Suhu dalam kelvin adalah ", kelvin, "Kelvin")

print("====REAMUR====")
#konferensi reamur ke satuan lain
reamur = float(input("Masukkan suhu = "))
print("Suhu yang dimasukkan adalah ", reamur, "Reamur")
#reamur ke celcius
celcius = (5/4) * reamur
print("Suhu dalam celcius adalah ", celcius, "Celcius")
#reamur ke fahrenheit
fahrenheit = ((9/4) * reamur) + 32
print("Suhu dalam fahrenheit adalah ", fahrenheit, "Fahrenheit")
#reamur ke kelvin
kelvin = ((5/4) * reamur) + 273
print("Suhu dalam kelvin adalah ", kelvin, "Kelvin")

print("====FAHRENHEIT====")
#konferensi fahrenheit ke satuan lain
fahrenheit = float(input("Masukkan suhu = "))
print("Suhu yang dimasukkan", fahrenheit, "Fahrenheit")
#fahrenheit ke celcius
celcius = (5/9) * (fahrenheit - 32)
print("Suhu dalam celcius adalah ", celcius, "Celcius")
#fahrenheit ke reamur
reamur = (4/9) * (fahrenheit - 32)
print("Suhu dalam reamur adalah ", reamur, "Reamur")
#fahrenheit ke kelvin
kelvin = (5/9) * (fahrenheit + 460)
print("Suhu dalam kelvin adalah ", kelvin, "Kelvin")

print("====KELVIN====")
#konferensi kelvin ke satuan lain
kelvin = float(input("Masukkan suhu = "))
print("Suhu yang dimasukkan adalah ", kelvin, "Kelvin")
#kelvin ke celcius
celcius = kelvin - 273
print("Suhu dalam celcius adalah ", celcius, "Celcius")
#kelvin ke reamur
reamur = (4/5) * (kelvin - 273)
print("Suhu dama reamur adalah ", reamur, "Reamur")
#kelvin ke fahrenheit
fahrenheit = (1.8 * (kelvin - 273)) + 32
print("Suhu dalam fahrenheit adalah ", fahrenheit, "Fahrenheit")
