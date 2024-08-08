import datetime

class DateCountVT:
    def __init__(self):
        self.currentDay = datetime.date.today()
        self.dataUser = []
        self.vtDay  = []

    def setDay(self):
        return self.currentDay.day
    
    def setMonth(self):
        return self.currentDay.strftime("%B")

    @property
    def GetDataUser(self):
        with open("test01.txt", "r") as data:
            return data.readlines()
    

    def setDataUser(self):
        self.dataUser = [line.strip().split(",") for line in self.GetDataUser]

    def atualizar_arquivo(self):
        with open("test01.txt", "w") as f:
            for user in self.dataUser:
                linha = ','.join(user) + '\n'
                f.write(linha)


    
    # nome, inteval, vtDay, value
    def countVt(self):
        months_days = {"January": 31, "February": 28, "March": 31, "April": 30, "May": 31, "June": 30, 
                        "July": 31, "August": 31, "September": 30, "October": 31, "November": 30, 
                        "December": 31}

        for user in self.dataUser:
            self.vtDay.clear()
            if int(user[2]) == self.setDay():
                self.vtDay.append(user[0])
                print(self.vtDay)

            if int(user[2]) > self.setDay():
                user[2] = "0"

            if user[2] == "0":
                xVt = int(user[1]) + self.setDay()
                if xVt > months_days.get(self.setMonth()):
                    xVt = xVt - months_days.get(self.setMonth())
                user[2] = str(xVt)  

            
            
        self.atualizar_arquivo()


if __name__ == "__main__":
    x = DateCountVT()
    x.setDataUser()
    x.countVt()

    with open("test01.txt", "r") as file:
        print(file.read())
