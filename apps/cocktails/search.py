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
    ingredients = String()

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

        ingredient_list = []
        for ingredient in cocktail.ingredient_set.all():
            if ingredient.spirit:
                ingredient_list.append(ingredient.spirit.name)
            elif ingredient.mixer:
                ingredient_list.append(ingredient.mixer.name)

        cocktail_doc.ingredients = ingredient_list

        cocktail_doc.save()
