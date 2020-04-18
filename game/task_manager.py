from task import Task


class TaskManager():

    def __init__(self, tasks=[]):
        self.tasks = tasks

    def create_tasks(self, task_param_objects):
        tasks = []
        for task_params in task_param_objects:
            task = self.create_task(task_params)
            tasks.append(task)
        return tasks

    def create_task(self, task_params):
        task = Task(task_params)
        self.tasks.append(task)
        return task

    def get_tasks(self):
        return self.tasks

    def assign_task(self, task, assignee):
        if task not in self.tasks:
            return False

        def complete_task():
            task.complete()
            self.tasks.remove(task)

        assignee.assign(task, complete_task)
        return True
