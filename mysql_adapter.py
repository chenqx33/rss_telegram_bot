import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="root",
    database="mysql"
)

cursor = conn.cursor()

def insert(title, summary, url):
    cursor.execute("insert into node_seek_rss (title,summary,url) values (%s,%s,%s)", (title,summary, url))
    conn.commit()

def query(url):
    cursor.execute("select * from node_seek_rss where url=%s", (url,))
    columns = [desc[0] for desc in cursor.description]
    results = cursor.fetchall()
    result =[]
    for row in results:
        row_dict = dict(zip(columns, row))
        result.append(row_dict)
    return result

def load_keyword():
    cursor.execute("select filter_word from keyword")
    columns = [desc[0] for desc in cursor.description]
    results = cursor.fetchall()
    result =[]
    for row in results:
        row_dict = dict(zip(columns, row))
        result.append(row_dict[columns[0]])
    return result

if __name__ == '__main__':
    print(load_keyword())