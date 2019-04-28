#!/usr/bin/env python

import json
import shutil
from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible.plugins.callback import CallbackBase
import ansible.constants as C


# since API is constructed for CLI it expects certain options to always be set, named tuple 'fakes' the args parsing options object
Options = namedtuple('Options', ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check', 'diff'])
options = Options(connection='local', module_path=['/to/mymodules'], forks=10, become=None, become_method=None, become_user=None, check=False, diff=False)
#connection: 定义连接方式, local表示本机, ssh表示ssh, smart表示自动选择
#module_path: 指定自定义的模块位置
#forks:指定启动的进程适量
#become: 如果使用普通用户远程登录服务器,那么切换成其他用户该怎么切换
#check: 预言操作的结果,而不真正操作
#diff: 显示修改小文件的前后变化

# initialize needed objects
loader = DataLoader() # Takes care of finding and reading yaml, json and ini files
passwords = dict(vault_pass='a')
#设置密码
# Instantiate our ResultCallback for handling results as they come in. Ansible expects this to be one of its main display outlets

# create inventory, use path to host config file as source or hosts in a comma separated string
#定义主机清单, 可以将各主机用都好隔开的字符串, 也可以指定文件路径列表
# inventory = InventoryManager(loader=loader, sources='localhost,')
inventory = InventoryManager(loader=loader, sources=['/ansible/hosts'])

# variable manager takes care of merging all the different sources to give you a unifed view of variables available in each context
# 变量管理器
variable_manager = VariableManager(loader=loader, inventory=inventory)

# create datastructure that represents our play, including tasks, this is basically what our YAML loader does internally.
# play_source =  dict(
#         name = "Ansible Play",
#         hosts = 'localhost',
#         gather_facts = 'no',
#         tasks = [
#             dict(action=dict(module='shell', args='ls'), register='shell_out'),
#             dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}')))
#          ]
#     )
play_source =  dict(
        name = "Ansible Play",
        hosts = 'webserver',
        gather_facts = 'no',
        tasks = [
            dict(action=dict(module='shell', args='ls'), register='shell_out'),
            dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}')))
         ]
    )


# Create play object, playbook objects use .load instead of init or new methods,
# this will also automatically create the task objects from the info provided in play_source
# 通过上面的配置创建一个 play
play = Play().load(play_source, variable_manager=variable_manager, loader=loader)

# Run it - instantiate task queue manager, which takes care of forking and setting up all objects to iterate over host list and tasks
# 创建任务管理器, 执行play
tqm = None
try:
    tqm = TaskQueueManager(
              inventory=inventory,
              variable_manager=variable_manager,
              loader=loader,
              options=options,
              passwords=passwords,
          )
    result = tqm.run(play) # most interesting data for a play is actually sent to the callback's methods
finally:
    # we always need to cleanup child procs and the structres we use to communicate with them
    if tqm is not None:
        tqm.cleanup()

    # Remove ansible tmpdir
    shutil.rmtree(C.DEFAULT_LOCAL_TMP, True)