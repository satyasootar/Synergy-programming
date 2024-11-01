//WAP to implements multiple inheritance through interface
import java.util.*;
interface Rate{
    double r = 12;
}
interface SI{
    double simpleIntrest();
}

class Calculate implements Rate, SI {
    double p , t;
    public Calculate (double p, double t){
        this.p = p;
        this.t = t;
    }
    public double simpleIntrest(){
        return ((p*t*r)/100);
    }
}

public class Code2 {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        System.out.println("Enter Principal and time");
        double p = s.nextDouble();
        double t = s.nextDouble();

        Calculate obj = new Calculate(p, t);
        System.out.println("The simple intrest ="+ obj.simpleIntrest());
    }   
}

// OUTPUT
// Enter Principal and time
// 2000 4
// The simple intrest =960.0
