
import mysql.connector


group_number="36" #FILL IN YOUR GROUP NUMBER

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="ht21_2_group_"+group_number,
  passwd="pwd_"+group_number,
  # database="ht21_2_hotels_group_"+group_number
)


d = input("Enter the department id: ")
mycursor = mydb.cursor()
sql= """select b.Productid, e.deptid, e.title,e.description from  ht21_2_project_group_36.Department as e,  ht21_2_project_group_36.Product as b  where  e.deptid=b.deptid and e.deptid=""" + d
mycursor.execute(sql)
myresult = mycursor.fetchall()
print("Productid"+" "+" deptid "+" "+" title"+" "+"description")
print(myresult)
# for x in myresult:
#     print(str(x[0])+"  \t"+str(x[1])+"  \t"+str(x[2])+"\t"+str(x[2]))
 
print("---------------------------------------------------------")

mycursor = mydb.cursor()
sql="""select b.Productid,b.Productdesc, d.discount, e.deptid, e.title,b.baseprice-b.baseprice * d.discount/100 AS discount_price from  ht21_2_project_group_36.Department as e, ht21_2_project_group_36.ordered_products as d, ht21_2_project_group_36.Product as b  where b.Productid=d.productid and e.deptid=b.deptid;"""
mycursor.execute(sql)
myresult = mycursor.fetchall()
print("Productid"+" "+" Productdesc "+" "+" discount"+"  "+"deptid"+" "+"title "+" "+"discount_price")
print(myresult)
# print("Productid"+" "+" Productdesc "+" "+" discount"+"  "+"deptid"+" "+"title "+" "+"discount_price")
# for x in myresult:
#     print(str(x[0])+"  \t"+str(x[1])+"  \t"+str(x[2])+str(x[3])+str(x[4])+str(x[5])+str(x[6]))

print("---------------------------------------------------------")

n=input("New discount: ")
name="\"Golden Nugget\""
mycursor = mydb.cursor()
sql= f"""update ht21_2_project_group_36.ordered_products set discount= {n} where Productid= {d}"""
mycursor.execute(sql)
# mycursor.execute("update ht21_2_project_group_36.ordered_products set discount= {} where Productid= {};",(n,d))
# mycursor.execute("select b.Productid,b.Productdesc, d.discount,d.pricewithouttax, e.deptid, e.title,b.baseprice-b.baseprice * d.discount/100 AS discount_price from  ht21_2_project_group_36.Department as e, ht21_2_project_group_36.ordered_products as d, ht21_2_project_group_36.Product as b  where b.Productid=d.productid and e.deptid=b.deptid;")
myresult = mycursor.fetchall()
print("---------------------------------------------------------")
mycursor = mydb.cursor()
sql="""select b.Productid,b.Productdesc, d.discount, e.deptid, e.title,b.baseprice-b.baseprice * d.discount/100 AS discount_price from  ht21_2_project_group_36.Department as e, ht21_2_project_group_36.ordered_products as d, ht21_2_project_group_36.Product as b  where b.Productid=d.productid and e.deptid=b.deptid;"""
mycursor.execute(sql)
myresult = mycursor.fetchall()
print("Productid"+" "+" Productdesc "+" "+" discount"+"  "+"deptid"+" "+"title "+" "+"discount_price")
print(myresult)
# print("Productid"+" "+" Productdesc "+" "+" discount"+"  "+"deptid"+" "+"title "+" "+"discount_price")
# for x in myresult:
#     print(str(x[0])+"  \t"+str(x[1])+"  \t"+str(x[2])+str(x[3])+str(x[4])+str(x[5])+str(x[6]))


mydb.commit()

mydb.close()