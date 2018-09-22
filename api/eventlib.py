#class definition for event object
#data members:	event_date, event_name, event_result_url
class EventObject:

	def __init__(self):
		self.event_date = ''
		self.event_name = ''
		self.event_result_url = ''

	def set_event_date(self, dt):
		self.event_date = dt

	def set_event_name(self, name):
		self.event_name = name

	def set_event_result_url(self, url):
		self.event_result_url = url

	def __str__(self):
		return "{event_date: " + str(self.event_date) + ", event_name: " + str(self.event_name) + \
				", event_result_url: " + self.event_result_url + "}"



class ResultObject:

	def __init__(self):
		self.event.name = ''
		self.results = []

	def set_event_name(self, name):
		self.event_name = name

	def set_event_results(self, res = []):
		self.results = res

	def add_result(self, res):
		self.results.append(res)