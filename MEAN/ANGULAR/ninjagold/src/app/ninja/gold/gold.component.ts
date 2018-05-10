import { Component, OnInit, Input } from '@angular/core';
import { BuildingComponent } from '../building/building.component';

@Component({
  selector: 'app-gold',
  templateUrl: './gold.component.html',
  styleUrls: ['./gold.component.css']
})
export class GoldComponent implements OnInit {
  @Input()
  gold: GoldComponent;

  constructor() { }

  ngOnInit() {
  }

}
