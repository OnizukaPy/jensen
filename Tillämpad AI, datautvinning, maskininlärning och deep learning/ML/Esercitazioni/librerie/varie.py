import csv

# Creiamo una funzione per convertire i file txt in csv andando a prendere i dati a partire dalla riga dove 
# cominciano i dati veri e propri
def convert_txt_to_csv(work_dir, dir_in, dir_out, file_name):
    # leggiamo il file txt
    with open(work_dir + dir_in + '/' + file_name, 'r') as in_file:
        stripped = (line.strip() for line in in_file)
        lines = (line.split(",") for line in stripped if line)

        # creiamo una lista delle righe
        file = []
        for line in lines:
            file.append(line)
        
        # nella prima riga di ogni file txt è presente il numero della righe di heater
        header = int(file[0][0].split()[-1])

        # creiamo il file csv a partire dalla riga header -1 perchè la numerazione delle righe parte da 0
        with open(work_dir + dir_out + '/' + file_name.replace('.txt', '.csv'), 'w') as out_file:
            writer = csv.writer(out_file)
            writer.writerows(file[header-1:])