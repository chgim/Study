package collection_;

import java.util.LinkedList;

public class LinkedListExam {
    public static void main(String[] args) {
        LinkedList<String> lnkList = new LinkedList<String>();



// add() 메소드를 이용한 요소의 저장

        lnkList.add("넷");

        lnkList.add("둘");

        lnkList.add("셋");

        lnkList.add("하나");



// for 문과 get() 메소드를 이용한 요소의 출력

        for (int i = 0; i < lnkList.size(); i++) {

            System.out.print(lnkList.get(i) + " ");

        }



// remove() 메소드를 이용한 요소의 제거

        lnkList.remove(1);



// Enhanced for 문과 get() 메소드를 이용한 요소의 출력

        for (String e : lnkList) {

            System.out.print(e + " ");

        }



// set() 메소드를 이용한 요소의 변경

        lnkList.set(2, "둘");



        for (String e : lnkList) {

            System.out.print(e + " ");

        }



// size() 메소드를 이용한 요소의 총 개수

        System.out.println("리스트의 크기 : " + lnkList.size());
    }
}
//배열은 저장된 요소가 순차적으로 저장된다.
//하지만 연결 리스트는 저장된 요소가 비순차적으로 분포되며, 이러한 요소들 사이를 링크(link)로 연결하여 구성한다.
//다음 요소를 가리키는 참조만을 가지는 연결 리스트를 단일 연결 리스트(singly linked list)라고 한다.
// 이전 요소를 가리키는 참조도 가지는 이중 연결 리스트가 있다.