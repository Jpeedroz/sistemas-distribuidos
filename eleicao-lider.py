import time
import random
processos = random.sample(range(1, 100), 6)  
print("Iniciando eleição de líder...")
time.sleep(2)

for processo in processos:
    print(f"Processo {processo} está participando da eleição.")
    time.sleep(1.2)
lider = max(processos)

print('----'*10)
print(f"O processo {lider} foi eleito como líder.")
print('----'*10)

for processo in processos:
    if processo != lider:
        print(f"Processo {processo} reconhece o processo {lider} como líder.")
        time.sleep(1.2)