import { Component, OnInit, Input } from '@angular/core';
import { NgForm } from '@angular/forms';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  //proiders: [pipes, pipes]
})
export class AppComponent {
  title = 'Ninja Gold';
}

/*import { Component, OnInit, Input } from '@angular/core';

import { Book } from '../../book';

import { TitleizePipe } from '../../titleize.pipe';
import { BookService } from '../../services/book.service';

@Component({
  selector: 'app-book-list',
  templateUrl: './book-list.component.html',
  styleUrls: ['./book-list.component.css'],
  providers: [TitleizePipe]
})
export class BookListComponent implements OnInit {
  @Input()
  book: Book;
  selectedBook: Book;
  books: Array<Book> = [];
  filter: Book = new Book(false);

  constructor(
    private titleize: TitleizePipe,
    private bookService: BookService
  ) { }

  ngOnInit() {
    this.bookService.getBooks()
      .subscribe(books => {
        console.log(books);
        this.books = books;

        this.books.forEach(book => {
          book.author = this.titleize.transform(book.author);

        });
      });
  }

  selectBook(book: Book): void {
    console.log('Selecting book', book);
    this.selectedBook = this.selectedBook === book ? null : book;
  }

  onClick(event: Event) {
    event.stopPropagation();
  }

  onCreate(event: Book) {
    console.log('Creating book', event);
    this.books.push(event);
  }

  clearFilter(): void {
    this.filter = new Book(false);
  }

  onDelete(book: Book) {
    this.bookService.deleteBook(book).subscribe(returnedBook => {
      this.books = this.books.filter(b => b.id !== returnedBook.id);
    });
  }
}
*/
