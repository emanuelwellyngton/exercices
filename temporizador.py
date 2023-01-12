from datetime import datetime

data_time = datetime.now()

print(data_time.time)

dia = data_time.day
mes= data_time.month
hora = data_time.hour

alarme_total_horas = int(input("Digite a quantidade de horas para o temporizador:"))
alarme_dias = alarme_total_horas // 24
alarme_horas = alarme_total_horas % 24

dia = (dia + alarme_dias) % 30
hora = (hora + alarme_horas) % 24

print("O alarme tocará ás",hora, ":00", "do dia", dia, "de Janeiro")