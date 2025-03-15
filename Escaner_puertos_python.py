import socket
import concurrent.futures

#Funcion escanear un puerto
def escanear_puerto(ip, puerto):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(0.5)
        if sock.connect_ex((ip, puerto)) == 0:
            print(f"Puerto abierto: {puerto}")

#Funcion main
def escaner_puertos(ip):
    print(f"Escaneando {ip}....\n")
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor: #Utilizamos threads para optimizar la busqueda en tiempo
        executor.map(lambda p: escanear_puerto(ip,p), range(1, 65535))

#Solicita IP al user
if __name__ == "__main__":
    ip = input("Ingrese la dirección IP a escanear: ")
    escaner_puertos(ip)


