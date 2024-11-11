//WAP to show ArithmeticException

class ArithmaticError{
    void divide(int a , int b){
        try {
            System.out.println("The result is "+ a/b);
        } catch (ArithmeticException e) {
            System.out.println("Error: " + e);
        }
    }

    public static void main(String[] args) {
        ArithmaticError d = new ArithmaticError();
        d.divide(40,20);
        d.divide(10, 0);
    }
}

// OUTPUT
// The result is 2
// Error: java.lang.ArithmeticException: / by zero