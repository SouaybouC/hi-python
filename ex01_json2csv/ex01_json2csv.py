import json
import csv

with open('Json.json') as fichier_json:
    data = json.load(fichier_json)
 
partenaires = data['partenaire']
toCsv = open('json_to_csv.csv', 'w')
csv_writer = csv.writer(toCsv)
count = 0

for partenaire in partenaires:
    if count == 0:
        header = partenaire.keys()
        csv_writer.writerow(header)
        count += 1        
    csv_writer.writerow(partenaire.values())
    
toCsv.close()