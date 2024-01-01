# -*- coding: utf-8 -*-

import cmd
from tinygen.agents.sql_db_agent import SqlDbAgent
from tinygen.llm.llama_2_70b import Llama2_70B


class SqlDbCmd(cmd.Cmd):

    intro = ('Welcome to use sql llm assistant. give me a db uri, and I use '
             'baidu qianfan llama2_70B model, so you shold give me an baidu token. '
             'Then you ask me any question about that db')

    prompt = '(sql-cmd): '

    db_uri: str = None
    token: str = None

    def do_setup_db(self, db_uri):
        self.db_uri = db_uri

    def do_setup_token(self, token):
        self.token = token

    def do_ask(self, question):
        llm = Llama2_70B(token=self.token)
        agent = SqlDbAgent(llm=llm, db_uri=self.db_uri)
        print(agent.invoke(question))


def sql_db_cmd_run():
    SqlDbCmd().cmdloop()
