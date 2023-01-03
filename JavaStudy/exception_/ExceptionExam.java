package exception_;


import java.io.IOException;

public class ExceptionExam {
    public static void main(String[] args)  {

        byte[] list = {'a', 'b', 'c'};

        try {

            System.out.write(list);

        } catch (IOException e){

            e.printStackTrace();

        } catch (Exception e) {

            e.printStackTrace();

        }

    }
}//범위가 더 좁은 예외를 처리하는 catch 블록을 먼저 명시하고, 범위가 더 넓은 예외를 처리하는 catch 블록은 나중에 명시해야만 정상적으로 해당 예외를 처리할 수 있습니다.
