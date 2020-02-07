def abc(self):
    print('%s talking' %self.name)
class Person():
    def __init__(self,name):
        self.name = name

p = Person('laowang')
setattr(p,'talk',abc)
p.talk(p)