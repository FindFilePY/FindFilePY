from os import*
from time import*

system('clear')
system('cd ~/')


p_last = ""
p = ""
j=0
g = ""


while(g!="q"):
    system('clear')
    print(" _____ _           _ _____ _ _      ")
    print("|  ___(_)_ ___  __| |  ___(_) | ___ ")
    print("| |_  | | '_  |/ _` | |_  | | |/ _ \ ")
    print("|  _| | | | | | (_| |  _| | | |  __/")
    print("|_|   |_|_| |_|\__,_|_|   |_|_|\___|")
    
    
    
    
    

    print("FindFilePY")
    print(p_last)
    while(1):
        p_c = input("file path:")
        if p_c=='':
            p = input(p_last+"")
            p = p_last +p
        else:
            p = p_c
            p_c = ""
    
        try:
            file_list = listdir(p)
            break
        except:
            print("Error_fx:listdir(p) The 'p:"+p+"' wasn't a effective path")
    print("files:")
    print("_____________________________________________________________")
    for i in file_list:
        sleep(0.01)
        j = j + 1
        
        if j >= 4:
            j = 0
            print("")
            #continue
        print(i,end="")
        if 20-len(i) < 0:
            j = j + 1
            for i in range(40-len(i)):
                print("",end=" ")
                
        else:
            for i in range(20-len(i)):
                print("",end=" ")
    print("")
    print("_____________________________________________________________")
    print("new file(1),open file(2),change path(c),delet file(d),exit(q)")
    g = ""
    while(g!="q"):
        g = input(":")

        if g == "1":
            g = input("file name:")
            p1 = getcwd()
            p1 = p1 + '/'
            system('touch '+g)
            system('mv '+p1+g+' '+p)
            
            
        if g =="d":
            g = input("file name:")
            if p[-1:] != '/':
                p = p + '/'
            print("Done:file '"+p+g+"'was deleted")
            system('rm -r -f '+p+g)
        if g =="show path":
            print(p)
        if g =="2":
            g = input("file name:")
            system('open '+p+'/'+g)
        if g =="c":
            p_last = p
            break
        if g =="q":
            break
        p_last = p
        if g=="":
            pass
