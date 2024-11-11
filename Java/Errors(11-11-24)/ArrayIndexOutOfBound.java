//WAP to show ArrayIndexOutOfBoundsException

public class ArrayIndexOutOfBound {
    public static void main(String[] args) {
        int a[] = new int[10];
        try {
            a[20] = 7;
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Error: "+e);
        }
   }
}


// OUTPUT
// Error: java.lang.ArrayIndexOutOfBoundsException: Index 20 out of bounds for length 10