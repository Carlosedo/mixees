from django.apps import AppConfig

from elasticsearch_dsl import connections


class CoreConfig(AppConfig):
    name = 'apps.core'

    def ready(self):
        self._init_elasticsearch()

    def _init_elasticsearch(self):
        # try:
        #     connections.connections.create_connection(
        #         hosts=settings.ES_URLS,
        #         timeout=settings.ES_TIMEOUT
        #     )
        # except Exception:
        #     logger.exception('Error connecting to the elasticsearch')

        connections.connections.create_connection(hosts=['localhost'], timeout=20)
