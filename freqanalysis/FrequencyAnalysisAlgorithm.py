#python imports
import matplotlib.pyplot as plt #graphing library
import numpy as np

#File Paths
data_folder = "datain/"
file_to_open = data_folder + "FrequencyAnalysisData.txt"

#Define function to find character frequencies with the key array, existing frequencies array, and line data as parameters
def find_file_freq(key, lines, frequencies):
    for i in range(len(arrKey)):
        for j in range(len(lines)):
            if arrKey[i] == lines[j]:
                arrFrequencies[i] += 1

#Read file contents and save as a variable
text_file = open(file_to_open)
lines1 = text_file.read()
text_file.close()

#Define 2d arrays to store frequencies and act as a "key"
arrFrequencies = []
arrKey = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "Other"]
for i in range(len(arrKey)):
    arrFrequencies.append(0)

#extract "ticks" for bar graph and file contents
y_pos = np.arange(len(arrKey))
file_lines = lines1.upper()

#use the previosly defined find_file_freq function to compute character frequencies
find_file_freq(arrKey, file_lines, arrFrequencies)


#Create list with the format (key : frequency)
comb_strings = []
for i in range(len(arrKey)):
    comb_strings.append(str(arrKey[i]) + " : " + str(arrFrequencies[i]))

#print the new list
print(comb_strings)

#Generate matplotlib bar graph
plt.bar(y_pos, arrFrequencies, align='center', alpha=0.5)
plt.xticks(y_pos, arrKey)
plt.ylabel("Frequency")
plt.xlabel("Characters")
plt.title("Frequency of characters in " + file_to_open)
plt.show()

try:
    #Ask user if decryption is wanted
    print("Is this string encrypted with a ceaser cypher? [Enter: Yes or No]")
    userresponse = str(input())

    if userresponse == "Yes":
        #store the frequencies
        arrTemp = arrFrequencies
        del arrTemp[-1]

        #find the index of the maximum frequency -- This is the letter "e" in english
        epos = arrTemp.index(max(arrTemp))
        shift1 = -1 *(4 - epos)
        print("The estimated cipher key is " + str(shift1) + " [Note: This key will only work if your text sample is very large and written in english]")
        shift = -1 * shift1
        cipherText = ""

        #Character Shift algorithm
        for char in lines1:
          pos = ord(char)
          if 48<= pos<= 57:
            newpos = (pos-48+shift)%10+48
          elif 65<=pos<= 90:
            newpos = (pos-65+shift)%26+65
          elif 97<=pos<=122:
            newpos = (pos-97+shift)%26+97
          else:
            newpos = pos
          cipherText += chr(newpos)

        print(cipherText)

        #store new decrypted text
        file_out = open("dataout/CrackedCipherText.txt", "w+")
        #file_out.write("The original encrypted text is: " + lines1)
        file_out.write("\nThe estimated cipher key is: " + str(shift1))
        file_out.write("\nThe new decrypted text is: " + cipherText)

        file_out.close()
        print("The cracked cipher text has been printed in dataout/CrackedCipgerText.txt")
    else:
        exit()
except Exception as e:
    print('An error has occured')
    print('error:', e)
