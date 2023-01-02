package generic_.yesGeneric;

public class GenericPrinter<T extends Material> { //extends 로 사용할 수 있는 자료형에 제한을 둠
    private T material;

    public T getMaterial() {
        return material;
    }

    public void setMaterial(T material) {
        this.material = material;
    }

    public String toString(){
        return material.toString();
    }

    public void printing(){
        material.doPrinting();
    }
}
//제네릭은 클래스나 메소드에서 사용할 내부 데이터 타입을 컴파일 시에 미리 지정하는 방법입니다.