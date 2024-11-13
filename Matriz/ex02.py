# Matriz 
horas_sono = [
    [8, 6, 7, 8, 6],  
    [5, 5, 6, 7, 8],  
    [6, 7, 8, 6, 5],  
    [7, 5, 9, 7, 4]   
]
#  armazenar a soma das horas por dia
soma_horas_por_dia = [0] * 5  

#  horas de sono para cada dia da semana
for semana in horas_sono:
    for dia in range(5):  
        soma_horas_por_dia[dia] += semana[dia]

#  dias da semana
dias_da_semana = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta']

#  dia com menor total de horas de sono
menor_hora = min(soma_horas_por_dia)
dia_com_menor_hora = dias_da_semana[soma_horas_por_dia.index(menor_hora)]

# result
print(f"O dia da semana com o menor horário de descanso foi {dia_com_menor_hora}, com um total de {menor_hora} horas de sono.")