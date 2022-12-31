package class_;

//클래스의 구성요소: 필드, 생성자, 메소드
public class Student {

    //필드(Field)
    String name; //이름
    int age; //나이
    int korean_score; //국어성적
    int math_score; //수학성적
    int english_score; //영어성적

    //생성자(Constructor)
    Student(String name, int age, int korean_score, int math_score, int english_score) {
        this.name = name;
        this.age = age;
        this.korean_score = korean_score;
        this.math_score = math_score;
        this.english_score = english_score;
    }

    //메소드(Method)
    public void printScore() {
        System.out.println("이름 : " + name);
        System.out.println("나이 : " + age);
        System.out.println("국어성적 : " + korean_score);
        System.out.println("수학성적 : " + math_score);
        System.out.println("영어성적 : " + english_score);
    }

    public static void main(String[] args) {
        Student student2 = new Student("홍길동", 18, 100, 90, 80);
        student2.printScore();
    }

}








