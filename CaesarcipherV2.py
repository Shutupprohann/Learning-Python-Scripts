alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
str_in = str(input("Enter Message : "))
shift_value = int(input("Enter Shift value : "))

n = len(str_in)
str_out = " "

for i in range(n):
    c = str_in[i]
    loc = alpha.find(c)
    print(i ,c , loc)
    new_loc = loc + shift_value
    if new_loc >= 26:
        new_loc = (loc + shift_value)%26
    str_out += alpha[new_loc]

print(str_out)    
file = open("output.txt","a")
file.write(str_out)
file.close    
exit()
