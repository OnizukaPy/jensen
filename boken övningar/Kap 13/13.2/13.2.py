
class Coord:

    def __init__(self, grader, minuter, sekunder, lat_long):
        self.grader = int(grader)
        self.minuter = int(minuter)
        self.sekunder = int(sekunder)
        self.lat_long = lat_long

    def get_coord(self):
        return f"{self.grader}\u00B0{self.minuter}\u0027{self.sekunder}\u0022 {self.lat_long}"

class GPS:
    
    def __init__(self, plats, latitude, longitude):
        self.plats = plats
        self.latitude = latitude
        self.longitude = longitude

    def get_info(self):
        return f"Plats: {self.plats}, Lat: {self.latitude.get_coord()} Long: {self.longitude.get_coord()}"


plats_list = []
while True:
    land = input("\nSkriv plats namn: ")
    print(f"\nSkriv coordinaterna av: {land}\n")
    while True:
        coord = input("Skriv latituden som: grader, minuter, sekunder, LAT: ").upper().split()
        if coord[3] == "N" or coord[3] == "S":
            latituden = Coord(coord[0], coord[1], coord[2], coord[3])
            break
        else:
            print(f"\nDu har skrivit fel, latituden måste vara N eller S")

    while True:
        coord = input("Skriv longituden som: grader, minuter, sekunder, LONG: ").upper().split()
        if coord[3] == "Ö" or coord[3] == "V":
            longituden = Coord(coord[0], coord[1], coord[2], coord[3])
            break
        else:
            print(f"\nDu har skrivit fel, longituden måste vara Ö eller V")
    
    plats_list.append(GPS(land, latituden, longituden))
    val = input("Vill du forsätta? S/N: ").upper()
    if val != "S":
        break

for i in plats_list:
    print(i.get_info())




