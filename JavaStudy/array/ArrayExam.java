package array;

public class ArrayExam {
    public static void main(String[] args) {
        int[] grade1 = new int[3];
        int[] grade2 = new int[3];

        grade1[0] = 85;
        grade1[1] = 65;
        grade1[2] = 90;

        grade2[0] = 85;

        for (int i = 0; i < grade1.length; i++) {

            System.out.print(grade1[i] + " "); // 인덱스를 이용한 배열로의 접근

        }


        for (int i = 0; i < grade2.length; i++) {

            System.out.print(grade2[i] + " "); // 인덱스를 이용한 배열로의 접근

        }
    }
}
