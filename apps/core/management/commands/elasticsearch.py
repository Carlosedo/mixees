from django.core.management.base import BaseCommand

from apps.cocktails.search import CocktailDocType
from apps.cocktails.models import Cocktail

INDICES = {
    CocktailDocType: Cocktail,
}

AVAILABLE_INDICES = {'cocktails': CocktailDocType}


class Command(BaseCommand):
    help = 'Sync documents with ElasticSearch index'
    args = True

    def _show_help(self):
        self.stdout.write(
            'Use: ./manage.py [update_document|rebuild_index] doc_type doc_id'
        )

    def handle(self, *args, **options):
        if len(args) < 1:
            self.stdout.write('You must provide a task to execute')
            self._show_help()
            return

        if args[0] == 'update_document' and len(args) == 3:
            self.update_document(args[1], args[2])
        elif args[0] == 'rebuild_index' and len(args) == 2:
            self.rebuild_index(args[1])
        else:
            self.stdout.write('Incorrect use')
            self._show_help()
            return

    def rebuild_index(self, model_name):
        if model_name not in AVAILABLE_INDICES:
            self.stdout.write(
                'We only understand models from: {indexes}'
                    .format(
                        indexes=", ".join(AVAILABLE_INDICES.keys())
                    )
            )
            return

        doc_type = AVAILABLE_INDICES[model_name]
        page_type = INDICES[doc_type]

        for page in page_type.objects.all():
            self.update_document(doc_type, page.pk)

        # doc_type.create_alias()

    def update_document(self, index_name, document_id):
        index = self._get_index(index_name)

        if not index:
            self.stdout.write(
                'Invalid index name "{index}"'.format(index=index_name)
            )
            return

        docs = INDICES[index].objects

        if document_id == 'all':
            docs = docs.all()
        else:
            docs = docs.filter(pk=document_id)

        for doc in docs:
            if not doc:
                self.stdout.write('Invalid document id')
                return

            index.create_index_if_does_not_exist()
            index.update_document(doc)

            self.stdout.write('Synced document %s' % document_id)

    def _get_index(self, index_name):
        # if we get a class instead, get its name
        name = (
            index_name if isinstance(index_name, basestring)
            else index_name.__name__
        )
        for index in INDICES:
            if index.__name__ == name:
                return index

        return None
