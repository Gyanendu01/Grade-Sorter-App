import time
print("\n\tWelcome to the Grade Sorter App")

def usr_input():
    usr_name = input("\n\tEnter your username: ")
    num_of_grade = int(input("\n\tEnter number of grades that you want to evaluate: "))
    lst_grade = list()
    for i in range(1,num_of_grade+1):
        while True:
            grade = float(input("\tEnter grade{} (0-100): ".format(i)))
            if grade >= 0 and grade <= 100:
                lst_grade.append(grade)
                break
            else:
                print("\n\tPlease eneter grade from 0-100!!")
    return usr_name,lst_grade



def grade_computation(name,grade):
    print("\n\tHello, {} Calculating desired requirements".format(name))
    time.sleep(1)
    print("\n\tYour grades are: {}".format(grade))
    grade.sort(reverse = True)
    print("\n\tYour grades from highest to lowest: {}".format(grade))
    print("\n\tLowest two grades dropping now....")
    time.sleep(0.6)
    print("\tRemoved grade: {}".format(grade[-1])) 
    grade.pop()
    print("\tRemoved grade: {}".format(grade[-1]))
    grade.pop()

    print("\n\tYour remaining grades are: {}".format(grade))
    print("\tYour highest grade is: {}".format(grade[0]))

# Main function
usr_data = usr_input()
grade_computation(usr_data[0], usr_data[1])