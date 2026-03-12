menu = {"아메리카노": 3000, "라떼": 3500, "에이드": 4000}


#def greet(name, msg="별일 없죠?"):
#print("안녕 ", name + ', ' + msg)
#greet("영희")

#안녕  영희, 별일 없죠?

def order_coffee(menus,num=1):
        if menus in menu:
            print(f"{menus} {num}잔 주문완료. 총액:  {menu[menus]*num}원")
        else:
            print(f"죄송합니다. {menus} 메뉴는 준비되어 있지 않습니다")

order_coffee("아메리카노")
order_coffee("에이드",3)
order_coffee("녹차",3)