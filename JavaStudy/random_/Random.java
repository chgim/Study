package random_;

public class Random {
    public static void main(String[] args) {

        System.out.println((int) (Math.random() * 100)); // 0 ~ 99
        System.out.println((int) (Math.random() * 6));       // 0 ~ 5
        System.out.println((int) (Math.random() * 6) + 1); // 1 ~ 6
        System.out.println((int) (Math.random() * 6) + 3); // 3 ~ 8


    }


}
