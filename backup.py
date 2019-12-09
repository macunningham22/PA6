# CS151, Dr. Isaacman, Programming Assignment 6
#
# Dataset: crime data
# Team Members:  Michael Cunningham, Gavin Corkett
# Date:  11/27/19
# Problem Summary: Answer certain questions by generating statistics and a chart
# Inputs: user choice from menu, crime.csv
# Outputs: juvenile arrest rates, a graph, annual mean gun homicide rates, a file of violent crime rate change



# Function name: menu
# Programmer: Mike
# Purpose: displays a menu to the user
# Parameters:
# Return: user choice
def menu():
    print("This program generates various statistics on crime data")
    print("1. calculate mean gun homicide rate for each year")
    print("2. calculate average juvenile arrests and compare to DV to determine if there's a correlation")
    print("3. find the change in VC from 2010-2014")
    print("4. generate a graph on the number of adult arrests")
    print("5. End program")
    user_choice = input("please pick one (enter an integer): ").lower().strip()
    return user_choice
# Function name: gun_hom_mean
# Programmer: Mike
# Purpose: Calculates the mean gun homicide rate for all sample neighborhoods for each year
# Parameters: master_list
# Return: annual mean rates
def gun_hom_mean(master_list):
    year_11 = 0.0
    year_12 = 0.0
    year_13 = 0.0
    year_14 = 0.0
    index = 0.0
    results = []
    for list in master_list:
        index += 1
        if list[29] is not "":
            year_11 += float(list[29])
        elif list[30] is not "":
            year_12 += float(list[30])
        elif list[31] is not "":
            year_13 += float(list[31])
        elif list[32] is not "":
            year_14 += float(list[32])
    mean1 = float(year_11) / float(index)
    mean2 = float(year_12) / float(index)
    mean3 = float(year_13) / float(index)
    mean4 = float(year_14) / float(index)
    results.append(mean1)
    results.append(mean2)
    results.append(mean3)
    results.append(mean4)
    return results



# Function name: avg_juv_arrests
# Programmer: Gavin
# Purpose: Find the average number of total juvenile arrests for each category of the DV-shootings column to determine
#          if it is related to DV
# Parameters: master_list
# Return: an average and a yes or no on a correlation
def avg_juv_arrests(master_list):

    temp

# Function name: vcr_change
# Programmer: Mike
# Purpose: find the change in VC from 2010-2014
# Parameters: master_list
# Return: a file of user choice
def vcr_change(master_list, user_filename):
    file = open(user_filename, "w")
    for list in master_list:
        year_10 = list[6]
        year_14 = list[10]
        change = float(year_14) - float(year_10)
        change = round(change, 3)
        if change > 0:
            description = "up"
            if change >= 5:
                description = "significantly up"
        elif change == 0:
            description = "flat"
        else:
            description = "down"
            if change <= -5:
                description = "significantly down"
        print(change, ": ", description, file=file)
    file.close()
    return file


# Function name: arrests_graph
# Programmer: Gavin
# Purpose: create a graph on the different numbers of adult arrests
# Parameters: master_list
# Return: a graph
def arrests_graph(master_list):
    open_file = open("crime.csv")
    list = master_list
    for line in open_file:
        line_list = line.strip().split()
        list.append(int(line_list[0]))
        list.append(float(line_list[2]))
    open_file.close()

    pylab.plot(list)
    pylab.ylabel("Number of Adults")
    pylab.xlabel("Arrests")
    pylab.title("Adult Arrests")


# Function name: list_gen
# Programmer: Mike
# Purpose: creates a list of lists to compare the crime data
# Parameters:
# Return: the list of lists
def list_gen():
    file = open("crime.csv", "r")
    master_list = []
    for line in file:
        temp = line.split(",")
        master_list.append(temp)
    return master_list



def main():
    master_list = list_gen()
    print(master_list)
    user_choice = menu()
    user_choice = int(user_choice)
    if user_choice == 1:
        results = gun_hom_mean(master_list)
        for element in results:
            print(element)
    elif user_choice == 2:
        avg_juv_arrests(master_list)
    elif user_choice == 3:
        user_filename = input("what would you like to name the output file?")
        print(vcr_change(master_list, user_filename))
    elif user_choice == 4:
        arrests_graph(master_list)
    elif user_choice == 5:
        return "DONE"
    main()

main()