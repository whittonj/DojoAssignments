import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent implements OnInit {
  cArray = [];
  fillcArray() {
    for (let y = 0; y < 10; y++) {
      const randNum = (Math.floor(Math.random() * 6)) + 1;
      if (randNum === 1) {
        this.cArray.push('BurlyWood ');
      } else if (randNum === 2) {
        this.cArray.push('CadetBlue ');
      } else if (randNum === 3) {
        this.cArray.push('Chartreuse ');
      } else if (randNum === 4) {
        this.cArray.push('Chocolate ');
      } else if (randNum === 5) {
        this.cArray.push('Coral ');
      } else if (randNum === 6) {
        this.cArray.push('CornflowerBlue');
      } else if (randNum === 7) {
        this.cArray.push('Cornsilk');
      }
    }
  }
  ngOnInit() {
    this.fillcArray();
  }
}
