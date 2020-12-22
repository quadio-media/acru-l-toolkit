class CustomResourceEventHandler:
    def __call__(self, event, context):
        print(event)
        request_type = event["RequestType"]
        if request_type == "Create":
            return self._on_create(event)
        if request_type == "Update":
            return self._on_update(event)
        if request_type == "Delete":
            return self._on_delete(event)
        raise Exception("Invalid request type: %s" % request_type)

    def on_create(self, event):
        raise NotImplementedError()

    def on_update(self, event):
        raise NotImplementedError()

    def on_delete(self, event):
        raise NotImplementedError()

    def _on_create(self, event):
        props = event["ResourceProperties"]
        print("create new resource with props %s" % props)
        physical_id = self.on_create(event)
        if physical_id:
            return {"PhysicalResourceId": physical_id}

    def _on_update(self, event):
        physical_id = event["PhysicalResourceId"]
        props = event["ResourceProperties"]
        print("update resource %s with props %s" % (physical_id, props))
        self.on_update(event)

    def _on_delete(self, event):
        physical_id = event["PhysicalResourceId"]
        print("delete resource %s" % physical_id)
        self.on_delete(event)
