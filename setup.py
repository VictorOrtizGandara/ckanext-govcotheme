from setuptools import setup

setup(
    name='govcotheme',
    version='0.0.1',
    description='Tema Govco para CKAN',
    author='Víctor Ortiz Gándara',
    install_requires=[],
    packages=['govcotheme'],
    include_package_data=True,
    zip_safe=False,
    entry_points='''
        [ckan.plugins]
        govcotheme=govcotheme.plugin:GovCoThemePlugin
    ''',
)
