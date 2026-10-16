
from datetime import datetime, timedelta

horario_servidor = datetime.now()
inicio = horario_servidor.timestamp()
fim = inicio + 2 
rtt = fim - inicio
atraso = rtt / 2
horario_ajustado = horario_servidor + timedelta(seconds=atraso)

print("-----"*10)  
print(f"Horário do servidor: {horario_servidor.strftime('%H:%M:%S.%f')}")
print(f"Tempo de ida e volta: {rtt:.2f} segundos")
print(f"Atraso estimado: {atraso:.2f} segundos")
print(f"Horário ajustado: {horario_ajustado.strftime('%H:%M:%S.%f')}")
print("-----"*10)  

