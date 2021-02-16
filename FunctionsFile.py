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
