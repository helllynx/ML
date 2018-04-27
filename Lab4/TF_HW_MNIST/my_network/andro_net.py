import socket
from TF_HW_MNIST.my_cnn import handwritingDetection
import time
import binascii


def hexint(b):
    return int(binascii.hexlify(b), 16)

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

    length = conn.recv(4)
    print(hexint(length))
    data = conn.recv(hexint(length))
    print(len(data))
    myfile.write(data)
    myfile.close()

    # conn.send(detector.detect('out.png'))
    conn.send(b'FUCKYOU')
    # print(detector.detect('out.png'))
    print('finished writing file')
    conn.close()
    print('client disconnected')


#
# while True:
#     conn, addr = serv.accept()
#     print('client connected ... ', addr)
#     myfile = open('out.png', 'wb')
#
#     while True:
#         data = conn.recv(BUFSIZE)
#         if not data: break
#         myfile.write(data)
#
#     myfile.close()
#     # conn.send(detector.detect('out.png'))
#     # conn.send(b'FUCKYOU')
#     print(detector.detect('out.png'))
#     print('finished writing file')
#     conn.close()
#     print('client disconnected')
#
#

