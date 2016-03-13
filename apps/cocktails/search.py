import time

from elasticsearch_dsl import (
    DocType, String, Index, Long
)

class CocktailDocType(DocType):
    VERSION = 1
    INDEX_NAME = 'cocktails'

    DEFAULT_FIELDS = [
        'mixees_id', 'title', 'glass_type', 'skill_level'
    ]

    mixees_id = Long()
    title = String()
    glass_type = String()
    skill_level = String()

    class Meta:
        index = 'cocktails'
        doc_type = 'cocktail'

    @classmethod
    def create_index_if_does_not_exist(cls):
        index = Index(cls.INDEX_NAME)
        index.doc_type(cls)

        if not index.connection.indices.exists(cls.INDEX_NAME):
            index.create()
            time.sleep(1)  # It takes some time to create the index


    @classmethod
    def update_document(cls, cocktail):
        cls.create_index_if_does_not_exist()

        cocktail_doc = cls.get(cocktail.pk, ignore=404)

        if not cocktail_doc:
            cocktail_doc = CocktailDocType(meta={'id': cocktail.pk})

        cocktail_doc.mixees_id = cocktail.pk
        cocktail_doc.title = cocktail.title
        cocktail_doc.glass_type = cocktail.glass_type
        cocktail_doc.skill_level = cocktail.skill_level

        cocktail_doc.save()
