# Psycopg2 Json
[TOC]

## 背景

团队大规模的使用 AWS 后果断无法忍受其多层次全方位多体位的计费算法!

所以,对结构化非关系型文本数据,自然的要进行归并:

- 原先每个用户引发的批量数据条目的写入
- 期望有种形式, 在兼容原先的业务时,可以在 AWS 体系中变成一次IO

## 分析

挖掘了一下 AWS 的现行数据储存服务:

- S3 贵!
- DynamoDB 贵!
    - SimpleDB 呵呵
- EBS 针对的是数据块
- RDS ~ 够传统,知识储备充足
    + 刚好支持 PostgreSQL 实例
    + 而 Pg 从9.2开始引入了json数据类型
    + 这简直就是用 RMDB 的稳定性,用 MongoDB 的自然 NoSQL 哪

参考: 

- [Why JSON in PostgreSQL is Awesome](https://functionwhatwhat.com/json-in-postgresql/)  
- [JSON Select Speed Test with MongoDB and PostgreSQL](http://tiborsimko.org/postgresql-mongodb-json-select-speed.html)

## 折腾

问题来了, 怎么进行检验思路呢!?

- AWS 那真心是分秒毕争的刷你的卡哪!
- 本地架 Pg 其它小伙伴是难以跨网域访问的
- 所以,需要一个广域网上的可以快速构建/关闭的测试环境

### 青云

刚好 青云 发布了 Pg 的支持

- 文档: [数据库服务指南 — QingCloud 文档](https://docs.qingcloud.com/guide/rdbs.html#postgresql)
- 而且工程师非常热情的送了点数
- 立即开通

> 创建 路由器
> 创建 私有网络
> 连接 私有网络<->路由器
> 创建 数据库
> 绑定 私有网络
> 申请 公网IP
> 配置 路由器 端口转发 数据库内部网络端口

BINGO!

> $ psql -h 公网IP -U root postgres

就完成了远程接入!

`小技巧`:

- 创建数据库时的用户口令,和 `root` 用户相同
- 实例化时, 青云没有创建用户 database, 所以,要连接内置的 `postgres` 配置数据库

先初始化测试表:

    zoomq=# CREATE TABLE json_test (
          id serial primary key,
          data jsonb
        );

    zoomq=# \d json_test
                             Table "public.json_test"
     Column |  Type   |                       Modifiers
    --------+---------+--------------------------------------------------------
     id     | integer | not null default nextval('json_test_id_seq'::regclass)
     data   | json    |
    Indexes:
        "json_test_pkey" PRIMARY KEY, btree (id)

    zoomq=# INSERT INTO json_test (data) VALUES 
          ('{}'),
          ('{"a": 1}'),
          ('{"a": 2, "b": ["c", "d"]}'),
          ('{"a": 1, "b": {"c": "d", "e": true}}'),
          ('{"b": 2}');

    zoomq=# SELECT * FROM json_test;
     id |                                data
    ----+---------------------------------------------------------------------
      1 | {}
      2 | {"a": 1}
      3 | {"a": 2, "b": ["c", "d"]}
      4 | {"a": 1, "b": {"c": "d", "e": true}}
      5 | {"b": 2}
    (5 rows)


可以看到,可以很好的支持各种情况

## psycopg2

当然的,作为一头 Pythoneer 肯定先用 py 来检验规划的
而针对 PostgreSQL, [Psycopg 2](http://pythonhosted.org//psycopg2/usage.html)
是绝对的首选模块.


    import psycopg2
    import psycopg2.extras

    conn = psycopg2.connect("dbname=zoomq")
    cur = conn.cursor()
    cur.execute("SELECT * FROM json_test;")
    data = cur.fetchall()
    conn.commit()
    print data

    _sql = '''INSERT INTO json_test (data) VALUES('
            {"name":"张三"
                ,"age":18
                ,"birthday":"2013-03-03"
            }
        ');'''
    cur.execute(_sql)
    cur.execute("SELECT * FROM json_test WHERE data ->> 'age' = '18';")
    data = cur.fetchone()

    conn.commit()
    print data, type(data), data[1]['name']

    # from psycopg2.extras.Jsonで辞書型を変換
    cur.execute(u"INSERT INTO json_test(data) VALUES (%s)",
        [psycopg2.extras.Json({'age': 11
            , 'name':'是也乎'
            , "birthday":"2013-11-11"
            })
        ])
    cur.execute("SELECT * FROM json_test WHERE data ->> 'age' = '11';")
    data = cur.fetchone()

    conn.commit()
    print data, type(data), data[1]['name']

    cur.close()
    conn.close()
    return None

执行后的 `psql` 查询结果

![150212-test.png](http://zoomq.qiniudn.com/ZQCollection/snap/pg4json/150212-test.png)

可以看到 Pg 容忍了各种意外空格的 JSON 文本,
并依然能正确的返回为 Py 的数据对象!

## TODO

- 部署到 AWS 实例中跑几批读写看计费次数是否大大减少
- 用 sqlalchemy 包装, 就可以兼容以往的 MySQL 实例应用

## 参考:

- 官方文档照例是非人性的:
    + [psycopg2.extras – Miscellaneous goodies for Psycopg 2 — Psycopg 2.5.5.dev0 documentation](http://pythonhosted.org//psycopg2/extras.html#psycopg2.extras.Json)
- 日本人的严谨:
    + [PythonからPostgreSQL 9.3.2のjson列へデータの登録、検索(Psycopg2) - Symfoware](http://symfoware.blog68.fc2.com/blog-entry-1258.html)
    + [psycopg2.extras – Miscellaneous goodies for Psycopg 2 — Psycopg 2.5.5.dev0 documentation](http://pythonhosted.org//psycopg2/extras.html#psycopg2.extras.Json)
    + [PythonからPostgreSQL 9.3.2のhstore列へデータの登録、検索(Psycopg2)](http://symfoware.blog68.fc2.com/blog-entry-1259.html)
    + [PostgreSQL JSON/JSONBの文書操作とMongoDBの文書操作 - 日々の記録 別館](http://d.hatena.ne.jp/nuko_yokohama/20141228/1419737030)
- [Schinckel](http://schinckel.net/about/) 的神入:
    + [Python, postgres and jsonb](http://schinckel.net/2014/05/24/python%2C-postgres-and-jsonb/)
    + [Querying JSON in Postgres - Schinckel.net](http://schinckel.net/2014/05/25/querying-json-in-postgres/)
- 以及 Pg周刊中非常应景的:
    + [Query JSON with Postgres 9.4 and Rails 4.2](http://robertbeene.com/rails-4-2-and-postgresql-9-4/?utm_source=postgresweekly&utm_medium=email)



## 是也乎
在这一快速验证过程中,相关的体验:

- MAC 系统中, 果断使用 [Postgres.app](http://postgresapp.com/) 渠道安装最省心!
    + 唯一注意的是要根据相关追问:
        * [python - Psycopg2 image not found - Stack Overflow](http://stackoverflow.com/questions/16407995/psycopg2-image-not-found)
        * [python - Libssl and libcrypto causing dyld: Library not loaded: /usr/lib/libpq.5.dylib - Stack Overflow](http://stackoverflow.com/questions/13643452/libssl-and-libcrypto-causing-dyld-library-not-loaded-usr-lib-libpq-5-dylib)
        * [Frequently Asked Questions — Psycopg 2.5.5.dev0 documentation](http://initd.org/psycopg/docs/faq.html)

    + 在 `~/.bash_profile` 中追加


> export DYLD_LIBRARY_PATH=/Applications/Postgres.app/Contents/Versions/9.3/lib:$DYLD_LIBRARY_PATH

否则, `import psycopg2` 是要失败的...


- 残念的是,上述配置后发生:
    + [MacのGeant4でlibjpegなどの画像ライブラリまわりでdyldエラーが出るとき - 週末はいつも晴れ](http://ikarino99.hatenablog.com/entry/2014/12/11/130101) 
    + `subl` 无法从命令行打开指定文件了, 这得另外解决.
    + 有相关支招: [python - Psycopg2 image not found - Stack Overflow](http://stackoverflow.com/questions/16407995/psycopg2-image-not-found)
    + 但是,又不兼容 psycopg2 的使用
    + 好在只是测试, 可以先将就着
- pg 的管理界面, 果断是 [PG Commander](https://eggerapps.at/pgcommander/) 最妥贴!
    + 但是 `psql` 其实也足够的了 ;-)
- 不过,在各种文档中追查时, 果断是 [Dash](http://kapeli.com/dash) 最妥贴!
    + 当然要点銭来停止保护视力的努力
    + 最后实在没忍住,买了一整年的...


`PS:`

- 最近任性的购买服务还有: [Boomerang for Gmail](http://www.boomeranggmail.com/faq.html)
    + ![](http://www.boomeranggmail.com/images/Logo.png)
    + `回旋镖` 服务!

## 修订

- 150212 随折腾随记


