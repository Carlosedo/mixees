import graphene

import apps.cocktails.schema


class Query(apps.cocktails.schema.Query):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

schema = graphene.Schema(name='Mixees Schema')
schema.query = Query
