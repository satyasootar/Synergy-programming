class X extends Thread{
    public void run(){
        try {
            for(int i = 1; i<=5; i++){
                System.out.println("Child Thread :" + i);
                Thread.sleep(2000);
            }
            System.out.println("Child thread ends");
        } catch (Exception e) {
            System.out.println("child thread interrupted");
        }
    }
}


public class Thread3 {
    public static void main(String[] args) {
        X t = new X();
        t.start();

        try {
            for(int i = 1 ; i<= 5; i++){
                System.out.println("Main thread: "+ i);
                Thread.sleep(3000);
            }
            System.out.println("Main thread ends");
        } catch (Exception e) {
            System.out.println("Main thread interrupted");
        }
    }
}


// OUTPUT
// Main thread: 1
// Child Thread :1
// Child Thread :2
// Main thread: 2
// Child Thread :3
// Main thread: 3
// Child Thread :4
// Child Thread :5
// Main thread: 4
// Child thread ends
// Main thread: 5
// Main thread ends