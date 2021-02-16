class ist:
    li=[]
    di=dict()
    def addElementToList(self,i):
        self.li.extend(i)
    def addElementToDict(self,d):
        for key in d:
            self.di[key]=d[key]
    def printObject(self):
        print("list = ",self.li,"\ndictionary = ",self.di)
a=ist()
b=[1,2,3]
c={"one":1,
    "two":2
   }
a.addElementToList(b)
a.addElementToDict(c)
a.printObject()
