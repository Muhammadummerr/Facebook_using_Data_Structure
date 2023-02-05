import datetime
import re
import getpass
class Account:
	usernames_list = []
	_passwords_list = []
	def __init__(self):
		while True:
			self.signupANDsingninpage()
	def signupANDsingninpage(self):
		task = int(input("WELCOME TO FACEBOOK\n 1.press 1 to sign in \n 2.press 2 to sign up "))
		if task == 1:
			self.create_account_method()
		elif task == 2:
			self.login_method()
	def create_account_method(self):
		self.name = self.set_name()
		self.username = self.set_username()
		self._passwrod = self.set_password()
		self.date_of_birth = self.set_date_of_birt()
		print(self.date_of_birth,10000)
		self.age  = self.calculate_age(self.date_of_birth)
		self.bio = self.set_bio()
		self.location = self.set_location()
		# self.friends = True
		# self.block_acc = True
		# self.messages = True
		# self.notifications = True
	def login_method(self):
		while True:
			username= input("Enter your username")
			_password = getpass.getpass(prompt="enter password")
			if username in Account.usernames_list:
				index_of_username = Account.usernames_list.index(username)
				print(index_of_username)
				if Account._passwords_list[index_of_username] == _password:
					print("you are logged in")
					break
				else:
					# print(Account._passwords_list[index_of_username],_password)
					print("Incorrect password")
			else:
				print("Email Doesn't exist")
	def main_page_of_logged_in_account(self):
		print("FACEBOOK/n press following buttons to perform following operations/n1. to search people\n2. to message people")
		task = int(input())
		if task == 1:
			pass
		elif task == 2:
			pass
	def input_of_date_of_birt(self): #To take and match date input.If true return it
		while True:
			date_of_birt = input("Enter Your Date Of Birt:(in format --- day/mont/year")
			flag = re.match('[0-9]{2}/[0-9]{2}/[0-9]{4}',date_of_birt)
			if flag:
				return date_of_birt
			else:
				print("Incorrect format")
				continue
	def set_date_of_birt(self):	# set dob and age according to it
		date_of_birth = self.input_of_date_of_birt()
		self.age = self.calculate_age(date_of_birth)
		return date_of_birth
	def calculate_age(self,date_of_birt): #Calculate age
		print(date_of_birt,99)
		todays_date = datetime.datetime.today().strftime('%d/%m/%Y')
		if int(date_of_birt[3:5])< int(todays_date[3:5]) and int(date_of_birt[0:2])>= int(todays_date[0:2]):
			return int(todays_date[6:10]) -int(date_of_birt[6:10])
		else:
			return int(todays_date[6:10]) -int(date_of_birt[6:10])-1
	def set_username(self):
		while True:
			username = input("Enter username:")
			if username != Account.usernames_list:
				self.username = username
				Account.usernames_list.append(self.username)
				break
			else:
				print("username already exists!")
	def set_password(self):
		while True:
			_password = getpass.getpass(prompt="Enter password:") #display * problem1
			print(_password)
			_temp = getpass.getpass(prompt="Again enter password:")
			print(_temp)
			if len(_password) >=4 and str(_password)== str(_temp):
				
				Account._passwords_list.append(_password)
				return _password
			else:
				print("try again")
	def information_display(self):
		print("Name = ",self.name)
		print("Dob = ",self.date_of_birth)
		print("Age = ",self.age,"Years")
	def set_name(self):
		name = input("Enter Name:")
		return name
	def set_bio(self):
		bio = input("Enter Your bio:")
		self.bio = bio
	def set_location(self):
		location = input("Enter Your City:")
		self.location= location
a = Account()
a.information_display()
