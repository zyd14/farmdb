import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { PlanttypesComponent } from './planttypes.component';

describe('PlanttypesComponent', () => {
  let component: PlanttypesComponent;
  let fixture: ComponentFixture<PlanttypesComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ PlanttypesComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(PlanttypesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
