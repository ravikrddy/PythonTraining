import mysql.connector
import datetime

try:
    conn = mysql.connector.connect(host='localhost', user='ravikumarchundi', passwd='Bangalore@3', database='test')

    sql_stmt = "INSERT INTO SV_2nRw1ySwgxCHkfX (RecordedDate, ResponseId, Q1Response, Q2Response, Q3Response) \
                VALUES (%s, %s,%s, %s,%s);"

    rdate = '25/06/2013  6:10:50 PM'
    rid = 'R_6ojzomFr7Bl6jJz'
    q1r = '6'
    q2r = '5'
    q3r = 'Test'

    sql_data = (datetime.datetime.strptime(rdate, '%d/%m/%Y %I:%M:%S %p'), rid, q1r, q2r, q3r)

    cursor = conn.cursor()
    result = cursor.execute(sql_stmt, sql_data)
    conn.commit()
    print("Record inserted successfully")

except mysql.connector.Error as error:
    print("Failed to insert the record {}".format(error))

finally:
    if (conn.is_connected()):
        cursor.close()
        conn.close()
        print("MySQL connection is closed")
