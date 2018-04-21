import socket
from Lab4.TF_HW_MNIST.my_cnn import handwritingDetection

HOST = '0.0.0.0'
PORT = 9090
ADDR = (HOST, PORT)
BUFSIZE = 4096

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serv.bind(ADDR)
serv.listen(5)

detector = handwritingDetection("../model/model.ckpt")

print('listening ...')

while True:
    conn, addr = serv.accept()
    print('client connected ... ', addr)
    myfile = open('out.png', 'wb')

    while True:
        data = conn.recv(BUFSIZE)
        if not data: break
        myfile.write(data)
        # print('writing file ....')

    myfile.close()
    # conn.send(detector.detect('out.png'))
    print(detector.detect('out.png'))
    print('finished writing file')
    conn.close()
    print('client disconnected')



