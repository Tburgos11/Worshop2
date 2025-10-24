class student:
 def __init__(self,id,name):
  self.id=id
  self.name=name
  self.grades=[]
  self.passed=None
 def addGrade(self,grade):
  if grade<0 or grade>100:
   print("bad")
  else:
   self.grades.append(grade)
 def avg(self):
  if len(self.grades)==0:
   return 0
  return sum(self.grades)/len(self.grades)
 def report(self):
  print("ID:",self.id)
  print("Name:",self.name)
  print("Avg:",self.avg())

if __name__=='__main__':
 s=student('001','Thomas')
 s.addGrade(95)
 s.addGrade(87)
 s.addGrade(91)
 s.report()
