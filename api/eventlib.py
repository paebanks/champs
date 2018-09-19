#class definition for event object
#data members:	event_date, event_name, event_result_url
class EventObject:

	def __init__(self):
		self.event_date = ''
		self.event_name = ''
		self.event_result_url = ''

	def set_event_date(self, date):
		self.event_date = date

	def set_event_name(self, name):
		self.event_name = name

	def set_event_result_url(self, url):
		self.event_result_url = url
