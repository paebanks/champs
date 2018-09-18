interface EventScheduleItem{
	event: String;
	time: String;
	sex: String;
	class: String;
	round: String
}

export interface ScheduleObject{
	date: String;
	event_list: EventScheduleItem[];
}

