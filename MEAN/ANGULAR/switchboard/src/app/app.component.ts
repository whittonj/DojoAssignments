import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent {
  title = 'Switchboard';
  buttons = 10;

  switches = [true, true, true, true, true, true, true, true, true, true];
  changeSwitch(idx) {
    this.switches[idx] = !this.switches[idx];
  }
}


