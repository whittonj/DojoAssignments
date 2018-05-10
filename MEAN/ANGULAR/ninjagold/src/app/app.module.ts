import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { NinjaService } from './services/ninja.service';

//Get components
//import { BookListComponent } from './books/book-list/book-list.component';
//import { BookNewComponent } from './books/book-new/book-new.component';
//import { BookDetailComponent } from './books/book-detail/book-detail.component';

//get pipes
//import { TitleizePipe } from './titleize.pipe';
//import { SearchPipe } from './search.pipe';

//Get services
//import { BookService } from './services/book.service';

//Get apps (auto)
import { AppComponent } from './app.component';
import { BuildingComponent } from './ninja/building/building.component';
import { LogComponent } from './ninja/log/log.component';
import { GoldComponent } from './ninja/gold/gold.component';


@NgModule({
  declarations: [
    AppComponent,
    BuildingComponent,
    LogComponent,
    GoldComponent
    //add pipes
  ],
  imports: [
    BrowserModule, FormsModule, HttpClientModule
  ],
  //add services to providers
  providers: [NinjaService],
  bootstrap: [AppComponent]
})
export class AppModule { }
