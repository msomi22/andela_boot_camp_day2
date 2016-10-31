"""
A person object
"""
import uuid
class Person(object):

	def __init__(self, name='', gender='', dob='', county=''):
		self.__uuid = uuid.uuid4()
		self.__name = name
		self.__gender = gender
		self.__dob = dob 
		self.__county = county

	def getUuid(self):
		return self.__uuid 

	def setUuid(self, uuid):
		self.__uuid = uuid

	def getName(self):
		return self.__name

	def setName(self, name):
		self.__name = name 

	def getGender(self):
		return self.__gender

	def setGender(self, gender):
		self.__gender = gender

	def getDob(self):
		return self.__dob

	def setDob(self,dob):
		self.__dob = dob 

	def getCounty(self):
		return self.__county

	def setCounty(self,county):
		self.__county = county 

	def __str__(self): 
		return '[person: uuid = '+str(self.__uuid)+', name = '+self.__name+', gender = '+self.__gender+', dob = '+self.__dob+', county = '+self.__county+']'
		
		
		
