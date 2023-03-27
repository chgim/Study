package collection_;

import java.util.HashSet;
import java.util.Set;

public class HashSetExam2 {
    public static void main(String[] args) {
        Set h=new HashSet();
        h.add(2);
        System.out.println(h);
        h.add(1);
        System.out.println(h);
        h.add(1);
        System.out.println(h);
        h.remove(1);
        System.out.println(h);
        System.out.println(h.size());
    }
}
