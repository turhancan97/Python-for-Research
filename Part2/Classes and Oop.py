class MyList(list):
    def remove_min(self):
        self.remove(min(self))
    def remove_max(self):
        self.remove(max(self))
        
        
x = [10,3,5,1,2,7,6,4,8]

y = MyList(x)

dir(y)

y.remove_min()

y.remove_max()

y

class NewList(list):
    def remove_max(self):
        self.remove(max(self))
    def append_sum(self):
        self.append(sum(self))

z = NewList([1,2,3])
while max(z) < 10:
    z.remove_max()
    z.append_sum()

print(z)
