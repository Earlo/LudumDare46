from .task import Task


class TaskManager():

    def __init__(self, GAME):
        self.active_tasks = []
        self.game = GAME
        self.assignee_pool = []
        self.task_buffer = []

    def add_tasks(self, tasks):
        print("Adding tasks")
        for task in tasks:
            self.assign_task(task)
            return task
        print("Added tasks: " + str(len(self.active_tasks) + " " + str(len(self.task_buffer))))

    def get_active_tasks(self):
        return self.active_tasks

    def get_task_buffer(self):
        return self.task_buffer

    def add_to_pool(self, *units):
        for unit in units:
            if len(self.task_buffer):
                self.assign_task(self.task_buffer.pop(), unit)
                return False
            else:
                self.assignee_pool.append(unit)
                #print("Added assignee to pool, no tasks " + str(len(self.task_buffer)))
                return True

    def assign_task(self, task, assignee=None):
        print("Assigning task")
        if not assignee:
            if len(self.assignee_pool):
                assignee = self.assignee_pool.pop()
                print("Found assignee from pool!")
            else:
                print("No assignee, adding to buffer")
                self.task_buffer.append(task)
                return False
        task.assign(assignee)
        print("Task assigned!")
        return True
