import { Injectable } from '@angular/core';
import { HttpClient} from '@angular/common/http';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import { apis } from '../app-config';
import { ScheduleObject } from './event-schedule';
//import 'rxjs/Rx';

@Injectable({
  providedIn: 'root'
})
export class ChampsDataService {

  constructor(private http: HttpClient) { }

  title = 'Champs Data';

  getEventSchedule(): Observable<ScheduleObject[]>{

  	return this.http.get<ScheduleObject[]>(apis.localApi);

  			   
  }

  private extractData(res: Response){
  	let data = res.json();
  	return data;
  }

  private handleError(err: Response | any){
  	console.error(err.message || err);

  	return Observable.throw(err.message || err); 
  } 
}

