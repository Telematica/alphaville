from misc.helperpg import run_stored_procedure

def alter_user(user_id, username, passwd, role_id, disabled, first_name, last_name):

    """Calls database function in order to create/update a user"""
    sql = """
            SELECT * FROM alter_user(
                {}::integer,
                '{}'::character varying,
                '{}'::character varying,
                {}::integer,
                {}::boolean,
                '{}'::character varying,
                '{}'::character varying
            ) AS (rc integer, msg text);
            """.format(
                user_id,
                username.replace("'", "''"),
                passwd.replace("'", "''"),
                role_id,
                disabled,
                first_name.replace("'", "''"),
                last_name.replace("'", "''")
            )

    return run_stored_procedure(sql)
