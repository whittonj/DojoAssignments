import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { DisplayLevelsComponent } from './display-levels.component';

describe('DisplayLevelsComponent', () => {
  let component: DisplayLevelsComponent;
  let fixture: ComponentFixture<DisplayLevelsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ DisplayLevelsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(DisplayLevelsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
