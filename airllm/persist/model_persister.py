


model_persister = None

class ModelPersister:
    def __init__(self):
        pass

    @classmethod
    def get_model_persister(cls):
        global model_persister
        if model_persister is not None:
            return model_persister
        from .safetensor_model_persister import SafetensorModelPersister
        model_persister = SafetensorModelPersister()
        return model_persister

    def model_persist_exist(self, layer_name, saving_path):
        pass

    def persist_model(self, state_dict, layer_name, path):
        pass

    def load_model(self, layer_name, path):
        pass