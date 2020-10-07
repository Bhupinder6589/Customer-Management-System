from pymysql import *
#BLL starts from here
class customer:

    def __init__(self):
        self.id = ''
        self.name = ''
        self.address = ''
        self.mob = ''
    def __str__(self):
        return 'Id='+str(self.id)+' '+'Name='+str(self.name)+' '+'Address='+str(self.address)+' '+'Mobile='+str(self.mob)


    def addcustomer(self):
        conn=connect(host='localhost',database='#####',user='root',password='#####')
        cursor=conn.cursor()
        cursor.execute(f"insert into custab values('{self.id}','{self.name}','{self.address}','{self.mob}')")
        conn.commit()
        cursor.close()
        conn.close()

    def searchcust(self,id):
        conn = connect(host='localhost', database='######', user='root', password='#######')
        cursor = conn.cursor()
        number=cursor.execute(f"select * from custab where cusid='{id}'")
        if(number):
            id,name,address,mob=cursor.fetchone()
            self.id=id
            self.name=name
            self.address=address
            self.mob=mob
            return
        else:
            raise Exception

    def deletecust(self,id):
        conn = connect(host='localhost', database='######', user='root', password='######')
        cursor = conn.cursor()
        if(cursor.execute(f"select * from custab where cusid='{id}'")):
            cursor.execute(f"delete from custab where cusid='{id}'")
            conn.commit()
            return
        else:
            raise Exception

    def modifycust(self,id,name,address,mob):
        conn = connect(host='localhost', database='######', user='root', password='#####')
        cursor = conn.cursor()
        if(cursor.execute(f"select * from custab where cusid='{id}'")):
            cursor.execute(f"update custab set cusname='{name}',cusadd='{address}',cusmob='{mob}' where cusid='{id}'")
            conn.commit()
            return
        else:
            raise Exception

    @staticmethod
    def sortcus():
        conn = connect(host='localhost', database='######', user='root', password='######')
        cursor = conn.cursor()
        number=cursor.execute("select * from custab order by cusmob asc")
        print(number)
        cus=customer()
        for id, name, add, mob in cursor.fetchall():
            cus.id = id
            cus.name = name
            cus.address = add
            cus.mob = mob
            print(cus)
        cursor.close()
        conn.close()


    @staticmethod
    def show_data():
        conn=connect(host='localhost',database='######',user='root',password='#####')
        cursor=conn.cursor()
        number=cursor.execute("select * from custab")
        cursor.close()
        conn.close()
        if(number):
            return cursor.fetchall()
        else:
            raise Exception
    @staticmethod
    def deleteallcus():
        conn = connect(host='localhost', database='######', user='root', password='#######')
        cursor = conn.cursor()
        cursor.execute(f'delete from custab')
        conn.commit()
        return
#PL starts from here
if(__name__=='__main__'):

    while(True):
        print('1.add customer\n2.search customer\n3.delete customer\n4.modify customer\n5.show all customer\n6.sort customer')
        print('7.delete all customer\n8.exit')
        ch=input('enter your choice')
        if(ch=='1'):
            try:
                cus=customer()
                cus.id=input('enter id')
                cus.name=input('enter name')
                cus.address=input('enter address')
                cus.mob=input('enter mobile number')
                cus.addcustomer()
                print('customer added successfully')
            except Exception:
                print('Duplicate ID not allowed')
        elif(ch=='2'):
            try:
                cus=customer()
                id=input('enter id of customer whose content to be searched')
                cus.searchcust(id)
                print(cus)
            except Exception:
                print('No customer found of enterd ID')

        elif(ch=='3'):
            try:
                cus=customer()
                id=input('enter id of the customer whose content to be deleted')
                cus.deletecust(id)
                print('customer deleted successfully')
            except Exception:
                print('No Customer found of entered ID')
        elif(ch=='4'):
            try:
                cus=customer()
                id=input('enter id of customer whose content to be modified')
                name = input('enter new name')
                address = input('enter new address')
                mob = input('enter new mobile number')
                cus.modifycust(id,name,address,mob)
                print('customer modified successfully')
            except Exception:
                print('No Customer found of entered ID')
        elif(ch=='5'):
            try:
                cus=customer()
                allcus=customer.show_data()
                for id,name,add,mob in allcus:
                    cus.id=id
                    cus.name=name
                    cus.address=add
                    cus.mob=mob
                    print(cus)

            except Exception:
                print('No Customer')
        elif(ch=='6'):
            # try:
            #     customer.sortcus()
            #     print('customer sorted successfully')
            # except Exception:
            #     print('No Customer found')
            customer.sortcus()
        elif(ch=='7'):
            try:
                customer.deleteallcus()
                print('all customer deleted')
            except Exception:
                print('No Customer')
        elif(ch=='8'):
            exit()
        else:
            print('!!!!enter correct choice!!!!')
