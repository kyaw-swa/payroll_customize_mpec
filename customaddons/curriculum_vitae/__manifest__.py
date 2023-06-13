{
    'name' : 'Curriculum Vitae',
     
    'author' : 'Phoe Ku',
    
    'summary' : """ 
                    Odoo ERP Develpment test project of Myanmar """ ,
                    
    'description' : """
                    test project for odoo ERP """,
                    
    'website': "https://www.kophoeku.mm.com",
                    
    'category': 'CV Form',
    'version': '0.1',
    
    'depends': [
        'base_setup',
        'mail',        
        'report_xlsx'
        ],
    
    'data' : [
        'security/ir.model.access.csv',
        'views/curriculum_vitae_simple.xml',
        'views/curriculum_vitae_simple_form_view.xml',
        'views/curriculum_vitae.xml',
        'views/curriculum_vitae_tree_view.xml',
        'views/curriculum_vitae_search_view.xml',
        'views/curriculum_vitae_form_view.xml',
        
        'reports/curriculum_vitae_simple_report.xml',
        'reports/curriculum_vitae_simple_excel_report.xml'
    ]
    
}