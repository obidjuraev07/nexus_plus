from django.db import connection


def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def region(id):
    with connection.cursor() as cursor:
        cursor.execute(f"""
                SELECT * FROM geo_district
                where geo_district = {id}
        """)
        data = dictfetchall(cursor)
    return data    