from setuptools import setup

setup(
    name='ckanext-govcotheme',
    version='0.0.1',
    description='Tema personalizado para CKAN',
    author='Tu Nombre',
    author_email='tu@email.com',
    packages=['ckanext.govcotheme'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[],
    entry_points='''
        [ckan.plugins]
        mytheme=ckanext.govcotheme.plugin:GovCoThemePlugin
    ''',
)
