import socket, cv2, pickle, struct

port = 9999
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
socket_address = (host_ip, port) # A tuple


host = {"HOST NAME": host_name, "HOST IP": host_ip, "PORT":port}
print("LISTENING AT: \n")
for k,v in host.items():
    print(k + " : " + str(v))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(socket_address)

data = b""
payload_size = struct.calcsize("Q")

while True:
    while len(data) < payload_size:
        packet = client.recv(4*1024) # 4Kb
        if not packet : break
        data += packet
    packeted_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack("Q", packeted_msg_size)[0]

    while len(data) < msg_size:
        data += client.recv(4*1024)
    frame_data = data[:msg_size]
    data = data[msg_size:]
    frame = pickle.loads(frame_data)
    print(frame)
    cv2.imshow("Received", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
client.close()
        