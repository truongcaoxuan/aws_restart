#!/bin/bash
###########################
# Challenge Description
###########################
# Create a directory with a name of <yourName>-<currentDate>.

# Write a bash script to:

### Create twenty-five empty (0 KB) files (Hint: Use the touch command).

### The file names should be <yourName><number>, 
### <yourName><number+1>, <yourName><number+2> and so on.

### Design the script so that each time you execute it, 
### it creates the next batch of 25 files 
### with increasing numbers starting with the last or max number that already exists.

### Do not hard code these numbers. You need to generate them using automation.

# Test the script. 
# Display a long list of the directory and its contents 
# to validate that the script created the expected files.

# Save the script and make a note of its location (absolute path) for future reference.

############################
### CHANGE HERE
###########################
### Set your name
your_name=truongcx

#############################
### DO NOT CHANGE
#############################
### Get folder name
dir_folder="${your_name}_$(date +%Y_%b_%d)"

### Check if a directory does not exist ###
if [ ! -d "./${dir_folder}" ]; then
    mkdir  ${dir_folder}
fi

### cd to folder
cd $dir_folder

### Get current number files in folder
num_files=$(ls -1 | wc -l)

### Set range number
num_start=$(($num_files+1))
num_stop=$(($num_files+25))

### Create files
for var in $(seq ${num_start} 1 ${num_stop});
do
    touch "${your_name}-${var}"
done

### Show all files
ls -l