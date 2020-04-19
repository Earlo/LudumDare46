from .task import Task
from .ui.screens import taskManagerGui


class TaskManager:
    def __init__(self, GAME):
        self.assigneePool = []
        self.taskBuffer = []
        self.activeTasks = []

        self.game = GAME

    def add_to_pool(self, unit):
        self.assigneePool.append(unit)

    def get_task(self, assignee, completed_task=None):
        if completed_task and completed_task in self.activeTasks:
            self.activeTasks.remove(completed_task)
            self.update_gui()
        if len(self.taskBuffer) > 0:
            nextTask = self.taskBuffer.pop(0)
            self.assign_task(nextTask, assignee)
            self.update_gui()
        elif assignee not in self.assigneePool:
            self.assigneePool.append(assignee)

    def assign_task(self, task, assignee=None):
        if not assignee:
            if len(self.assigneePool):
                assignee = self.assigneePool.pop(0)
            else:
                self.taskBuffer.append(task)
                self.update_gui()
                return False
        task.assign(assignee)
        self.activeTasks.append(task)
        self.update_gui()
        return True

    def update_gui(self):
        self.game.load_gui(taskManagerGui(
                self.game,
                self.activeTasks,
                self.taskBuffer
            ))
