package polymorphism;

public class PolyTest {
    public static void main(String[] args) {
        Parent p=new Child();
        Child c=new Child();

        System.out.println("p.x="+p.x);
        p.method();
        System.out.println("c.x="+c.x);
        c.method();
    }
}
//다형성(polymorphism)이란 하나의 객체가 여러 가지 타입을 가질 수 있는 것을 의미.
//참조변수 p와 c의 타입은 서로 다르지만 두 개의 참조변수 모두 Child 인스턴스를 참조하고 있다.
// 그리고 Parent, Child 클래스는 서로 같은 멤버들을 정의하고 있다. 이 때 부모타입의 참조변수 p와 자식타입의 참조변수 c에서 Child 인스턴스의 멤버들을 사용하는데 차이가 있다는 걸 알 수 있다.

//메소드인 method()의 경우 참조변수의 타입에 관계없이 항상 실제 인스턴스의 타입인 Child 클래스에 정의된 메소드가 호출되지만 인스턴스 변수인 x는 참조변수의 타입에 따라서 달라진다.
//만약 Child 클래스에 아무런 멤버도 정의되어 있지 않다면 부모로부터 멤버들을 상속받아 사용한다.
//참조변수의 타입에 따라 결과가 달라지는 경우는 부모 클래스의 멤버변수와 같은 이름의 멤버변수를 자식 클래스에서 중복해서 정의한 경우 뿐이다.