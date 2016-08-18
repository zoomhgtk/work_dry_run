import pprint as pp
import socket
def set_address(hostname):
	ip = socket.gethostbyname(hostname)
	print "set address %s %s/32" % (hostname, ip)

for i in range(1,24):
	host = "dn%d.phx2.cbsig.net" % i
	set_address(host)

def set_address_book(hostname):

