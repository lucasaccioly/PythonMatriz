# Matriz 
horas_sono = [
    [8, 6, 7, 8, 6],  
    [5, 5, 6, 7, 8],  
    [6, 7, 8, 6, 5],  
    [7, 5, 9, 7, 4]   
]
#  variável para armazenar o menor tempo de descanso
menor_tempo = float('inf') 

#  encontrar o menor tempo de descanso
for semana in horas_sono:
    for horas in semana:
        if horas < menor_tempo:
            menor_tempo = horas

# result
print(f"O menor tempo de descanso foi de {menor_tempo} horas.")