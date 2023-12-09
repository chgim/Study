import 'package:flutter/material.dart';
import 'package:fluttertoast/fluttertoast.dart';
import 'package:sprintf/sprintf.dart';

// 초를 MM:SS 형식의 문자열로 변환하는 함수
String secondsToString(int seconds) {
  return sprintf("%02d:%02d", [seconds ~/ 60, seconds % 60]);
}

// 화면 하단에 토스트 메시지를 표시하는 함수
void showToast(String message) {
  Fluttertoast.showToast(
    msg: message,
    toastLength: Toast.LENGTH_LONG,
    gravity: ToastGravity.BOTTOM,
    timeInSecForIosWeb: 5,
    backgroundColor: Colors.grey,
    textColor: Colors.white,
    fontSize: 16.0,
  );
}
