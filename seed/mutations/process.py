"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import graphene
from app.models import Process
from app.models import User
from seed.schema.types import Process as ProcessType

class SaveProcessMutation(graphene.Mutation):
    
    process = graphene.Field(ProcessType)
    
    class Arguments:
        input = graphene.String(required=True)
        k = graphene.Int(required=True)
        output = graphene.Int(required=True)
        user = graphene.Int(required=True)
        pass
        
    # pylint: disable=R0912,W0622
    def mutate(self, info, **kwargs):
        user = info.context.user
        process = {}
        if "input" in kwargs:
            process["input"] = kwargs["input"]
        if "k" in kwargs:
            process["k"] = kwargs["k"]
        if "output" in kwargs:
            process["output"] = kwargs["output"]
        if "user" in kwargs:
            user = User.filter_permissions(
                User.objects,
                User.permission_filters(user)) \
                .get(pk=kwargs["user"])
            process["user"] = user
        process = \
            Process.objects.create(**process)
        process.save()
    
        return SaveProcessMutation(
            process=process)

class SetProcessMutation(graphene.Mutation):
    
    process = graphene.Field(ProcessType)
    
    class Arguments:
        id = graphene.Int(required=True)
        input = graphene.String(required=False)
        k = graphene.Int(required=False)
        output = graphene.Int(required=False)
        user = graphene.Int(required=False)
        
    # pylint: disable=R0912,W0622
    def mutate(self, info, **kwargs):
        user = info.context.user
        process = Process.filter_permissions(
            Process.objects,
            Process.permission_filters(user)) \
            .get(pk=kwargs["id"])
        if "input" in kwargs:
            process.input = kwargs["input"]
        if "k" in kwargs:
            process.k = kwargs["k"]
        if "output" in kwargs:
            process.output = kwargs["output"]
        if "user" in kwargs:
            user = User.objects \
                .get(pk=kwargs["user"])
            process.user = user
        process.save()
    
        return SetProcessMutation(
            process=process)

class DeleteProcessMutation(graphene.Mutation):
    
    id = graphene.Int()
    
    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, **kwargs):
        process_id = kwargs["id"]
        process = Process.objects.get(pk=kwargs["id"])
        process.delete()
        return DeleteProcessMutation(
            id=process_id)