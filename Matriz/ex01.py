# Matriz 
horas_sono = [
    [8, 6, 7, 8, 6],  
    [5, 5, 6, 7, 8],  
    [6, 7, 8, 6, 5],  
    [7, 5, 9, 7, 4]   
]
#  armazenar a soma das horas por dia
soma_horas_por_dia = [0] * 5  

# soma as horas de sono para cada dia da semana
for semana in horas_sono:
    for dia in range(5):  # 0 a 4 correspondendo aos dias da semana
        soma_horas_por_dia[dia] += semana[dia]

#  dias da semana
dias_da_semana = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta']

#  maior total de horas de sono
maior_hora = max(soma_horas_por_dia)
dia_com_maior_hora = dias_da_semana[soma_horas_por_dia.index(maior_hora)]

# result
print(f"O dia da semana com o maior horário de descanso foi {dia_com_maior_hora}, com um total de {maior_hora} horas de sono.")