package collection_;

import java.util.LinkedList;

public class DequeExam {
    public static void main(String[] args) {
        LinkedList<String> qu = new LinkedList<String>(); // 큐의 생성

//Deque<String> qu = new ArrayDeque<String>();



// add() 메소드를 이용한 요소의 저장

        qu.add("넷");//해당 큐의 맨 뒤에 전달된 요소를 삽입함.

        qu.add("둘");

        qu.add("셋");

        qu.add("하나");



// peek() 메소드를 이용한 요소의 반환

        System.out.println(qu.peek());
        //해당 큐의 맨 앞에 있는(제일 먼저 저장된) 요소를 반환함.
        //
        //만약 큐가 비어있으면 null 을 반환함.

        System.out.println(qu);



// poll() 메소드를 이용한 요소의 반환 및 제거

        System.out.println(qu.poll());
        //해당 큐의 맨 앞에 있는(제일 먼저 저장된) 요소를 반환하고, 해당 요소를 큐에서 제거함.
        //
        //만약 큐가 비어있으면 null 을 반환함.

        System.out.println(qu);



// remove() 메소드를 이용한 요소의 제거

        qu.remove("하나");//해당 큐의 맨 앞에 있는(제일 먼저 저장된) 요소를 제거함.

        System.out.println(qu);
    }
}
