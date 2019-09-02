import csv
import glob

# Asking the user if they would like to convert multiple or just one file
# We are expecting an answer of '1' or '2' so we will need to validate the input
print("Would you like to enter a target directory(1) or file name(2)?")
userChoice = input()

while userChoice != '1' and userChoice != '2':
	print("Enter '1' if you would like to convert a whole directory of files or '2' if you would like to convert a single file")
	userChoice = input()

if userChoice == '1':
	print("Are the files in your current working directory? (Y or N)")
	target = input()
	if target.upper() == 'Y':
		target = ''
	else:
		print("Enter the path to the target directory: ")
		tempTarget = input()

else:
	print("Enter the full file name (including .txt file extension): ")
	target = input()


if userChoice == '1':
	if tempTarget != '':
		if tempTarget[len(tempTarget) - 1] == '\\':
			target = tempTarget[:len(tempTarget) - 1] + '/'
			print("new target is: " + target)
		elif tempTarget[len(tempTarget) - 1] != '/':
			target = tempTarget + '/'
	print(target)
	for file in glob.glob(target + "*.txt"):
		print(file)
		with open(file, 'r') as in_file:
		    stripped = (line.strip() for line in in_file)
		    lines = (line.split(",") for line in stripped if line)
		    with open(file.replace('.txt', '.csv'), 'w') as out_file:
		        writer = csv.writer(out_file)
		        writer.writerows(lines)

else:
	with open(target, 'r') as in_file:
	    stripped = (line.strip() for line in in_file)
	    lines = (line.split(",") for line in stripped if line)
	    with open(target.replace('.txt', '.csv'), 'w') as out_file:
	        writer = csv.writer(out_file)
	        writer.writerows(lines)