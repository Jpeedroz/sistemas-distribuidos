import datetime
import time

horario_servidor = datetime.datetime.now()
hora1 = horario_servidor.timestamp()
hora2 = horario_servidor.timestamp()

rtt = hora2 + hora1 / 2

horario_ajustado = horario_servidor + datetime.timedelta(seconds=rtt)
print("-----"*10)
print(f"Horário do servidor: {horario_servidor.strftime('%H:%M:%S.%f')}")
print(f"Tempo de ida e volta: {rtt:.2f} segundos")
print(f"Horário ajustado: {horario_ajustado.strftime('%H:%M:%S.%f')}")
