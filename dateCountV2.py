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

    def setYear(self):
        return self.currentDay.year

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

    def isLeapYear(self, year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    def getMonthDays(self, year):
        return {
            "January": 31, 
            "February": 29 if self.isLeapYear(year) else 28, 
            "March": 31, 
            "April": 30, 
            "May": 31, 
            "June": 30,
            "July": 31, 
            "August": 31, 
            "September": 30, 
            "October": 31, 
            "November": 30, 
            "December": 31
        }   

    def countVt(self):

        

        current_year = self.setYear()
        months_days = self.getMonthDays(current_year)

        self.vtDay.clear()

        # Armazenar valores retornados por métodos em variáveis locais
        current_day = self.setDay()
        current_month = self.setMonth()
        
        for user in self.dataUsers:
            user_date = int(user["date"])
        
            # Verificar se a data do usuário é igual ao dia atual
            if user_date == current_day:
                self.vtDay.append(user["name"])
                print(self.vtDay)
            
        
            # Verificar se a data do usuário é maior que o dia atual
            elif user_date > current_day:
                user["date"] = "0"
        
            # Verificar se a data do usuário foi resetada para "0"
            if user["date"] == "0":
                xvt = int(user["vtDay"]) + current_day
        
                # Ajustar xvt se exceder o número de dias no mês atual
                if xvt > months_days[current_month]:
                    xvt -= months_days[current_month]
                
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
