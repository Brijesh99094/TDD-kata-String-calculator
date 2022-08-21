class StringCalculator:

    def add(self, string_number):
        if len(string_number.strip()) == 0:
            return 0

        if len(string_number) >= 1:
            lst = list()

            for i in string_number.split(","):
                if not i.isdigit():
                    num = ord(i) - 96
                    lst.append(num)
                else:
                    lst.append(int(i))
            return sum(lst)

        return 1
