# -*- coding: utf-8 -*-
from abc import ABC
from sqlalchemy import create_engine, MetaData, text
from sqlalchemy.orm import Session
from tinygen.common.base_tool import BaseTool


class BaseQueryDatabase(BaseTool, ABC):

    def __init__(self, *, db_uri, **kwargs):
        super(BaseQueryDatabase, self).__init__()
        self.engine = create_engine(url=db_uri)


class ToolShowTableNames(BaseQueryDatabase):

    def update(self, **kwargs):
        pass

    @property
    def priori_information(self):
        return f'The tables you can use are: {",".join(self._get_tables())}'

    def _get_tables(self):
        meta_obj = MetaData()
        meta_obj.reflect(bind=self.engine)
        return [table_name for table_name in meta_obj.tables]

    def run(self):
        self._get_tables()


class ToolShowTableColumnInfo(BaseQueryDatabase):

    def __init__(self, *, db_uri, **kwargs):
        super(ToolShowTableColumnInfo, self).__init__(db_uri=db_uri)
        self._table_info = []
        self._tables = []

    def update(self, **kwargs):
        self._tables = kwargs.get('table_names', [])

    @property
    def priori_information(self):
        ret = [f'The table and their columns are as followings: ']
        for info in self._table_info:
            ret.append(f'{info["name"]}: {",".join(info["columns"])}')
        return '\n'.join(ret) if len(ret) > 1 else ''

    def __get_table_columns_infos(self):
        meta_obj = MetaData()
        meta_obj.reflect(bind=self.engine)
        ret = []
        for table_name in self._tables:
            tmp = dict(name=table_name, columns=[])
            for column in meta_obj.tables[self._tables[0]].c:
                tmp['columns'].append(column.name)
            ret.append(tmp)
        self._table_info = ret

    def run(self):
        self.__get_table_columns_infos()


class ToolQueryDataBySql(BaseQueryDatabase):

    def __init__(self, *, db_uri,  **kwargs):
        super(ToolQueryDataBySql, self).__init__(db_uri=db_uri)
        self._sql = None

    def update(self, **kwargs):
        self._sql = kwargs.get('sql', None)

    @property
    def priori_information(self):
        return ''

    def run(self):
        with Session(self.engine) as session:
            return session.execute(text(self._sql)).all()

