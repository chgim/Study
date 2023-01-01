package static_;




public class StaticExam {
    public static void main(String[] args) {
        Number number1 = new Number(); //첫번째 number
        Number number2 = new Number(); //두번쨰 number

        number1.num++; //클래스 필드 num을 1증가시킴
        number1.num2++; //인스턴스 필드 num을 1증가시킴
        System.out.println(number2.num); //두번째 number의 클래스 필드 출력
        System.out.println(number2.num2); //두번째 number의 인스턴스 필드 출력
    }
}
//인스턴스 변수는 인스턴스가 생성될 때마다 생성되므로 인스턴스마다 각기 다른 값
//정적 변수는 모든 인스턴스가 하나의 저장공간을 공유하기에 항상 같은 값