from .task_steps import TASK_NOT_STARTED

class Task():

    def __init__(self, title, steps):
        self.title = title
        self.completed = False
        self.steps = steps
        self.current_step_index = -1
        self.assignee = None

    def has_started(self):
        return self.current_step_index > -1

    def get_steps(self):
        return self.steps
        
    def get_next_steps(self):
        next_steps = self.steps[self.current_step_index+1:] \
            if self.has_started() else self.steps

        return next_steps

    def current_step(self):
        if self.current_step_index <= -1:
            return TASK_NOT_STARTED
        else:
            return self.steps[self.current_step_index]

    def next_step(self):
        self.current_step_index += 1
        return self.current_step()

    def complete(self):
        self.completed = True
        return self.completed
