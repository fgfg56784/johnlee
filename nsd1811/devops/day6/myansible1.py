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
import sys

def ansible_run(sources, hosts, module, args):
    Options = namedtuple('Options', ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check', 'diff'])
    options = Options(connection='ssh', module_path=['/to/mymodules'], forks=10, become=None, become_method=None, become_user=None, check=False, diff=False)
    loader = DataLoader() # Takes care of finding and reading yaml, json and ini files
    passwords = dict(vault_pass='a')

    inventory = InventoryManager(loader=loader, sources=sources)
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    play_source =  dict(
            name = "Ansible Play",
            hosts = hosts,
            gather_facts = 'no',
            tasks = [
                dict(action=dict(module=module, args=args), register='shell_out'),
            ]
        )

    play = Play().load(play_source, variable_manager=variable_manager, loader=loader)
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
        if tqm is not None:
            tqm.cleanup()

        # Remove ansible tmpdir
        shutil.rmtree(C.DEFAULT_LOCAL_TMP, True)

if __name__ == "__main__":
    sources=['/ansible/hosts']
    hosts=['webserver']
    module='shell'
    args=sys.argv[1]
    ansible_run(sources, hosts, module, args)