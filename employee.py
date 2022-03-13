import sqlite3
from prettytable import PrettyTable
data = sqlite3.connect("employeemanage.db")
table = data.execute("select name from sqlite_master where type='table' and name='details'").fetchall()
if table!=[]:
    print("Table already exists")
else:
    data.execute('''create table details(
                            empcode integer,
                            name text,
                            phone integer,
                            email text,
                            designation text,
                            salary integer,
                            cmpname text); ''')
    print("table created")

while True:
    print("1.Add employee data")
    print("2.View all employees")
    print("3.Search using employee name")
    print("4.Update using employee code")
    print("5.Delete an employee using employee code")
    print("6.Display employees whose salary is greater than 50000")
    print("7.Total number of employees")
    print("8.Display employee from lower to higher salary range")
    print("9.Display employees whose salary is less than average")
    print("10.Exit")

    a = int(input("Enter the choice:"))
    if a==1:
        getEcode = input("Enter the employee code:")
        getEname = input("Enter employee name:")
        getPhone = input("Enter employee phone number:")
        getEmail = input("Enter the email-id of employee:")
        getDesig = input("Enter the designation of employee:")
        getSal = input("Enter the salary:")
        getCname = input("Enter the company name:")
        data.execute("insert into details(empcode,name,phone,email,designation,salary,cmpname)\
         values("+getEcode+",'"+getEname+"',"+getPhone+",'"+getEmail+"','"+getDesig+"',"+getSal+",'"+getCname+"')")
        data.commit()
    elif a==2:
        result = data.execute("select * from details")
        table = PrettyTable(["Employeecode","Name","Phone","Email-Id","designation","salary","Companyname"])
        for i in result:
            table.add_row([i[0],i[1],i[2],i[3],i[4],i[5],i[6]])
        print(table)
    elif a==3:
        getEname = input("Enter the employee name to search:")
        result=data.execute("select * from details where name like '"+getEname+"%'")
        table=PrettyTable(["Employeecode","Name","Phone","Email-Id","designation","salary","Companyname"])
        for i in result:
            table.add_row([i[0],i[1],i[2],i[3],i[4],i[5],i[6]])
        print(table)
    elif a==4:
        getEcode=input("Enter the employee code to update:")
        getEname = input("Enter new employee name:")
        getPhone = input("Enter the new phone number:")
        getEmail = input("Enter the new email-id:")
        getDesig = input("Enter the new employee designation:")
        getSal = input("Enter the new salary:")
        getCname = input("Enter the new Company name:")
        data.execute("update details set name='"+getEname+"',phone="+getPhone+",email='"+getEmail+"',designation='"+getDesig+"',\
                salary="+getSal+",cmpname='"+getCname+"'\
                 where empcode="+getEcode)
        data.commit()
        print("updated successfully")
    elif a==5:
        getEcode = input("Enter the employee code to delete:")
        data.execute("delete from details where empcode="+getEcode)
        data.commit()
        print("deleted successfully")
    elif a==6:
        result=data.execute("select * from details where salary>50000")
        table = PrettyTable(["Employeecode","Name","Phone","Email-Id","designation","salary","Companyname"])
        for i in result:
            table.add_row([i[0],i[1],i[2],i[3],i[4],i[5],i[6]])
        print(table)
    elif a==7:
        result = data.execute("select count(*) as count from details")
        for i in result:
            print("Total employee:",i[0])
    elif a==8:
        getLower = input("Enter the lowest salary:")
        getHigher = input("Enter the highest salary:")
        result = data.execute("select * from details where salary between "+getLower+" and "+getHigher)
        table = PrettyTable(["Employeecode","Name","Phone","emailid","designation","salary","Companyname"])
        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6],])
        print(table)
    elif a==9:
        result = data.execute("select * from details where salary<(select avg(salary) from details)")
        table = PrettyTable(["Employeecode", "Name", "Phone", "Email-Id", "designation", "salary", "Companyname"])
        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6]])
        print(table)
    elif a==10:
        print("Exited")
        break
    else:
        print("Invalid selection")
        data.close()


