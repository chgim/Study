package generic_.noGeneric;

import generic_.noGeneric.Powder;
import generic_.noGeneric.ThreeDPrinter;

public class ObjectTest {
    public static void main(String[] args) {
        ThreeDPrinter printer=new ThreeDPrinter();

        Powder p1=new Powder();
        printer.setMaterial(p1);

        Powder p2=(Powder) printer.getMaterial();
    }
}
//어떤 변수가 여러 참조 자료형을 사용할 수 있도록 Object 클래스를 사용하면 다시 원래 자료형으로 반환해주기 위해 매번 형 변환을 해야함.
