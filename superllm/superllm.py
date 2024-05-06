

from .superllm_base import SuperLLMBaseModel



class SuperLLMLlama2(SuperLLMBaseModel):
    def __init__(self, *args, **kwargs):
        super(SuperLLMLlama2, self).__init__(*args, **kwargs)

