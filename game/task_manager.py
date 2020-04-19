from .task import Task


class TaskManager:
    def __init__(self, GAME):
        self.assigneePool = []
        self.taskBuffer = []
        self.activeTasks = []

        self.game = GAME

    def add_task(self, task):
        self.taskBuffer.append(task)

    def add_to_pool(self, unit):
        self.assigneePool.append(unit)

    def get_task(self, assignee):
        if len(self.taskBuffer) > 0:
            nextTask = self.taskBuffer.pop()
            self.assign_task(nextTask, assignee)
            # not used?
            # self.activeTasks.append(nextTask)

    def assign_task(self, task, assignee=None):
        print("Assigning task")
        if not assignee:
            if len(self.assigneePool):
                assignee = self.assigneePool.pop()
                print("Found assignee from pool!")
            else:
                print("No assignee, adding to buffer")
                self.taskBuffer.append(task)
                return False
        task.assign(assignee)
        print("Task assigned!")
        return True
