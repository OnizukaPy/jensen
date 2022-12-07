# Deklarera en klass Datum. Klassen ska innehålla de tre instansvariablerna år, 
# mån och dag. Låt klassen innehålla en instansmetod __str__ som returnerae ett datum som en text. 
# Använd standardformet åååå-mm-dd

class Datum:
    def __init__(self, år, mån, dag):
        self.år = år
        self.mån = mån
        self.dag = dag

    # om aman använder __str__ som metod i classen kan man definera ett sätt att printa ut 
    # en sträng när vi printer objekten eller utbyter den som en sträng str()
    def __str__(self):
        return f"{self.år:04}-{self.mån:02}-{self.dag:02}"

d = Datum(2022, 12, 7)
print(d)