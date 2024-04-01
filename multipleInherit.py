class Father():
    def gardening(self):
        print("i love gardening")
        
class Mother():
    def cooking(self):
        print("i love cooking")
        
class Child(Father,Mother):
    def playing(self):
        print("i love sports")
        
c=Child()
c.gardening()
c.cooking()
c.playing()


