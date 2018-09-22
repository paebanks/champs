#import libraries
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
from eventlib import EventObject


class ChampsCrawler:
	'''
	Scraper for Jamaica high school athletcs championships results website

	Attributes:
		url(str): url of the champs resutl website
	'''
	def __init__(self, root, page):
		self.root = root
		self.page = page
		html = urllib.request.urlopen(self.root + self.page).read()
		self.soup = BeautifulSoup(html, 'html.parser')


	def get_events_timetable(self):
		'''
		Extracts the dates and corresponding events of all events on champs website

		Args:
			None

		Returns:
			list(EventObject): a list of EventObjects - an EventObject stores a date, event name
							   and url of results pages for that event
		'''
		events = []
		lines = str(self.soup).split('\n') #split html contents into lines

		#event_dates = self.get_events_dates()

		window = []
		for el in self.get_events_dates():
			for pos in [pos for pos, item in enumerate(lines) if item.startswith(el)]:
				window.append(pos)

		start = 0
		stop = start + 1
		while stop <= len(window):
			
			if(stop == len(window)):
				event_lines = lines[window[len(window)-1]+1:]
			else:
				event_lines = lines[window[start]+1:window[stop]-1]

			res = self.get_section(event_lines, start, stop)
			#print(res)
			events += res

			start += 1
			stop = start + 1

		return events


	def get_events_results(self):
		'''
		Extracts results of all events on champs website

		Args:
			None

		Returns:
			str: A JSON string representing teh results of all events onte h champs website
		'''
		count = 0
		result_window = []
		for event in self.get_events_timetable():
			count += 1
			result_page = self.root + event.event_result_url;

			#visit result url and extract results
			html = urllib.request.urlopen(result_page).read()
			result_soup = BeautifulSoup(html, 'html.parser')

			result_list = str(result_soup('pre')).split('\n')

			for idx in [idx for idx, line in enumerate(result_list) if line.startswith('=')]:
				
				result_window.append(idx)


			if(count == 2):
				break

		print(result_window)
		start = 1
		stop = start + 1
		while stop <= len(result_window):
			if(stop == len(result_window)):
				results = result_list[result_window[len(result_window) - 1]:]
			else:
				results = result_list[result_window[start] + 1:result_window[stop] ]
				
			for item in results:
				item = item.strip()
				proper = " ".join(item.split())
				print(proper)	

			#print(results)

			start += 2
			stop = start + 1
			

	def get_events_dates(self):
		'''
		Extracts event dates from the champs site h2 tags

		Args:
			None

		Returns:
			list: list of strings representing dates
		'''
		date_soup = self.soup('h2')
		event_dates = []
		#get the dates of the events
		for el in date_soup:
			date_string = el.contents	#date is array of contents of h2 tag
			if('Session' in date_string[0]):
				date = date_string[len(date_string) - 1].strip('\n')
				event_dates.append(date)

		return event_dates


	def get_section(self, lines, start, stop):
		'''
		Extracts a segment of dates adn events between a start and stop point

		Args:
			lines(str): lines of content from which section is to be extracted
			start(integer): start index in html conntent

			stop(integer): end position in html content

		Returns:
			list(EventObjects)
		'''
		#print(start, stop)
		event_dates = self.get_events_dates()

		events = []

		#event_lines = lines[start:stop]

		for item in lines:
			if(item.startswith('<a href')):
				evt_url = item.split('"')[1]
				evt_name = item.split('>')[1].strip('<a/')
					#print(evt_name) 
				evt = EventObject()
				evt.set_event_date(event_dates[start])
				evt.set_event_name(evt_name)
				evt.set_event_result_url(evt_url)
				events.append(evt)

		#print(events)		
		return events



#result_year = '11';
#url = 'http://www.issasports.com/results/champs' + result_year + '/evtindex.htm';

'''
event_lines = lines[window[len(window)-1]+1:]
for item in event_lines:
		if(item.startswith('<a href')):
			evt_url = item.split('"')[1]
			evt_name = item.split('>')[1].strip('<a/')
			#print(evt_name) 
			evt = EventObject()
			evt.set_event_date(event_dates[len(event_dates) - 1])
			evt.set_event_name(evt_name)
			evt.set_event_result_url(evt_url)
			events.append(str(evt))
			#print(str(evt))
print(events)
'''
root_url = 'http://www.issasports.com/results/champs11/'
first_page = 'evtindex.htm'
crawler = ChampsCrawler(root_url, first_page)

crawler.get_events_results()