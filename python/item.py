import smtplib
from datetime import date as date
import sqlite3
class item:
	def __init__(self,**kwargs):
		self.variables = kwargs
	def setAttribute(self,attribute,value):
		self.variables[attribute]=value
	def getAttribute(self, attribute):
		return self.variables.get(attribute,None)
		
		
def send_email(subject,text):
	sender="kidusasfaw1990@gmail.com"
	password = "secret"
	FROM = sender
	TO = ['kidusasfaw1990@gmail.com']
	SUBJECT = subject
	MESSAGE = text
	note = "From: {}\nTo: {}\nSubject: {}\n\n{}".format(FROM,", ".join(TO),SUBJECT,MESSAGE)
	try:
		server = smtplib.SMTP("smtp.gmail.com",587)
		server.ehlo()
		server.starttls()
		server.login(sender,password)
		server.sendmail(FROM,TO,note)
		server.close()
		print 'Email Sent!'
	except:
		print 'Email Failed!'

		
def checker(file):
	"""Checks from database if something is due
	Args:
	  file (str): The file path to database		
	"""
	db = sqlite3.connect(file)
	db.row_factory = sqlite3.Row
	cursor = db.execute('select * from items')
	for row in cursor:
		if date.today().day == row['item_day']: 
			text = "Item {} with amount {} is due today!".format(row['item_name'],row['item_amount'])
			subject = "You have a payment due!"
			send_email(subject,text)
		else:
			print 'You have no reminders'

def main():
	name = raw_input('Name of reminder item: ')
	file = "test.db"
	print 'Okay, I have added {} into the list of items to remind you about'.format(name)
	day = raw_input('What day of the month should I remind you? ')
	print 'Got it'
	amount = raw_input('What amount should I remind you to pay? ')
	reminder = item(item_name=name,item_day=day,item_amount=amount)
	print 'You are all set with scheduling a reminder for {} for day {} of every month for amount {}.'.format(reminder.getAttribute('item_name'),reminder.getAttribute('item_day'),reminder.getAttribute('item_amount'))
	db = sqlite3.connect(file)
	db.row_factory = sqlite3.Row
	db.execute('drop table if exists items')
	db.execute('create table if not exists items(item_name str, item_day int, item_amount int,PRIMARY KEY (item_name,item_day))')
	db.execute('insert into items(item_name,item_day,item_amount) values (?,?,?)',(name,day,amount))
	db.commit()
	print '\n Your current items'
	checker(file)
if __name__ == "__main__": main()
	