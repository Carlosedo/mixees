from graphene import relay, ObjectType, resolve_only_args
from graphene.contrib.django.filter.fields import DjangoFilterConnectionField
from graphene.contrib.django.types import DjangoNode

from .models import Cocktail


# Graphene will automatically map the User model's fields onto the UserType.
# This is configured in the UserType's Meta class (as you can see below)
# class CategoryNode(DjangoNode):
#     class Meta:
#         model = Category
#         filter_fields = ['name', 'ingredients']
#         filter_order_by = ['name']


class CocktailNode(DjangoNode):
    class Meta:
        model = Cocktail
        # Allow for some more advanced filtering here
        # filter_fields = {
        #     'title': ['exact', 'icontains', 'istartswith'],
        #     # 'notes': ['exact', 'icontains'],
        #     # 'category': ['exact'],
        #     # 'category__name': ['exact'],
        # }
        # filter_order_by = ['title']


class Query(ObjectType):
    cocktail = relay.NodeField(CocktailNode)
    all_cocktails = relay.ConnectionField(CocktailNode)

    @resolve_only_args
    def resolve_all_cocktails(self, **kwargs):
        return Cocktail.objects.all()

    class Meta:
        abstract = True
