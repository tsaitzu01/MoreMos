def checknumber (ans,guess):
    num=9
    for i in range(7,-1,-1):
        if(ans[i] == guess[i]):
           num -= 1
        else:
           break
    if(num > 6): 
        num=0
    if(num==6):
        print("恭喜你中六獎 2百元。")
        print("中獎號碼為:"+line)
    elif(num==5):
        print("恭喜你中五獎 1千元。")
        print("中獎號碼為:"+line)
    elif(num==4):
        print("恭喜你中四獎 4千元。")
        print("中獎號碼為:"+line)
    elif(num==3):
        print("恭喜你中三獎 1萬元。")
        print("中獎號碼為:"+line)
    elif(num==2):
        print("恭喜你中二獎 4萬元。")
        print("中獎號碼為:"+line)
    elif(num==1):
        print("恭喜你中頭獎 20萬元。")
        print("中獎號碼為:"+line)

f = open('invoice.txt','r')
for line in f:
    if(int(line)-12342126==0):
        print("恭喜妳中特別獎 1千萬元")
        print("中獎號碼為:"+line)
    if(int(line)-80740977==0):
        print("恭喜妳中特獎 2百萬元")
        print("中獎號碼為:"+line)
    else:
        for i in range(0,3):
            ans=["36822639","38786238","87204837"]
            num = checknumber(ans[i] , line)