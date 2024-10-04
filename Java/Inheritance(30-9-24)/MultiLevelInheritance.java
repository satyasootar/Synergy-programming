// Base class
class Grandpa {
    public void displayGrandpa() {
        System.out.println("This is Grandpa.");
    }
}

// Intermediate class that inherits from Grandpa
class Pa extends Grandpa {
    public void displayPa() {
        System.out.println("This is Pa.");
    }
}

// Derived class that inherits from Pa
class Son extends Pa {
    public void displaySon() {
        System.out.println("This is Son.");
    }
}

// Main class to demonstrate multi-level inheritance
public class MultiLevelInheritance {
    public static void main(String[] args) {
        Son son = new Son();

        // Calling methods from each class
        son.displayGrandpa(); // From Grandpa
        son.displayPa();      // From Pa
        son.displaySon();     // From Son
    }
}


// output
// This is Grandpa.
// This is Pa.
// This is Son.