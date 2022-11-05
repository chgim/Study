package hello2.core;

import lombok.Getter;
import lombok.Setter;
import lombok.ToString;

@Getter
@Setter
@ToString
public class HelloLombok {

    private String Name;
    private int age;

    public static void main(String[] args) {
        HelloLombok helloLombok=new HelloLombok();
        helloLombok.setName("asd00");

        String name= helloLombok.getName();
        System.out.println("name=" +name);
        System.out.println("helloLombok="+helloLombok);
    }
}
