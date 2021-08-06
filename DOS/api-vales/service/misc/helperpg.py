import psycopg2
import psycopg2.extras

from misc.common import env_property

class EmptySetError(Exception):
    pass

class ServerError(Exception):
    pass


def _connect():
    """Opens a connection to database"""
    # order here matters
    env_vars = (
        "POSTGRES_DB",
        "POSTGRES_USER",
        "POSTGRES_HOST",
        "POSTGRES_PASSWORD",
        "POSTGRES_PORT",
    )

    t = tuple(map(env_property, env_vars))
    try:
        conn_str = "dbname={0} user={1} host={2} password={3} port={4}".format(*t)
        return psycopg2.connect(conn_str)
    except:
        raise


def pgslack_exec(conn, sql):
    """Carries an sql query out to database"""
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute(sql)
    conn.commit()
    rows = cur.fetchall()
    cur.close()

    if len(rows) > 0:
        return rows

    # We should not have reached this point
    raise EmptySetError("There is no data to be returned")


def pgslack_update(conn, sql):
    """Stands for updating tables"""
    updated_rows = 0
    cur = conn.cursor()
    cur.execute(sql)
    updated_rows = cur.rowcount
    conn.commit()
    cur.close()

    if updated_rows > 0:
        return updated_rows

    # We should not have reached this point
    raise EmptySetError("Nothing was updated at all")


def pgslack_connected(func):
    """Handy decorator to fetch a database connection"""

    def wrapper(sql):
        c = _connect()
        try:
            return func(c, sql)
        except:
            raise
        finally:
            c.close()

    return wrapper


@pgslack_connected
def run_stored_procedure(conn, sql):
    """Runs a stored procedure with rich answer"""

    r = pgslack_exec(conn, sql)

    # For this case we are just expecting one row
    if len(r) != 1:
        return ["Unexpected result regarding execution of stored procedure"]

    return r.pop()


@pgslack_connected
def exec_steady(conn, sql):
    return pgslack_exec(conn, sql)


@pgslack_connected
def update_steady(conn, sql):
    return pgslack_update(conn, sql)
