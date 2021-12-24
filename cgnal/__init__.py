from copy import deepcopy as copy
from functools import reduce
from typing import Mapping


def union(*dicts: dict) -> dict:
    def __dict_merge(dct: dict, merge_dct: dict):
        """ Recursive dict merge. Inspired by :meth:``dict.update()``,
        instead of updating only top-level keys, dict_merge recurses
        down into dicts nested to an arbitrary depth, updating keys.
        The ``merge_dct`` is merged into``dct``.
        :param dct: dict onto which the merge is executed
        :param merge_dct: dct merged into dct
        :return: None
        """
        merged = copy(dct)
        for k, v in merge_dct.items():
            if (k in dct and isinstance(dct[k], dict)
                    and isinstance(merge_dct[k], Mapping)):
                merged[k] = __dict_merge(dct[k], merge_dct[k])
            else:
                merged[k] = merge_dct[k]
        return merged

    return reduce(__dict_merge, dicts)
