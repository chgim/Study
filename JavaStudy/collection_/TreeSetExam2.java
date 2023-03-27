package collection_;

import java.util.TreeSet;

public class TreeSetExam2 {
    public static void main(String[] args) {
        TreeSet set=new TreeSet();
        set.add(89);
        set.add(32);
        set.add(71);
        set.add(50);
        System.out.println("50 미만의 값:"+ set.headSet(50)); //headSet: 미만
        System.out.println("50 이상의 값:"+ set.tailSet(50)); //tailSet: 이상
    }
}
