from .task_steps import TASK_NOT_STARTED, TASK_COMPLETED


class Task:
    def __init__(self, title, steps=[], assignee=None):
        self.title = title
        self.completed = False
        self.steps = [TASK_NOT_STARTED, *steps, TASK_COMPLETED]
        self.current_step_index = 0
        self.current_substep_index = 0
        self.assignee = assignee

    def has_started(self):
        return self.current_step_index > 0

    def get_steps(self):
        return self.steps

    def current_step(self):
        return self.steps[self.current_step_index]

    def next_step(self):
        self.current_step_index += 1
        self.current_substep_index = 0
        return self.current_step()

    def act(self):
        print(self.current_step().title)
        step_completed = self.current_step().act(self.assignee, self)
        if step_completed:
            next_step = self.next_step()
            if next_step == TASK_COMPLETED:
                return True
        return False

    def complete(self):
        self.completed = True
        return self.completed
