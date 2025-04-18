from setuptools import setup

setup(
    name='ckanext-govcotheme',
    version='0.0.1',
    description='Tema GOV.CO para CKAN',
    author='Víctor Ortiz',
    packages=['ckanext.govcotheme'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[],
    entry_points='''
        [ckan.plugins]
        govcotheme=ckanext.govcotheme.plugin:GovCoThemePlugin
    ''',
)
