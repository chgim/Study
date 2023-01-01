package interface_;

public class InterTest {
    public static void main(String[] args) {
        Cat c = new Cat();

        Dog d = new Dog();



        c.cry();

        c.play();

        d.cry();

        d.play();
    }
}
//자바에서는 클래스를 이용한 다중상속을 지원하지 않음.
//인터페이스를 통해 다중상속.
//인터페이스(interface)란 다른 클래스를 작성할 때 기본이 되는 틀을 제공하면서, 다른 클래스 사이의 중간 매개 역할까지 담당하는 일종의 추상 클래스를 의미