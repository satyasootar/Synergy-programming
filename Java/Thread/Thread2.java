class X extends Thread {
    @Override
    public void run() {
        for (int i = 1; i <= 3; i++) {
            System.out.println("Child Thread");
        }
    }
}

public class Thread2 {
    public static void main(String[] args) {
        X t = new X();
        t.start();

        try {
            t.join(); 
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

    
        for (int i = 1; i <= 3; i++) {
            System.out.println("Main thread");
        }
    }
}


// OUTPUT
// Child Thread
// Child Thread
// Child Thread
// Main thread
// Main thread
// Main thread