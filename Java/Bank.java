import java.util.Scanner;

class Bank {
    String customerName;
    long accountNo;
    long balance;

    // Method to create the account
    void create(Scanner sc) {
        System.out.println("Enter the name:");
        customerName = sc.nextLine();
        System.out.println("Enter Account Number:");
        accountNo = sc.nextLong();
        sc.nextLine(); // Consume the remaining newline character
    }

    // Method to deposit money
    long deposit(Scanner sc) {
        System.out.println("Enter deposit amount:");
        long depositAmount = sc.nextLong();
        balance += depositAmount;
        return balance;
    }

    // Method to withdraw money
    void withdraw(Scanner sc) {
        System.out.println("Enter withdraw amount:");
        long withdrawAmount = sc.nextLong();
        if (withdrawAmount <= balance) {
            balance -= withdrawAmount;
            System.out.println("Withdrawal successful. Current balance: " + balance);
        } else {
            System.out.println("Insufficient balance. Withdrawal failed.");
        }
    }

    // Method to display account details
    void display() {
        System.out.println("Customer Name: " + customerName);
        System.out.println("Account Number: " + accountNo);
        System.out.println("Balance: " + balance);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Bank obj = new Bank();

        obj.create(sc);
        obj.deposit(sc);
        obj.withdraw(sc);
        obj.display();

        sc.close(); // Close the Scanner
    }
}
