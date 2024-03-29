import csv
import glob

# Asking the user if they would like to convert multiple or just one file
print("Would you like to enter a target directory(1) or file name(2)?")
userChoice = input()

# We are expecting an answer of '1' or '2' so we will need to validate the input
while userChoice != '1' and userChoice != '2':
	print("Enter '1' if you would like to convert multiple files or '2' if you would like to convert a single file")
	userChoice = input()

# Now we just need to figure out where the files are
if userChoice == '1':
	print("Are the files in your current working directory? (Y or N)")
	target = input()
	if target.upper() == 'Y':
		target = ''
	else:
		print("Enter the path to the target directory: ")
		tempTarget = input()
		
# Only the file name is needed if we are converting a single file
else:	
	print("Enter the full file name (including .txt file extension): ")
	target = input()

# Converting a glob of files
if userChoice == '1':
	if tempTarget != '':
		if tempTarget[len(tempTarget) - 1] == '\\':
			target = tempTarget[:len(tempTarget) - 1] + '/'
		elif tempTarget[len(tempTarget) - 1] != '/':
			target = tempTarget + '/'
	for file in glob.glob(target + "*.txt"):
		print("Transforming",file)
		with open(file, 'r') as in_file:
		    stripped = (line.strip() for line in in_file)
		    lines = (line.split(",") for line in stripped if line)
		    with open(file.replace('.txt', '.csv'), 'w') as out_file:
		        writer = csv.writer(out_file)
		        writer.writerows(lines)
# Just converting one
else:
	print("Transforming", target)
	with open(target, 'r') as in_file:
	    stripped = (line.strip() for line in in_file)
	    lines = (line.split(",") for line in stripped if line)
	    with open(target.replace('.txt', '.csv'), 'w') as out_file:
	        writer = csv.writer(out_file)
	        writer.writerows(lines)
