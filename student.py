"""

"""
from person import Person
class Student(Person):
	def __init__(self, admNumber='', stream=''):
		super(Student, self).__init__()
		self.__admNumber = admNumber 
		self.__stream = stream

	def getAdmNumber(self):
		return self.__admNumber

	def setAdmNumber(self, admNumber):
		self.__admNumber = admNumber

	def getStream(self):
		return self.__stream

	def setStream(self,stream):
		self.__stream = stream

	def __str__(self):
		return '[Student: uuid = '+str(super(Student, self).getUuid())+\
		       ' , name = '+super(Student, self).getName()+', gender = '+super(Student, self).getGender()+\
		       ', dob = '+super(Student, self).getGender()+', county = '+super(Student, self).getGender()+\
		       ', admNumber = '+self.__admNumber+',stream = '+self.__stream+']'
		
