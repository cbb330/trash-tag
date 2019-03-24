import register as reg
import runner as runner
from db import Database

if __name__ == "__main__":

	again = 'y'
	dbms = Database()

	while(again in ['y', 'Y', 'r']):
		again = input("register? Press r : ")
		if (again == 'r'):
			fn = input("first name: ")
			ln = input("last name: ")
			binary_object = reg.take_picture()
			dbms.insertPerson("CrimsonHacks", fn, ln, binary_object, 0)

		runner.init()
		again = 'n'
		again = input("Try again? Press y Asking to save AWS/GCP credits, haha! : ")
