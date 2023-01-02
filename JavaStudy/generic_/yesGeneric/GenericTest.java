package generic_.yesGeneric;


public class GenericTest {
    public static void main(String[] args) {
        GenericPrinter<Powder> powderPrinter = new GenericPrinter<Powder>();
        powderPrinter.setMaterial(new Powder());
        Powder powder=powderPrinter.getMaterial();//명시적 형변환 x
        System.out.println(powderPrinter);
        powderPrinter.printing();

        GenericPrinter<Plastic> plasticPrinter = new GenericPrinter<Plastic>();
        plasticPrinter.setMaterial(new Plastic());
        Plastic plastic=plasticPrinter.getMaterial();//명시적 형변환 x
        System.out.println(plasticPrinter);
        plasticPrinter.printing();

    }
}
