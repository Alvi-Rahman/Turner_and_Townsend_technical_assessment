class Fifth(object):
    def __init__(self, test=False, command_list=None):
        self.stack = []
        self.test = test
        self.command_list = command_list

    def __perform_push(self, x):
        self.stack.append(x)
        return True

    def __perform_pop(self):
        if not self.stack:
            return False
        self.stack.pop()
        return True

    def __perform_swap(self):
        if len(self.stack) < 2:
            return False
        self.stack[-1], self.stack[-2] = self.stack[-2], self.stack[-1]
        return True

    def __perform_duplicate(self):
        if not self.stack:
            return False
        self.stack.append(self.stack[-1])
        return True

    def __perform_calculation(self, operator):
        try:
            if len(self.stack) < 2:
                return False
            value_2, value_1 = self.stack.pop(), self.stack.pop()
            if operator == "+":
                self.stack.append(value_1 + value_2)
            elif operator == "-":
                self.stack.append(value_1 - value_2)
            elif operator == "*":
                self.stack.append(value_1 * value_2)
            elif operator == "/":
                self.stack.append(value_1 // value_2)
            else:
                return False
            return True
        except (ValueError, TypeError):
            return False

    def __perform_command(self, inp):
        try:
            if inp.startswith("PUSH"):
                x = int(inp.split(" ")[-1])
                action = self.__perform_push(x)
            elif inp == "POP":
                action = self.__perform_pop()
            elif inp == "SWAP":
                action = self.__perform_swap()
            elif inp == "DUP":
                action = self.__perform_duplicate()
            else:
                action = False

            return action
        except ValueError:
            return False

    def __driver(self, inp, operators):
        if inp in operators:
            # Perform operation
            result = self.__perform_calculation(inp)

            if not result:
                print("ERROR")
                return False
            print(f"stack is {self.stack}")
        else:
            # perform commands
            result = self.__perform_command(inp)
            if not result:
                print("ERROR")
                return False
            print(f"stack is {self.stack}")

        return True

    def run(self):
        operators = ["+", "-", "*", "/"]
        print(f"stack is {self.stack}")
        if self.test and self.command_list:
            response = True
            for inp in self.command_list:
                response = self.__driver(inp, operators)
                if not response:
                    break
            return response

        while True:
            inp = input()
            response = self.__driver(inp, operators)
            if not response:
                break


if __name__ == "__main__":
    fifth = Fifth()
    fifth.run()
