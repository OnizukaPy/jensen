import kaggle

def search():

    scelta = input("Inserisci il criterio di ricerca: ")
    print("Hai inserito: " + scelta)
    datasets = kaggle.api.dataset_list(search=scelta)
    lista = []
    i = 0
    for d in datasets:
        print(i, " - ", str(d['ref']))
        lista.append(str(d['ref']))
        i += 1
    scelta = int(input("Scegli il dataset inserendo il numero corrispondente: "))

    return lista[scelta]


    