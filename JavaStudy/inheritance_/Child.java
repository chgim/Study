package inheritance_;

public class Child  extends  Parent{

        public int c=30;// public 필드

        void display(){
//          System.out.println(a); 상속받은 private 필드 참조. a는 private 로 선언. 접근불가
            System.out.println(b);// 상속받은 public 필드 참조
            System.out.println(c);// 자식 클래스에서 선언한 public 필드 참조
        }

    public static void main(String[] args) {
        Child ch=new Child();
        ch.display();
    }

}
