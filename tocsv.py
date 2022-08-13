import pandas as pd

###''' Aqui eu uso o Pandas para fazer a leitura do arquivo .json '''###
df = pd.read_json (r'curve.json')
###''' Aqui eu uso a função .to_csv para criar um arquivo .csv '''###
df.to_csv (r'curves.csv', index = False)
