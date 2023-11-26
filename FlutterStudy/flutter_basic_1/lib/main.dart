import 'package:flutter/material.dart';
import 'package:flutter_basic_1/screens/list_screen.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Book List App',
      home: ListScreen(),
    );
  }
}
