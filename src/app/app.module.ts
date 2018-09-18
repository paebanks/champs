import { BrowserModule } from '@angular/platform-browser';
//import {BrowserAnimationsModule} from '@angular/platform-browser/animations';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
//import { CustomMaterialModule } from './custom-material.module';

import { AppComponent } from './app.component';
import { TimetableByDayComponent } from './timetable-by-day/timetable-by-day.component';
import { TimetableByEventComponent } from './timetable-by-event/timetable-by-event.component';
import { ChampsDataService } from './champs-data.service';

@NgModule({
  declarations: [
    AppComponent,
    TimetableByDayComponent,
    TimetableByEventComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule
    //CustomMaterialModule
  ],
  providers: [ChampsDataService],
  bootstrap: [AppComponent]
})
export class AppModule { }

