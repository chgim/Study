package abstract_;

public class PolyTest {
    public static void main(String[] args) {
        // Animal a = new Animal(); // 추상 클래스는 인스턴스를 생성할 수 없음.

        Cat c = new Cat();

        Dog d = new Dog();

        c.cry();

        d.cry();
    }
}
//Animal 클래스를 상속받는 자식 클래스인 Dog 클래스와 Cat 클래스는 cry() 메소드를 오버라이딩해야만 비로소 인스턴스를 생성할 수 있습니다.
//자바에서 추상 메소드를 선언하여 사용하는 목적은 추상 메소드가 포함된 클래스를 상속받는 자식 클래스가 반드시 추상 메소드를 구현하도록 하기 위함