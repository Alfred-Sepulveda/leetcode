class Solution{
    static int v;
    public static boolean isPalindrome(int x){
        if(x<0) return false;
        if(x<10) return false;
        if(x%10==0) return false;
        if(x<100&&x%11 == 0) return false;
        if(x<1000&&((x/100)*10+x%10)%11 == 0) return true;

        v = x%10;
        x = x/10;
        while(x-v>0){
            v=v*10+x%10;
            x/=10;
        }
        if(v>x){v/=10;}
        return v==x? true:false;
    }
}

class Vehicle{
    protected String brand = "Ford";
    public void honk(){
        System.out.println("tuut,tuut!");
    }
}

class Car extends Vehicle{
    private String modelName = "Mustang";
    public static void main(String[] args){
        Car myCar = new Car();
        myCar.honk();
        System.out.println(myCar.brand + " " + myCar.modelName);
    }
}

class Animal{
    public void animalSound(){
        System.out.println("the animal makes a sound");
    }
}

class Pig extends Animal{
    public void animalSound(){
        System.out.println("The pig says: wee wee");
    }
}

class Dog extends Animal{
    public void animalSound(){
        System.out.println("the dog says: bow wow");
    }
}

class Main{
    public static void main(String[] args){
        Animal myAnimal = new Animal();
        Animal myPig = new Pig();
        Animal myDog = new Dog();
        myAnimal.animalSound();
        myPig.animalSound();
        myDog.animalSound();
    }
}

class Main{
    public static void main(String[] args){
        Animal myAnimal = new Animal();
        Animal myPig = new Pig();
        myAnimal.animalSounds();
        myPig.animalSounds();
    }
}



// a high level programming language
// what are the features of java?

// OOP concepts
// object-oriented
// inheritance
// encapsulation
// polymorphism
// abstraction


// we can use polymorphism on inheritance 
// inheritance lets us inherit attributes and methods from another class, polymorphism uses
// those methods to perform different tasks. this allows us to perform a single action in 
// different ways
