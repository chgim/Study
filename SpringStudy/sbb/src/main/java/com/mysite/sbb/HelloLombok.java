package com.mysite.sbb;

//import lombok.Getter;
//import lombok.Setter;
//
//@Getter
//@Setter
//public class HelloLombok { //롬복으로 컴파일된 클래스에는 Getter와 Setter 메서드가 실제로 포함된다.
//
//    private String hello;
//    private int lombok;
//
//    public static void main(String[] args) {
//        HelloLombok helloLombok = new HelloLombok();
//        helloLombok.setHello("헬로");
//        helloLombok.setLombok(5);
//
//        System.out.println(helloLombok.getHello());
//        System.out.println(helloLombok.getLombok());
//    }
//}

import lombok.Getter;
import lombok.RequiredArgsConstructor;

@RequiredArgsConstructor
@Getter
//hello, lombok 속성에 final을 적용하고 롬복의 @RequiredArgsConstructor 애너테이션을 적용하면 해당 속성을 필요로하는 생성자가 롬복에 의해 자동으로 생성된다.
// (※ final이 없는 속성은 생성자에 포함되지 않는다.)
public class HelloLombok {

    private final String hello;
    private final int lombok;

//    public HelloLombok(String hello, int lombok) {
//        this.hello = hello;
//        this.lombok = lombok;
//    }
    public static void main(String[] args) {
        HelloLombok helloLombok = new HelloLombok("헬로", 5);
        System.out.println(helloLombok.getHello());
        System.out.println(helloLombok.getLombok());
    }
}