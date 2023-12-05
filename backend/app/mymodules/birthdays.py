import csv

def leggi_csv():
    with open('filedati.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)  # Salta la riga dell'intestazione
        dati = [row for row in reader]
    return header, dati

def cerca_dato(comune, anno, dati):
    for riga in dati:
        if riga[2] == comune and riga[8] == anno:
            return riga[1]  # Restituisci il valore di 'Rifiuto residuo (in Kg)'
    return None  # Se non trova corrispondenze