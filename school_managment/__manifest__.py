{
    'name':'school managment',
    'version':'1.0.0',
    'summary':'this is student record',
    'Description':
    """
        student description in my first odoo model
    """,
    'application':True,
    'data':
    [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/track_wizard.xml',
        'views/student.xml',
        'views/track.xml',
        'views/skill.xml',
        'views/menus.xml',
        'reports/report.xml',
    ]
}