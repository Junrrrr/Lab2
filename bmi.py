def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    
    bmi = weight / (height ** 2)
    
    if bmi < 18.5:
        print("Your BMI is: ", bmi)
        print("you are under weight.")
    elif bmi <= 25.0:
        print("Your BMI is: ", bmi)
        print("you are normal weight.")
    else:
        print("Your BMI is: ", bmi)
        print("you are over weight.")

calculate_bmi(weight=57, height=1.73)

def main():
print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
display_main_menu()
num_list = get_user_input()

if __name__ == "__main__":
main()