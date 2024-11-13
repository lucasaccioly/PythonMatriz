# Matriz 
horas_sono = [
    [8, 6, 7, 8, 6],  
    [5, 5, 6, 7, 8],  
    [6, 7, 8, 6, 5],  
    [7, 5, 9, 7, 4]   
]
# lista para armazenar a soma das horas por semana
soma_horas_por_semana = []

# soma as horas de sono para cada semana
for semana in horas_sono:
    soma_horas_por_semana.append(sum(semana))

#  semana com maior total de horas de sono
maior_hora = max(soma_horas_por_semana)
semana_com_maior_hora = soma_horas_por_semana.index(maior_hora) + 1  

# result
print(f"A semana com o maior horário de descanso foi a Semana {semana_com_maior_hora}, com um total de {maior_hora} horas de sono.")