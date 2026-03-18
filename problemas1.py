# Este programa irá calcular a distância entre 2 pontos na superfície da Terra

# Exemplo de coordenadas para escrever:
# 23° 32' 51 s 46° 38' 10 w 22° 54' 00 s 43° 10' 00 w (no formato DMS)
# ou
# -23.5475 -46.6361 -22.9000 -43.1667 (no formato decimal)

# ATENÇÃO: Tente escrever sem pontuação desnecessária e na ordem: latitude e 
# longitude do primeiro ponto e latitude e longitude do segundo ponto, assim como
# no exemplo

import numpy as np


# Passo 1: definir a formula e as variaveis

coordenadas = input("Digite as coordenadas:") # recebe o input

##### Conversão de coordenadas DMS para decimais: 

# faz a limpeza e transforma em lista:
coordenadas = coordenadas.replace("°"," ").replace("'", " ").replace('"', ' ').replace(",", " ")
coordenadas = coordenadas.replace("′", " ").replace("″", " ").strip(" ")
coordenadas = " ".join(coordenadas.split())
num_coordenadas = coordenadas.split(" ")


# define a função:

def dms_para_decimal(graus, minutos, segundos, direcao):
    # Converte coordenadas DMS para Decimal.
    decimal = float(graus) + float(minutos)/60 + float(segundos)/3600
    
    # Inverte o sinal para Sul ou Oeste
    if direcao.upper() in ['S', 'W', 'O']:
        decimal *= -1
    return decimal

if len(num_coordenadas) > 4:
    latitude1 = dms_para_decimal(num_coordenadas[0],num_coordenadas[1],num_coordenadas[2],num_coordenadas[3])
    longitude1 = dms_para_decimal(num_coordenadas[4],num_coordenadas[5],num_coordenadas[6],num_coordenadas[7])
    latitude2 = dms_para_decimal(num_coordenadas[8],num_coordenadas[9],num_coordenadas[10],num_coordenadas[11])
    longitude2 = dms_para_decimal(num_coordenadas[12],num_coordenadas[13],num_coordenadas[14],num_coordenadas[15])

    x1_graus = latitude1
    y1_graus = longitude1
    x2_graus = latitude2
    y2_graus = longitude2
    # passando para radianos:
    x1 = np.radians(x1_graus)
    y1 = np.radians(y1_graus)
    x2 = np.radians(x2_graus)
    y2 = np.radians(y2_graus)

    resultado = 2 * np.arcsin(np.sqrt(
        (np.sin((x2 - x1)/2)**2) + np.cos(x1) * np.cos(x2) * (np.sin((y2 - y1)/2)**2)
        ))
    raio = 6378 # valor do raio da Terra em Km (no equador)

    distancia = resultado * raio

    print(f"{distancia:.1f} Km")
    exit()



# pega o elemento certo da lista:
x1_graus = float(num_coordenadas[0]) # transformando em float
y1_graus = float(num_coordenadas[1])
x2_graus = float(num_coordenadas[2])
y2_graus = float(num_coordenadas[3])

# passando para radianos:
x1 = np.radians(x1_graus)
y1 = np.radians(y1_graus)
x2 = np.radians(x2_graus)
y2 = np.radians(y2_graus)

resultado = 2 * np.arcsin(np.sqrt(
    (np.sin((x2 - x1)/2)**2) + np.cos(x1) * np.cos(x2) * (np.sin((y2 - y1)/2)**2)
    ))

raio = 6378 # valor do raio da Terra em Km (no equador)

distancia = resultado * raio

print(f"{distancia:.1f} Km")