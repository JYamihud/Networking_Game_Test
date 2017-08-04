import socket
import time

cs = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
cs.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
cs.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

mes = 0

while True:
    
    mes = mes + 1
    
    cs.sendto("This is the test message ", ('255.255.255.255', 54545))
    time.sleep(1)
