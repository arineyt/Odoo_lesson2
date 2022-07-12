# -*- coding: utf-8 -*-
{
    'name': "Hospital",

    'summary': """
        Hospital System""",

    'description': """
        Hospital System
    """,

    'author': "Dmytro Stopchak",
    'category': 'Uncategorized',
    'version': '1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/patient_view.xml',
        'views/doctor_view.xml',
        'views/card_view.xml',
        'views/diagnosis_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
    'application': True,
    'license': 'LGPL-3',
}
