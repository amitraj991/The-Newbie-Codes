name= input("Enter Your Name : ");
height=float(input("Enter your height in meters:"));
weight=float(input("Enter your weight in KG:"));

BMI=weight/(height**2)
print("your BMI is:",BMI);
if BMI<25:
    print("You Are Under Weight");
    print("Recommended Diet Pla : Breakfast- IDlY +Milk+banana, Lunch- Rice+Curyy+Dal+Curd,\n","Snacks- Nuts,Banana,Sandwich,\n" "Dinner- Ghee Chapathi+ Curry ");
elif BMI==25:
    print("You have proper weight but to maintain it keep eating healthy");

elif BMI>25:
    print("You are Over Weight");



    

             
