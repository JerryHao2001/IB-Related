# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 22:19:43 2018

@author: 11658
"""

class point:
    '''
    a class represent a point with x,y coordinates
    '''
    
    def __init__(self,initX,initY):
        self.x = initX
        self.y = initY
    def getX(self):
        '''
        get the x coordinate
        '''
        return self.x
    def getY(self):
        '''
        get the y coordinate
        '''
        return self.y
    def __str__(self):
        '''
        print()
        (x,y)
        '''
        return "("+str(self.x)+','+str(self.y)+")"
    def __add__(self,other):
        '''
        return a point(x1+x2,y1+y2)
        '''
        newPoint = point(self.x+other.x,self.y+other.y)
        return newPoint
        

class student():
    '''
    a student with 
    name, age, gender, class, and subjectsGrades
    '''
    def __init__(self,name = '-',age = 17,gender = '-',classs = 'C7',subjectsGrades = 'no grade avilable'):
        '''
        name:str
        age:int
        gender:string
        class:string
        subjectsGrades:dict
        '''
        self.name = name
        self.age = age
        self.gender = gender
        self.classs = classs
        self.subjectsGrades = subjectsGrades
        
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    def getGender(self):
        return self.gender
    def getClass(self):
        return self.classs
    def getSubjectsGrades(self):
        return self.subjectsGrades
    
    def setName(self,newName):
        '''
        reset the name
        '''
        self.name = newName
        return "new name: " + str(self.name) 
    
    def setAge(self,newAge):
        '''
        reset the age
        '''
        self.age = newAge
        return "now is "+str(self.age)
    
    def setGender(self,newGender):
        '''
        reset the gender
        '''
        self.gender = newGender
        return "now is "+str(self.gender)
    
    def setSubjectsGrades(self,newSubjectsGrades):
        '''
        reset the SubjectsGrades
        '''
        self.subjectsGrades = newSubjectsGrades
        return "now is " + str(self.subjectsGrades)
        
    def averageGrade(self):
        '''
        get the average grade of all subjects
        '''
        return sum([i for i in self.subjectsGrades.values()])/len(self.subjectsGrades)
    
    def showGrades(self):
        '''
        return the grade level of average grade
        '''
        averageScore = self.averageGrade()
        if averageScore > 90:
            return "A"
        elif averageScore > 80:
            return "B"
        elif averageScore > 70:
            return "C"
        elif averageScore > 60:
            return "D"
        else:
            return "F"
        
    def __str__(self):
        return ( str(self.name) + " is a " + str(self.age) +" years old " + str(self.gender) + " student who study in " + str(self.classs))
        
    

class IBStudent(student):
    '''
    IB Students
    '''
    tokGrade = ['A','B','C','D','E','F']
    def __init__(self, hairRemain = 0, TOK = "F", CAS = 0, EE = 0, IA = 0):
        '''
        name:str
        age:int
        gender:string
        class:string
        subjectsGrades:dict
        hairRemain(in percentage): initial 0%
        TOK: grade level(A to F) initial F
        CAS: percentage complete(in percentage) initial 0%
        EE: percentage complete(in percentagre) initial 0%
        IA: completed number(min:0 max:6)
        '''
        student.__init__(self)
        self.hairRemain = hairRemain
        self.tok = TOK
        self.cas = CAS
        self.ee = EE
        self.ia = IA
    
    def getHairRemain(self):
        return "hair remain " + str(self.hairRemain) + "%"
    def getTOK(self):
        return "TOK grade is " + str(self.tok)
    def getCAS(self):
        return "CAS complete " + str(self.cas) + "%"
    def getEE(self):
        return "EE complete " + str(self.ee) + "%"
    def getIA(self):
        return "IA complete " + str(self.ia) + " of 6"
    
    def sleep(self):
        '''
        go to sleep and save your hair
        '''
        self.hairRemain += 5
        print("hair increase 5%")
    def learnTok(self): 
        '''
        hair - 5%
        TOK improved
        '''
        if not(self.tokGrade.index(self.tok) == 0):
            self.tok = self.tokGrade[self.tokGrade.index(self.tok)-1]
        self.hairRemain -= 5
        print("TOK grade improved to",self.tok)
        print("lost 5% hair")
    def doCas(self):
        '''
        CAS +5%
        '''
        self.cas += 5
        print("CAS complete increase 5%")
    def writeEE(self):
        '''
        EE +20%
        hair -10%
        '''
        if self.ee < 100:
            self.ee += 20
        self.hairRemain -= 10
        print("EE complete increase 20%")
        print("lost 10% hair")
    def writeIA(self):
        '''
        Complete one IA
        hair -20%
        '''
        if self.ia < 6:
            self.ia += 1
        self.hairRemain -= 20
        print("complete 1 IA")
        print("lost 20% hair")
        
    def __str__(self):
        print(student.__str__(self))
        print(self.getHairRemain())
        print(self.getTOK())
        print(self.getCAS())
        print(self.getEE())
        print(self.getIA())
        if self.hairRemain <= 0:
            print("MONK")
        if self.tok == 'F' and self.cas == 0 and self.ee == 0 and self.ia == 0:
            print("Wonderful Student. IS It Your Hobby To Get A Zero?",'\n                                 ———— Mr.Eugene',)
            return 'Loser'
        elif self.tok == 'A' and self.cas == 100 and self.ee == 100 and self.ia == 6:
            print("Gooda","\n         ———— Mr.Eugene")
            return 'Good Student'
        else:
            return 'Do Me A Favor. Disapper, Now'+"\n                          ———— Mr.Eugene"
 


def testStudent():
    jelly = student('jelly',10,'male','C7',{'English':1,'Math':3,"Man":5,"CS":7,"Phys":9,"Eco":11})
    print(jelly.getName())
    print(jelly.getAge())
    print(jelly.getGender())
    print(jelly.getClass())
    print(jelly.getSubjectsGrades())
    print(jelly.averageGrade())
    print(jelly.showGrades())
    print(jelly.setAge(200))
    print(jelly.setSubjectsGrades({'English':3,'Math':5,"Man":7,"CS":9,"Phys":11,"Eco":13}))
    print(jelly)
       
def testIBStudent():
    Charlie = IBStudent(100,'F',0,0,0)
    Charlie.setName("Charlie")
    Charlie.setAge(16)
    Charlie.setGender('Female')
    print(Charlie)
    
    print("\n")
    
    Hanbo = IBStudent(0,'A',100,100,6)
    Hanbo.setName("Hanbo")
    Hanbo.setAge(17)
    Hanbo.setGender('Male')
    print(Hanbo)
    
    