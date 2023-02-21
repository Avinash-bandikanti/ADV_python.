import paramiko
ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname="192.168.149.128",username="avinash",password="abhi123")
stdin,stdout,stderr=ssh.exec_command("whoami")
for f in stdout:
    print(f)
stdout.close()