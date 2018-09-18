import { Component, OnInit } from '@angular/core'
import { ChampsDataService } from '../champs-data.service';
 
@Component({
	selector: 'app-timetable-by-event',
	templateUrl: './timetable-by-event.component.html',
	styleUrls: ['./timetable-by-event.component.css']
})
export class TimetableByEventComponent implements OnInit{

	constructor(private api: ChampsDataService){}

	name: String;
	api_pos: number;
	schedule = [];

	scheduleContent = [];

	ngOnInit(){
		this.name = this.api.title;
		this.api_pos = 0;
		this.api.getEventSchedule().subscribe(
			data => {
				this.schedule = data;
				//console.log(this.schedule);
				this.scheduleContent = this.schedule[0];
			},

			error =>{
				console.log(error)
			}
		);
	}


	showEventSchedule(pos){
		this.scheduleContent = this.schedule[pos];
		//console.log(this.scheduleContent);
	}

	eventDay(pos){
		return 'Day ' + ++pos;
	}

	getClass(pos){

		if(pos === 0)
		{
			return "nav-link active"
		}
		else{
			return "nav-link"
		}	

		//console.log(pos);
	}

}