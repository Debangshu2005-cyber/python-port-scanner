import socket

target = input("Enter target IP: ")

print("Scanning target:", target)

for port in range(1,1025):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)

    result = s.connect_ex((target, port))

    if result == 0:
        try:
            service = socket.getservbyport(port)
        except:
            service = "Unknown"

        print(f"Port {port} is open ({service})")

    s.close()
