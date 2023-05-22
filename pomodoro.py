import time
import winsound

# Definindo as variáveis de tempo em segundos
work_time = 25 * 60
short_break_time = 5 * 60
long_break_time = 15 * 60

# Inicializando o número de pomodoros e o tempo total
pomodoro_count = 0
total_time = 0

# Loop infinito para executar o método Pomodoro
while True:
    # Contagem regressiva do tempo de trabalho
    print("Trabalhando...")
    for i in range(work_time, 0, -1):
        time.sleep(1)
    
    # Tocando som de alerta para pausa curta
    winsound.Beep(1000, 1000)

    # Contagem regressiva do tempo de pausa curta
    print("Pausa curta...")
    for i in range(short_break_time, 0, -1):
        time.sleep(1)

    # Incrementando o número de pomodoros e o tempo total
    pomodoro_count += 1
    total_time += work_time
    
    # Se já foram executados quatro pomodoros, fazer uma pausa longa
    if pomodoro_count % 4 == 0:
        # Tocando som de alerta para pausa longa
        winsound.Beep(1000, 1000)
        
        # Contagem regressiva do tempo de pausa longa
        print("Pausa longa...")
        for i in range(long_break_time, 0, -1):
            time.sleep(1)
    else:
        # Tocando som de alerta para novo pomodoro
        winsound.Beep(1000, 1000)
        
        # Mensagem informando o início de um novo pomodoro
        print("Novo pomodoro começando em 3 segundos...")
        time.sleep(3)