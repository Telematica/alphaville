--
-- Name: alter_user(integer, character varying, character varying, integer, boolean, character varying, character varying); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION public.alter_user(_user_id integer, _username character varying, _passwd character varying, _role_id integer, _disabled boolean, _first_name character varying, _last_name character varying) RETURNS record
    LANGUAGE plpgsql
    AS $$

DECLARE
    -- >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    -- >> Description: Create/Edit user                                             >>
    -- >> Version:     big in japan                                                 >>
    -- >> Date:        04/ago/2021                                                  >>
    -- >> Developer:   Omar Montes                                                  >>
    -- >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    current_moment timestamp with time zone := now();
    last_id integer := 0;
	row_counter integer := 0;

    -- dump of errors
    rmsg text := '';

BEGIN

    CASE
        WHEN _user_id = 0 THEN

            INSERT INTO users (
                username,
                passwd,
                role_id,
				disabled,
				first_name,
				last_name,
				last_touch_time,
                creation_time
            ) VALUES (
                _username,
                _passwd,
                _role_id,
				_disabled,
				_first_name,
				_last_name,
                current_moment,
                current_moment
            ) RETURNING id INTO last_id;

        WHEN _user_id > 0 THEN

			if _passwd = '' then
				
				UPDATE users
				SET username = _username,
					role_id = _role_id,
					disabled = _disabled,
					first_name = _first_name,
					last_name = _last_name,
					last_touch_time = current_moment
				WHERE id = _user_id;
			
			else
				
				UPDATE users
				SET username = _username,
					passwd = _passwd,
					role_id = _role_id,
					disabled = _disabled,
					first_name = _first_name,
					last_name = _last_name,
					last_touch_time = current_moment
				WHERE id = _user_id;
			
			end if;
			
			GET DIAGNOSTICS row_counter = ROW_COUNT;
			if row_counter <> 1 then
				RAISE EXCEPTION 'user identifier % does not exist', _user_id;
			end if;

            -- Upon edition we return user id as last id
            last_id = _user_id;

        ELSE
            RAISE EXCEPTION 'negative user identifier % is unsupported', _user_id;

    END CASE;

    return ( last_id::integer, ''::text );

    EXCEPTION
        WHEN OTHERS THEN
            GET STACKED DIAGNOSTICS rmsg = MESSAGE_TEXT;
            return ( -1::integer, rmsg::text );

END;
$$;


ALTER FUNCTION public.alter_user(_user_id integer, _username character varying, _passwd character varying, _role_id integer, _disabled boolean, _first_name character varying, _last_name character varying) OWNER TO postgres;
