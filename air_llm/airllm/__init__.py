from sys import platform

is_on_mac_os = False

if platform == "darwin":
    is_on_mac_os = True

if is_on_mac_os:
    from .auto_model import AutoModel
else:
    from .airllm import AirLLMLlama2
    from .airllm_base import AirLLMBaseModel
    from .auto_model import AutoModel
    from .utils import split_and_save_layers
    from .utils import NotEnoughSpaceException

