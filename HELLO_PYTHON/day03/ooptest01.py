class Animal:
    def __init__(self):
        self.hungry = 5
    
    def timegoby(self):
        if self.hungry > 0 :
            self.hungry -= 1
        
    def manttang(self):
        self.hungry=10;
    
    
class Human(Animal):
    def __init__(self):
        super().__init__()
        self.skill_lang = 0
    def momstouch(self,stroke):
        self.skill_lang += stroke        
    
ani = Animal()
hum = Human()

print(ani.hungry)
ani.timegoby()
ani.manttang()
print(ani.hungry)

print(hum.hungry)
print(hum.skill_lang)
hum.manttang()
hum.momstouch(11)
print(hum.hungry)
print(hum.skill_lang)
