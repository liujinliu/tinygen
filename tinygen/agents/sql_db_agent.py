# -*- coding: utf-8 -*-

from tinygen.common.base_agent import BaseAgent
from tinygen.tools.query_database import (
    ToolShowTableNames, ToolShowTableColumnInfo, ToolQueryDataBySql)
from tinygen.output_parser.sql_db_query import (
    TableNameRequireParser, SqlRequireParser)


class SqlDbAgent(BaseAgent):

    def __init__(self, *, llm, db_uri, **kwargs):
        super(SqlDbAgent, self).__init__(llm=llm)
        self.__tools_parser_pair = self.__tools(db_uri)

    @property
    def tool_parser_pair(self):
        return self.__tools_parser_pair

    @staticmethod
    def __tools(db_uri):
        return [(ToolShowTableNames(db_uri=db_uri), TableNameRequireParser),
                (ToolShowTableColumnInfo(db_uri=db_uri), SqlRequireParser),
                (ToolQueryDataBySql(db_uri=db_uri), None)]
