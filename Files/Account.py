
psd=None

def lire(who) :
    info=open(f'Saves/{who}.txt','r')
    info1=info.readlines()
    info.close()
    info2=[]
    for x in info1 :
        info2.append(x[:-1])
    return info2

def Choice(j) :
    loop1=True
    while loop1 :
        choice=input(f"\nPlayer {j},\nWhrite 'login' to log on your account,\nOr 'create' if tou havn't one yet,\nOr play without account with 'guest'\n\n - ").lower()
        global psd
        if choice=='login' :
            a,b=Login(j)
            if a!=None :
                
                psd=b
                return a, b
        elif choice=='create' :
            a,b=Create(j)
            if a!=None :
                psd=b
                return a,b
        elif choice=='guest' :
            return None, None


def Login(j) :
    loop=True
    pseudo=input(f"\nPlayer {j}, Type your nickname,\n\n - ")
    while loop :
        if pseudo.lower()=='exit' :
            return None, None
        elif pseudo==psd :
            pseudo=input("\nPseudonym already connected D:\nUse 'exit' to go back to main menu,\nOr whrite another nickname\n\n - ")
        else :
            try :
                info=lire(pseudo)
                loop=False
            except :
                pseudo=input("\nPseudonym not found D:\nUse 'exit' to go back to main menu,\nOr whrite existant nickname\n\n - ")
    loop=True
    password=input(f"\nWelcome back {pseudo},\nNow, type your password to enter\n\n - ")
    while loop :
        if password.lower()=='exit' :
            return None, None
        elif str(password)==info[0] :
            print(f"\nPlayer {j} succesfully connected !")
            return info, pseudo
        else :
            password=input("\nPassword incorrect D:\nUse 'exit' to go back to main menu,\nOr try again\n\n - ")

def Create(j) :
    loop=True
    pseudo=input("\nCreate a pseudonym (3 to 10 characters)\n\n - ")
    while loop :
        if pseudo.lower=='exit' :
            return None, None
        elif len(pseudo)>10 or len(pseudo)<3 :
            pseudo=input("\nNickname too short or too long (3 to 6 characters),\nUse 'exit' to go back to main menu,\nOr choose an other one\n\n - ")
        else :
            try :
                lire(pseudo)
                pseudo=input("\nThis nickname is already chosen,\nUse 'exit' to go back to main menu,\nOr pick an other one\n\n - ")
            except :
                loop=False
    loop=True
    password=input(f"\nGreat {pseudo},\nNow, type your password to secur your account (5 to 20 characters)\n\n - ")
    while loop :
        if password.lower()=='exit' :
            return None, None
        elif len(password)>20 or len(password)<5 :
            pseudo=input("\nPassword too short or too long (5 to 20 characters),\nUse 'exit' to go back to main menu,\nOr choose an other one\n\n - ")
        else :
            new_acc=open(f'Saves/{pseudo}.txt','w')
            new_acc.write(f"{password}\n10\nTrue\nTrue\nTrue\nFalse\nFalse\nFalse\nFalse\nFalse\nFalse\nFalse\nFalse\nFalse\nFalse\nFalse\nFalse\nFalse\nFalse\nFalse\nFalse\nTrue\n")
            new_acc.close()
            print(f"\nCongratulation {pseudo} your account has benn created !\n")
            print(f"\nPlayer {j} succesfully connected !")
            info=lire(pseudo)
            return info, pseudo
        

def Write(pseudo, pers, coin) :
    info=lire(pseudo)
    final=open(f'Saves/{pseudo}.txt','w')
    new_coin=int(info[1])+coin
    info[1]=str(new_coin)
    if pers !=None :
        info[pers]=True
    new_info=""
    for x in info :
        new_info+=f"{x}\n"
    #final.write(f"{info[0]}\n{new_coin}\n{info[2]}\n{info[3]}\n{info[4]}\n{info[5]}\n{info[6]}\n{info[7]}\n{info[8]}\n{info[9]}\n{info[10]}\n{info[11]}\n{info[12]}\n")
    final.write(new_info)
    final.close()
    info=lire(pseudo)
    return info, pseudo
