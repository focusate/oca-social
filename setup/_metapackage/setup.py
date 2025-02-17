import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo-addons-oca-social",
    description="Meta package for oca-social Odoo addons",
    version=version,
    install_requires=[
        'odoo-addon-mail_activity_board>=15.0dev,<15.1dev',
        'odoo-addon-mail_activity_creator>=15.0dev,<15.1dev',
        'odoo-addon-mail_activity_done>=15.0dev,<15.1dev',
        'odoo-addon-mail_activity_partner>=15.0dev,<15.1dev',
        'odoo-addon-mail_attach_existing_attachment>=15.0dev,<15.1dev',
        'odoo-addon-mail_debrand>=15.0dev,<15.1dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 15.0',
    ]
)
