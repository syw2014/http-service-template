# 服务框架代码使用说明

## 文件夹与文件说明

1. data文件夹：用于存储服务需要使用的数据文件和模型

2. log文件夹：用于存储日志文件

3. logout文件夹：用于存储保存服务进程pid的文件，这些文件用于停止服务

4. service文件夹：用于存储服务框架代码。

5. src文件夹：用于存储提供服务功能的源文件。例如，服务为分词服务，则该文件夹下保存分词功能源代码。

6. utils文件夹：存储服务所需的一些基础功能的源文件。

   ​                      当前包含有三个子文件夹：eureka（负责服务注册、心跳上报、服务注销）

   ​                                                                     log（负责服务日志打印与回滚）

   ​                                                                     status（负责服务错误码相关）

7. requirements.txt：服务所依赖的python包。

8. service_deployment_procedure.txt：服务部署方法说明文档。

9. start.sh：服务启动脚本

10. stop.sh：服务停止脚本



## 框架代码使用步骤

1. 相关功能源码放置在src文件夹下。（没有，则跳过）
2. 相关模型和数据放置在data文件夹下。（没有，则跳过）
3. 修改service文件下service.py中所有TODO项，并将service.py按照服务功能重新命名。
4. 根据服务相关需求，自定义utils/status/status.py中的错误码，注意规范。同时，修改service文件下api_tools.py文件中的对应部分（没有，则跳过）
5. 修改utils/log/log_socket_receiver.py文件中的log_file_name，修改utils/log/log_socket_sender.py文件中的log_service_port。修改规则见对应文件中的TODO项。
6. 修改start.sh中nlp_techs.py为你重新命名的服务文件名。
7. 修改stop.sh中ai-nlp-techs为service.py中的service_name对应值。
8. 撰写requirement.txt文件。
9. 撰写service_deployment_procedure.txt文件。



## 启动服务

sh -x start.sh



## 暂停服务

sh -x stop.sh



## 服务启动错误时

需要将服务相关的进程直接用pid kill掉，并且查验相关端口是否被占用，占用时同样kill。然后才能重启服务。