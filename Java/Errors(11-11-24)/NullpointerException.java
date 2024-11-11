//WAP to show NullPointerException

public class NullpointerException {
    public static void main(String[] args) {
        String a =  null;
        try {
            System.out.println("Length of the string is: " + a.length());
        } catch (NullPointerException e) {
            System.out.println("Error: "+ e);
        }

    }
}


// OUTPUT
// Error: java.lang.NullPointerException