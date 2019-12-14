import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
data_folder = "datain/"
file_to_open = data_folder + "FrequencyAnalysisData.txt"
text_file = open(file_to_open)
lines1 = text_file.read()
#print(lines1)
text_file.close()
arrFrequencies = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
arrKey = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "Other"]
y_pos = np.arange(len(arrKey))
lines = lines1.upper()
#print(lines)
for i in range(len(arrKey)):
    for j in range(len(lines)):
        if arrKey[i] == lines[j]:
            arrFrequencies[i] += 1
print(arrFrequencies)
plt.bar(y_pos, arrFrequencies, align='center', alpha=0.5)
plt.xticks(y_pos, arrKey)
#plt.xticks(y_pos, arrKey)
plt.ylabel("Frequency")
plt.xlabel("Characters")
plt.title("Frequency of characters in " + file_to_open)
plt.show()
print("Is this string encrypted with a ceaser cypher? [Enter: Yes or No]")
userresponse = str(input())
if userresponse == "Yes":
    arrTemp = arrFrequencies
    del arrTemp[-1]
    epos = arrTemp.index(max(arrTemp))
    shift1 = -1 *(4 - epos)
    print("The estimated cipher key is " + str(shift1) + " [Note: This key will only work if your text sample is very large and written in english]")
    shift = -1 * shift1
    cipherText = ""
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
    file_out = open("dataout/CrackedCipherText.txt", "w+")
    file_out.write("The original encrypted text is: " + lines1)
    file_out.write("\nThe estimated cipher key is: " + str(shift1))
    file_out.write("\nThe new decrypted text is: " + cipherText)
    file_out.close()
    print("The cracked cipher text has been printed in dataout/CrackedCipgerText.txt")