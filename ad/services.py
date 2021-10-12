import json
from collections import OrderedDict

from django.db import connection


def dictfetchall(cursor):
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]


def get_product_all():
    with connection.cursor() as cursor:
        cursor.execute(f"""
               SELECT * ,ad.slug FROM ad_product as ad
               INNER JOIN ad_productimage as ad_pr
               ON ad.id = ad_pr.product_id
               INNER JOIN ad_image as image
               ON image.id = ad_pr.image_id                   
               INNER JOIN ad_category as ctg
               ON ad.category_id = ctg.id
               INNER JOIN auth_user 
               ON auth_user.id = ad.user_id
               ORDER BY created_date DESC       
           """)
        data = dictfetchall(cursor)
    data = _format_all(data)
    return data


def _format_all(data):
    new_data = []
    for d in data:
        if d['location']:
            region = json.loads(d['location'])['region']
            district = json.loads(d['location'])['district']
        else:
            region = None
            district = None
        new_data.append(OrderedDict([
            ('id', d['id']),
            ('title', d['title']),
            ('slug', d['slug']),
            ('decription', d['decription']),
            ('phone_number', d['phone_number']),
            ('created_date', d['created_date']),
            ('category_id', d['category_id']),
            ('product_id', d['product_id']),
            ('image', d['image']),
            ('name', d['name']),
            ('region', region),
            ('district', district),
            ('price', d['price']),
            ('username', d['username'])
        ]))
    return new_data


def get_one_product(slug):
    with connection.cursor() as cursor:
        cursor.execute(f"""
        SELECT * ,ad.slug FROM ad_product as ad
        INNER JOIN ad_productimage as ad_pr
        ON ad.id = ad_pr.product_id
        INNER JOIN ad_image as image
        ON image.id = ad_pr.image_id
        INNER JOIN ad_category as ctg
        ON ad.category_id = ctg.id
        INNER JOIN auth_user 
        ON auth_user.id = ad.user_id
        WHERE ad.slug='{slug}'           
        """)
        data = dictfetchall(cursor)
    data = _format_all(data)
    return data


def get_categories():
    with connection.cursor() as cursor:
        cursor.execute('''
            SELECT * FROM ad_category            
        ''')
        data = dictfetchall(cursor)
    return data


def category_product(ctg_slug):
    with connection.cursor() as cursor:
        cursor.execute(f"""
            SELECT ad.id as ad_id, ad.title as title, ad.slug as ad_slug, ad.decription as decription,
            ad.phone_number as phone_number, ad.created_date as created_date, ad.category_id as category_id,
            ad_pr.product_id as product_id, image.image as image,ctg.name as name, ad.location as location,
            ad.price as price, auth_user.username as username, ctg.slug as ctg_slug FROM ad_product as ad
            INNER JOIN ad_productimage as ad_pr
            ON ad.id = ad_pr.product_id
            INNER JOIN ad_image as image
            ON image.id = ad_pr.image_id
            INNER JOIN ad_category as ctg
            ON ad.category_id = ctg.id
            INNER JOIN auth_user 
            ON auth_user.id = ad.user_id
            WHERE ctg.slug ='{ctg_slug}'    
            """)
        data = dictfetchall(cursor)
    data = _format_one_caregory(data)
    return data


def _format_one_caregory(data):
    new_data = []
    for d in data:
        if d['location']:
            region = json.loads(d['location'])['region']
            district = json.loads(d['location'])['district']
        else:
            region = None
            district = None
        new_data.append(OrderedDict([
            ('id', d['ad_id']),
            ('title', d['title']),
            ('slug', d['ad_slug']),
            ('decription', d['decription']),
            ('phone_number', d['phone_number']),
            ('created_date', d['created_date']),
            ('product_id', d['product_id']),
            ('image', d['image']),
            ('name', d['name']),
            ('region', region),
            ('district', district),
            ('price', d['price']),
            ('username', d['username']),
            ('ctg_slug', d['ctg_slug'])
        ]))
    return new_data

