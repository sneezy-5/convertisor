# !/usr/bin/python
# -*- coding: UTF-8 -*-
# -*- coding: utf-8 -*-


####################################################################################################
# on declare 3 tableaux pour stoker les debuts des numéro de chaque réseau                         #                                                                                                 #
####################################################################################################

orange = ['07', 59, 57, 47, 78, 49, 48, 67, 68, 97, "08", "09", 97, 77, 78, 89, 58, 7, 87, 88, 69, 79, 98]
moov = ['02', '01', 51, 50, 71, 72, 41, 72, 73, "03", 52, 53, 43, 42, 40, 70]
mtn = [55, 56, '05', 65, '04', 45, 46, 44, 84, '06', 85, 74, 75, 76, 64, 65, 66, 54, 86, 94, 95, 96]



rec = ""

def open_file():

    try:
        with open("contacts.vcf", "r") as source_file:

            """
                           Ouverture du fichier principale en lecture .
                           On recupere les numeros dans un tableau.
                           Attention le fichier doit bien se trouver dans le meme repertoire que le script
                       """

            rec = source_file.read()
            chaine = rec.split("\n")




    except FileNotFoundError:
        print("ATTENTION VOTRE FICHIER DOIT IMPERATIVEMENT SE TROUVER DANS LE MEME REPERTOIR QUE LE PROGRAME ET DOIT AVOIR L'EXTENTION (.vcf)")

    return chaine

def controle():
    filtre = ""
    aigain5 = ""
    chaine = open_file()
    for i in chaine:
        if 'TEL' in i:
            conser = i.replace("TEL;CELL:", "")
            brob = conser.replace("TEL;HOME:", "")
            new = brob.replace("TEL;TYPE=CELL:", "")
            recnew = new.replace("TEL;TYPE=HOME:", "")
            recnews = recnew.replace("item1.TEL:", "")
            aigain = recnews.replace("TEL;CELL;PREF:", "")
            aigain2 = aigain.replace("TEL;TYPE=WORK:", "")
            aigain3 = aigain2.replace("TEL;X-Portable:", "")
            aigain4 = aigain3.replace("TEL:", "")
            aigain5 = aigain4.replace("+225", "")
            filtre = aigain5.strip(" ")
            a = filtre[:2]

            for x in orange:
                if a == str(x):
                    filtre = "07"+filtre

                else:
                    filtre = filtre

            for x in moov:
                if a == str(x):
                    filtre = "01"+filtre

                else:
                    filtre = filtre

            for x in mtn:
                if a == str(x):
                    filtre = "05"+filtre

                else:
                    filtre = filtre
        if i:
            d = i.replace(aigain5, filtre)
            print(d)

controle()

###########################################################################################
#    on pourra recuperer la sortie de fichier en console avec un ex > NomFic.csv          #                                                                           #
###########################################################################################

