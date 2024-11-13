# Matriz 
horas_sono = [
    [8, 6, 7, 8, 6],  
    [5, 5, 6, 7, 8],  
    [6, 7, 8, 6, 5],  
    [7, 5, 9, 7, 4]   
]
#  armazenar o maior tempo de descanso
maior_tempo = float('-inf')  

#  encontrar o maior tempo de descanso
for semana in horas_sono:
    for horas in semana:
        if horas > maior_tempo:
            maior_tempo = horas

#  dias q tiveram o maior tempo de descanso
contagem_maior_tempo = 0
for semana in horas_sono:
    for horas in semana:
        if horas == maior_tempo:
            contagem_maior_tempo += 1

# result
print(f"O maior tempo de descanso foi de {maior_tempo} horas, e isso ocorreu em {contagem_maior_tempo} dias.")