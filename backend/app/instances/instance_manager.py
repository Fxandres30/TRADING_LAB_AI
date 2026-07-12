class InstanceManager:

    def __init__(self):

        self.instances = {}

    def add(self, instance):

        self.instances[instance.id] = instance

    def remove(self, instance_id):

        self.instances.pop(instance_id, None)

    def get(self, instance_id):

        return self.instances[instance_id]

    def all(self):

        return list(self.instances.values())

    def enabled(self):

        return [

            i

            for i in self.instances.values()

            if i.enabled

        ]