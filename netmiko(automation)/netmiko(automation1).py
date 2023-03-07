from netmiko import ConnectHandler
device={
    'device_type':'linux',
    'ip':'192.168.149.128',
    "username":"avinash",
     "password":"abhi123"
}
connection=ConnectHandler(**device)
cpu_output=connection.send_command('cat /proc/cpuinfo')
mem_output=connection.send_command('free -h')
connection.disconnect()
print('CPU Information:')
print(cpu_output)
print('/nMemory Information:')
print(mem_output)