//WAP to show StringIndexOutOfBoundsException

public class StringIndexOutOfBound {
    public static void main(String[] args) {
        String s = "satya";

        try {
            char c = s.charAt(10);
            System.out.println(c);
        } catch (StringIndexOutOfBoundsException e) {
            System.out.println("Error: "+ e);
        }
    }
}


// OUTPUT
// Error: java.lang.StringIndexOutOfBoundsException: String index out of range: 10