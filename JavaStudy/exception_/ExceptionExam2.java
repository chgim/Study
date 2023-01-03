package exception_;


public class ExceptionExam2 {

    static void handlingException() throws Exception { throw new Exception(); }

    public static void main(String[] args) {
        try {

            handlingException();

        } catch (Exception e) {

            System.out.println("main() 메소드에서 예외가 처리됨!");

        }
    }
}
//호출된 메소드에서 발생한 예외를 해당 메소드를 호출한 main() 메소드에서 처리

