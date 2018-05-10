import { Component, OnInit, Input } from '@angular/core';

import { Building } from '../building';
import { NinjaService } from '../../services/ninja.service';
import { BUILDINGS } from '../data/building-data';

@Component({
  selector: 'app-building',
  templateUrl: './building.component.html',
  styleUrls: ['./building.component.css']
})
export class BuildingComponent implements OnInit {
  @Input()
  building: Building;
  selectedBuilding: Building;
  buildings: Array<Building> = BUILDINGS;
  gold = 0;
  log = [];


  constructor(private ninjaService: NinjaService) { }

  ngOnInit() {
    console.log(this.buildings);
  }

  getEarnings(building) {
    this.selectedBuilding = this.selectedBuilding === building ? null : building;
    const earning = this.ninjaService.figGold(this.selectedBuilding);
    console.log(earning);
    this.log.push('You visited the' + this.selectedBuilding.name);
    console.log(this.log);
    this.selectedBuilding = null;
    this.gold = this.gold + earning;
    console.log(this.gold);
  }

}
