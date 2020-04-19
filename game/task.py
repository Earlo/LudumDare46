from .task_steps import TASK_COMPLETED


class Task:
    def __init__(self, title, steps=[], assignee=None):
        self.title = title
        self.completed = False
        self.steps = steps
        self.current_substep_index = 0
        self.assignee = assignee

    def assign(self, assignee):
        self.assignee = assignee
        assignee.task = self

    def act(self):
        if self.steps[0].act(self.assignee, self):
            self.steps.pop(0)
            if len(self.steps) == 0:
                return True
        return False

    def complete(self):
        print("completed task!!!")
        self.completed = True
        return self.completed
