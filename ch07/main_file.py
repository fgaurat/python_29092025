


def main():
    # écrire dans un fichier
    # f = open("le_fichier.txt","w")
    # ajout dans un fichier
    
    # f = open("le_fichier.txt","a")
    # f.write('Hello world\n')
    # f.close()
    # f = open("le_fichier.txt","r")

    f = open("le_fichier.txt") 

    for line in f:
        clean_line = line.strip() # suppression du caractère \n
        print(clean_line)
    
    f.close()

if __name__=='__main__':
    main()
