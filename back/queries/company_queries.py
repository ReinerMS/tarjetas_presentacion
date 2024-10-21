from sqlalchemy import text

get_bd_company = text("select * from company")

post_company = text("INSERT INTO company (name, img) VALUES (:name, :img)")