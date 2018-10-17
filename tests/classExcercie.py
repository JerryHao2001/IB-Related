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
    def __init__(self,name,age = 17,gender = '-',classs = 'C7',subjectsGrades = 'no grade avilable'):
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
    
    def setAge(self,newAge):
        '''
        reset the age
        '''
        self.age = newAge
        return "now is "+str(self.age)
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
        return str(self.name) + " is a " + str(self.age) +" years old " + str(self.gender) + " student, who study in " + str(self.classs)
        
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
    
    
    