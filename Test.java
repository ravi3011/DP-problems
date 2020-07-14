import java.util.Scanner;


import java.util.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class Test
{
    static LinkedList<String> ls = new LinkedList<String>();
    static Scanner sc = new Scanner(System.in);
    static BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

    public static void createLot(final int size)throws IOException {
        for (int i = 0; i < size; i++) {
            int t = i + 1;
            System.out.println("Enter " + t + " lot");
            final String st = reader.readLine();
            ls.add(st);
        }
        int t = 1;
        for(int i = ls.size()-1; i > size ;i++){
            t += size;
            System.out.println("Allocated slot number : "+t);
        }

    }

    public static void makeFreeSolt(int num){
            ls.set(num-1,"true");
            System.out.println("Slot number "+num+" is now free");        
    }
    public static void checkStatus(){
        for(int i = 0 ; i<ls.size(); i++){
            int t = i+1;
            if(ls.get(i) != "true")
            {  
                System.out.println("Slot No. Registration No. Color");
                String[] str = ls.get(i).split(" ");
                System.out.print(t);
                for(String w:str){
                    System.out.print("           "+w);

                }
                System.out.println();
            }

        }
    }
    public static void park()throws IOException{
        String str = reader.readLine();
        int f = 0;
        int slot = 0;
        for(int i = 0; i<ls.size();i++){
            if(ls.get(i) == "true"){
                ls.set(i,str);
                slot = i+1;
                f = 1;
                break;
            }
        }
        if(f == 0){
            System.out.println("Allocated slot number: "+slot);
        }
        else
        {
            System.out.println("Sorry, parking lot is full");

        }

    }
    public static void checkRegistration(String color){
        int check = 0;
        for(int i = 0 ; i<ls.size(); i++){
            int t = i+1;
            if(ls.get(i) != "true")
            {  
                String[] str = ls.get(i).split(" ");
                if(str[1].trim() == color){
                    check = 1;
                    if(t == 1){
                        System.out.print(str[0]);
                    }else{
                        System.out.print(", "+str[0]);
                    }
                    
                }

            }

        }
        if(check == 0){
            System.out.println("Not found");
            }
            else{
            System.out.println();
            }
    }
    public static void checkSlot(String color){
        int check = 0;
        for(int i = 0 ; i<ls.size(); i++){
            int t = i+1;
            if(ls.get(i) != "true")
            {  
                String [] str = ls.get(i).split(" ");
                System.out.println(str[1]);
                if(str.contains(color))
                {
                    check = 1;
                    if(t == 1)
                    {
                        System.out.print(t);
                    }else
                    {
                        System.out.print(", "+t);
                    }
                    
                }

            }

        }
        if(check == 0){
        System.out.println("Not found");
        }
        else{
        System.out.println();
        }
    }
    public static void checkSlotByReg(String reg){
        for(int i = 0 ; i<ls.size(); i++){
            int t = i+1;
            if(ls.get(i) != "true")
            {  
                String[] str = ls.get(i).split(" ");
                if(str[0].trim() == reg){
                        System.out.print(t);
                }
                else{
                    System.out.print("Not found");
                }

            }

        }

    }
    public static void main(final String args[])throws IOException 
    {

        while (true) {
            System.out.println("Please input 1 for book slot");
            System.out.println("Please input 2 for relif slot");
            System.out.println("Please input 3 for check slot status");
            System.out.println("Please input 4 Park car");
            System.out.println("Please input 5 for check registration no. by car color.");
            System.out.println("Please input 6 for check slot no. by car color.");
            System.out.println("Please input 7 for check slot no. by car registration no.\n\n");

            final int in = sc.nextInt();
            switch (in) {
                case 1:
                    System.out.println("Create a parking lot ");
                    final int size = sc.nextInt();
            createLot(size);
            System.out.println("Created a parking lot with "+size+" slots");
            break;
            case 2 :
            System.out.println("leave slot");
            int num = sc.nextInt();
            makeFreeSolt(num);
            break;
            case 3 :
            System.out.println("Status of slots\n\n");
            checkStatus();
            System.out.println("\n\n");
            break;
            case 4 :
            System.out.println("Enter number and color");
            park();
            System.out.println("\n\n");
            break;
            case 5 :
            System.out.println("Enter car color for registration numbers");
            String color = sc.next();
            checkRegistration(color);
            System.out.println("\n\n");
            break;
            case 6 :
            System.out.println("Enter car color for slot numbers");
            String color1 = sc.next();
            checkSlot(color1);
            System.out.println("\n\n");
            break;
            case 7 :
            System.out.println("Enter car registration no for slot numbers");
            String reg = sc.next();
            System.out.println(reg);
            checkSlotByReg(reg);
            System.out.println("\n\n");
            break;
            default :
            System.out.println("Input is wrong try again");
        }

     }   
        
    }
}