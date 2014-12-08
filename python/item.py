#need to import smtp,datetime,and figure out how to keep this running and sending emails even when not 
class item:
	def __init__(self,**kwargs):
		self.variables = kwargs
	def setAttribute(self,attribute,value):
		self.variables[attribute]=value
	def getAttribute(self, attribute):
		return self.variables.get(attribute,None)

def main():
	name = raw_input('Name of reminder item: ')
	print 'Okay, I have added {} into the list of items to remind you about'.format(name)
	day = raw_input('What day of the month should I remind you? ')
	print 'Got it'
	amount = raw_input('What amount should I remind you to pay? ')
	reminder = item(item_name=name,item_day=day,item_amount=amount)
	print '\nYou are all set with scheduling a reminder for {} for day {} of every month for amount {}.'.format(reminder.getAttribute('item_name'),reminder.getAttribute('item_day'),reminder.getAttribute('item_amount'))
	
if __name__ == "__main__": main()
	