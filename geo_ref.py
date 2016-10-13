import pygeoip

gi = pygeoip.GeoIP('/home/rich/development/net_tool_box/dat/GeoLiteCity.dat')


def printrcd(tgt):
	rec = gi.record_by_name(tgt)
	print rec

tgt = '172.255.226.98'
printrcd(tgt)
