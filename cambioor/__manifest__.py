# -*- coding: utf-8 -*-
{
    'name': "cambioor",

    'summary': """
        Cambios al ticket de ación del módulo reparaciones pra hacerlo compatible con impresora de 58 mm""",

    'description': """
        Modificaciones al action del report y al template
        Se creo nuevo formato de papel, se creo nuevo layout
    """,

    'author': "By_Rfflz",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'repair'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    'assets': {
        'cambioor.assets': [
            'cambioor/static/src/css/**/*',
        ],
        'web.assets_qweb': [
            'cambioor/static/src/css/**/*',
        ],
    },
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
