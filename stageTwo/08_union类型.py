"""
演示union类型注解
"""

from typing import Union

my_list: list[Union[int, str]] = [1, 2, "hello", "spongebob"]


def func(data: Union[int, str]) -> Union[int, str]:
    pass


func()