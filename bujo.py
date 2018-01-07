import click
from tinydb import TinyDB, Query

@click.group()
def cli():
    pass

@cli.command()
@click.option('--kind', default='task', help='Entry type. Valid options are: task or note')
@click.argument('text')
def add(kind, text):
   tasks = TinyDB('tasks.json') 
   tasks.insert({'kind': kind, 'text': text})
   for task in tasks:
       print("{}    {}  {}".format(task.doc_id, task['kind'], task['text']))
