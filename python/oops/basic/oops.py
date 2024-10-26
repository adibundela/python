class Car:
    # def accealrate() : 
    #     print("car is accelarate....")  it will throw an errr    
    
    def accealrate(self):
        print("car is accelarate....")
        
        
        
c1 =Car()

c1.accealrate()  # calling method by object name 

# Extract odd and even no from an list  

class listO:
    def __init__(self,l):   ##    Magic Method Or Dunder Method
        self.l = l
    def getOdd(self,l):
        return [i for i in l if i % 2 != 0]
    
    def getEven(self,l):
        return [i for i in l if i % 2 == 0]

l1 = listO([1,2,3,4,5,6,7,8,9])

print(l1.getOdd(l1.l))
print(l1.getEven([12,13,14,15]))