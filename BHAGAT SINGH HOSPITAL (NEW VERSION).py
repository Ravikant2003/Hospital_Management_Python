val1={1:'display',2:'appointment_form',3:"health_report",4:"patient_form",5:"staff_entry",6:"bill",7:"edit",8:"delete",9:"revenue",10:"exit"}
def menu1():
    print("_"*50)
    print("|          BHAGAT SINGH MEMORIAL HOSPITAL         |       ")
    print("|           SECTOR-5,NEAR AZAD MAIDAN             |")
    print("|             BHILAI,CHHATTISGARH                 |                 ")
    print("_"*50)
    print("                                                     ")
    print("             W    E    L    O    M   E               ")
    print("   Please type the key corresponding to your need:")
    print("_"*50)
    print('{:<6} {:1} {:30} {:2} {:15}'.format("SNO-NO","|","ACTION","|","KEY     |"))
    print("{:<6} {:1} {:30} {:2} {:15}".format("01","|","TO DISPLAY A RECORD ","|","press  1|"))
    print("{:<6} {:1} {:30} {:2} {:15}".format("02","|","APPOINTMENT OF NEW PATIENT","|","press  2|"))
    print("{:<6} {:1} {:30} {:2} {:15}".format("03","|","CREATE HEALTH REPORT","|","press  3|"))    
    print("{:<6} {:1} {:30} {:2} {:15}".format("04","|","TO FILL PATIENT FORM","|","press  4|"))
    print("{:<6} {:1} {:30} {:2} {:15}".format("05","|","ENTRY OF A NEW STAFF","|","press  5|"))
    print("{:<6} {:1} {:30} {:2} {:10}".format("06","|","MAKE A BILL","|","press  6|"))
    print("{:<6} {:1} {:30} {:2} {:15}".format("07","|","TO EDIT AN EXISTING RECORD ","|","press  7|"))
    print("{:<6} {:1} {:30} {:2} {:10}".format("08","|","TO DELETE AN EXISTING RECORD ","|","press  8|"))
    print("{:<6} {:1} {:30} {:2} {:10}".format("09","|","TOTAL REVENUE OF HOSPITAL ","|","press  9|"))
    print("{:<6} {:1} {:30} {:2} {:10}".format("10","|","TO EXIT ","|","press 10|"))
    print("_"*50)
    key=int(input("WRITE THE CORRESPONDING KEY:"))
    return val1[key]
def menu2():
    print("   PLEASE TYPE THE KEY CORRESPONDING TO THE RECORD")
    print("   FROM THE FOLLOWING MENU ")
    print("_"*25)
    print("RECORD/TABLE      |  KEY                    ")
    print("_"*25)
    import mysql.connector as sqltor
    mycon=sqltor.connect(host="localhost",user="root",passwd=pass_mysql,database="HOSPITAL_BHAGATSINGH")
    cursor=mycon.cursor()
    cursor.execute("SHOW TABLES")
    data=cursor.fetchall()
    table={}
    for i in range(len(data)):
        table[i+1]=data[i][0]
        print("{}-------->{}".format(data[i][0],i+1))
        print()
    print("_"*25)
    print()
    while True:
        name=int(input("PLEASE ENTER THE CORRESPONDING KEY :"))
        if name in table:
            name=table[name]
            return name
            break
    print()
    print()
    mycon.close()
def display1(tab):# display for health report ,patientform,new appointment,staff_entry       
    import mysql.connector as sqltor
    mycon=sqltor.connect(host="localhost",user="root",passwd=pass_mysql,database="HOSPITAL_BHAGATSINGH")
    cursor=mycon.cursor()
    cursor.execute("DESC {}".format(tab))
    data=cursor.fetchall()
    menu_items=[]
    for info in data:
        menu_items.append(info[0])
    if tab=="staff_entry":
        code=input("ENTER THE staff_ID:")
        cursor.execute('select * from {} where staff_id="{}" '.format(tab,code))
    else:
        code=input("ENTER THE patient_ID:")
        cursor.execute('select * from {} where patient_id="{}" '.format(tab,code))   
    data=cursor.fetchone()
    print("_"*60)
    print("|          BHAGAT SINGH MEMORIAL HOSPITAL                    |  ")
    print("|           SECTOR-5,NEAR AZAD MAIDAN                        |   ")
    print("|             BHILAI,CHHATTISGARH                            |    ")
    print("_"*62)
    print("                   {}                                   ".format(tab.upper()))
    print("_"*62)
    for i in range(len(menu_items)):
        print(i+1,')',''*5,menu_items[i],":",''*5,data[i])
        print(" "*60,'|')
    print("_"*60)
    print()
    print()
    mycon.close()
def display2():#FOR TABLE OF BILL        
    import mysql.connector as sqltor
    mycon=sqltor.connect(host="localhost",user="root",passwd=pass_mysql,database="HOSPITAL_BHAGATSINGH")
    cursor=mycon.cursor()   
    code=input("ENTER THE PATIENT_ID:")
    cursor.execute('select * from {} where PATIENT_ID="{}" '.format("bill",code))
    data=cursor.fetchone()
    cursor.execute("select advanced_payment from appointment_form where patient_id='{}';".format(code))
    data1=cursor.fetchone()
    if data==None:
        print("_"*80)
        print("The patient id is invalid")
        print("_"*80)
    elif data1==None:
        print("_"*80)
        print("                       NOTE                                   ")
        print("_"*80)
        print("Information related to advanced payment of the patient is not there in Appointment table ")
        print("First fill the Appointment table for the person whose bill you want to print")
        print("This is required in order to know the adavanced payment of the patient ")
        print("_"*80)
    else:
        print("_"*90)
        print("           |          BHAGAT SINGH MEMORIAL HOSPITAL                    |  ")
        print("           |           SECTOR-5,NEAR AZAD MAIDAN                        |   ")
        print("           |             BHILAI,CHHATTISGARH                            |    ")
        print("_"*90)
        print("                                  BILL                                 ")
        print("_"*90)
        print('ID:',data[0]," "*21,"NAME:",data[1]," "*10,"PHONE_NO:",data[2])
        print("ROOM:",data[3]," "*10,"DOCTOR:",data[4]," "*10,"NURSE:",data[5])
        print("MODE OF PAYMENT:",data[9])
        print("_"*90)
        print("{:<5}{:45}{:15}{:13}{:15}".format("SNO","HOSPITAL-CHARGES","COST(Rs)","TAX(5%)","TOTAL(Rs)"))
        print("{:<5}{:33}{:15}{:15}{:15} ".format(1,"BASIC FEES",200,int(200*0.05),210))   
        print("{:<5}{:33}{:15}{:15}{:15}".format(2,"DOCTOR'S CONSULTATIONS AND OTHERS",data[8],0,data[8]))
        print("{:<5}{:33}{:15}{:15}{:15}".format(3,"EARLIER ADVANCED PAYMENTS MADE",data1[0],0,data1[0]))
        print("_"*90)
        print("TOTAL COST OF MEDICINES")
        print()
        print(1,data[6],"------------->Rs",data[7])
        print("_"*90)
        print("OVERALL COST(INCLUDING ADVANCED PAYMENT)------------->Rs",210+int(data[8]+data[7]+data1[0]))#TOTAL PAYMENTDUE+ADVANCED PAYMENT
        print("PAYMENT DUE(INCLUDES MEDICINE,BASIC FEES,CONSULTATION,OTHERS)"+"------>Rs",210+data[8]+data[7]) #BASIC-FEES+CONSULTATINS CHARGES+MEDICINES-COST+DUE PAYMENT
        print()
        print("_"*90)
        print("                      T H A N K      Y O U !!!!!!                                        ")
        print("_"*90)
    print()
    print()
    mycon.close()
def new_entry(table_name):
    import mysql.connector as sqltor
    mycon=sqltor.connect(host="localhost",user="root",passwd=pass_mysql,database="HOSPITAL_BHAGATSINGH")
    cursor=mycon.cursor()
    menu=col_head(table_name)
    value=[]
    for info in menu:
        if menu[info]==b'int' or menu[info]==b'bigint':#the class is byte <class 'bytes'>
            a="enter the value for"+" "+info+":"
            a=int(input(a))
            value.append(a)
        else:
            a="enter the value for"+" "+info+":"
            a=input(a)
            value.append(a)
    value=tuple(value)
    cursor.execute("INSERT INTO {} VALUES{};".format(table_name,value))
    mycon.commit()
    print("NEW ENTRY OF RECORD HAS BEEN DONE !!!!!!!!!")
    print()
    print()
    mycon.close()
def edit(table_name):
    import mysql.connector as sqltor
    mycon=sqltor.connect(host="localhost",user="root",passwd=pass_mysql,database="HOSPITAL_BHAGATSINGH")
    cursor=mycon.cursor()
    menu=col_head(table_name)
    print("_"*60)
    for item in menu:
        if item!="PATIENT_ID" and item!="STAFF_ID":
            print(item)
        else:
            identity=item
    print("_"*50)
    col_name=input("Enter columnname whose value you want to change : ")
    if col_name in menu:#the class is byte <class 'bytes'>
        if menu[col_name]==b'int' or menu[col_name]==b'bigint':
            pat_id=input("Enter the patient_id or the staff_id according to the chosen record:")
            value=int(input("Enter the value by which you want to replace the value : "))
            cursor.execute("update {} set {colname}={val} where {ids}='{pat}'".format(table_name,ids=identity,pat=pat_id,colname=col_name,val=value))
            mycon.commit()
        else:
            pat_id=input("Enter the patient_id or the staff_id according to the chosen record:")
            val=input("Enter the value by which you want to replace : ")
            final_val=col_name+"="+'"'+val+'"'
            cursor.execute("update {} set {} where {ids}='{pat}'".format(table_name,final_val,ids=identity,pat=pat_id))
            mycon.commit()
        print("RECORD HAS BEEN EDITED !!!!!!!!!")
    else:
        print("GIVEN COLUMN NAME NOT IN THE TABLE!!!!!")
        print("TRY AGAIN!!!!")
        edit(table_name)
   
    print()
    print()
    mycon.close()
def delete(table_name):
    import mysql.connector as sqltor
    mycon=sqltor.connect(host="localhost",user="root",passwd=pass_mysql,database="HOSPITAL_BHAGATSINGH")
    cursor=mycon.cursor()
    print()
    print()
    print("_"*90)
    print("IF YOU HAVE CHOSEN STAFF_ENTRY AS RECORD PLEASE TYPE STAFF_ID")
    print("AND")
    print("IF YOU HAVE CHOSEN ANY OTHER RECORD FROM PREVIOUS MENU TYPE PATIENT_ID")
    print("_"*90)
    patient_id=input("Enter the id for the record you want to delete: ")
    if table_name=="staff_entry":
        cursor.execute("delete from {} where staff_id='{}'".format(table_name,patient_id))
        mycon.commit()
        print("RECORD CORRESPONDING TO GIVEN ID HAS BEEN DELETED !!!!!!!!!")
    else:
        cursor.execute("delete from {} where patient_id='{}'".format(table_name,patient_id))
        mycon.commit()
        print("RECORD CORRESPONDING TO GIVEN ID HAS BEEN DELETED !!!!!!!!!")
    print()
    print()
def col_head(table_name):
    import mysql.connector as sqltor
    mycon=sqltor.connect(host="localhost",user="root",passwd=pass_mysql,database="HOSPITAL_BHAGATSINGH")
    cursor=mycon.cursor()
    cursor.execute("desc {}".format(table_name))
    data=cursor.fetchall()
    menu={}
    for info in data:
        menu[info[0]]=info[1]
    return menu
def income():
    print()
    print()
    import mysql.connector as sqltor
    mycon=sqltor.connect(host="localhost",user="root",passwd=pass_mysql,database="HOSPITAL_BHAGATSINGH")
    cursor=mycon.cursor()
    cursor.execute('select cost_of_medicines,consultation_charge from bill')
    data1=cursor.fetchall()
    count=0
    basic=0
    tax=0
    cursor.execute('select advanced_payment from appointment_form')
    data2=cursor.fetchall()
    for i in data1:
        count+=int(i[0])+int(i[1])#charge of medicines colleceted
        basic+=200#summming the basic charges
        tax+=10
    for j in data2:
        count+=int(j[0])#advanced payment collected
    print("_"*60)
    print("                   THE REVENUE AND TAXES                                      ")
    print("_"*60)
    print("TAX COLLECTED IS 5% OF THE BASIC FEE COLLECTED FROM EACH PATIENT ")
    print("BASIC FEES IS:RS",200)
    print("TOTAL PATIENTS ARE:",len(data1))
    print("TAX PER PERSON IS:RS",10)
    print("TOTAL TAX COLLECTED IS :RS",tax)
    print()
    print("_"*60)
    print("THE REVENUE OF THE HOSPITAL IS :")
    print("_"*60)
    print()
    print("TOTAL BASIC FEES COLLECTED(INCLUDES tax):RS",basic)
    print()
    print("WITHOUT TAX THE TOTAL BASIC FEES IS:",basic-tax)
    print("TOTAL MONEY EARNED FROM MEDICINES/DOCTOR_CONSULTATIONS CHARGE/OTHERS:RS",count)
    print()
    print("THE NET AMOUNT EARNED(WITHOUT TAX):RS",count+basic-tax)
    print("_"*60)
    print()
    print()
def load():
    print("#"*70)
    print("IF ALREADY ENTERED THE DATABASE IN YOUR SYSTEM PRESS 'N':")
    answer=input("DO YOU WANT TO LOAD THE DATABASE AND THE TABLES(Y/N):")
    if answer=="Y":
        print("_"*50)
        print("L     O      A      D       I      N      G ")
        print("_"*50)
        with open ("mysql tables.txt",'r',encoding="utf8") as file:
            import mysql.connector as sqltor
            mycon=sqltor.connect(host="localhost",user="root",passwd=pass_mysql)
            cursor=mycon.cursor()
            cursor.execute("CREATE DATABASE HOSPITAL_BHAGATSINGH")
            cursor.execute("USE HOSPITAL_BHAGATSINGH")
            mycon.commit()
            import mysql.connector as sqltor
            mycon=sqltor.connect(host="localhost",user="root",passwd=pass_mysql,database="HOSPITAL_BHAGATSINGH")
            cursor=mycon.cursor()
            readinfo=file.readlines()
            lis=[]
            for info1 in readinfo:
                if info1=='\n' and info1==' ':
                    pass
                else:
                    info1=info1.strip("\n")
                    lis.append(info1)
            for info2 in lis[:len(lis)-1]:
                if info2==" ":
                    pass
                else:
                    #print(info2)
                    cursor.execute(info2)
                    mycon.commit()
            mycon.close()
            file.close()
            print("_"*50)
            print("DATABASE AND TABLES SUCCESFULLY LOADED...........")
            print("_"*50)
    else:
        pass
def end():
    print("#"*70)
    print("PRESS 'N' IF YOU WANT TO EXIT AND 'Y' TO DO A NEW OPERATION:")
    ans=input("DO YOU WANT TO GO TO THE MAIN MENU AND DO NEW OPERATION(Y/N):")
    if ans=="Y":
        final()
    else:
        print("_"*80)
        print("                 T  H  A  N  K       Y   O   U                  ")   
        print("        FOR    USING    THE     HOSPITAL   MANAGEMENT    SYSTEM")
        print("_"*80)      
def final():
    a=menu1()
    if a=="exit":
        print("_"*80)
        print("                 T  H  A  N  K       Y   O   U                  ")   
        print("        FOR    USING    THE     HOSPITAL   MANAGEMENT    SYSTEM")
        print("_"*80)  
    elif a=="revenue":
        income()
        end()
    elif a in ['appointment_form',"health_report","patient_form","staff_entry","bill"]:
            new_entry(a)
            end()
    else:
        b=menu2()
        if a=="display" and b=="bill":
            display2()
        elif a=="display" and b in ["health_report","appointment_form","patient_form","staff_entry"]:
            display1(b)
        elif a=="edit":
            edit(b)
        elif a=="delete":
            delete(b)
        end()
pass_mysql=input("ENTER YOUR MYSQL PASSWORD,(PRESS ENTER IF NO PASSWORD):")
load()
final()   
