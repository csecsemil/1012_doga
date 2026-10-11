jegyek_szama = int(input("Add meg a vásárolni kívánt jegyek számát: "))

jegy_tipusa = ""
while jegy_tipusa.lower()!='normál' and jegy_tipusa.lower()!='diák':
    jegy_tipusa = input("Add meg a jegy típusát (normál vagy diák): ")


if jegy_tipusa == "normál":
    egy_ar = 3200
elif jegy_tipusa == "diák":
    egy_ar = 2400

if egy_ar > 0:
    teljes_ar = jegyek_szama * egy_ar
    
    if teljes_ar >= 10000:
        kedvezmeny = teljes_ar * 0.1
        fizetendo = round(teljes_ar - kedvezmeny)
        print(f"Eredeti ár: {teljes_ar} Ft")
        print("10% kedvezmény")
    else:
        fizetendo = round(teljes_ar)
        
    print(f"A fizetendő végösszeg: {fizetendo} Ft")