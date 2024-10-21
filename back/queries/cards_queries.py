from sqlalchemy import text

get_bd_cards = text("select * from cards")

post_card = text("insert into cards (name, lastName, email, company, postName, socialNetwork1, socialNetwork2, socialNetwork3, about, photo, phone, wa, areaCode) values (:name, :lastName, :email, :company, :postName, :socialNetwork1, :socialNetwork2, :socialNetwork3, :about, :photo, :phone, :wa, :areaCode)")

delete_card_query = text("DELETE FROM tarjetaspresentacion.cards WHERE email = :email")


# Construimos manualmente la query de actualización
update_query = text("""
        UPDATE cards
        SET 
            name = COALESCE(:name, name),
            lastName = COALESCE(:lastName, lastName),
            company = COALESCE(:company, company),
            postName = COALESCE(:postName, postName),
            socialNetwork1 = COALESCE(:socialNetwork1, socialNetwork1),
            socialNetwork2 = COALESCE(:socialNetwork2, socialNetwork2),
            socialNetwork3 = COALESCE(:socialNetwork3, socialNetwork3),
            about = COALESCE(:about, about),
            photo = COALESCE(:photo, photo),
            phone = COALESCE(:phone, phone),
            wa = COALESCE(:wa, wa),
            areaCode = COALESCE(:areaCode, areaCode)
        WHERE email = :email
    """)

# Definir consulta para verificar si el correo ya existe
check_email_query = text("SELECT COUNT(*) FROM cards WHERE email = :email")