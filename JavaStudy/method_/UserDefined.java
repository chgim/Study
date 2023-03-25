package method_;

public class UserDefined {
    static char fn(int num){
        if(num%2==0)
            return 'Y';
        else
            return 'N';
    }
    public static void main(String[] args) {
        char a=fn(5);
        System.out.println(a);
    }
}
