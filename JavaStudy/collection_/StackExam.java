package collection_;

import java.util.Stack;

public class StackExam {
    public static void main(String[] args) {
        Stack<Integer> st = new Stack<Integer>(); // 스택의 생성

//Deque<Integer> st = new ArrayDeque<Integer>();



// push() 메소드를 이용한 요소의 저장

        st.push(4);//해당 스택의 제일 상단에 전달된 요소를 삽입함.

        st.push(2);

        st.push(3);

        st.push(1);



// peek() 메소드를 이용한 요소의 반환

        System.out.println(st.peek());//해당 스택 제일 상단(마지막)의 요소 반환

        System.out.println(st);



// pop() 메소드를 이용한 요소의 반환 및 제거

        System.out.println(st.pop());//해당 스택의 제일 상단에 있는(제일 마지막으로 저장된) 요소를 반환하고, 해당 요소를 스택에서 제거함.

        System.out.println(st);



// search() 메소드를 이용한 요소의 위치 검색

        System.out.println(st.search(4));

        System.out.println(st.search(3));

        //해당 스택에서 전달된 객체가 존재하는 위치의 인덱스를 반환함.
        //이때 인덱스는 제일 상단에 있는(제일 마지막으로 저장된) 요소의 위치부터 0이 아닌 1부터 시작함.
    }
}
