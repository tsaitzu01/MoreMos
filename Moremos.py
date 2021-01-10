import tkinter as tk            #匯入套件一：使用者介面
from bs4 import BeautifulSoup   #匯入套件二：網路爬蟲
import requests                 #匯入套件三：資料存儲
url = 'https://www.i-fit.com.tw/context/208.html' 
html = requests.get(url)
html.encoding ="utf-8"
import matplotlib.pyplot as plt #匯入套件四：繪圖
win = tk.Tk()                   
win.geometry("400x350")
win.title("More Mos")

sp = BeautifulSoup(html.text,"html.parser")  #擷取<td>中的內容
data1 = sp.select("tbody")[0]                #data1是食物的熱量
hb = []
hbe = []
a = data1.find_all("tr")
for i in a:
    b = i.find_all('td')
    for k in range(1,11):
        if(i == a[k]):
            hb.append(float(b[1].text))
            hbe.append(float(b[2].text))
            
data2 = sp.select("tbody")[2]               #data2是需要慢跑的時間
ad = []
ade = []
a = data2.find_all("tr")
for i in a:
    b = i.find_all('td')
    for k in range(5,12):
        if(i == a[k]):
            ad.append(float(b[1].text))
            ade.append(float(b[2].text))
    
def BMI():  #計算使用者BMI及活動量，並求出每人每日應攝取熱量；呼叫check函式儲存發票號碼
    global bmi,BMI,cal
    bmi=float(w.get())/((0.01*float(h.get()))*(0.01*float(h.get())))
    label4 = tk.Label(inp, text="%.2f"%bmi)
    label4.place(relx=0.15, rely=0.7)
    cal=1
    if work.get()=="low":
        if bmi<18.5:
            cal=35*int(w.get())
        elif bmi>=18.5 and bmi<24:
            cal=30*int(w.get())
        else:
            cal=25*int(w.get())
    if work.get()=="mid":
        if bmi<18.5:
            cal=40*int(w.get())
        elif bmi>=18.5 and bmi<24:
            cal=35*int(w.get())
        else:
            cal=30*int(w.get())
    if work.get()=="high":
        if bmi<18.5:
            cal=45*int(w.get())
        elif bmi>=18.5 and bmi<24:
            cal=40*int(w.get())
        else:
            cal=35*int(w.get())
    check(num.get())

def check(num): #將發票號碼存入記事本
    f = open('invoice.txt','a')
    f.write("{}\n".format(num))
    f.close()
    
def inp():  #按下輸入資料後會執行的程式
    global inp, h, w, work, num
    win.destroy()
    inp = tk.Tk()
    inp.geometry("350x400")
    inp.title("More Mos")
    
    #標題
    label1 = tk.Label(inp, text="請輸入基本資料", font=16)
    #輸入用餐日期
    label2 = tk.Label(inp, text="用餐日期：")
    label2.place(relx=0, rely=0.1)
    year = tk.StringVar()
    entrybr1 = tk.Entry(inp, textvariable=year, width=8)
    entrybr1.place(relx=0.185, rely=0.1)
    label3 = tk.Label(inp, text="年")
    label3.place(relx=0.35, rely=0.1)
    month = tk.StringVar()
    entrybr2 = tk.Entry(inp, textvariable=month, width=5)
    entrybr2.place(relx=0.45, rely=0.1)
    label3 = tk.Label(inp, text="月")
    label3.place(relx=0.55, rely=0.1)
    day = tk.StringVar()
    entrybr3 = tk.Entry(inp, textvariable=day, width=5)
    entrybr3.place(relx=0.65, rely=0.1)
    label3 = tk.Label(inp, text="日")
    label3.place(relx=0.75, rely=0.1)
    #輸入發票號碼
    label4 = tk.Label(inp, text="發票號碼：")
    label4.place(relx=0, rely=0.2)
    num = tk.StringVar()
    entrybr4 = tk.Entry(inp, textvariable=num, width=12)
    entrybr4.place(relx=0.185, rely=0.2)
    label5 = tk.Label(inp, text="(輸入8碼數字即可)")
    label5.place(relx=0.45, rely=0.2)
    #選取每日活動量
    label3 = tk.Label(inp, text="每日活動量:")
    label3.place(relx=0, rely=0.3)
    work = tk.StringVar()
    item1 = tk.Radiobutton(inp, text="輕度工作", value="low", variable=work)
    item1.place(relx=0.2, rely=0.3)
    item2 = tk.Radiobutton(inp, text="中度工作", value="mid", variable=work)
    item2.place(relx=0.45, rely=0.3)
    item3 = tk.Radiobutton(inp, text="重度工作", value="high", variable=work)
    item3.place(relx=0.7, rely=0.3)
    item1.select()
    #提供官方資料讓使用者參考
    label5 = tk.Label(inp, text="活動量參考如下：")
    label5.place(relx=0, rely=0.35)
    label6 = tk.Label(inp, text="輕度工作 | 大部分從事靜態或坐著的工作")
    label6.place(relx=0, rely=0.4)
    label7 = tk.Label(inp, text="中度工作 | 從事機械操作、接待或家事等站立活動較多的工作")
    label7.place(relx=0, rely=0.45)
    label8 = tk.Label(inp, text="重度工作 | 從事農耕、漁業、建築等重度使用體力之工作")
    label8.place(relx=0, rely=0.5)
    #輸入身高體重
    label1.place(relx=0.35, rely=0.02)
    label1 = tk.Label(inp, text="身高：")
    label1.place(relx=0, rely=0.6)
    h = tk.StringVar()
    entrybr5 = tk.Entry(inp, textvariable=h, width=8)
    entrybr5.place(relx=0.15, rely=0.6)
    label3 = tk.Label(inp, text="公分")
    label3.place(relx=0.3, rely=0.6)
    label1 = tk.Label(inp, text="體重：")
    label1.place(relx=0.4, rely=0.6)
    w = tk.StringVar()
    entrybr6 = tk.Entry(inp, textvariable=w, width=8)
    entrybr6.place(relx=0.55, rely=0.6)
    label3 = tk.Label(inp, text="公斤")
    label3.place(relx=0.7, rely=0.6)
    #確認後按下"轉換BMI"，執行"BMI函式"
    button = tk.Button(inp, text="轉換BMI", width=8, command=BMI)
    button.place(relx=0.8, rely=0.6)
    #得到BMI結果
    label3 = tk.Label(inp, text="BMI:")
    label3.place(relx=0, rely=0.7) 
    #下一步按鈕到下一個階段
    button = tk.Button(inp, text="下一步", width=10, height=2, font=16, command=food)
    button.place(relx=0.6, rely=0.9, anchor="e")
    inp.mainloop()
    
def food(): #選取攝取食物
    global food, sbr1, sbr2, sbr3, sbr4, sbr5, sbr6, sbr7, sbr8, sbr9, sbr10
    global br1, br2, br3, br4, br5, br6, br7, br8, br9, br10
    global spa1, spa2, spa3, spa4, spa5, spa6, spa7
    global pa1, pa2, pa3, pa4, pa5, pa6, pa7
    inp.destroy()
    food = tk.Tk()
    food.geometry("370x400")
    food.title("More Mos")
    label3 = tk.Label(food, text="主食", font=16)
    label3.grid(row=0, column=0, sticky="w")

    sbr1 = tk.IntVar()
    br1 = tk.StringVar()
    entrybr1 = tk.Entry(food, textvariable=br1, width=5)
    brv1 = tk.Checkbutton(food, text="摩斯豬排堡", variable=sbr1)
    brv1.grid(row=1, column=0, sticky="w")
    entrybr1.grid(row=1, column=1, sticky="w")
    label11 = tk.Label(food, text="份    ")
    label11.grid(row=1, column=2, sticky="w")

    sbr2 = tk.IntVar()
    br2 = tk.StringVar()
    entrybr2 = tk.Entry(food, textvariable=br2, width=5)
    brv2 = tk.Checkbutton(food, text="咖哩豬排堡", variable=sbr2)
    brv2.grid(row=2, column=0, sticky="w")
    entrybr2.grid(row=2, column=1, sticky="w")
    label11 = tk.Label(food, text="份    ")
    label11.grid(row=2, column=2, sticky="w")

    sbr3 = tk.IntVar()
    br3 = tk.StringVar()
    entrybr3 = tk.Entry(food, textvariable=br3, width=5)
    brv3 = tk.Checkbutton(food, text="塔塔鱈魚堡", variable=sbr3)
    brv3.grid(row=3, column=0, sticky="w")
    entrybr3.grid(row=3, column=1, sticky="w")
    label11 = tk.Label(food, text="份    ")
    label11.grid(row=3, column=2, sticky="w")

    sbr4 = tk.IntVar()
    br4 = tk.StringVar()
    entrybr4 = tk.Entry(food, textvariable=br4, width=5)
    brv4 = tk.Checkbutton(food, text="火腿歐姆蛋堡", variable=sbr4)
    brv4.grid(row=4, column=0, sticky="w")
    entrybr4.grid(row=4, column=1, sticky="w")
    label11 = tk.Label(food, text="份    ")
    label11.grid(row=4, column=2, sticky="w")

    sbr5 = tk.IntVar()
    br5 = tk.StringVar()
    entrybr5 = tk.Entry(food, textvariable=br5, width=5)
    brv5 = tk.Checkbutton(food, text="培根雞蛋堡", variable=sbr5)
    brv5.grid(row=5, column=0, sticky="w")
    entrybr5.grid(row=5, column=1, sticky="w")
    label11 = tk.Label(food, text="份    ")
    label11.grid(row=5, column=2, sticky="w")
    
    sbr6 = tk.IntVar()
    br6 = tk.StringVar()
    entrybr6 = tk.Entry(food, textvariable=br6, width=5)
    brv6 = tk.Checkbutton(food, text="番茄吉士蛋堡", variable=sbr6)
    brv6.grid(row=6, column=0, sticky="w")
    entrybr6.grid(row=6, column=1, sticky="w")
    label11 = tk.Label(food, text="份    ")
    label11.grid(row=6, column=2, sticky="w")
    
    sbr7 = tk.IntVar()
    br7 = tk.StringVar()
    entrybr7 = tk.Entry(food, textvariable=br7, width=5)
    brv7 = tk.Checkbutton(food, text="雞肉三明治", variable=sbr7)
    brv7.grid(row=7, column=0, sticky="w")
    entrybr7.grid(row=7, column=1, sticky="w")
    label11 = tk.Label(food, text="份    ")
    label11.grid(row=7, column=2, sticky="w")
    
    sbr8 = tk.IntVar()
    br8 = tk.StringVar()
    entrybr8 = tk.Entry(food, textvariable=br8, width=5)
    brv8 = tk.Checkbutton(food, text="香米蝦三明治", variable=sbr8)
    brv8.grid(row=8, column=0, sticky="w")
    entrybr8.grid(row=8, column=1, sticky="w")
    label11 = tk.Label(food, text="份    ")
    label11.grid(row=8, column=2, sticky="w")
    
    sbr9 = tk.IntVar()
    br9 = tk.StringVar()
    entrybr9 = tk.Entry(food, textvariable=br9, width=5)
    brv9 = tk.Checkbutton(food, text="火腿蛋三明治", variable=sbr9)
    brv9.grid(row=9, column=0, sticky="w")
    entrybr9.grid(row=9, column=1, sticky="w")
    label11 = tk.Label(food, text="份    ")
    label11.grid(row=9, column=2, sticky="w")
    
    sbr10 = tk.IntVar()
    br10 = tk.StringVar()
    entrybr10 = tk.Entry(food, textvariable=br10, width=5)
    brv10 = tk.Checkbutton(food, text="日式豬排三明治", variable=sbr10)
    brv10.grid(row=10, column=0, sticky="w")
    entrybr10.grid(row=10, column=1, sticky="w")
    label11 = tk.Label(food, text="份    ")
    label11.grid(row=10, column=2, sticky="w")
    label3 = tk.Label(food, text="超值加購", font=16)
    label3.grid(row=0, column=3, sticky="w")

    spa1 = tk.IntVar()
    pa1 = tk.StringVar()
    entrypa1 = tk.Entry(food, textvariable=pa1, width=5)
    pav1 = tk.Checkbutton(food, text="洋蔥圈", variable=spa1)
    pav1.grid(row=1, column=3, sticky="w")
    entrypa1.grid(row=1, column=4, sticky="w")
    label11 = tk.Label(food, text="份    ")
    label11.grid(row=1, column=5, sticky="w")

    spa2 = tk.IntVar()
    pa2 = tk.StringVar()
    entrypa2 = tk.Entry(food, textvariable=pa2, width=5)
    pav2 = tk.Checkbutton(food, text="北海道可樂餅", variable=spa2)
    pav2.grid(row=2, column=3, sticky="w")
    entrypa2.grid(row=2, column=4, sticky="w")
    label11 = tk.Label(food, text="份    ")
    label11.grid(row=2, column=5, sticky="w")

    spa3 = tk.IntVar()
    pa3 = tk.StringVar()
    entrypa3 = tk.Entry(food, textvariable=pa3, width=5)
    pav3 = tk.Checkbutton(food, text="青蔬雞柳棒", variable=spa3)
    pav3.grid(row=3, column=3, sticky="w")
    entrypa3.grid(row=3, column=4, sticky="w")
    label11 = tk.Label(food, text="份    ")
    label11.grid(row=3, column=5, sticky="w")

    spa4 = tk.IntVar()
    pa4 = tk.StringVar()
    entrypa4 = tk.Entry(food, textvariable=pa4, width=5)
    pav4 = tk.Checkbutton(food, text="摩斯雞塊五塊", variable=spa4)
    pav4.grid(row=4, column=3, sticky="w")
    entrypa4.grid(row=4, column=4, sticky="w")
    label11 = tk.Label(food, text="份    ")
    label11.grid(row=4, column=5, sticky="w")
    
    spa5 = tk.IntVar()
    pa5 = tk.StringVar()
    entrypa5 = tk.Entry(food, textvariable=pa5, width=5)
    pav5 = tk.Checkbutton(food, text="和風炸雞", variable=spa5)
    pav5.grid(row=5, column=3, sticky="w")
    entrypa5.grid(row=5, column=4, sticky="w")
    label11 = tk.Label(food, text="份    ")
    label11.grid(row=5, column=5, sticky="w")
    
    spa6 = tk.IntVar()
    pa6 = tk.StringVar()
    entrypa6 = tk.Entry(food, textvariable=pa6, width=5)
    pav6 = tk.Checkbutton(food, text="法蘭克熱狗", variable=spa6)
    pav6.grid(row=6, column=3, sticky="w")
    entrypa6.grid(row=6, column=4, sticky="w")
    label11 = tk.Label(food, text="份    ")
    label11.grid(row=6, column=5, sticky="w")
    
    spa7 = tk.IntVar()
    pa7 = tk.StringVar()
    entrypa7 = tk.Entry(food, textvariable=pa7, width=5)
    pav7 = tk.Checkbutton(food, text="夏威夷鮮蔬沙拉", variable=spa7)
    pav7.grid(row=7, column=3, sticky="w")
    entrypa7.grid(row=7, column=4, sticky="w")
    label11 = tk.Label(food, text="份    ")
    label11.grid(row=7, column=5, sticky="w")
    #下一步按鈕到下一個階段
    button = tk.Button(food, text="下一步", width=10, height=2, font=16, command = com)
    button.place(relx=0.6, rely=0.9, anchor="e")
    food.mainloop()
    
def com():  #得到總熱量結果
    global com
    food.destroy()
    com = tk.Tk()
    com.geometry("400x200")
    com.title("More Mos")
    ttl=0
    ans ="\n您訂購的主食為 : \n"
    if sbr1.get() == 1:
        ans += "摩斯豬排堡" + br1.get() +"份，"
        ttl += hb[0] * int(br1.get())
    if sbr2.get() == 1:
        ans += "咖哩豬排堡" + br2.get() + "份，"
        ttl += hb[1] * int(br2.get())
    if sbr3.get() == 1:
        ans += "塔塔鱈魚堡" + br3.get() + "份，"
        ttl += hb[2] * int(br3.get())
    if sbr4.get() == 1:
        ans += "火腿歐姆蛋堡" + br4.get() + "份，"
        ttl += hb[3] * int(br4.get())
    if sbr5.get() == 1:
        ans += "培根雞蛋堡" + br5.get() + "份，"
        ttl += hb[4] * int(br5.get())
    if sbr6.get() == 1:
        ans += "番茄吉士蛋堡" + br6.get() + "份，"
        ttl += hb[5] * int(br6.get())
    if sbr7.get() == 1:
        ans += "雞肉三明治" + br7.get() + "份，"
        ttl += hb[6] * int(br7.get())
    if sbr8.get() == 1:
        ans += "香米蝦三明治" + br8.get() + "份，"
        ttl += hb[7] * int(br8.get())
    if sbr9.get() == 1:
        ans += "火腿蛋三明治" + br9.get() + "份，"
        ttl += hb[8] * int(br9.get())
    if sbr10.get() == 1:
        ans += "日式豬排三明治" + br10.get() + "份，"
        ttl += hb[9] * int(br10.get())
    ans +="\n您訂購的超值加購為 : \n"
    if spa1.get() == 1:
        ans += "洋蔥圈" + pa1.get() + "份，"
        ttl += ad[0] * int(pa1.get())
    if spa2.get() == 1:
        ans += "北海道可樂餅" + pa2.get() + "份，"
        ttl += ad[1] * int(pa2.get())
    if spa3.get() == 1:
        ans += "青蔬雞柳棒" + pa3.get() + "份，"
        ttl += ad[2] * int(pa3.get())
    if spa4.get() == 1:
        ans += "摩斯雞塊五塊" + pa4.get() + "份，"
        ttl += ad[3] * int(pa4.get())
    if spa5.get() == 1:
        ans += "和風炸雞" + pa5.get() + "份，"
        ttl += ad[4] * int(pa5.get())
    if spa6.get() == 1:
        ans += "法蘭克熱狗" + pa6.get() + "份，"
        ttl += ad[5] * int(pa6.get())
    if spa7.get() == 1:
        ans += "夏威夷鮮蔬沙拉" + pa7.get() + "份，"
        ttl += ad[6] * int(pa7.get())
    out = ans+"\n總共%.2f大卡"%ttl
    label4 = tk.Label(com, text=out, fg="#345995", font=14)
    label4.place(relx=0.5, anchor="n")
    #繪製圓餅圖
    labels = ["已攝取","尚未攝取"]
    absorb=float(ttl/int(cal))
    unabsorb=1-float(ttl/int(cal))
    sizes = [absorb, unabsorb]
    colors = ["#967D69","#74D3AE"]
    plt.pie(sizes,labels = labels,colors = colors , \
            labeldistance = 1.1,autopct = "%3.1f%%",shadow = False,\
            startangle = 0,pctdistance = 0.6)
    plt.legend()
    plt.axis("equal")
    plt.title("今日攝取熱量")
    label5 = tk.Label(com, text=plt.ion())
    label5.place(rely=0.5)
    #查看更多按鈕提供使用者查看更詳細資訊
    button = tk.Button(com, text="查看更多", width=10, height=2, font=16, command=exer)
    button.place(relx=0.6, rely=0.7, anchor="e")
    com.mainloop() 
    
def exer(): #計算需要運動多少時間才能消耗已攝取的熱量
    com.destroy()
    exer = tk.Tk()
    exer.geometry("400x90")
    exer.title("More Mos")
    ttl=0
    if sbr1.get() == 1:
        ttl += hbe[0] * int(br1.get())
    if sbr2.get() == 1:
        ttl += hbe[1] * int(br2.get())
    if sbr3.get() == 1:
        ttl += hbe[2] * int(br3.get())
    if sbr4.get() == 1:
        ttl += hbe[3] * int(br4.get())
    if sbr5.get() == 1:
        ttl += hbe[4] * int(br5.get())
    if sbr6.get() == 1:
        ttl += hbe[5] * int(br6.get())
    if sbr7.get() == 1:
        ttl += hbe[6] * int(br7.get())
    if sbr8.get() == 1:
        ttl += hbe[7] * int(br8.get())
    if sbr9.get() == 1:
        ttl += hbe[8] * int(br9.get())
    if sbr10.get() == 1:
        ttl += hbe[9] * int(br10.get())
    if spa1.get() == 1:
        ttl += ade[0] * int(pa1.get())
    if spa2.get() == 1:
        ttl += ade[1] * int(pa2.get())
    if spa3.get() == 1:
        ttl += ade[2] * int(pa3.get())
    if spa4.get() == 1:
        ttl += ade[3] * int(pa4.get())
    if spa5.get() == 1:
        ttl += ade[4] * int(pa5.get())
    if spa6.get() == 1:
        ttl += ade[5] * int(pa6.get())
    if spa7.get() == 1:
        ttl += ade[6] * int(pa7.get())
    out = "\t\t\t\t\t\n\n您需要慢跑【 %d 】分鐘才能消耗"%ttl
    label4 = tk.Label(exer, text=out, fg="#345995", font=14)
    label4.place(relx=0.5, anchor="n")
    
def checknumber (ans,guess):    #核對每組發票號碼分別中了幾碼
    num=9
    for i in range(7,-1,-1):
        if(ans[i] == guess[i]):
           num -= 1
        else:
           break
    return num

def ccheck():   #查看每組發票分別中了什麼獎
    win.destroy()
    ccheck = tk.Tk()
    ccheck.geometry("350x400")
    ccheck.title("More Mos")
    frame1 =tk.Frame(ccheck)
    frame1.pack()
    f = open('invoice.txt','r')
    for line in f:
        if(int(line)-12342126==0):
            label1 = tk.Label(frame1, text="恭喜您中特別獎 1千萬元。")
            label1.pack()
            label2 = tk.Label(frame1, text=("中獎號碼為:"+line))
            label2.pack()
        elif(int(line)-80740977==0):
            label3 = tk.Label(frame1, text="恭喜您中特獎 2百萬元。")
            label3.pack()
            label4 = tk.Label(frame1, text=("中獎號碼為:"+line))
            label4.pack()
        else:
            for i in range(0,3):
                ans=["36822639","38786238","87204837"]
                num = checknumber(ans[i] , line)
                if(num==6):
                    label1 = tk.Label(frame1, text="恭喜您中六獎 2百元。")
                    label1.pack()
                    label2 = tk.Label(frame1, text=("中獎號碼為:"+line))
                    label2.pack()
                elif(num==5):
                    label3 = tk.Label(frame1, text="恭喜您中五獎 1千元。")
                    label3.pack()
                    label4 = tk.Label(frame1, text=("中獎號碼為:"+line))
                    label4.pack()
                elif(num==4):
                    label5 = tk.Label(frame1, text="恭喜您中四獎 4千元。")
                    label5.pack()
                    label6 = tk.Label(frame1, text=("中獎號碼為:"+line))
                    label6.pack()
                elif(num==3):
                    label7 = tk.Label(frame1, text="恭喜您中三獎 1萬元。")
                    label7.pack()
                    label8 = tk.Label(frame1, text=("中獎號碼為:"+line))
                    label8.pack()
                elif(num==2):
                    label9 = tk.Label(frame1, text="恭喜您中二獎 4萬元。")
                    label9.pack()
                    label10 = tk.Label(frame1, text=("中獎號碼為:"+line))
                    label10.pack()
                elif(num==1):
                    label11 = tk.Label(frame1, text="恭喜您中頭獎 20萬元。")
                    label11.pack()
                    label12 = tk.Label(frame1, text="中獎號碼為:"+line)
                    label12.pack()
##主程式                
button = tk.Button(win, text="輸入資料", width=15, height=5, font=16, command=inp)  #輸入資料按鈕
button.place(relx=0.1, rely=0.5, anchor="w")
button = tk.Button(win, text="發票兌獎", width=15, height=5, font=16, command=ccheck)   #發票兌獎按鈕
button.place(relx=0.9, rely=0.5, anchor="e")

win.mainloop()