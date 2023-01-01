package super_;

public class Child1 extends Parent1 {
    void display() {

        System.out.println(a);

        System.out.println(this.a);

        System.out.println(super.a);

    }


    public static void main(String[] args) {
        Child1 ch = new Child1();

        ch.display();
    }
}
// int형 변수 num는 부모 클래스인 Parent 클래스에서만 선언되어 있습니다.
//따라서 지역 변수와 this 참조 변수 그리고 super 참조 변수 모두 같은 값을 출력합니다.
