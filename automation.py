# Purpose: Create a new file
# Future Improvements: Set-up for DAQ
import datetime
import time

testID = ""
test_type = ""
test_type_num = ""
measurement_type = ""
measurement_list = [1,2,3,4,5]      # Currently using a pre-made list of measurement for the time being
get_data = 0
data = ""
index = 0

# Take manual inputs from user to set up file
testID = input("Enter the test ID: ")
test_type_num = input("Select the kind of test ( 1 - Continuity, 2 - Thermal, 3 - Functionality): ")


# Create a nested function to read a template and create a new file based off it
with open('template', 'r') as rf:
     with open('test_' + testID + ".csv",'w') as wf:
         for line in rf:
            # Set up test ID
            if line == "Test ID:\n":
                line = ("Test ID: " + testID + "\n")

            # Set up test type
            if line == "Test Type:\n":
                if test_type_num == "1":
                    test_type = "Continuity"
                    measurement_type = "Resistance"
                elif test_type_num == "2":
                    test_type = "Thermal"
                    measurement_type = "Temperature"
                elif test_type_num == "3":
                    test_type = "Functionality"
                    measurement_type = "Voltage"

            # Set up to take measurements
            if line == "Measurements:\n":
                line = ("Index, " + measurement_type + ", Timestamp\n")

            # Print to the console (for troubleshooting)
            print(line, end='')

            # Create or Overwrite file test_testID
            wf.write(line)

            # Enter data into the test file
            if line == "Index, " + measurement_type + ", Timestamp\n":
                # Prompt user to enter the amount of samples wanted
                get_data = int(input("Enter the amount of sample size you want: "))
                for index in range(get_data):
                    now = datetime.datetime.now()
                    # Format data to include timestamps
                    data = str(index) + ", " + str(measurement_list[index]) + ", " + now.strftime("%H:%M:%S %d/%m/%Y") + "\n"
                    print(data, end='')
                    index = index + 1
                    wf.write(data)
                    time.sleep(1)
