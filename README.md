## tinygen

This project showed a possible architecture that use an llm to slove the actual problem, which in other scenarios,
called ```agent``` 

### Install
```
make install
```

### Try wit an example
first download an db file [Chinook_Sqlite.sql](https://github.com/lerocha/chinook-database/blame/master/ChinookDatabase/DataSources/Chinook_Sqlite.sql)  
```
# load the db
sqlite demo.db
> .read Chinook_Sqlite.sql
```
cmd example
```
(dev38) λ sql-db-cmd
Welcome to use sql llm assistant. give me a db uri, and I use baidu qianfan llama2_70B model,
so you shold give me an baidu token. Then you ask me any question about that db
(sql-cmd): ?

Documented commands (type help <topic>):
========================================
help

Undocumented commands:
======================
ask  setup_db  setup_token

(sql-cmd): setup_db sqlite:///E:/code/tinygen/demo.db
(sql-cmd): setup_token <your-token>
(sql-cmd): ask List the total sales per country
[('Argentina', 37.620000000000005), ('Australia', 37.620000000000005), ......]
```
 
The original intention of this project, is when referring to an agent example provided by ```langchain``` 
to solve an SQL query problem, it seems that only using GPT4 can make that example success.  
Then I think that maybe we human could walk toward the llm for further, I mean we could define the steps first,
then ask llm model to give the input for each step.  
First glance at this idea, people may think it is worthless.  
But think about this scenario, you have a database, you want to know something about the datas. 
You know the following steps can help you findout the answer:   
1. findout the tables you could use
2. findout what columns they have
3. use these information to write a sql
4. query database with the sql

But...but, not every step is easy to get an answer.  

And this project, provide an possible architecture to solve this kind of problems. 
