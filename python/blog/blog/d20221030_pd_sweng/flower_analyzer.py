from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Type

import numpy as np
import pandas as pd
from python.blog.blog.d20221030_pd_sweng.flower_metaclass import \
    FlowerMetaclass


def _assert_types_compatible(prop, pd_type: type, py_type: type) -> None:
    # TODO improve
    exp_dtype = pd_type
    if pd_type == np.float64:
        exp_dtype = float
    elif isinstance(pd_type, pd.StringDtype):
        exp_dtype = str
    assert (
        exp_dtype == py_type
    ), f"{prop} type mismatch {pd_type} incompatible with {py_type}"


class FlowerReport:
    # some standard structure that can be converted to pdf, html, etc
    pass


class FlowerSample(metaclass=FlowerMetaclass):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float
    species: str


class FlowerData:
    def __init__(self, df: pd.DataFrame):
        annos = FlowerSample.__dict__["__annotations__"]
        for prop, dtype in annos.items():
            _assert_types_compatible(prop, df.dtypes[prop], dtype)
        self.df = df

    @property
    def descriptor(self) -> Type[FlowerSample]:
        return FlowerSample


class FlowerAnalyzer(ABC):
    @abstractmethod
    def analyze(self, data: FlowerData) -> FlowerReport:
        ...
