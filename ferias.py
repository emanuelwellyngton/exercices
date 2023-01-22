print("Vamos descobrir quando você voltará das férias!")

dia_semana = int(input("Qual o dia da semana em que você vai sair de férias? Digite o número correspodente ao dia: 1 segunda; 2 terça; 3 quarta; 4 quinta; 5 sexta; 6 sábado; 7 domingo"))
total_dias = int(input("Por quantos dias você ficará de férias?"))

semanas = total_dias // 7
resto_dias = total_dias % 7

dia_volta = (dia_semana + resto_dias) % 7

print("Usando o índice dos dias da semana usado acima, você voltará das férias em:", dia_volta)