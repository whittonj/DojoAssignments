import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';


import { AppComponent } from './app.component';
import { AlphaComponent } from './alpha/alpha.component';
import { BetaComponent } from './beta/beta.component';
import { SumComponent } from './sum/sum.component';

import { DataService } from './data.service';


@NgModule({
  declarations: [
    AppComponent,
    AlphaComponent,
    BetaComponent,
    SumComponent
  ],
  imports: [
    BrowserModule
  ],
  providers: [DataService],
  bootstrap: [AppComponent]
})
export class AppModule { }
