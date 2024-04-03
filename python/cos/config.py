import cos.path
from configparser import ConfigParser

_CONFIG_FILEPATH = cos.path.PROJECT_DIR / "config.ini"
_CONFIG_TEMPLATE_FILEPATH = cos.path.PROJECT_DIR / "config.ini.template"

config = ConfigParser()
if not (_CONFIG_FILEPATH).exists():
    cos.path.copy(_CONFIG_TEMPLATE_FILEPATH, _CONFIG_FILEPATH)
config.read(_CONFIG_FILEPATH)


def get(section, val, allow_missing=False):
    if allow_missing and not (
        config.has_section(section) and config.has_option(section, val)
    ):
        return None
    return config.get(section, val)
