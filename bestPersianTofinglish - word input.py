###############################################################
# PROJECT NAME: persian2finglish                              #
# SIGN:12148407579314783130754591437669                       #
# LICENCED : MIT License                                      #
# CODE BY: MohammadMahdi Barghi                               #
# Date: 15 MAY 2021                                           #
# Copyright (c) 2021 mohammad mahdi barghi                    #
###############################################################

import io

# farsi dataset file
persianFile = io.open("farsi-Words-DATASET.txt", mode="r", encoding="utf-8")
persianWord = persianFile.readlines()


# english dataset file
englishFile = io.open("english-Words-DATASET.txt", mode="r", encoding="utf-8")
englishWord = englishFile.readlines()

for i in range(100):
    checkerLine=input("enter persian sentence:   ")
    res = []
    checkertemp = checkerLine.split()

    for checker in checkertemp:
        flag = False
        couter=0
        for perWord in persianWord:
            couter = couter + 1;
            if(perWord.split()==checker.split()):
              wait=englishWord[couter-1].rstrip()
              res.append(wait)
              flag=True
              break

        if (flag == False):
            res.append(checker)

    res = ' '.join(res)
    print(res)

