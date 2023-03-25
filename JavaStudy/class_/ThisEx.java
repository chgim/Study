package class_;

public class ThisEx {
    private int a;
    public void setA(int a){
        this.a=a;
    }
    public int getA(){
        return a;
    }

    public static void main(String[] args) {
        ThisEx soo=new ThisEx();
        soo.setA(5);
        System.out.println(soo.getA());
    }
}
