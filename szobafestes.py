print('Szobafestes kalkulator')
print('----------------------')

hossz = float(input("Adja meg a szoba hosszát (m): "))
szelesseg = float(input("Adja meg a szoba szélességét (m): "))
magassag = float(input("Adja meg a szoba magasságát (m): "))

falfelulet = 2 * hossz * magassag + 2 * szelesseg * magassag
mennyezet = hossz * szelesseg
teljesfelulet = falfelulet + mennyezet

festekfelulet = teljesfelulet / 8

print(f"A teljes festendő felület: {teljesfelulet:.2f} m^2" )
print(f"A szükséges festék mennyisége: {festekfelulet:.2f} m^2" )

print('Viszlát!')