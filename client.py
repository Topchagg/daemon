import psutil
import socket
import json


class Client():
    def __init__(self):
        HOST = "127.0.0.1"  
        PORT = 12345        

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.client.connect((HOST, PORT))
    
    def _getPrograms(self):
        listOfProc = list(psutil.process_iter())
        listOfProcToSend = []

        for index,process in enumerate(listOfProc):
            try:
                listOfProcToSend.append({
                index: {
                "name": process.name(),
                "pid": process.__getattribute__('pid')
                }})
            except Exception as e:
                print(e)
        
        self.client.send(json.dumps(listOfProcToSend).encode())
        return

    def _destroyProgram(self):
        pass
    
    def run(self):
        while(True):
            recivedData = json.loads(self.client.recv(1024).decode())
            action = recivedData['action']

            if(action  == '1'):
                self._getPrograms()
            if(action == 'q'):
                self.client.close()


client = Client()
client.run()