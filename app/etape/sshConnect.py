import os

import paramiko
from scp import SCPClient

hostname = "10.100.116.10"
password = "vikings"
command = "ls -lrt"

username = "mcisse"
port = 22


# print(client.get_transport().is_active())

### Fonction de Connexion au serveur distant par SSH

def sshConnexion(username, password):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.WarningPolicy)
    client.connect(hostname, port=port, username=username, password=password)
    return client


### Fucntion that check if credentials that are given have access to the cluster
def sshCheckAuthentication(username, password):
    try:
        sshConnexion(username, password)
        return True
    except Exception as e:
        print(e)
        return False


def scpTransfert(username, password, filetoTransfert):
    try:
        ssh = sshConnexion(username, password)
        # SCPCLient takes a paramiko transport as an argument
        scp = SCPClient(ssh.get_transport())
        dirname = os.path.dirname(__file__)
        filename = dirname + "/" + filetoTransfert
        print(filename)
        scp.put(filename, remote_path="/home/dndiaye/paramiko")
        scp.close()
        return True
    except Exception as e:
        print(e)
        return False

# print(sshCheckAuthentication(username,password))
# print(scpTransfert(username,password,"testScp.txt"))
