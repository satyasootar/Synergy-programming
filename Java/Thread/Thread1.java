class A extends Thread{
    public void run(){
        System.out.println("Task 1 executing........");
    }
}

class B extends Thread{
    public void run(){
            System.out.println("Task 2 executing........");
    }
}
class C extends Thread{
    public void run(){
            System.out.println("Task 3 executing........");
    }
}

public class Thread1 {
    public static void main(String[] args) {
        A t1 = new A();
        B t2 = new B();
        C t3 = new C();

        t1.start();
        t2.start();
        t3.start();

    }
}

// OUTPUT
// Task 1 executing........
// Task 3 executing........
// Task 2 executing........