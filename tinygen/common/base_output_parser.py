# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
from typing import Union


class BaseOutputParser(ABC):

    @staticmethod
    @abstractmethod
    def answer_hint() -> Union[str, None]:
        pass

    @staticmethod
    @abstractmethod
    def parse_llm_output(res) -> dict:
        pass

    @staticmethod
    @abstractmethod
    def question():
        pass


