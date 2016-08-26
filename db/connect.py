import config.database
import tornado_mysql
from tornado.options import options
from tornado_mysql import cursors

def mysql(sql, params=""):
    conn = yield tornado_mysql.connect(
        host    = options.host,
        port    = options.port,
        user    = options.user,
        passwd  = options.passwd,
        db      = options.db,
        charset = options.charset
    )
    cur  = conn.cursor(cursors.DictCursor)
    yield cur.execute(sql % params)
    conn.commit()
    rows = cur
    cur.close()
    conn.close()
    return rows
