"""
An employee object 
"""
from person import Person
class Employee(Person): 
	def __init__(self, empNumber='', department='', position='', salaryClass='', salary=''):
		super(Employee, self).__init__() 
		self.__empNumber = empNumber
		self.__department = department
		self.__position = position
		self.__salaryClass = salaryClass
		self.__salary = salary

	def getEmpNumber(self):
		return self.__empNumber

	def setEmpNumber(self, empNumber):
		self.__empNumber = empNumber

	def getDepartment(self):
		return self.__position 

	def setDepartment(self, department):
		self.__department = department

	def getPosition(self):
		return self.__position

	def setPosition(self, position):
		self.__position = position

	def getSalaryClass(self):
		return self.__salaryClass

	def setSalaryClass(self, salaryClass):
		self.__salaryClass = salaryClass

	def getSalary(self):
		return self.__salary

	def setSalary(self, salary):
		self.__salary = salary 

	def __str__(self):
		return '[Employee: uuid = '+str(super(Employee, self).getUuid())+\
		       ', name = '+super(Employee, self).getName()+',  gender = '+super(Employee, self).getGender()+\
		       ', dob = '+super(Employee, self).getGender()+', county = '+super(Employee, self).getGender()+\
		       ', empnumber = '+self.__empNumber+', department = '+self.__department+', position = '+self.__position+', salaryclass = '+self.__salaryClass+', salary = '+self.__salary+']'
		
		

		
		
		
		

