#import libraries
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
from eventlib import EventObject



result_year = '11';
url = 'http://www.issasports.com/results/champs' + result_year + '/evtindex.htm';

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

event_list = []

event_dates = soup('h2')
#print(event_dates)

for el in event_dates:
	date = el.contents	#date is array of contents of h2 tag
	if('Session' in date[0]):
		evt = EventObject()
		evt.set_event_date(date[len(date) - 1].strip('\n'))
		event_list.append(evt)		 

#for ev in event_list:
#	print(ev.event_date)
#pattern = re.match('[0-9]{2}/[0-9]{2}/[0-9]{4}', '50')
#if(pattern == None):
#	print('no match')

#get list of events from soup
events = soup('hr')
print(events[1].next_sibling.next_sibling)


