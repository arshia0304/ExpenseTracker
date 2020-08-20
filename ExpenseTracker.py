import mysql.connector
import datetime
from tabulate import tabulate

mydb = mysql.connector.connect(
	  host="localhost",
	  user="root",
	  password="",
	  database="expense_tracker"
	)

mycursor = mydb.cursor()


def options():
	print("\n\n****Main Menu****\n\n1. Add Expense \n2. Generate Reports \n3. Set Expense Limit \n4. Exit")
	n  = int(input("Enter the number for the transaction you wish to perform: "))
	return n

def checkExpenseLimit(week_no): #function to check and give warning for weekly expense limit
	sqlweek="SELECT SUM(amount) FROM `expense_table` WHERE week_no = {}".format(week_no)
	mycursor.execute(sqlweek)
	week_total = mycursor.fetchall()[0][0] #Stores a total amount spent in a week

	sqllimit="SELECT MAX(weekly_limit) FROM `expense_table` WHERE week_no = {}".format(week_no)
	mycursor.execute(sqllimit)
	limit = mycursor.fetchall()[0][0] #Stores the value of weekly limit

	if(week_total>limit): # If week total exceeds weekly limit it throws a warning
		print("***Warning: Your weekly limit {} has been exceeded.\nCurrent Total: {}".format(limit,week_total))
	else:
		pass

def addExpense():#function to add new entry of users daily expense
	print("\n\n***Add Expense Menu***")
	name=input("\nEnter the Name of Expense: ")
	amount=input("Enter the Expense Amount: ")
	x=datetime.datetime.now()
	date=str(x.strftime("%x"))
	day=str(x.strftime("%A"))

	sqlweek="SELECT MAX(`week_no`) FROM `expense_table`"
	mycursor.execute(sqlweek)
	week_no = mycursor.fetchall()[0][0] #Stores a maximum week number from all the weeks list

	sqllimit="SELECT MAX(weekly_limit) FROM `expense_table` WHERE week_no = {}".format(week_no)
	mycursor.execute(sqllimit)
	limit = mycursor.fetchall()[0][0] #Stores a value of weekly limit


	if (week_no==None): #if there is no entry in the database
		week_no=1
		limit=int(input("Enter a weekly expense limit for new week: "))

	if (day=="Sunday"): #Our new week starts from Sunday so it increases the week number whenever a new week starts
		sqldate="SELECT * FROM `expense_table` where date = '{}'".format(date)
		mycursor.execute(sqldate)
		lastdate = mycursor.fetchall()
		if(len(lastdate)==0): 
			week_no+=1
			limit=int(input("Enter a weekly  expense limit for new week: "))

	# SQL query to store the new expense entry in database
	sql = "INSERT INTO expense_table (name,amount,date,day,week_no,weekly_limit) VALUES (%s, %s, %s, %s, %s, %s)"
	val = (name,amount,date,day,week_no,limit)
	mycursor.execute(sql, val)
	mydb.commit()

	print("\n**Expense Record Inserted Successfully.\n\n")
	checkExpenseLimit(week_no) # Checking the maximum limit condition

def generateReports(): #function to generate a expense report
	print("\n\n***Generate Reports Menu***\n\n1. Weekly Expense Total \n2. Daily Expense Total \n3. Expense on particular date\nPress anything else to return to Main Menu")
	m=int(input("Please Select a valid option: "))

	if (m==1): #Fetch and Display Expense Total for all the weeks
		sqlweek="SELECT MAX(`week_no`) FROM `expense_table`"
		mycursor.execute(sqlweek)
		week_no = mycursor.fetchall()[0][0]

		sqlweekly="SELECT week_no,SUM(amount),MAX(weekly_limit) FROM `expense_table` GROUP BY week_no ORDER BY week_no DESC"
		mycursor.execute(sqlweekly)
		weekly=mycursor.fetchall()

		print("\n\t****Weekly Report****\n")
		print("**You have expense record of {} weeks.".format(week_no))
		print("**Note: Most Recent Expenses are shown first.\n")
		totalamt=0
		table = tabulate(weekly, headers=['Week', 'Amount', 'Weekly Limit'], tablefmt='orgtbl')
		print(table)

		for i in range(week_no):
			totalamt+=weekly[week_no-i-1][1]

		print("\n**Total Amount Spent in all weeks: {}".format(totalamt))


	elif(m==2):#Fetch and Display Expense total for all the days in particular week
		sqlweek="SELECT MAX(`week_no`) FROM `expense_table`"
		mycursor.execute(sqlweek)
		week_no = mycursor.fetchall()[0][0]
		p=int(input("Please enter a valid week number from 1 to {}: ".format(week_no)))
		if (p<=week_no):
			sqlweekly="SELECT date,day,SUM(amount) FROM `expense_table` WHERE week_no={} GROUP BY day ORDER BY FIELD(day, 'SUNDAY', 'MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY')".format(p)
			mycursor.execute(sqlweekly)
			weekly=mycursor.fetchall()

			print("\n\t******Daily Report******\n")
			print("**Date is in the order MM/DD/YY")
			print("**Note: Your week {} expenses are shown in ascending order of days.\n".format(p))
			totalamt=0
			table = tabulate(weekly, headers=['Date', 'Day', 'Amount'], tablefmt='orgtbl')
			print(table)
			for i in weekly:
				totalamt+=i[2]

			print("\n**Total Amount Spent in week {}: {}".format(p,totalamt))
		else:
			print("\n**Please try again by entering a valid week number.")

	elif (m==3):#Fetch and Display Expense Details of all the expenses on the particular day
		q=input("Please enter a valid date in the form MM/DD/YY: ")
		sqldaily="SELECT name,amount FROM `expense_table` WHERE date = '{}'".format(q)
		mycursor.execute(sqldaily)
		daily=mycursor.fetchall()

		if(len(daily)!=0):
			print("\n******Report on Particular Date******\n")
			print("**Note: Your expenses on {} are as follows:\n".format(q))
			totalamt=0

			table = tabulate(daily, headers=['Name', 'Amount'], tablefmt='orgtbl')
			print(table)

			for i in daily:
				totalamt+=i[1]

			print("\n**Total Amount Spent on {}: {}".format(q,totalamt))

		else:
			print("\n**Please try again with a valid date.")

def setExpenseLimit():#Set an Expense Limit for the current week
	limit = int(input("\n\n***Set Expense Limit Menu***\n\nEnter a Weekly Limit Amount:"))
	sqlweek="SELECT MAX(`week_no`) FROM `expense_table`"
	mycursor.execute(sqlweek)
	week_no = mycursor.fetchall()[0][0]
	
	sql = "UPDATE `expense_table` SET weekly_limit = {} WHERE week_no = {}".format(limit,week_no)
	mycursor.execute(sql)

	mydb.commit()

	print("\n**Weekly Limit Updated Successfully.\n\n")



while True:
	try:
		n = options()
		if (n==1):
			addExpense()
		elif (n==2):
			generateReports()
		elif (n==3):
			setExpenseLimit()
		elif (n==4):
			print("\n***Thank You***")
			break
		else:
			print("Please enter a correct option.")
	except Exception as e:
			print("Error:",e)
			print("Please enter a correct option")
