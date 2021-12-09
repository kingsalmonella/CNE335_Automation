import os

import paramiko
from paramiko import SSHClient, AutoAddPolicy
class Server:

    """ Server class for representing and manipulating servers. """

    def __init__(self, server_ip):
        # TODO -
        self.server_ip = server_ip

    def ping(self):
        # TODO - Use os module to ping the server

        return os.system('ping ' + self.server_ip)
    def paramiko(self):
        #Launch SSH
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(self.server_ip, 22, 'ec2-user')
        #installing update by executing command
        stdin, stdout, stderr = ssh.exec_command('sudo yum update')
        for line in stdout.read().splitlines():
            print(line)
        #Installing upgrade by executing command
        stdin, stdout, stderr = ssh.exec_command('sudo yum upgrade')
        for line in stdout.read().splitlines():
            print(line)

        ssh.close()
