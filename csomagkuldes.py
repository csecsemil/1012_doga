print("Csomagküldési költség kalkulátor")
print("--------------------------------")
csomagtomege = 0

while csomagtomege <= 0:
    try:
        csomagtomege = float(input('Adja meg a csomag tömegét (kg):'))
    except :
        continue

szallitastipusa = ''
while szallitastipusa.lower()!='normal' and szallitastipusa.lower()!='expressz':
    szallitastipusa = input("Kézbesítés módja (normal/expressz): ")


alapkotlseg = csomagtomege * 500

if szallitastipusa.lower() == 'expressz':
    teljeskorltseg = alapkotlseg + 1500
else:
    teljeskorltseg = alapkotlseg

print(f'A csomagküldés teljes költsége: {round(teljeskorltseg)} Ft')



    