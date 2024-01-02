# -*- coding: utf-8 -*-
from typing import List
from abc import ABC, abstractmethod
from tinygen.common.base_tool import BaseTool
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
    def tools(self) -> List[BaseTool]:
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

    def _ask_llm(self, tool: BaseTool, question):
        content = self.PROMPT.format(
            priori_information=self.priori_information,
            tool_input=tool.answer_hint(), question=question,
            tool_question=tool.question())
        res = self.llm.run(content=content)
        return tool.parse_llm_output(res)

    def invoke(self, question):
        last_output, ret = None, None
        for tool in self.tools:
            if last_output:
                tool.update(**last_output)
            ret = tool.run()
            self.__tool_msgs.append(tool.priori_information)
            if tool.question():
                last_output = self._ask_llm(tool, question)
        return ret
