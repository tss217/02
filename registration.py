import os
from dateCountV2 import  DateCountVT
#dont forget to update of path way when i  finishe

class resgWoker(DateCountVT):
    def __init__(self, name, vtDay, date, value):
        super().__init__()
        self.ls = []
        self.name = name
        self.vtDay = vtDay
        self.date = date
        self.value = value
        self.dataUserDic = {"name": self.name, "vtDay": self.vtDay, "date": self.date, "value": self.value}

    #1-check if text existe
    #2- if not it. create txt
    #3- register

    def setLs(self):
        self.ls = os.listdir()

    def CheckTxtExiste(self):
        self.setLs()
        if "test02.txt" not in self.ls:
            return False
        
        return True
        
    def checkToMakeTxt(self):
        if not self.CheckTxtExiste():
            with open("test02.txt", "w") as file:
                pass
    
    def registerwoker(self):
        self.GetDataUser
        self.dataUsers.append(self.dataUserDic)
        print(self.dataUsers)
        self.atualizar_arquivo()


if __name__ == "__main__":
    x = resgWoker("tatat","5","0","5.95")
    print(x.CheckTxtExiste())
    x.checkToMakeTxt()
    x.registerwoker()
