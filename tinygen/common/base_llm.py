# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod


class BaseLLM(ABC):

    @abstractmethod
    def run(self, content: str) -> str:
        """
        Args:
            content: the input content to the llm model
        Returns:
            return the response string of the llm model
        """
        pass
