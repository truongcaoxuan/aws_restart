#Lab 10 :: Preparing to Analyze Insulin with Python
import csv
import re
strF = '''ORIGIN      
        1 malwmrllpl lallalwgpd paaafvnqhl cgshlvealy lvcgergffy tpktrreaed
       61 lqvgqvelgg gpgagslqpl alegslqkrg iveqcctsic slyqlenycn
//'''

line_1=""
line_2=""
pattern_1 = r'\d+[\w|\s]{66}'
pattern_2 = r'\d{2}[\w|\s]{55}'

with open('files/preproinsulin-seq.txt') as f:
    s = f.read()
    line_1 = str(re.findall(pattern_1,s))
    line_2 = str(re.findall(pattern_2,s))

# replace [] and space 
line_1 = line_1[4:-2].replace(' ','')
line_2 = line_2[5:-2].replace(' ','')

# get amino acids in the sequence of human preproinsulin (110 characters)
human_preproinsulin = line_1 + line_2
print("amino acids in the sequence of human preproinsulin")
print("---------------------------------------------------")
print (human_preproinsulin)
print("---------------------------------------------------")

# save the amino acids : 110 characters
with open('files/preproinsulin-seq-clean.txt','w') as f1:
    f1.write(human_preproinsulin[:])

# save amino acids 1–24 : 24 characters.
with open('files/lsinsulin-seq-clean.txt','w') as f1:
    f1.write(human_preproinsulin[0:24])

# save amino acids 25–54 : 30 characters.
with open('files/binsulin-seq-clean.txt','w') as f1:
    f1.write(human_preproinsulin[24:55])

# save amino acids 55–89 : 35 characters.
with open('files/cinsulin-seq-clean.txt','w') as f1:
    f1.write(human_preproinsulin[54:90])

# save amino acids 90–110 : 21 characters.
with open('files/ainsulin-seq-clean.txt','w') as f1:
    f1.write(human_preproinsulin[89:111])
