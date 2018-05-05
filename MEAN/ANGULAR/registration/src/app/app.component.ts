import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';
import { User } from './user';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title = 'Registration';
  user = new User();
  users = [];

  constructor() { }

  ngOnInit() {
  }

  onSubmit() {
    console.log(this.user);
    this.users.push(this.user);
    console.log(this.users);
    this.user = new User();
  }
}
