import zmq, os, json

if __name__ == '__main__':
  # load communes
  communes = []
  data_folder = os.path.abspath(f'{os.path.dirname(__file__)}/../data')
  with open(f'{data_folder}/villes_france_insee.json', 'r') as json_file:
    communes = json.loads(json_file.read())