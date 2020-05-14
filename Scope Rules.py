# edX - Python for Research

# Scope Rules

def update(n,x):
    n = 2 
    x.append(4)
    print("update:",n,x)
    
def main():
    n = 1
    x = [0,1,2,3]
    print("main:",n,x)
    update(n,x)
    print("main:",n,x)
    
main()   
 
print("-------------------")

def increment(n):
    n += 1
    print(n)

n = 1
increment(n)
print(n)
print("-------------------")
def increment(n):
    n += 1
    return n

n = 1
while n < 10:
    n = increment(n)
print(n)
print("-------------------")