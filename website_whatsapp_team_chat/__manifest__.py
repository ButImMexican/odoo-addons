# -*- coding: utf-8 -*-
{
    'name': "Website Whatsapp Team Chat",
    'summary': "Allows you to create whatsapp team support in odoo website.",
    'description': "Allows you to create whatsapp team support in odoo website.",
    'author': "ErpMstar Solutions",
    'category': 'Website',
    'version': '0.1',
    'depends': ['website'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    'images': [
        'static/description/website.jpg',
    ],
    'installable': True,
    'website': '',
    'auto_install': False,
    'price': 25,
    'currency': 'USD',
    'assets': {
         'web.assets_frontend': [
             'website_whatsapp_team_chat/static/src/js/website.js'
         ]
    },

}
