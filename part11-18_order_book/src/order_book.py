class Task:
    id_counter = 1

    def __init__(self, description: str, programmer: str, workload: int):
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.id = Task.id_counter
        self._finished = False
        Task.id_counter += 1

    def is_finished(self) -> bool:
        return self._finished

    def mark_finished(self):
        self._finished = True

    def __str__(self) -> str:
        status = "FINISHED" if self._finished else "NOT FINISHED"
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {status}"


class OrderBook:
    def __init__(self):
        self.orders = []

    def add_order(self, description: str, programmer: str, workload: int):
        """Add a new order to the OrderBook"""
        task = Task(description, programmer, workload)
        self.orders.append(task)

    def all_orders(self):
        """Return a list of all tasks in the OrderBook"""
        return self.orders

    def programmers(self):
        """Return a list of unique programmer names"""
        return list(set(task.programmer for task in self.orders))

    def mark_finished(self, task_id: int):
        """Mark a task as finished by its id"""
        for task in self.orders:
            if task.id == task_id:
                task.mark_finished()
                return
        raise ValueError(f"Task with id {task_id} not found")

    def finished_orders(self):
        """Return a list of finished tasks"""
        return [task for task in self.orders if task.is_finished()]

    def unfinished_orders(self):
        """Return a list of unfinished tasks"""
        return [task for task in self.orders if not task.is_finished()]

    def status_of_programmer(self, programmer: str):
        """Return a tuple with (finished_count, unfinished_count, finished_hours, unfinished_hours)"""
        programmer_tasks = [
            task for task in self.orders if task.programmer == programmer
        ]

        if not programmer_tasks:
            raise ValueError(f"Programmer {programmer} not found")

        finished = [task for task in programmer_tasks if task.is_finished()]
        unfinished = [task for task in programmer_tasks if not task.is_finished()]

        finished_count = len(finished)
        unfinished_count = len(unfinished)
        finished_hours = sum(task.workload for task in finished)
        unfinished_hours = sum(task.workload for task in unfinished)

        return (finished_count, unfinished_count, finished_hours, unfinished_hours)
