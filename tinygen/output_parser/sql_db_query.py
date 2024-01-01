# -*- coding: utf-8 -*-
import re
from typing import Union
from tinygen.common.base_output_parser import BaseOutputParser


class TableNameRequireParser(BaseOutputParser):

    @staticmethod
    def answer_hint() -> Union[str, None]:
        return f'One table name or multiple table names separated by commas '

    @staticmethod
    def parse_llm_output(res) -> dict:
        for line in res.split('\n'):
            if not line:
                continue
            if not re.match(r'[Aa]nswer: ', line.strip()):
                continue
            line_parts = re.findall(r'\b\w+\b', line)
            return dict(table_names=line_parts[1:])

    @staticmethod
    def question():
        return f'what tables should I query?'


class SqlRequireParser(BaseOutputParser):

    @staticmethod
    def answer_hint():
        return f'the sql to solve the question, wrap the sql in ```'

    @staticmethod
    def parse_llm_output(res) -> dict:
        matched = re.match(r'.*```(?:[Ss]ql)*(.*)```', res, re.DOTALL)
        return dict(sql=matched.group(1) if matched else '')

    @staticmethod
    def question():
        return f'give me the sql to solve the question, wrap the sql with ```'
