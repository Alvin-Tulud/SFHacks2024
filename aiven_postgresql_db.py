import psycopg2

def main():
    conn = psycopg2.connect('postgres://avnadmin:************************@pg-343669d3-seankenruiz-0153.a.aivencloud.com:27035/defaultdb?sslmode=require')

    query_sql = 'SELECT VERSION()'

    cur = conn.cursor()
    cur.execute(query_sql)

    version = cur.fetchone()[0]
    print(version)

if __name__ == "__main__":
    main()