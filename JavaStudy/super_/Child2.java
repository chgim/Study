package super_;

public class Child2 extends Parent1{
    int a = 20;
    void display() {

        System.out.println(a);

        System.out.println(this.a);

        System.out.println(super.a);

    }


    public static void main(String[] args) {
        Child2 ch = new Child2();

        ch.display();
    }
}
//int형 변수 num는 자식 클래스인 Child 클래스에서도 선언
//지역 변수와 this 참조 변수는 자식 클래스에서 대입된 값을 출력하며, super 참조 변수만이 부모 클래스에서 대입된 값을 출력