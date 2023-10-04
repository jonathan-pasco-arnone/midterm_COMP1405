""" Printing data of students program """

# Created by: Jonathan Pasco-Arnone
# Created on: October 2023

def print_sorted_grades(filename):
    """ This function prints the sorted data of students """
    full_file = open("/workspaces/midterm_COMP1405/1405-midterm-materials/"
          + filename, "r", encoding="utf8")

    # Opening a file in write mode erases the data from it making it a new document
    output_deletion = open(filename[:len(filename) - 4] + "_output.txt", "w", encoding="utf8")
    output_deletion.close()

    # Creates file for output
    output_file = open(filename[:len(filename) - 4] + "_output.txt", "r+", encoding="utf8")

    full_file.seek(0)
    output_file.seek(0)

    # Main meat of the function
    current_student_name = ""
    current_student_mark = 0.0
    for index, line in enumerate(full_file.readlines()):

        # Removes the new lines at the end of each line
        line = line.strip()

        # Checks if the file is at the first name of each student
        if index % 6 == 0:

            # Resets the name and mark
            current_student_mark = 0
            current_student_name = line

        # Checks if the file is at the last name of each student
        elif index % 6 == 1:
            current_student_name += " " + line

        # If the file is not at a name of a student then it can be converted to a number
        else:
            # If the file is not on the first or second line then it can be turned into a float
            line = float(line)

        # Finds the mark of the assignement, midterm, and exam and adds them
        if index % 6 == 3:
            current_student_mark += 0.25 * line
        elif index % 6 == 4:
            current_student_mark += 0.30 * line
        elif index % 6 == 5:
            current_student_mark += 0.45 * line
            # Replaces the new name and marks if necessary

            name_added = False
            # Grabs the data of all the file and puts it into a string
            output_file.seek(0)
            data = output_file.read()
            output_file.seek(0)
            for line_number, string in enumerate(output_file.readlines()):
                # Since the marks are on every second line, we have to check
                # that the line we are reading is the mark
                if line_number % 2 == 1:
                    if current_student_mark > float(string[:len(string) - 1]):
                        name_added = True
                        new_data = ""
                        new_line_count = 0
                        for char_number, char in enumerate(data):
                            if char == "\n":
                                new_line_count += 1
                            if line_number == new_line_count + 1:
                                if line_number == 1:
                                    new_data = (current_student_name + "\n"
                                          + str(current_student_mark) + "\n" + data[char_number:])
                                else:
                                    new_data = (data[:char_number + 1] + current_student_name
                                          + "\n" + str(current_student_mark)
                                          + "\n" + data[char_number + 1:])
                                break

                        # Opening a file in write mode erases the
                        # data from it making it a new document
                        output_deletion = open(filename[:len(filename) - 4]
                              + "_output.txt", "w", encoding="utf8")
                        output_deletion.close()

                        output_file.seek(0)
                        output_file.write(new_data)
                        break
            if not name_added:
                output_file.write(str(current_student_name) + "\n" + str(current_student_mark)
                      + "\n")

for number in range(0,5):
    print_sorted_grades("studentinfo" + str(number) + ".txt")
