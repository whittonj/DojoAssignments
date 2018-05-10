import { Component, OnInit, Input } from '@angular/core';
import { BuildingComponent } from '../building/building.component';

@Component({
  selector: 'app-log',
  templateUrl: './log.component.html',
  styleUrls: ['./log.component.css']
})

export class LogComponent implements OnInit {
  @Input()
  log: LogComponent;

  constructor() { }

  ngOnInit() {
  }

}
