from setuptools import setup

setup(
    name='govcotheme',
    version='0.0.1',
    description='Tema Govco para CKAN',
    author='Víctor Ortiz Gándara',
    install_requires=[],
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    namespace_packages=['ckanext'],
    include_package_data=True,
    zip_safe=False,
    entry_points='''
        [ckan.plugins]
        govcotheme=ckanext.govcotheme.plugin:GovCoThemePlugin
    ''',
)
