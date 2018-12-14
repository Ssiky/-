import pymysql

from conf import config


def get_conn():
    conn=pymysql.connect(host=config.db_host,
                         port=config.db_port,
                         user=config.db_user,
                         password=config.db_password,
                         db=config.db,
                         charset='utf8')
    return conn

def db_query(sql):
    conn=get_conn()
    cur=conn.cursor()
    cur.execute(sql)
    r=cur.fetchall()
    config.logging.debug(r)
    cur.close()
    conn.close()

def db_change(sql):
    config.logging.debug(sql)
    conn=get_conn()
    cur=conn.cursor()
    try:
        cur.execute(sql)
        conn.commit()
    except Exception as e:
        config.logging.error(repr(e))
        conn.rollback()
    finally:
        cur.close()
        conn.close()

def check_cardNumber(cardNumber):
    a=db_query("select * from cardinfo where cardNumber='%s'" %cardNumber )
    if a:
        return True
    return False
def check_userName(userName):
    b=db_query("select * from carduser where userName='%s'" %userName)
    if b:
        return True
    return False

def del_cardNumber(cardNumber):
    db_change("delete from cardinfo where cardNumber='%s'" %cardNumber)


if __name__=="__main__":
    print(check_cardNumber("20190101"))
    print(del_cardNumber("20190101"))
