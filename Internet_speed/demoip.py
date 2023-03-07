import socket
import re
ipaddress=['10.20.30.34','234.678.0.2','10.20.1','2000.3.4.5','10.20.34.56.6']
valid_ip1=[]
valid_ip2=[]
'''for ip in ipaddress:
    if(ip.count('.')<3):                                                                   
        valid_ip.append(ip)
    else:                                 
        try:
            socket.inet_aton(ip)
            valid_ip.append(ip)
        except Exception:
            pass'''
for ip in ipaddress:
    r=re.findall(r'\.',ip)
    if len(r)==3:
        valid_ip1.append(ip)
for ip in valid_ip1:
    try:
        socket.inet_aton(ip)
        valid_ip2.append(ip)
    except Exception as e:
        pass
print(valid_ip2)
