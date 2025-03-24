import socket
import json

class Server():
    def __init__(self):

        self.lastRecievedData = []
        
        HOST = "127.0.0.1"
        PORT = 12345

        server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        server.bind((HOST,PORT))
        server.listen(1)
        self.conn,self.addr = server.accept()
        print("Client accepted")
    
    def _closeProgram(self):
        pass

    def _getPrograms(self):
        self.conn.send(json.dumps({"action":"1"}).encode())
        recivedData = json.loads(self.conn.recv(999999).decode())
        self.lastRecievedData = recivedData
        for process in recivedData:
            print(process)
        return

    def run(self):
        while(True):
            userChoice = input("Enter action\n1: Get programs\n2: Close program ")

            if(userChoice == "1"):
                self._getPrograms()
            if(userChoice == "2"):
                self._closeProgram()

    

server = Server()
server.run()