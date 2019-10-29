from sense_hat import SenseHat
import socket
import fcntl
import struct

sense = SenseHat()

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

print get_ip_address('lo')
print get_ip_address('eth0')

while True:
    sense.show_message(get_ip_address('lo'), text_colour=yellow, back_colour=blue, scroll_speed=0.05)