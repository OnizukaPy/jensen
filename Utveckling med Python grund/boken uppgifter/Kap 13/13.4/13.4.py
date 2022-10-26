import Bil

bil1 = Bil.Bil()
bil2 = Bil.Bil()

äg1 = Bil.Ägare("Markus")
äg2 = Bil.Ägare("Ulle")


    
b1 = ["DRT987", "volvo", 2018, 230, 65, äg1]
b2 = ["ABC123", "fiat", 2020, 220, 45, äg2]

list = [b1, b2]
bilar = [bil1, bil2]

for i in range(len(list)):
    bilar[i].regnr = list[i][0]
    bilar[i].fabrik = list[i][1]
    bilar[i].årsmodel = list[i][2]
    bilar[i].tjästevikt = list[i][3]
    bilar[i].motoreffekt = list[i][4]
    bilar[i].ägare = list[i][5].namn

for i in range(len(list)):
    print(f"Bil{i+1}, {bilar[i].regnr}, {bilar[i].fabrik},{bilar[i].årsmodel},{bilar[i].tjästevikt},{bilar[i].motoreffekt}, {bilar[i].ägare}")



