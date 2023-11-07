f = open("three_digit_numbers.txt")
sample = f.read()
cols = sample.split()
num_list = []
for col in cols:
    num = int(col)
    num_list.append(num)
start = min(num_list)
for count in range(start, max(num_list)):
    if count not in num_list:
        print(f"{count} is missing")
# Takes number in "three_digit_numbers.txt"
# Shows which numbers are missing as well as in order
f_samples = open("sorted_numbers.txt", "w")
f_samples.write(f"Numbers sorted numerically. \n  ")
        

        
