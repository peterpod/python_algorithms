class Monster(object):
    def sayBoo(self):
        print "boo!"

class SeaMonster(Monster):
    def swim(self):
        print "glug glug!"

m1 = SeaMonster()
m2 = Monster()
print m1.sayBoo()== "boo!"
