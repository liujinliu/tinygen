# -*- coding: utf-8 -*-

from tinygen.common.base_agent import BaseAgent
from tinygen.tools.query_database import (
    ToolShowTableNames, ToolShowTableColumnInfo, ToolQueryDataBySql)


class SqlDbAgent(BaseAgent):

    def __init__(self, *, llm, db_uri, **kwargs):
        super(SqlDbAgent, self).__init__(llm=llm)
        self.__tools = [ToolShowTableNames(db_uri=db_uri),
                ToolShowTableColumnInfo(db_uri=db_uri),
                ToolQueryDataBySql(db_uri=db_uri)]

    @property
    def tools(self):
        return self.__tools
