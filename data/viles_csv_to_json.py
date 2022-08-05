import csv, os, json

if __name__ == '__main__':
  this_folder = os.path.dirname(__file__)
  input_file_name = 'villes_france_insee.csv';
  with open(f'{this_folder}/{input_file_name}', 'r') as csv_file:
    reader = csv.reader(csv_file, delimiter=';')
    line0 = True
    communes = []
    for row in reader:
      if line0:
        print(row)
        line0 = False
        continue
      commune = {'code_insee': row[3] , 'nom': row[0] , 'code_postal': row[1] , 'departement': row[2] }
      communes.append(commune)

    input_file_name = f'{os.path.splitext(input_file_name)[0]}.json'
    with open(f'{this_folder}/{input_file_name}', 'w') as json_file :
      json_file.write(json.dumps(communes))