class TaskStep():

    def __init__(self, title, substeps=[]):
        self.title = title
        self.substeps = substeps

    def act(self, assignee, task):
        if len(self.substeps):
            if self.substeps[task.current_substep_index].act(assignee, task):
                task.current_substep_index += 1
                return len(self.substeps) <= task.current_substep_index
        else:
            return True
            # No default step behaviour,
            # override method in subclass to implement behaviour
        return False


    