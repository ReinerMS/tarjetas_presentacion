from sqlalchemy import text

get_bd_logs = text("select * from logs")

post_bd_logs = text("INSERT INTO tarjetaspresentacion.logs (email, `table`, `change`) VALUES(:email, :table , :change)")