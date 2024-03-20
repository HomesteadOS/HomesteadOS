import graphene
from home.GraphQL.types.crop_type import CropType
from home.models import Crop, YieldUnits


class UpdateCropMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        description = graphene.String(required=True)
        plant_date = graphene.Date(required=True)
        harvest_date = graphene.Date()
        harvest_target_date = graphene.Date()
        yield_goal = graphene.Int()
        yield_unit = graphene.ID()
        yield_actual = graphene.Int()
        id = graphene.ID()

    crop = graphene.Field(CropType)

    @classmethod
    def mutate(cls, root, info, name, description, harvest_date, harvest_target_date, yield_goal, yield_unit_id,
               yield_actual):
        crop = Crop.objects.get(pk=id)
        save_crop(crop, description, harvest_date, harvest_target_date, name, yield_actual, yield_goal,
                  yield_unit_id)

        return UpdateCropMutation(crop=crop)


class CreateCropMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        description = graphene.String(required=True)
        plant_date = graphene.Date(required=True)
        harvest_date = graphene.Date()
        harvest_target_date = graphene.Date()
        yield_goal = graphene.Int()
        yield_unit = graphene.ID()
        yield_actual = graphene.Int()

    crop = graphene.Field(CropType)

    @classmethod
    def mutate(cls, root, info, name, description, harvest_date, harvest_target_date, yield_goal, yield_unit_id,
               yield_actual):
        crop = Crop()
        save_crop(crop, description, harvest_date, harvest_target_date, name, yield_actual, yield_goal,
                      yield_unit_id)

        return CreateCropMutation(crop=crop)


def save_crop(crop, description, harvest_date, harvest_target_date, name, yield_actual, yield_goal,
              yield_unit_id):
    crop.name = name
    crop.description = description
    crop.harvest_date = harvest_date
    crop.harvest_target_date = harvest_target_date
    new_yield_unit = YieldUnits.objects.get(pk=yield_unit_id)
    crop.yield_unit = new_yield_unit
    crop.yield_goal = yield_goal
    crop.yield_actual = yield_actual
    crop.save()
