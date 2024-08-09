
//Write a program to create a bank account having following data members and member method. 


import java.io.*;
import java.util.Scanner;

class Bank {
    String customerName;
    long accountNo;
    long balance;

    void create() {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the name:");
        customerName = sc.nextLine();
        System.out.println("Enter Account Number:");
        accountNo = sc.nextLong();
    }

    long deposit() {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter deposit amount:");
        long depositAmount = sc.nextLong();
        balance += depositAmount;
        return balance;
    }

    void withdraw() {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter withdraw amount:");
        long withdrawAmount = sc.nextLong();
        if (withdrawAmount <= balance) {
            balance -= withdrawAmount;
            System.out.println("Withdrawal successful. Current balance: " + balance);
        } else {
            System.out.println("Insufficient balance. Withdrawal failed.");
        }
    }

    void display() {
        System.out.println("Customer Name: " + customerName);
        System.out.println("Account Number: " + accountNo);
        System.out.println("Balance: " + balance);
    }

    public static void main(String[] args) {
        Bank obj = new Bank();
        obj.create();
        obj.deposit();
        obj.withdraw();
        obj.display();
    }
}