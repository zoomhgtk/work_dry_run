import pprint as pp
import socket

address_set_name = raw_input("please enter name of address-set >")

def set_address(hostname):
	ip = socket.gethostbyname(hostname)
	print "set security zones security-zone Transit address-book address %s %s/32" % (hostname, ip)

def set_address_book(hostname):
	print "set security zones security-zone Transit address-book address-set %s address %s" % (address_set_name, hostname)

for i in range(1,24):
	host = "dn%d.phx2.cbsig.net" % i
	set_address(host)
	set_address_book(host)

