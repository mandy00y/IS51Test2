
"""

There is a file called Final.txt. You want to open it and count how 
many grades there are. The program will tell you how many grades there
are in the file, and the average grade. It will also tell you the 
percentage of grades that are above the average grade.

Main function will kickstart the program, open the file, and 
output 24 total grades and output average 83.25

Within the main function, the calculate_percent_above_average function
will output average percentage above average 54.17%.


"""




"""

#def main()

open file "Final.txt"
grades = []
close file
for i range:
    grades = int[]
average = sum/ total count



    #def calcualte_percentage_above_average()

    initialize counter and sum to 0
    if grade > average:
        add
        100 / len(grades)
        above_average = format


    
print "Number of grades:
print "Average grade:
print "Percentage of grades above average: 

    calculate_percentage_above_average()


main()

"""





def main():
    infile = open("Final.txt", 'r')
    grades = [line.rstrip() for line in infile]
    infile.close()
    for i in range(len(grades)):
        grades [i] = int(grades[i])
    average = sum(grades) / len(grades)


    def calculate_percent_above_average():
        above = 0
        for grade in grades:
            if grade > average:
                above += 1
        

        print("Number of grades:", len(grades))
        print("Average grade:", average)
        print("Percentage of grades above average:{0: .2f}%".format(100 * above / len(grades)))
    calculate_percent_above_average()


main()