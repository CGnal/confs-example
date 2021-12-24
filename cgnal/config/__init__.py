import os
import re
import sys
from datetime import datetime
from functools import reduce
from typing import Sequence, Optional
from typing import Union, Any, Hashable

import cfg_load  # type: ignore
import pytz
from cfg_load import Configuration
from yaml import Loader, add_implicit_resolver, add_constructor, \
    Node, FullLoader, UnsafeLoader

from cgnal import union

PathLike = Union[str, 'os.PathLike[str]']

__this_dir__, __this_filename__ = os.path.split(__file__)

path_matcher = re.compile(r'\$\{([^}^{]+)\}')


def path_constructor(
        loader: Union[Loader, FullLoader, UnsafeLoader], node: Node
) -> PathLike:
    """
    Extract the matched value, expand env variable, and replace the match
    """
    value = node.value
    match = path_matcher.match(value)

    if match is None:
        raise SyntaxError("Can't match pattern")

    env_var = match.group()[2:-1]
    return os.environ.get(env_var) + value[match.end():]


# define custom tag handler
def joinPath(
        loader: Union[Loader, FullLoader, UnsafeLoader], node: Node
) -> PathLike:
    seq = loader.construct_sequence(node)
    return os.path.join(*seq)


# register tag handlers
add_implicit_resolver('!path', path_matcher)
add_constructor('!path', path_constructor)
add_constructor('!joinPath', joinPath)


def load(filename: PathLike) -> Configuration:
    """
    Load configuration reading given filename

    :param filename: file to read
    :return: loaded configuration
    """
    try:
        return cfg_load.load(filename, safe_load=False, Loader=Loader)
    except TypeError:
        return cfg_load.load(filename)


def get_all_configuration_file(
        application_file: PathLike = "application.yml",
        name_env: str = "CONFIG_FILE"
) -> Sequence[str]:
    """
    Retrieve all configuration files from system path, including
    the one in environment variable

    :param application_file: name of the configuration file to
        retrieve
    :param name_env: environment variable specifying the path
        to a specific configuration file
    :return: list of retrieved paths
    """
    confs = [os.path.join(path, application_file)
             for path in sys.path
             if os.path.exists(os.path.join(path, application_file))]
    env = [] if name_env not in os.environ.keys() \
        else os.environ[name_env].split(":")
    print(f"Using Configuration files: {', '.join(confs + env)}")
    return confs + env


def merge_confs(
        filenames: Sequence[PathLike],
        default: Optional[str] = "defaults.yml"
) -> Configuration:
    """
    Merge configurations in given files

    :param filenames: files to merge
    :param default: default configurations
    :return: merged configuration
    """
    lst = [default, *filenames] if default is not None else filenames
    print(f"Using Default Configuration file: {lst[0]}")
    return reduce(
        lambda config, fil: config.update(load(fil)),
        lst[1:], load(lst[0])
    )


class BaseConfig(object):
    def __init__(self, config: Configuration):
        self.config = config

    def sublevel(self, name: Hashable) -> Configuration:
        return Configuration(
            self.config[name],
            self.config.meta,
            self.config.meta["load_remote"]
        )

    def getValue(self, name: Hashable) -> Any:
        return self.config[name]

    def safeGetValue(self, name: Hashable) -> Any:
        return self.config.get(name, None)

    def update(self, my_dict: dict) -> 'BaseConfig':
        meta = union(
            self.config.meta,
            {"updated_params": my_dict,
             "modification_datetime": datetime.now().astimezone(
                 tz=pytz.timezone('Europe/Rome'))}
        )
        return type(self)(
            Configuration(union(dict(self.config), my_dict), meta)
        )
