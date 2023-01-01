package interface_;

public class Dog implements Animal, Pet{
    public void cry() {

        System.out.println("멍멍!");

    }
    public void play() {

        System.out.println("산책가자~!");

    }
}
