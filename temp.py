import mysql.connector


def check_db():
    # mydb = mysql.connector.connect(
    #     host="dsnpdsqlhsdidev.mysql.database.azure.com",
    #     database="case_management_dev",
    #     user="case_management_admin_dev@dsnpdsqlhsdidev",
    #     password="N2JhYzc0NWFiYjIxOGE5ZjQyZDQ0YWVl",
    # )

    mydb = mysql.connector.connect(
        host="localhost",
        database="tom",
        user="root",
        password="test",
    )

    cursor = mydb.cursor()
    cursor.execute("SHOW DATABASES")

    for x in cursor:
        print(x)


if __name__ == "__main__":
    check_db()