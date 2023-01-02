package wrapper_;

public class WrapperExam {
    public static void main(String[] args) {
        String str = "10";
        String str2 = "10.5";
        String str3 = "true";

        byte b = Byte.parseByte(str);
        int i = Integer.parseInt(str);
        short s = Short.parseShort(str);
        long l = Long.parseLong(str);
        float f = Float.parseFloat(str2);
        double d = Double.parseDouble(str2);
        boolean bool = Boolean.parseBoolean(str3);

        System.out.println("문자열 byte값 변환 : "+b);
        System.out.println("문자열 int값 변환 : "+i);
        System.out.println("문자열 short값 변환 : "+s);
        System.out.println("문자열 long값 변환 : "+l);
        System.out.println("문자열 float값 변환 : "+f);
        System.out.println("문자열 double값 변환 : "+d);
        System.out.println("문자열 boolean값 변환 : "+bool);
    }
}
