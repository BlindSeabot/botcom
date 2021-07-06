import socket

# create a TCP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# TODO: connect to the target server

# TODO: prepare the data to send
# example data
one_byte = b"\x01"
data = b"\xff\xff{}" + one_byte + b"\xde\xad\xbe\xff"

# TODO: send the data to the server
