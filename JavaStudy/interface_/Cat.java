package interface_;

public class Cat implements Animal,Pet{ //인터페이스를 사용한 다중상속.
    public void cry() {

        System.out.println("냐옹냐옹!");

    }
    public void play() {

        System.out.println("쥐 잡기 놀이하자~!");

    }
}
