import { TestBed, inject } from '@angular/core/testing';

import { ChampsDataService } from './champs-data.service';

describe('ChampsDataService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [ChampsDataService]
    });
  });

  it('should be created', inject([ChampsDataService], (service: ChampsDataService) => {
    expect(service).toBeTruthy();
  }));
});
