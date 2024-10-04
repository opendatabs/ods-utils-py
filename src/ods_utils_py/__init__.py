import pkgutil
import importlib

from ._config import _check_all_environment_variables_are_set

_check_all_environment_variables_are_set()

# Automatically import all modules in this package
for loader, module_name, is_pkg in pkgutil.walk_packages(__path__):
    module = importlib.import_module(f"{__name__}.{module_name}")
    # Import all functions defined in __all__ from the module
    if hasattr(module, '__all__'):
        globals().update({name: getattr(module, name) for name in module.__all__})
