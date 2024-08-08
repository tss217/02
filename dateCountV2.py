import datetime

class DateCountVT:
    def __init__(self):
        self.currentDay = datetime.date.today()
        self.dataUsers = []
        self.vtDay = []

    def setDay(self):
        return self.currentDay.day
    
    def setMonth(self):
        return self.currentDay.strftime("%B")

    def createDictionary(self, parts):
        user = {}  # Inicializa um novo dicionário para cada usuário
        for part in parts:
            key, value = part.split(":")
            user[key] = value.strip()  # Remove espaços em branco no início e no fim
        self.dataUsers.append(user)

    def setDataUser(self, data):
        for line in data:
            line = line.strip()
            parts = line.split(", ")
            self.createDictionary(parts)
   
    @property
    def GetDataUser(self):
        with open("test02.txt", "r") as data:
            self.setDataUser(data)

    def atualizar_arquivo(self):
        with open("test02.txt", "w") as f:
            for user in self.dataUsers:
                linha = ', '.join([f"{key}: {value}" for key, value in user.items()]) + '\n'
                f.write(linha)

    def countVt(self):
        months_days = {
            "January": 31, "February": 28, "March": 31, "April": 30, "May": 31, "June": 30,
            "July": 31, "August": 31, "September": 30, "October": 31, "November": 30, "December": 31
        }

        self.vtDay.clear()

        for user in self.dataUsers:
           
            if int(user["date"]) == self.setDay():
                self.vtDay.append(user["name"])
                print(self.vtDay)
            
            if int(user["date"]) > self.setDay():
                user["date"] = "0"

            if user["date"] == "0":
                xvt = int(user["vtDay"]) + self.setDay()

                if xvt > months_days[self.setMonth()]:
                    xvt = xvt - months_days[self.setMonth()]
                
                user["date"] = str(xvt)

        self.atualizar_arquivo()

if __name__ == "__main__":
    x = DateCountVT()
    x.GetDataUser
    x.countVt()
    print(x.vtDay)
  
    
    print(x.vtDay)

    with open("test02.txt", "r") as file:
        print(file.read())
