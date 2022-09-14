datum = input("Skriv datum på svenska åååå-mm-dd: \n> ")

år = datum[0:4]
månad = datum[5:7]
dag = datum[8:len(datum)]

print(f"Datum på amerikansk är: {dag}/{månad}/{år}")
