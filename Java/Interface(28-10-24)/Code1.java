//WAP to create an interface "Rate". Implements classes from it to show to the intrest rate of different bank as per your choice.

import java.util.*;

interface Rate {
    float RINT();
}

class SBI implements Rate{
    public float RINT(){
        return (3.0f);
    }
}

class RBI implements Rate{
    public float RINT(){
        return (3.5f);
    }
}

class IOB implements Rate{
    public float RINT(){
        return (3.9f);
    }
}

class Code1{
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter BANK name \n1.SBI\n2.RBI\n3.IOB");
        String bn = sc.nextLine();

        Rate bank;

        if (bn.equalsIgnoreCase("RBI")){
            bank = new RBI();
            System.out.println("Intrest rate is = "+ bank.RINT());
        }else if(bn.equalsIgnoreCase("SBI")) {
            bank = new SBI();
            System.out.println("Intrest rate is = "+ bank.RINT());
        }else if(bn.equalsIgnoreCase("IOB")){
            bank = new IOB();
            System.out.println("Intrest rate is = "+ bank.RINT());
        }else{
            System.out.println("Not Available");
        }
    }
}

// OUTPUT
// Enter BANK name 
// 1.SBI
// 2.RBI
// 3.IOB
// SBI
// Intrest rate is = 3.0