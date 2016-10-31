"""

"""
from employee import Employee 
from student import Student 
class Demo(Employee, Student):

	def __init__(self):
		super(Demo, self).__init__()  
    #Save student/employee into RDMBS 
	def put(self,obj):
		if isinstance(obj,Student): 
			print 'student' , obj 
		else:
			print 'employee' , obj 
		 
		


student = Student('100','Form 2 N') 
demo = Demo()

student.setName('Naomi Kawira')
student.setGender('Female')
student.setDob('16-07-1990')
student.setCounty('Meru') 
#demo.put(student) 

emp = Employee('100','IT','Developer','G','56,000')	
emp.setName('Peter Mwenda')
emp.setGender('Male')
emp.setDob('31-05-1990')
emp.setCounty('Tharaka Nithi')
# call put method 
demo.put(emp)





	







