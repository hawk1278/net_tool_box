import socket
import socks
from mechanize import Browser

socks.set_default_proxy(socks.SOCKS5,'211.195.74.100',3128)
socket.socket = socks.socksocket
br = Browser()
print br.open('http://icanhazip.com').read()
