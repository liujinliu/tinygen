# -*- coding: utf-8 -*-
from typing import Union
from abc import ABC, abstractmethod


class BaseTool(ABC):

    def __init__(self, **kwargs):
        self.para = None

    @abstractmethod
    def answer_hint(self) -> Union[str, None]:
        pass

    @abstractmethod
    def parse_llm_output(self, res) -> dict:
        pass

    @abstractmethod
    def question(self):
        pass

    @abstractmethod
    def update(self, **kwargs):
        pass

    @property
    @abstractmethod
    def priori_information(self) -> Union[str, None]:
        pass

    @abstractmethod
    def run(self) -> Union[str, bool, None]:
        pass
