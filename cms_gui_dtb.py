from cms_dtb import *
from tkinter import *
from tkinter import messagebox

def delete_all_entery():
    enterybox_id.delete(0, END)
    enterybox_name.delete(0, END)
    enterybox_address.delete(0, END)
    enterybox_mob.delete(0, END)
    enterybox_id.focus()
    return
def addcust_btnclick():
    try:
        if(varid.get()!='' and varname.get()!='' and varaddress.get()!='' and varmob.get()!=''):
            cus=customer()
            cus.id=varid.get()
            cus.name=varname.get()
            cus.address=varaddress.get()
            cus.mob=varmob.get()
            cus.addcustomer()
            messagebox.showinfo('CMS','Customer Added Successfully')
            delete_all_entery()
        else:
            messagebox.showwarning('CMS','Please fill all the fields')
    except Exception as err:
        messagebox.showerror('CMS',err)

def searchcus_btnclick():
    if (varid.get()!= ''):
        try:
            cus=customer()
            id=varid.get()
            cus.searchcust(id)
            varname.set(cus.name)
            varaddress.set(cus.address)
            varmob.set(cus.mob)
        except Exception:
            messagebox.showwarning('CMS','No Customer found of entered ID')
    else:
        messagebox.showwarning('CMS','Please fill ID field')
def reset_btnclick():
    delete_all_entery()
def exit_btnclick():
    exit()
def delete_btnclick():
    if (varid.get() != ''):
        try:
            cus=customer()
            id = varid.get()
            cus.deletecust(id)
            messagebox.showinfo('CMS','Customer Deleted Successfully')
            delete_all_entery()
        except Exception:
            messagebox.showwarning('CMS','No Customer found of entered ID')
    else:
        messagebox.showwarning('CMS','Please fill ID field')
def modify_btnclick():
    if (varid.get() != ''):
        try:
            cus=customer()
            id=varid.get()
            name=varname.get()
            address=varaddress.get()
            mob=varmob.get()
            cus.modifycust(id,name,address,mob)
            varname.set(cus.name)
            varaddress.set(cus.address)
            varmob.set(cus.mob)
            messagebox.showinfo('CMS', 'Customer Modified Successfully')
            delete_all_entery()
        except Exception:
            messagebox.showwarning('CMS','No Customer found of entered ID')
    else:
        messagebox.showwarning('CMS','Please fill ID field')
def deleteall_btnclick():
    try:
        cus=customer()
        cus.deleteallcus()
        messagebox.showinfo('CMS', 'All Customer Deleted Successfully')
        delete_all_entery()
    except Exception:
        messagebox.showwarning('CMS','No Customer')
def sortcus_btnclick():
    try:
        cus=customer()
        cus.sortcus()
        messagebox.showinfo('CMS', 'Customer Sorted Successfully')
        delete_all_entery()
    except Exception:
        messagebox.showwarning('CMS','No Customer')
def showallcus_btnclick():
    try:
        alldata=customer.show_data()
        root2 = Tk()
        root2.title('CUSTOMER TABLE')
        lb1 = Label(root2, text='Customer ID', width=16, font=1, bg='orange').grid(row=0, column=0)
        lb1 = Label(root2, text='Customer Name', width=16, font=1, bg='red1').grid(row=0, column=1)
        lb1 = Label(root2, text='Customer Address', width=16, font=1, bg='cyan').grid(row=0, column=2)
        lb1 = Label(root2, text='Customer Mobile No.', width=16, font=1, bg='GreenYellow').grid(row=0, column=3)
        count=1
        for id,name,address,mob in alldata:
            lb2 = Label(root2, text=f'{id}', font=1,width=16, bg='yellow').grid(row=count, column=0)
            lb3 = Label(root2, text=f'{name}', font=1,width=16 ,bg='yellow').grid(row=count, column=1)
            lb4 = Label(root2, text=f'{address}',width=16 ,font=1, bg='yellow').grid(row=count, column=2)
            lb5 = Label(root2, text=f'{mob}', font=1,width=16 ,bg='yellow').grid(row=count, column=3)
            count+=1
    except Exception:
        messagebox.showwarning('CMS','No Customer')


root1=Tk()
root1.title('CUSTOMER MANAGEMENT SYSTEM')
root1.geometry()
root=Frame(root1)
root.pack()

#labels
label=['Enter Customer Id :','Enter Customer Name :','Enter Customer Address :','Enter Customer Mobile number :']
for i in range(len(label)):
    cur_label=Label(root,text=label[i],font=1).grid(row=i,column=0,sticky=W,padx=10,pady=10)

#entery variables
varid=StringVar()
varname=StringVar()
varaddress=StringVar()
varmob=StringVar()

#entery widgets
enterybox_id=Entry(root,width=40,textvariable=varid,bd=10)
enterybox_id.grid(column=1,row=0,sticky=W,padx=10,pady=10)
enterybox_id.focus()
enterybox_name=Entry(root,width=40,textvariable=varname,bd=10)
enterybox_name.grid(column=1,row=1,sticky=W,padx=10,pady=10)
enterybox_address=Entry(root,width=40,textvariable=varaddress,bd=10)
enterybox_address.grid(column=1,row=2,sticky=W,padx=10,pady=10)
enterybox_mob=Entry(root,width=40,textvariable=varmob,bd=10)
enterybox_mob.grid(column=1,row=3,sticky=W,padx=10,pady=10)

#buttons
button_add=Button(root,text='Add Customer',width=20,height=3,font=1,bg='orange',bd=10,command=addcust_btnclick)
button_add.grid(row=6,column=0,sticky=N,padx=10,pady=10)

button_search=Button(root,text='Search Customer',width=20,height=3,font=1,bg='yellow',bd=10,command=searchcus_btnclick)
button_search.grid(row=6,column=1,sticky=N,padx=10,pady=10)

button_delete=Button(root,text='Delete Customer',width=20,height=3,font=1,bg='cyan',bd=10,command=delete_btnclick)
button_delete.grid(row=6,column=2,sticky=N,padx=30,pady=10)

button_modify=Button(root,text='Modify customer',width=20,height=3,font=1,bg='GreenYellow',bd=10,command=modify_btnclick)
button_modify.grid(row=7,column=0,sticky=N,padx=10,pady=10)

button_deleteall=Button(root,text='Delete all Customer',width=20,height=3,font=1,bg='DeepPink',bd=10,command=deleteall_btnclick)
button_deleteall.grid(row=7,column=1,sticky=N,padx=10,pady=10)

button_sortcus=Button(root,text='Sort Customer',width=20,height=3,font=1,bg='pink',bd=10,command=sortcus_btnclick)
button_sortcus.grid(row=7,column=2,sticky=N,padx=30,pady=10)

button_showallcus=Button(root,text='Show all Customer',width=20,height=3,font=1,bg='lightblue',bd=10,command=showallcus_btnclick)
button_showallcus.grid(row=8,column=0,sticky=N,padx=10,pady=10)

button_reset=Button(root,text='Reset',width=20,height=3,font=1,bg='grey',bd=10,command=reset_btnclick)
button_reset.grid(row=8,column=1,sticky=N,padx=10,pady=10)

button_quit=Button(root,text='Quit',width=20,height=3,font=1,bg='red',bd=10,command=exit_btnclick)
button_quit.grid(row=8,column=2,sticky=N,padx=30,pady=10)

root.mainloop()