from graphene import relay, ObjectType, resolve_only_args
from graphene.contrib.django.filter.fields import DjangoFilterConnectionField
from graphene.contrib.django.types import DjangoNode

from .models import Spirit, Mixer


# Graphene will automatically map the User model's fields onto the UserType.
# This is configured in the UserType's Meta class (as you can see below)
# class CategoryNode(DjangoNode):
#     class Meta:
#         model = Category
#         filter_fields = ['name', 'ingredients']
#         filter_order_by = ['name']


class SpiritNode(DjangoNode):
    class Meta:
        model = Spirit


class MixerNode(DjangoNode):
    class Meta:
        model = Mixer


class Query(ObjectType):
    Spirit = relay.NodeField(SpiritNode)
    Mixer = relay.NodeField(MixerNode)

    all_spirits = relay.ConnectionField(SpiritNode)
    all_mixers = relay.ConnectionField(MixerNode)

    @resolve_only_args
    def resolve_all_spirits(self, **kwargs):
        return Spirit.objects.all()

    @resolve_only_args
    def resolve_all_mixers(self, **kwargs):
        return Mixer.objects.all()

    class Meta:
        abstract = True
