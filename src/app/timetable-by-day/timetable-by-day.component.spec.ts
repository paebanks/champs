import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { TimetableByDayComponent } from './timetable-by-day.component';

describe('TimetableByDayComponent', () => {
  let component: TimetableByDayComponent;
  let fixture: ComponentFixture<TimetableByDayComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ TimetableByDayComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(TimetableByDayComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
