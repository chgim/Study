package collection_;

import java.util.Iterator;
import java.util.LinkedList;

public class IteratorExam {
    public static void main(String[] args) {
        LinkedList<Integer> lnkList = new LinkedList<Integer>();



        lnkList.add(4);

        lnkList.add(2);

        lnkList.add(3);

        lnkList.add(1);



        Iterator<Integer> iter = lnkList.iterator();

        while (iter.hasNext()) {//해당 이터레이션(iteration)이 다음 요소를 가지고 있으면 true 를 반환하고, 더 이상 다음 요소를 가지고 있지 않으면 false 를 반환함.


            System.out.print(iter.next() + " "); //이터레이션(iteration)의 다음 요소를 반환함.

        }
    }
}
