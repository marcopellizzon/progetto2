"""
Backend module for the FastAPI application.

This module defines a FastAPI application that serves
as the backend for the project.
"""
import csv
from fastapi import FastAPI
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from datetime import datetime
import pandas as pd



app = FastAPI()



df = pd.read_csv('/app/app/filedati.csv')



@app.get('/')
def read_root():
    """
    Root endpoint for the backend.

    Returns:
        dict: A simple greeting.
    """
    return {"Hello": "World"}
    return leggi_csv

def delete_row(file_path, row_index):
    # Read the CSV file
    with open(file_path, 'r', encoding='utf-8') as file:
        data = list(csv.reader(file))

    # Check if the row index is valid
    if 0 < row_index <= len(data):
        # Remove the specified row
        del data[row_index - 1]

        # Write the updated data back to the CSV file
        with open(file_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(data)

        print(f'Row {row_index} deleted successfully.')
    else:
        print(f'Invalid row index: {row_index}.')

# Example of usage to delete row 3
delete_row('filedati.csv', 3416)

def leggi_csv():
    dati_completi = []
    try:
        with open('filedati.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                comune = row.get('Comune', '').strip()
                anno = row.get('Anno', '').strip()
                if comune and anno:
                    dati_completi.append({
                        'Comune': comune,
                        'Anno': anno,
                        'Rifiuto_residuo': row.get('Rifiuto residuo (in Kg)', '').strip()
                    })
    except UnicodeDecodeError as e:
        print(f"Errore nella decodifica Unicode: {e}")
        # Puoi gestire l'errore in modo appropriato, ad esempio, uscire dal programma o fornire un messaggio all'utente.
    return dati_completi

def cerca_dato(comune_utente, anno_utente, dati):
    for riga in dati:
        comune_csv = riga['Comune']
        anno_csv = riga['Anno']
        if comune_csv.strip() == comune_utente.strip() and anno_csv.strip() == anno_utente.strip():
            return riga['Rifiuto_residuo']
    return None