import { Injectable } from '@angular/core';

@Injectable()
export class DataService {
  numbers: number[] = [];

  constructor() { }

  randomNumber() {
    Math.floor(Math.random() * 20);
  }

  addNum(num: number) {
    this.numbers.push(num);
  }

  getNum(): number[] {
    return this.numbers;
  }


  //Each component's number list should be displayed near their button in their respective template (HTML) files.

  //When the third component button is clicked, sum all the values stored in the service generated from clicking Alpha components button and then subtract from that the sum of all the values generated from clicking the button in the Beta component. Store this number in the service and display it near the third components button.

}
