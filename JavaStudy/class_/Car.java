package class_;

public class Car {

    public void accelerate(float speed, float second){
        System.out.println(second + "초간 속도를 시속 " + speed + "(으)로 가속함!!");
    }


    public static void main(String[] args) {
        Car myCar = new Car();   // 객체 생성
        myCar.accelerate(60.5f, 3.2f); // 메소드 호출
    }
}
