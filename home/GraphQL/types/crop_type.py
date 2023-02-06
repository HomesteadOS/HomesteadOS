from graphene_django import DjangoObjectType
from home.models import Crop


class CropType(DjangoObjectType):
    class Meta:
        model = Crop
        fields = ("name", "description", "plant_date", "harvest_date", "harvest_target_date", "yield_goal", \
                  "yield_unit", "yield_actual")