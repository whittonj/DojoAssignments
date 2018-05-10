import { Injectable } from '@angular/core';

@Injectable()
export class NinjaService {
  gold: Number = 0;
  log: string[] = [];

  constructor() { }

  figGold(building) {
    console.log(building);
    return Math.floor(Math.random() * (building.max - building.min + 1) + building.min);
  }

}
