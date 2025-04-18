from ckan.common import CKANConfig
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class GovcoThemePlugin(plugins.SingletonPlugin):
    '''An example theme plugin.

    '''
    # Declare that this class implements IConfigurer.
    plugins.implements(plugins.IConfigurer)

    def update_config(self, config: CKANConfig):

        toolkit.add_template_directory(config, 'templates')
        toolkit.add_public_directory(config, 'public')

