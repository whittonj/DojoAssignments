import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Time Zone';
  datetime = new Date();
  lastTimeZoneSelected = null;

  getDateByZone(timezone) {
    this.datetime = new Date();
    if (timezone === 'MST') {
      this.datetime.setHours(this.datetime.getHours() + 1);
    } else if (timezone === 'CST') {
      this.datetime.setHours(this.datetime.getHours() + 2);
    } else if (timezone === 'EST') {
      this.datetime.setHours(this.datetime.getHours() + 3);
    }
    this.lastTimeZoneSelected = timezone;
  }

}
