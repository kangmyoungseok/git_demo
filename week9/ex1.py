# class 생성 예제
class car:
    model = None    # 클래스 변수. 모든 클래스 및 인스턴스가 공유
    owner = None

    def move(self):
        print("this is move function")

    def fuel(self):
        print("this is fuel function")
    
    def set_idx(self,idx):
        self.idx = idx


my_car = car()
my_car2 = car()
car.model = 'puang'

print(my_car.model)

my_car.set_idx(3)
my_car.idx
my_car2.set_idx(8)
my_car2.idx