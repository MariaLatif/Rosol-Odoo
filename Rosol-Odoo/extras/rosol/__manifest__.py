# -*- coding: utf-8 -*-
{
    'name': "Rosol Family",
    'sequence': 1,
    'summary': """
        This is a model for Rosol Family.""",
    'description': """
        This is a model for Rosol Family to help teachers to have clear review and notice every and each child they have in class.
    """,

    'author': "Maria",
    'website': "http://www.rosol.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Generic Modules',
    'version': '1.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
    'icon': 'rosol/static/description/icon.jpg',
    'application': True,
    'installable': True,
    'auto_install': False,
}
