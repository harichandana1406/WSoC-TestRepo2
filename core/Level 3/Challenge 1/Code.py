class Cricket(object):
    def __init__(self,Name,Noof,Time,Equipment,Countryoforigin):
        self.Name=Name
        self.Noof=Noof
        self.Time=Time
        self.Equipment=Equipment
        self.Countryoforigin=Countryoforigin
        
    def display(self):
        print("Name of the sport is "+self.Name)
        print("Number of player required is "+self.Noof)
        print("Time duration is "+self.Time)
        print("Equipment needed are "+self.Equipment)
        print("Country of origin "+self.Countryoforigin)
        
a=Cricket('cricket','11','3-5 days','Bat,ball,helmet,legpads,gloves,stumps','England')
a.display()
class T20(Cricket):
    def __init__(self,name1,TotalOvers,Time):
        #Cricket.__init__(self,Name,Noof,Time,Equipment,Countryoforigin)
        self.name1=name1
        self.TotalOvers=TotalOvers
        self.Time=Time
    def cricketT20(self):
        print()
        print("Name of Match is "+self.name1)
        print("Total number of overs "+self.TotalOvers)
        print("Time duration is "+self.Time)
        #print(self.Name,self.Noof,self.Time,self.Equipment,self.Countryoforigin)
c=T20('T20','20 Overs','90 min').cricketT20()
        
class TestMatch(Cricket):
    def __init__(self,name1,TotalOvers,Time):
        #Cricket.__init__(self,Name,Noof,Time,Equipment,Countryoforigin)
        self.name1=name1
        self.TotalOvers=TotalOvers
        self.Time=Time
    def cricketTest(self):
        print()
        print("Name of Match is "+self.name1)
        print("Total number of overs "+self.TotalOvers)
        print("Time duration is "+self.Time)
        #print(self.Name,self.Noof,self.Time,self.Equipment,self.Countryoforigin)
b=TestMatch('Test Match','90 Overs','5 days').cricketTest()

class ICC(Cricket):
    def __init__(self,name1,TotalOvers,Time):
        #Cricket.__init__(self,Name,Noof,Time,Equipment,Countryoforigin)
        self.name1=name1
        self.TotalOvers=TotalOvers
        self.Time=Time
    def cricketICC(self):
        print()
        print("Name of Match is "+self.name1)
        print("Total number of overs "+self.TotalOvers)
        print("Time duration is "+self.Time)

ob=ICC('ICC','50 Overs','5 days').cricketICC()

class player1():
    def details(self):
        print()
        print("1.Name of the player is Mahendra Singh Dhoni")
        print("  Age of player is 39")
        print("  Origin of player is India")
        print("  At present playing")
class player2():
    def details(self):
        print("2.Name of the player is Mithali Raj")
        print("  Age of player is 37")
        print("  Origin of player is India")
        print("  At present playing")
class player3():
    def details(self):
        print("3.Name of the player is Rohit Sharma")
        print("  Age of player is 33")
        print("  Origin of player is India")
        print("  At present playing")
class player4():
    def details(self):
        print("4.Name of the player is David Andrew Warner")
        print("  Age of player is 27")
        print("  Origin of player is Australia")
        print("  At present playing")
class player5():
    def details(self):
        print("5.Name of the player is Kane Williamson")
        print("  Age of player is 30")
        print("  Origin of player is New Zealand")
        print("  At present playing")
        
obj_a1=player1()
obj_b1=player2()
obj_c1=player3()
obj_d1= player4()
obj_e1= player5()
for players in (obj_a1,obj_b1,obj_c1,obj_d1,obj_e1):
    players.details()

   