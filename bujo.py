import click
from tinydb import TinyDB, Query, where

@click.group()
def cli():
  pass

@cli.command()
@click.option('--kind', default='task', help='Entry type. Valid options are: task or note')
@click.argument('text', nargs=-1)
def add(kind, text):
  """ Add a new task to the task list"""
  tasks = TinyDB('tasks.json')
  tasks.insert({'kind': kind, 'text': " ".join(text)})
  for task in tasks:
    print("{}    {}  {}".format(task.doc_id, task['kind'], task['text']))

@cli.command()
@click.argument('task_id')
def delete(task_id):
  """ Remove a task from the task list """
  tasks = TinyDB('tasks.json')
  tasks.remove(doc_ids=[int(task_id)])

@cli.command()
def list():
  """ List current tasks """
  tasks = TinyDB('tasks.json')
  for task in tasks:
    print("{}    {}  {}".format(task.doc_id, task['kind'], task['text']))
