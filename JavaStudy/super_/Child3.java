package super_;

public class Child3 extends Parent2{
    public void product() {
        System.out.println("상품의 가격은 10만원이 아니고, 30만원 입니다.");
        super.product();
    }
    public static void main(String[] args){
        Parent2 p = new Parent2();
        Child3 c = new Child3();
        p.product();//부모
        System.out.println("=====================");
        c.product();//자식
    }
}
