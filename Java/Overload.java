//wap to overload a constructor complex to add two complex number


public class Overload {
    int real;
    int img;

    public Overload(){
        real= 5;
        img = 7;
    }
    public Overload(int r){
        real =r;
        img = 10;
    }
    public Overload(int r , int i){
        real =r;
        img = i;

    }
    public void show(){
        System.out.println(real+"i"+img);
    }

    public static void main(String[] args) {
        Overload A = new Overload();
        Overload b = new Overload(7);
        Overload c = new Overload(2,3);
        A.show();
        b.show();
        c.show();
    } 
}

// OUTPUT
// 5i7
// 7i10
// 2i3