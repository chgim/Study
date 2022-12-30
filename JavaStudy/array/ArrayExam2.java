package array;

public class ArrayExam2 {
    public static void main(String[] args) {
        int[] grade1 = {70, 80, 90};
        int[] grade2 = new int[]{50, 40, 30};
        int[] grade3;
        grade3 = new int[]{10, 20, 30};

        for (int i = 0; i < grade1.length; i++) {

            System.out.print(grade1[i] + " "); // 인덱스를 이용한 배열로의 접근

        }

        for (int i = 0; i < grade2.length; i++) {

            System.out.print(grade2[i] + " "); // 인덱스를 이용한 배열로의 접근

        }

        for (int i = 0; i < grade3.length; i++) {

            System.out.print(grade2[i] + " "); // 인덱스를 이용한 배열로의 접근

        }
    }
}
