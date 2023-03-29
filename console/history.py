class CommandHistory:
    def __init__(self):
        self.commands = []
        self.current_index = -1

    def add_command(self, command):
        self.commands.append(command)
        self.current_index = len(self.commands) - 1

    def get_previous_command(self):
        if self.current_index >= 0:
            command = self.commands[self.current_index]
            self.current_index -= 1
            return command
        else:
            return None

    def get_next_command(self):
        if self.current_index < len(self.commands) - 1:
            self.current_index += 1
            return self.commands[self.current_index]
        else:
            return None
