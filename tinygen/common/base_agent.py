# -*- coding: utf-8 -*-
from typing import List
from abc import ABC, abstractmethod
from tinygen.common.base_tool import BaseTool
from tinygen.common.base_output_parser import BaseOutputParser
from tinygen.common.base_llm import BaseLLM


class BaseAgent(ABC):

    PROMPT = """
You are an intelligent assistant

{priori_information}

Answer my question in the following format:
Answer: {tool_input}

Begin
Question: In order to solve "{question}", {tool_question} 
"""

    def __init__(self, *, llm: BaseLLM, **kwargs):
        self.llm = llm
        self.__tool_msgs = []

    @property
    @abstractmethod
    def tool_parser_pair(self) -> list:
        pass

    @property
    def priori_information(self):
        if not self.__tool_msgs:
            return ''
        informations = ['The following information are for reference:']
        msg_index = 0
        for msg in self.__tool_msgs:
            if msg:
                msg_index += 1
                informations.append(f'{msg_index}: {msg}')
        return '\n'.join(informations)

    def _ask_llm(self, output_parser: BaseOutputParser, question):
        content = self.PROMPT.format(
            priori_information=self.priori_information,
            tool_input=output_parser.answer_hint(), question=question,
            tool_question=output_parser.question())
        res = self.llm.run(content=content)
        return output_parser.parse_llm_output(res)

    def invoke(self, question):
        last_output, ret = None, None
        for tool, parser in self.tool_parser_pair:
            if last_output:
                tool.update(**last_output)
            ret = tool.run()
            self.__tool_msgs.append(tool.priori_information)
            if parser:
                last_output = self._ask_llm(parser, question)
        return ret
