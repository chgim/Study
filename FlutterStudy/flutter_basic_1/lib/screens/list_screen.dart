import 'package:flutter/material.dart';
import 'package:flutter_basic_1/models/book.dart';
import 'package:flutter_basic_1/repositories/book_repository.dart';
import 'package:flutter_basic_1/screens/detail_screen.dart';

// 도서 목록 화면을 담당하는 StatelessWidget
class ListScreen extends StatelessWidget {
  // 도서 목록을 가져옴
  final List<Book> books = BookRepository().getBooks();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('도서 목록 앱'),
      ),
      body: ListView.builder(
        itemCount: books.length,
        itemBuilder: (context, index) {
          // 각 도서 항목을 표시하는 BookTile 위젯 생성
          return BookTile(book: books[index]);
        },
      ),
    );
  }
}

// 각 도서 항목을 표시하는 ListTile을 담당하는 StatelessWidget
class BookTile extends StatelessWidget {
  final Book book;

  // 생성자를 통해 book을 전달받음
  BookTile({required this.book});

  @override
  Widget build(BuildContext context) {
    return ListTile(
      title: Text(book.title),
      leading: Image.network(book.image),
      onTap: () {
        // 해당 도서를 눌렀을 때 DetailScreen으로 이동
        Navigator.of(context).push(MaterialPageRoute(
          builder: (context) => DetailScreen(
            book: book,
          ),
        ));
      },
    );
  }
}
