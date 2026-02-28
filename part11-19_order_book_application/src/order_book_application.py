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


def main():
    orders = OrderBook()

    print("commands:")
    print("0 exit")
    print("1 add order")
    print("2 list finished tasks")
    print("3 list unfinished tasks")
    print("4 mark task as finished")
    print("5 programmers")
    print("6 status of programmer")
    print()

    while True:
        command = input("command: ")

        if command == "0":
            break
        elif command == "1":
            # Add order
            description = input("description: ")
            programmer_and_workload = input("programmer and workload estimate: ")

            try:
                parts = programmer_and_workload.split()
                if len(parts) < 2:
                    print("erroneous input")
                    continue

                programmer = parts[0]
                workload = int(parts[1])
                orders.add_order(description, programmer, workload)
                print("added!")
            except (ValueError, IndexError):
                print("erroneous input")

        elif command == "2":
            # List finished tasks
            finished = orders.finished_orders()
            if not finished:
                print("no finished tasks")
            else:
                for task in finished:
                    print(task)

        elif command == "3":
            # List unfinished tasks
            unfinished = orders.unfinished_orders()
            if not unfinished:
                print("no unfinished tasks")
            else:
                for task in unfinished:
                    print(task)

        elif command == "4":
            # Mark task as finished
            try:
                task_id = int(input("id: "))
                orders.mark_finished(task_id)
                print("marked as finished")
            except ValueError:
                print("erroneous input")

        elif command == "5":
            # List programmers
            programmers = sorted(orders.programmers())
            print(" ".join(programmers))

        elif command == "6":
            # Status of programmer
            programmer = input("programmer: ")
            try:
                finished_count, unfinished_count, finished_hours, unfinished_hours = (
                    orders.status_of_programmer(programmer)
                )
                print(
                    f"tasks: finished {finished_count} not finished {unfinished_count}, hours: done {finished_hours} scheduled {unfinished_hours}"
                )
            except ValueError:
                print("erroneous input")


main()
