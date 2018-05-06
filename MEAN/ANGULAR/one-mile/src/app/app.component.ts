import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = "One Mile";
  oneMile = 1;
  lastUnit = null;
  distance = 1;

  getDistance(unit) {
    this.distance = 0;
    if (unit === 'Feet') {
      console.log("It's the feet");
      this.distance = 5280;
    }
    else if (unit === 'Inches') {
      this.distance = 63360;
    }
    else if (unit === 'Kms') {
      this.distance = 1.60934;
    }
    else if (unit === 'Meters') {
      this.distance = 1609.33999997549;
    }
    else if (unit === 'Clear') {
      this.distance = null;
    }
    this.lastUnit = unit;
  }
