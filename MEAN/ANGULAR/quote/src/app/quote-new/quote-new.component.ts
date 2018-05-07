import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-quote-new',
  templateUrl: './quote-new.component.html',
  styleUrls: ['./quote-new.component.css']
})
export class QuoteNewComponent implements OnInit {
  @Input() quotes;
  @Output() createQuoteEvent = new EventEmitter();

  newQuote = { body: '', author: '', rating: 0 };

  constructor() { }

  ngOnInit() {
  }

  onSubmit(formData) {
    console.log(formData)
    console.log(this.newQuote);
    this.createQuoteEvent.emit(this.newQuote);
    this.newQuote = { body: '', author: '', rating: 0 };
  }

}
