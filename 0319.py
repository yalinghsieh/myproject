import vending_machine as machine
#販賣機
flag = True

while flag:
    print('\n============================')
    select = eval(input('1.儲值\n2.購買\n3.查詢餘額\n4.離開\n請選擇:'))

    if select == 1: #儲值
        machine.deposit()

    elif select == 2: #購買
        machine.buy()

    elif select == 3: #查詢餘額
        print(f'目前餘額為{machine.balance}元')

    elif select == 4: #離開
        print('bye')
        flag = 0
        break

    else: #重新輸入
        print('====請輸入1-4之間====')
        continue
'''

weight1 = 100
weight2 = 80

def add_weight(w1, w2=1):
    result = w1 + w2
    result1 = w1 / w2
    return result, result1

x1, x2 = add_weight(weight1, weight2)
print(x1, x2)

y1, y2 = add_weight(w2=weight1, w1=weight2)
print(y1, y2)

x = add_weight(weight1,weight2)
y = add_weight(weight1)
#出錯因為函式規定要兩個變數除非將def add_weight(w1, w2=1)設定預設值Main有
print(x, y)
'''
a = "yaling is aun"
