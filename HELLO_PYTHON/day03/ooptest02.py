class Car:
    def __init__(self):     # 생성자
        self.speed = 0
        print("생성",self.speed)
        
    def accel(self,strength):
            self.speed += strength
    
    def __del__(self):      # 소멸자
        self.speed = 0
        print("소멸",self.speed)
        
if __name__ == '__main__':
    c = Car()
    print(c.speed)
    c.accel(100)
    print(c.speed)        