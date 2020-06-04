

import mysql.connector 

companyList = []


try:

    connection = mysql.connector.connect(host='localhost',
                                         database='PruebaPython',
                                         user='root',
                                         password='root')

    sql_select_Query = "select * from Company"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    print("Total number of rows in Laptop is: ", cursor.rowcount)

    for row in records:

        companyList.append(row[0])

        # print("Id = ", row[0], )
        # print("Name = ", row[1])
        # print("Purchase date  = ", row[2], "\n")

except mysql.connector.Error as error:

    print("Error reading data from MySQL table", error)
finally:

    if (connection.is_connected()):
        connection.close()
        cursor.close()
        print("MySQL connection is closed")


print(companyList)