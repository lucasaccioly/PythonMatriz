# Matriz 
horas_sono = [
    [8, 6, 7, 8, 6],  
    [5, 5, 6, 7, 8],  
    [6, 7, 8, 6, 5],  
    [7, 5, 9, 7, 4]   
]
# variáveis para armazenar o total por semana e o total do mês
total_por_semana = []
total_do_mes = 0

#  total de horas de sono por semana e o total do mês
for semana in horas_sono:
    total_semana = sum(semana)  
    total_por_semana.append(total_semana)  
    total_do_mes += total_semana  

# porcentagem por semana em relação ao total do mês
percentuais_por_semana = [(total / total_do_mes) * 100 for total in total_por_semana]

# result
for i, percentual in enumerate(percentuais_por_semana, start=1):
    print(f"Semana {i}: {percentual:.2f}% do total do mês.")