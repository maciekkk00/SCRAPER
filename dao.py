import psycopg2
def getConnection():
    conn = psycopg2.connect(
            host = "",
            database = "",
            user = "",
            password = ""
        )
    return conn

def insertData(recipe, tableName):

    conn = getConnection()
    cur = conn.cursor()
    insertSql = f"""
                INSERT INTO recipes 
                (id_recipe, title, description, image)
                values ('{recipe[0]}', '{recipe[1]}', '{recipe[2]}', '{recipe[3]}')
                 """

    cur.execute(insertSql)
    conn.commit()
    cur.close()
    conn.close()

def insertData2(listaSkladnikow, tableName):

    conn = getConnection()
    cur = conn.cursor()
    insertSql = f"""
                UPDATE recipes
                SET skladnik1 = '{listaSkladnikow[1]}',
                    skladnik2 = '{listaSkladnikow[2]}',
                    skladnik3 = '{listaSkladnikow[3]}',
                    skladnik4 = '{listaSkladnikow[4]}',
                    skladnik5 = '{listaSkladnikow[5]}',
                    skladnik6 = '{listaSkladnikow[6]}',
                    skladnik7 = '{listaSkladnikow[7]}',
                    skladnik8 = '{listaSkladnikow[8]}',
                    skladnik9 = '{listaSkladnikow[9]}',
                    skladnik10 = '{listaSkladnikow[10]}'
                WHERE id_recipe = {listaSkladnikow[0]};
                 """

    cur.execute(insertSql)
    conn.commit()
    cur.close()
    conn.close()

def truncateTable(tableName):

    conn = getConnection()
    cur = conn.cursor()

    truncateSql = f"""
                truncate table {tableName}
                """
    cur.execute(truncateSql)
    conn.commit()
    cur.close()
    conn.close()