class GfG:
    def sort(self, stack):
        if not stack:
            return stack

        top = stack.pop()
        self.sort(stack)
        self.insert(stack, top)

        return stack

    def insert(self, stack, element):
        if not stack or stack[-1] <= element:
            stack.append(element)
            return

        top = stack.pop()
        self.insert(stack, element)
        stack.append(top)
