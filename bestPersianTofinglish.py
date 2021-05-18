###############################################################
# PROJECT NAME: persian2finglish                              #
# SIGN:12148407579314783130754591437669                       #
# LICENCED : MIT License                                      #
# CODE BY: MohammadMahdi Barghi                               #
# Date: 15 MAY 2021                                           #
# Copyright (c) 2021 mohammad mahdi barghi                    #
###############################################################

import io

# changing file
checkerFile = io.open("5.txt", mode="r", encoding="utf-8")
checkerLine = checkerFile.readlines()
# farsi dataset file
persianFile = io.open("farsi-Words-DATASET.txt", mode="r", encoding="utf-8")
persianWord = persianFile.readlines()
# english dataset file
englishFile = io.open("english-Words-DATASET.txt", mode="r", encoding="utf-8")
englishWord = englishFile.readlines()
# print(checkerLine)
for i in range(len(checkerLine)):
    # print(checkerLine[i])
    res = []
    checkertemp = checkerLine[i].split()
    # print(checkertemp)
    for checker in checkertemp:
        # print(checker)
        # print(res)
        flag = False
        couter=0
        for perWord in persianWord:
            # print(perWord.split())
            couter = couter + 1;
            if(perWord.split()==checker.split()):
              # print(perWord)
              # print(englishWord[couter-1])
              wait=englishWord[couter-1].rstrip()
              res.append(wait)
              flag=True
              break

        if (flag == False):
            res.append(checker)
    # print("seeeeen")
    # print(res)
    res = ' '.join(res)
    print(res)










     # print(f2f(Lines[i].strip()))
     # print(i)





# file1 = io.open("PersianToFinglishDataset.txt", mode="r", encoding="utf-8")
# Lines = file1.readlines()
# f = io.open("farsiDataset.txt", mode="a", encoding="utf-8")
#
# for i in range(len(Lines)):
#     temp = Lines[i].split("\t")
#     f.write(temp[1])
#     # f.write("\n")
# f.close()



