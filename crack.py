from string import digits, ascii_letters, punctuation

for i in digits + ascii_letters + punctuation:
    for j in digits + ascii_letters + punctuation:
        for k in digits + ascii_letters + punctuation:
            for l in digits + ascii_letters + punctuation:
                print (i, j, k, l)

# use just 'digits' first 10000, then try letters upper and lower: ascii_letters (52^4), 
# then try adding punctuation (94^4):
# Run in terminal using "python3 crack.py" 