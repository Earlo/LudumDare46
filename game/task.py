class Task():

    def __init__(self, title, steps):
        self.title = title
        self.completed = False
        self.steps = steps

    def get_steps(self):
        return self.steps

    def complete(self):
        self.completed = True
        return self.completed
