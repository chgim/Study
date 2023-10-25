import 'package:flutter/material.dart';

class FirstScreen extends StatefulWidget {
  // StatefulWidget을 상속받는 FirstScreen 클래스 선언
  _FirstScreenState createState() => _FirstScreenState();
  // FirstScreen 클래스에 대한 상태를 관리하는 _FirstScreenState 클래스를 생성하고 반환
}

class _FirstScreenState extends State<FirstScreen> {
  // FirstScreen 클래스의 상태를 관리하는 _FirstScreenState 클래스 선언
  int count = 0;
  // 정수형 변수 count 선언, 초기값 0

  void increase() {
    setState(() {
      // 상태 변경을 알리는 함수 호출
      count = count + 1;
      // count 변수를 1 증가시킴
    });
  }

  void decrease() {
    setState(() {
      // 상태 변경을 알리는 함수 호출
      count = count - 1;
      // count 변수를 1 감소시킴
    });
  }

  @override
  Widget build(BuildContext context) {
    // 화면을 구성하는 UI를 생성하는 build 함수 재정의
    return Scaffold(
      // 기본적인 앱 구조를 생성하는 Scaffold 위젯
      appBar: AppBar(
        // 앱 바 설정
        title: Text('카운터 앱'),
        // 앱 바에 표시될 제목
      ),
      body: Center(
        // 화면 중앙에 UI를 배치하는 Center 위젯
        child: Column(
          // 세로로 여러 위젯을 배열하는 Column 위젯
          mainAxisAlignment: MainAxisAlignment.center,
          // 위젯들을 세로 방향으로 중앙에 정렬
          children: [
            // 자식 위젯 목록
            Text('카운트:$count', style: TextStyle(fontSize: 25)),
            // 현재 카운트 값을 표시하는 텍스트 위젯
            Padding(padding: EdgeInsets.all(20)),
            // 간격을 조절하기 위한 Padding 위젯
            Row(
              // 가로로 여러 위젯을 배열하는 Row 위젯
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              // 위젯들을 가로 방향으로 고르게 간격을 둠
              children: [
                // 자식 위젯들 목록
                ElevatedButton(onPressed: decrease, child: Text('- 감소')),
                // 클릭 시 decrease 함수 호출하는 버튼
                ElevatedButton(onPressed: increase, child: Text('+ 증가')),
                // 클릭 시 increase 함수 호출하는 버튼
              ],
            )
          ],
        ),
      ),
    );
  }
}
