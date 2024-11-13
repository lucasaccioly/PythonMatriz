# Matriz 
horas_sono = [
    [8, 6, 7, 8, 6],  
    [5, 5, 6, 7, 8],  
    [6, 7, 8, 6, 5],  
    [7, 5, 9, 7, 4]   
]
#  variável para armazenar o maior tempo de descanso
maior_tempo = float('-inf')  

#  encontrar o maior tempo de descanso
for semana in horas_sono:
    for horas in semana:
        if horas > maior_tempo:
            maior_tempo = horas

# result
print(f"O maior tempo de descanso foi de {maior_tempo} horas.")