# -*- coding: utf-8 -*-
{
    'name': "medic_hn",

    'category': 'Sales',
    'version': '12.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'muk_web_theme'],

    # always loaded
    'data': [
        #'data/hn_sale_data.xml',
        #'data/hn_sale_sequence.xml',
        'security/rules.xml',
        'security/ir.model.access.csv',
        
        #'wizard/consolidate_orders.xml'
        #'report/report_layout.xml',
        #'report/account_invoice.xml',
        #'report/poa_report_templates.xml',
        #'report/poa_report_pivot.xml',
        #'report/pei_pivot.xml',
        'views/patient.xml',
        
    ],
    # only loaded in demonstration mode
    
}