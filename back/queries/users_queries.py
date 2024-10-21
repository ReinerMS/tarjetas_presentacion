from sqlalchemy import text

get_bd_users = text("select * from users")

post_users = text("INSERT INTO tarjetaspresentacion.users (email, name, lastName, company, password, status) VALUES(:email, :name, :lastName, :company, :password, :status)")

consult_bd_users = text("SELECT email, password FROM tarjetaspresentacion.users WHERE email = :email AND password = :password")

check_email_query = text("SELECT COUNT(*) FROM users WHERE email = :email")