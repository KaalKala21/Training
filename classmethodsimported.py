from FunctionsFile import ist
import time
def sleepdec(func):
    def inner(x):
        for i in range(10):
            time.sleep(1)
            print(str(i+1)+"\n")
        return func(x)
    return inner
        
a=ist()
b=[1,2,3]
c={"one":1,
    "two":2
   }
addElementToList1=sleepdec(a.addElementToList)
addElementToList1(b)
addElementToDict1=sleepdec(a.addElementToDict)
addElementToDict1(c)
a.printObject()
