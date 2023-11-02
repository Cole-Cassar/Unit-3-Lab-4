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
# ===============================================
# number: 0
# f_obj = open("three_digit_numbers.txt", "r")
# for line in f_obj:
#     print(line)
# f_obj.close
# ================================================
# What I started with to develop a foundation and idea