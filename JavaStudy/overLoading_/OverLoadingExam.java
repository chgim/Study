package overLoading_;

public class OverLoadingExam {
    static void display(int num1) {
        System.out.println(num1);
    }

    static void display(int num1, int num2) {
        System.out.println(num1 * num2);
    }

    static void display(int num1, double num2) {
        System.out.println(num1 + num2);
    }

    public static void main(String[] args) {
        OverLoadingExam ovl = new OverLoadingExam();

        ovl.display(10);

        ovl.display(10, 20);

        ovl.display(10, 3.14);

        ovl.display(10, 'a');
    }
}
//메소드 오버로딩(overloading)이란 같은 이름의 메소드를 중복하여 정의하는 것을 의미합니다.
//오버로딩의 조건
//1. 메소드의 이름이 같아야 합니다.
//2. 메소드의 시그니처, 즉 매개변수의 개수 또는 타입이 달라야 합니다.