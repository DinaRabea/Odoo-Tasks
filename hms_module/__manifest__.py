{
    'name':'hms patient module',
    'version':'1.0.0',
    'summary':'this is patient record',
    'Description':
    """
        Patient description
    """,
    'application':True,
    'data':
    [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/patient.xml',
        'views/department.xml',
        'views/doctor.xml',
        'views/menus.xml',
        'reports/report.xml',
    ]
}