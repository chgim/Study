package class_;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Soojebi2 {
    public static void main(String[] args) throws IOException {
        String a=null;
        BufferedReader r= new BufferedReader((new InputStreamReader(System.in)));
        a= r.readLine();
        System.out.println(a);
    }
} //readLine은 입력장치로부터 한개의 문자를 읽는 함수 라인 전체를 읽는 표준 입력 함수
