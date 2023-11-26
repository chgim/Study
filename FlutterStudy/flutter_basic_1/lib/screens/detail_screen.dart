import 'package:flutter/material.dart';
import 'package:flutter_basic_1/models/book.dart';

class DetailScreen extends StatelessWidget {
  final Book book;

  // 생성자를 통해 해당 화면에서 표시할 도서 정보를 받음
  DetailScreen({required this.book});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      // 상단 앱바에 도서 제목을 표시
      appBar: AppBar(
        title: Text(book.title),
      ),
      body: Container(
        child: Column(
          children: [
            // 도서의 이미지를 네트워크에서 가져와 표시
            Image.network(book.image),

            // 조금의 여백을 주기 위한 Padding 위젯
            Padding(
              padding: EdgeInsets.all(3),
            ),

            // 도서 정보를 표시하는 부분
            Row(
              crossAxisAlignment: CrossAxisAlignment.start,
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                // 도서 제목과 부제목을 나타내는 컬럼
                Container(
                  width: MediaQuery.of(context).size.width * 0.8,
                  padding: EdgeInsets.all(10),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      // 도서 제목
                      Container(
                        child: Text(
                          book.title,
                          style: TextStyle(
                              fontSize: 23, fontWeight: FontWeight.bold),
                        ),
                      ),
                      // 도서 부제목
                      Text(
                        book.subtitle,
                        style: TextStyle(fontSize: 18, color: Colors.grey),
                      ),
                    ],
                  ),
                ),

                // 오른쪽에 별 모양의 아이콘을 표시하는 컬럼
                Container(
                  width: MediaQuery.of(context).size.width * 0.15,
                  padding: EdgeInsets.all(10),
                  child: Center(
                    child: Icon(
                      Icons.star,
                      color: Colors.red,
                    ),
                  ),
                )
              ],
            ),

            // 각 아이콘 및 텍스트를 나타내는 부분
            Padding(
              padding: EdgeInsets.all(3),
            ),
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceAround,
              children: [
                // "Contact" 아이콘과 텍스트
                Column(
                  children: [
                    Icon(
                      Icons.call,
                      color: Colors.blue,
                    ),
                    Text(
                      'Contact',
                      style: TextStyle(color: Colors.blue),
                    )
                  ],
                ),

                // "Route" 아이콘과 텍스트
                Column(
                  children: [
                    Icon(
                      Icons.near_me,
                      color: Colors.blue,
                    ),
                    Text(
                      'Route',
                      style: TextStyle(color: Colors.blue),
                    )
                  ],
                ),

                // "Save" 아이콘과 텍스트
                Column(
                  children: [
                    Icon(
                      Icons.save,
                      color: Colors.blue,
                    ),
                    Text(
                      'Save',
                      style: TextStyle(color: Colors.blue),
                    )
                  ],
                ),
              ],
            ),

            // 도서의 상세 설명을 표시하는 컨테이너
            Container(
              padding: EdgeInsets.all(15),
              child: Text(book.description),
            )
          ],
        ),
      ),
    );
  }
}
