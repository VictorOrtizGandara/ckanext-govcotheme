import ckan.plugins as p

class GovCoThemePlugin(p.SingletonPlugin):
    p.implements(p.IConfigurer)

    def update_config(self, config):
        p.toolkit.add_template_directory(config, 'templates')
        p.toolkit.add_public_directory(config, 'public')
        p.toolkit.add_resource('assets', 'govcotheme')

