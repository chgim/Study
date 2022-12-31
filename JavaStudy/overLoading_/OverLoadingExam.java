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
