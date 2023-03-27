package collection_;

import java.util.ArrayList;
import java.util.List;

public class ArrayListExam3 {
    public static void main(String[] args) {
        List a=new ArrayList();
        a.add(2);
        System.out.println(a);
        a.add(1);
        System.out.println(a);
        a.add(1);
        System.out.println(a);
        a.add(1,3);
        System.out.println(a);
        a.remove(2);
        System.out.println(a);
        System.out.println(a.get(2));
        System.out.println(a.size());

    }
}
