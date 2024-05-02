import psycopg2

# Connect to your postgres DB
conn = psycopg2.connect("dbname=test user=postgres password=secret")

# Open a cursor to perform database operations
cur = conn.cursor()

# Function that returns all records based on a pattern
cur.execute("""
CREATE OR REPLACE FUNCTION get_records(pattern VARCHAR)
RETURNS TABLE(name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY SELECT * FROM PhoneBook WHERE name LIKE '%' || pattern || '%' OR phone LIKE '%' || pattern || '%';
END; $$ LANGUAGE plpgsql;
""")

# Procedure to insert new user by name and phone, update phone if user already exists
cur.execute("""
CREATE OR REPLACE PROCEDURE insert_or_update_user(name VARCHAR, phone VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM PhoneBook WHERE name = insert_or_update_user.name) THEN
        UPDATE PhoneBook SET phone = insert_or_update_user.phone WHERE name = insert_or_update_user.name;
    ELSE
        INSERT INTO PhoneBook(name, phone) VALUES (insert_or_update_user.name, insert_or_update_user.phone);
    END IF;
END; $$;
""")

# Procedure to insert many new users by list of name and phone
cur.execute("""
CREATE OR REPLACE PROCEDURE insert_many_users(users_list PhoneBook[])
LANGUAGE plpgsql AS $$
DECLARE
    user_record PhoneBook;
    incorrect_data PhoneBook[] := ARRAY[]::PhoneBook[];
BEGIN
    FOREACH user_record IN ARRAY users_list
    LOOP
        IF user_record.phone ~ '^[0-9]+$' THEN
            CALL insert_or_update_user(user_record.name, user_record.phone);
        ELSE
            incorrect_data := incorrect_data || user_record;
        END IF;
    END LOOP;
    RETURN incorrect_data;
END; $$;
""")

# Function to querying data from the tables with pagination
cur.execute("""
CREATE OR REPLACE FUNCTION get_records_with_pagination(limit INT, offset INT)
RETURNS TABLE(name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY SELECT * FROM PhoneBook ORDER BY name LIMIT get_records_with_pagination.limit OFFSET get_records_with_pagination.offset;
END; $$ LANGUAGE plpgsql;
""")

# Procedure to deleting data from tables by username or phone
cur.execute("""
CREATE OR REPLACE PROCEDURE delete_user(name_or_phone VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    DELETE FROM PhoneBook WHERE name = delete_user.name_or_phone OR phone = delete_user.name_or_phone;
END; $$;
""")

# Close communication with the database
cur.close()
conn.close()
