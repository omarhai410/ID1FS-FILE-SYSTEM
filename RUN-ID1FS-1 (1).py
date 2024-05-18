import os, os.path
import os
import json
import shutil
import time
import socket
import datetime
import pathlib
QUIT = 'ID1FS -QUIT'
COMMANDS = ('ID1FS -PUT','ID1FS -GET','ID1FS -G -LOG','ID1FS -G -META','ID1FS -ROM','ID1FS -SU','ID1FS -LI','ID1FS -QUIT','ID1FS -CF','ID1FS -CD','ID1FS -COP','ID1FS -HELP')
MENU = """
>>ID1FS -PUT
>>ID1FS -GET
>>ID1FS -G -LOG
>>ID1FS -G -META
>>ID1FS -ROM
>>ID1FS -SU
>>ID1FS -LI
>>ID1FS -CF
>>ID1FS -CD
>>ID1FS -COP
>>ID1FS -HELP
>>ID1FS -QUIT"""
print(">>WELCOME TO ID1 FILE SYSTEM<<")
print(">>VOUS POUVEZ CHOISIR PARMI LES COMMANDES SUIVANTES QUE VOUS SOUHAITEZ UTILISER:")
def main():
    while True:
        print(MENU)
        command = acceptCommand()
        runCommand(command)
        if command == QUIT:
            print("HAVE A NICE DAY!")
            break

def acceptCommand():
    command = input("\nENTRER UNE COMMANDE: ")
    if command in COMMANDS:
        return command
    else:
        print("ERREUR: COMMANDE PAS RECONUE")
        return acceptCommand()

def runCommand(command):
    """Selects and runs a command based on users menu choice"""
    if command == 'ID1FS -PUT':
         PUT()
    elif command == 'ID1FS -GET':
          GET()
    elif command == 'ID1FS -G -LOG':
         F_LOG()
    elif command == 'ID1FS -G -META':
         F_META()
    elif command == 'ID1FS -ROM':
         rename()
    elif command == 'ID1FS -LI':
         ls()
    elif command == 'ID1FS -CF':
         C_file()
    elif command == 'ID1FS -CD':
        C_dossier()
    elif command == 'ID1FS -COP':
        file_copy()
    elif command == 'ID1FS -HELP':
        HELP()
    elif command == 'ID1FS -SU':
        delete()

        '''if not fileList:
            print("Files not found")
        else:
            for f in fileList:
                print(f)'''

def PUT():
    folder_path = input("ENTRER LE CHEMIN DE FICHIER: ")
    destination1 = 'C:\\id1fs\\client\\heterogene_secondaire'
    shutil.copy(folder_path, destination1)
    file_name = os.path.basename(folder_path)
    name_f = file_name + '-meta'
    metadata = os.stat(folder_path)
    metadata_dict = {
        "size": metadata.st_size,
        "creation_time": metadata.st_ctime,
        "modification_time": metadata.st_mtime,
        "access_time": metadata.st_atime,
        "permissions": metadata.st_mode,
    }
    os.chdir('C:\\id1fs\\client\\metadata')
    with open(name_f, 'w') as file:
        json_data = json.dumps(metadata_dict)
        file.write(json_data)
        file.close()
    destination = 'C:\\id1fs\\client\\heterogene_primaire'
    shutil.move(folder_path, destination)

    os.chdir('C:\\id1fs\\client')
    os.chdir('C:\\id1fs\\client\\log')

    folder_rec = 'C:\\id1fs\\client\\heterogene_primaire'
    des2 = 'C:\\id1fs\\client\\log'
    os.chdir(folder_rec)
    now = datetime.datetime.now()
    y = ("Access attempted at {} for file {}".format(now.strftime("%Y-%m-%d %H:%M:%S"), file_name))
    client_ip = socket.gethostbyname(socket.gethostname())
    x = (client_ip)
    info = os.stat(file_name)
    last_access_time = info.st_atime
    duration = time.time() - last_access_time
    minutes, seconds = divmod(duration, 60)
    hours, minutes = divmod(minutes, 60)
    z = (f"Le fichier a été consulté pendant {hours} heures, {minutes} minutes et {seconds} secondes.")
    name_d = file_name + "-log"
    os.chdir(des2)
    with open(name_d, 'w') as file:
        file.write(y + '\n')
        file.write(x + '\n')
        file.write(z)
        file.close()

    path = 'C:\\id1fs\\client\\heterogene_primaire'
    os.chdir(path)

    ext = []
    for i in os.listdir():
        ext.append(i[::-1].split('.')[0][::-1])
    ext = list(set(ext))

    for i in ext:
        if os.path.exists(i) == False:
            os.mkdir(i)

    for i in os.listdir():
        shutil.move(i, i[::-1].split('.')[0][::-1])
    print("le fichier est été ajouté avec succès")

def GET():
    directory = "C:\\id1fs\\client\\heterogene_secondaire"
    os.chdir(directory)
    files = os.listdir(directory)
    name = input("enter the name of the file :")

    for file in files:
        if os.path.isfile(os.path.join(directory, file)):
            if file.startswith(name):
                os.startfile(file)
                os.chdir('C:\\id1fs\\client')
                os.chdir('C:\\id1fs\\client\\log')

                folder_rec = 'C:\\id1fs\\client\\heterogene_primaire'
                des2 = 'C:\\id1fs\\client\\log'
                os.chdir(folder_rec)
                now = datetime.datetime.now()
                y = ("Access attempted at {} for file {}".format(now.strftime("%Y-%m-%d %H:%M:%S"), name))
                client_ip = socket.gethostbyname(socket.gethostname())
                x = (client_ip)
                info = os.stat(name)
                last_access_time = info.st_atime
                duration = time.time() - last_access_time
                minutes, seconds = divmod(duration, 60)
                hours, minutes = divmod(minutes, 60)
                z = (f"Le fichier a été consulté pendant {hours} heures, {minutes} minutes et {seconds} secondes.")
                name_d = name + ".log"
                os.chdir(des2)
                with open(name_d, 'w') as file:
                    file.write(y + '\n')
                    file.write(x + '\n')
                    file.write(z)
                    file.close()

def F_LOG():
    name = input('entrer le nom de fichier: ')
    name1 = name +'-log'
    path='C:\\id1fs\\client\\log'
    os.chdir(path)
    files = os.listdir(path)
    for file in files:
        if os.path.isfile(os.path.join(path, file)):
            if file.startswith(name1):
                os.startfile(file)

def F_META():
    name = input('entrer le nom de fichier: ')
    name1 = name + '-meta'
    path = 'C:\\id1fs\\client\\metadata'
    os.chdir(path)
    files = os.listdir(path)
    for file in files:
        if os.path.isfile(os.path.join(path, file)):
            if file.startswith(name1):
                os.startfile(file)

def ls():
    path = input('ENTRER LE CHEMIN: ')
    os.chdir(path)
    files_and_directories = os.listdir(path)
    l = []
    for i in path:
        l.append(os.listdir(path))
        break

    print(l)
def rename():
   old_name = input("Saisissez l'ancien nom de fichier : ")
   new_name = input("Saisissez le nouveau nom de fichier : ")

   folder1 = "C:\\id1fs\\client\\heterogene_primaire"
   folder2 = "C:\\id1fs\\client\\heterogene_secondaire"

   for folder in [folder1, folder2]:
       for root, dirs, files in os.walk(folder):
           if old_name in files:
               old_path = os.path.join(root, old_name)
               new_path = os.path.join(root, new_name)
               os.rename(old_path, new_path)
               print(f"Le fichier a été renommé de '{old_name}' à '{new_name}' dans le dossier '{root}'.")

def delete():
    filename = input("Entrez le nom du fichier à supprimer : ")

    folders = [d for d in os.listdir("C:\\id1fs\\client\\heterogene_primaire") if os.path.isdir(os.path.join("C:\\id1fs\\client\\heterogene_primaire", d))]

    for folder in folders:
       filepath = os.path.join("C:\\id1fs\\client\\heterogene primaire", folder, filename)
       if os.path.exists(filepath):
           os.remove(filepath)
    filepath1 = os.path.join("C:\\id1fs\\client\\heterogene_secondaire", filename)
    os.remove(filepath1)
    print("Le fichier a été supprimé avec succès.")

def C_file():
    directory1 = "C:\\id1fs\\client\\heterogene_primaire\\txt"
    file_name = input("Enter the file name: ")
    file_path = os.path.join(directory1, directory1, file_name)
    with open(file_path, "w") as file:
        file.write("\n")

    while True:
        print("\nMenu:")
        print("1. Write to the beginning of the file")
        print("2. Write to the middle of the file")
        print("3. Write to the end of the file")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":

            text = input("Enter the text to write: ")

            with open(file_path, "r") as file:
                contents = file.read()

            with open(file_path, "w") as file:
                file.write(text + "\n" + contents)

        elif choice == "2":
            line_number = int(input("Enter the line number: "))
            text = input("Enter the text to write: ")

            with open(file_path, "r") as file:
                lines = file.readlines()

            lines.insert(line_number - 1, text + "\n")

            with open(file_path, "w") as file:

                file.writelines(lines)

        elif choice == "3":

            text = input("Enter the text to write: ")

            with open(file_path, "a") as file:

                file.write(text + "\n")

        elif choice == "4":
            break
def C_dossier():
    folder_name = input("Entrez le nom du dossier : ")
    folder_path = r"C:\id1fs\client\heterogene_primaire\{}".format(folder_name)
    os.makedirs(folder_path)
def file_copy():
    filename = input("Entrez le nom du fichier à copier: ")

    src_folder = input("Entrez le chemin d'accès complet du dossier d'origine (exemple: C:\id1fs\client\heterogene_primaire\mon_dossier_origine): ")
    dst_folder = input("Entrez le chemin d'accès complet du nouveau dossier (exemple: C:\mon_nouveau_dossier): ")
    shutil.copy(src_folder + '/' + filename, dst_folder + '/' + filename)

    print("Le fichier a été copié avec succès dans le nouveau dossier.")

def HELP() :
    print(" ***************************************************************:UTILISATION DES COMMANDES:******************************************************")
    print("*     ID1FS -GET: La commande permet aux utilisateurs d'extraire un fichier par son nom                                                          *")
    print("*         >> exemple d'utilisation de la commande get : get filename.docx                                                                        *")
    print("*     ID1FS -PUT: La commande permet aux utilisateurs d'ajouter un nouveau fichier au système de fichiers en donnant le chemin                   *")
    print("*         >> exemple d'utilisation de la commande put : put /path/to/documentname.txt                                                            *")
    print("*     ID1FS -G -LOG:       cette commande permet d'affcher des information sur laconsultation de fichier                                         *")
    print("*     ID1FS -SU:	  cet outil utilise pour supprimer les fichiers.                                                                             *")
    print("*     ID1FS -HELP:    cet outil fournit des informations d'aide apropos des commandes de id1fs.                                                  *")
    print("*     ID1FS -CF:   cet outil utilise pour créer un nouveau fichier.                                                                              *")
    print("*     ID1FS -ROM:  cet outil utilise renommer un fichier.                                                                                        *")
    print("*     ID1FS -QUIT:    cet outil utilise l'arrêt du system.                                                                                       *")
    print("*     ID1FS -LI:      cet outil utilise pour lister le contenu d'un dossier                                                                      *")
    print("*     ID1FS -G -META:  cet outile utilise pour donner le format de fichier(taille , permession,temp de creation,temp de modification,temp d'acce)*")
    print("*     ID1FS -CF : cette commande permet de cree un fichier                                                                                       *")
    print("*     ID1FS -COP: cette commande permet a copier un fichier                                                                                      *")
    print(" ************************************************************************************************************************************************")

if __name__== "__main__":
    main()
