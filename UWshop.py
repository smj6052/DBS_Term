import pymysql

# MySQL Connection 연결
conn=pymysql.connect(host='192.168.56.3', user='mjseo',
                    password='umshop', db='umshop', charset='utf8')

# Connection으로부터 Cursor 생성
curs=conn.cursor()

while True:
    # 사용자에게 입력받기
    print('********************************************************************')
    print('Connection')
    print('-----------------')
    ans=int(input("1. SIGN IN\n 2.SIGN UP"))
    print('********************************************************************')
    
    if(ans==1):     # 로그인 -> retrieve  
        enter_id=int(input("Id : "))
        enter_pwd=input("PWD : ")
        enter=(insert_id, insert_pwd)
        # SQL문 실행
        check_cust="select * from user"
        curs.execute(check_cust,select)
        conn.commit()
    elif(ans==2):   # 회원가입 -> insert
        insert_id=input("ID : ")
        insert_pwd=input("PWD : ")
        insert_name=input("Name : ")
        insert_tel=input("Tel : ")
        insert_adr=input("Adress : ")
        insert=(insert_id,insert_pwd,insert_name,insert_tel,insert_adr)
        # SQL문 실행
        add_cust="insert into customer (id, pwd, name, tel, adr) values(%s,%s,%s,%s)"
        curs.execute(add_cust,insert)
        conn.commit()
    elif(ans==0):   # 종료
        break
    else:
        print('잘못입력하셨습니다.')

# Connection 닫기
conn.close()


