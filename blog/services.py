from django.db import connection


def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def dictfetchone(cursor):
    desc = cursor.description
    return dict(zip([col[0] for col in desc], cursor.fetchone()))


def get_blog():
    with connection.cursor() as cursor:
        cursor.execute("""
                SELECT * FROM blog_blog
                ORDER BY created_date DESC
        """)
        data = dictfetchall(cursor)
    return data



def get_comments(id):
    with connection.cursor() as cursor:
        cursor.execute(f"""
                SELECT * FROM blog_comments
                where blog_id = {id}
        """)
        data = dictfetchall(cursor)
    return data


def last_commet():
    with connection.cursor() as cursor:
        cursor.execute("""
                SELECT au.first_name as name, bc.message, bc.created_date FROM blog_comments as bc
                INNER JOIN auth_user as au
                ON au.id = bc.user_id
                ORDER BY created_date DESC
                limit 5;
        """)
        data = dictfetchall(cursor)
    return data


def info_blog(id):
    with connection.cursor() as cursor:
        cursor.execute(f"""
                SELECT * FROM blog_blog
                where id = {id}
        """)
        data = dictfetchone(cursor)
    return data


def get_category():
    with connection.cursor() as cursor:
        cursor.execute("""
                SELECT * FROM ad_category
        """)
        data = dictfetchall(cursor)
    return data
