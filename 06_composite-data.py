# Lab6. Working with Composite Data Types
import csv
import copy

# define a dictionary that will serve as your composite type for reading the tabular data
myVehicle = {
    "vin" : "<empty>",
    "make" : "<empty>" ,
    "model" : "<empty>" ,
    "year" : 0,
    "range" : 0,
    "topSpeed" : 0,
    "zeroSixty" : 0.0,
    "mileage" : 0
}

# use a for loop to iterate over the initial keys and values of the dictionary.
for key, value in myVehicle.items():
    print("{} : {}".format(key,value))

# Define an empty list to hold the car inventory that you will read:
myInventoryList = []


""" You will read in the data from disk (hard drive) and make an in-memory (random access memory, or RAM) copy. 
In a computer, a hard drive stores data long term, including when the power is turned off. 
RAM refers to temporary memory that is faster, but it is erased when the computer's power is turned off.

You will be introduced to the >>> with open syntax statement <<<, which keeps a file open while you read data. 
It will automatically close the CSV file when the code inside the with block is finished running.

You will also use a new way of formatting a string. 
Instead of using double quotation marks and .format to pass in the variables, you can use a single quotation mark and write in the variables between the "{}" symbols.

Finally, csv.reader() is a function that you are using from the csv library that you imported with the import csv statement.

Most of the rest of the code should be familiar. """

with open('files/car_fleet.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')  
    lineCount = 0  
    for row in csvReader:
        if lineCount == 0:
            print(f'Column names are: {", ".join(row)}')  
            lineCount += 1  
        else:  
            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')  
            # By default, Python does a shallow copy of complex data types. A shallow copy refers, or points, to the storage location of the myVehicle dictionary variable. 
            # Without this line >>> currentVehicle = copy.deepcopy(myVehicle) <<<, you would have only one storage box, and only the last item in the list would be copied into memory. 
            # This line makes sure that new storage boxes are created in memory to store the new tabular data that is being read.
            currentVehicle = copy.deepcopy(myVehicle)  
            currentVehicle["vin"] = row[0]  
            currentVehicle["make"] = row[1]  
            currentVehicle["model"] = row[2]  
            currentVehicle["year"] = row[3]  
            currentVehicle["range"] = row[4]  
            currentVehicle["topSpeed"] = row[5]  
            currentVehicle["zeroSixty"] = row[6]  
            currentVehicle["mileage"] = row[7]  
            myInventoryList.append(currentVehicle)  
            lineCount += 1  
    print(f'Processed {lineCount} lines.')

# printing the car inventory from the myInventoryList variable
for myCarProperties in myInventoryList:
    for key, value in myCarProperties.items():
        print("{} : {}".format(key,value))
        print("-----")

