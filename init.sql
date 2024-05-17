CREATE TABLE IF NOT EXISTS users_phones (
  id SERIAL PRIMARY KEY,
  phone_number BIGINT NOT NULL
);

CREATE TABLE IF NOT EXISTS users_emails (
  id SERIAL PRIMARY KEY,
  email VARCHAR(255) NOT NULL
);

INSERT INTO users_phones(phone_number) VALUES (70000000000);
INSERT INTO users_emails(email) VALUES ('test@test.test');

DO
$$
BEGIN
  IF NOT EXISTS (SELECT 1 FROM pg_catalog.pg_roles WHERE rolname ='postgres1') THEN
    CREATE USER postgres1 WITH REPLICATION ENCRYPTED PASSWORD 'Qq12345';
  END IF;
END
$$;
