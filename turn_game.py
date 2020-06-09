import random

class boss():
    def __init__(self):
        self.HP = 100000

    def skill(self, num):
        self.HP -= num
        return self.HP
call = boss()

for i in range(1, 100):
    print(call.skill(random.randint(1, 999)))

