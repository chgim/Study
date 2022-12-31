package array_;

public class ArrayExam3 {
    public static void main(String[] args) {
        int[] grade = new int[]{85, 65, 90};

        int sum = 0;



        for (int i = 0; i < grade.length; i++) {

            sum += grade[i];

        }

        System.out.println("모든 과목에서 받은 점수의 합은 " + sum + "입니다.");

        System.out.println("이 학생의 평균은 " + (sum / grade.length) + "입니다.");
    }
}
