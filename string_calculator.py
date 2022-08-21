class StringCalculator:

    def add(self, string_number):
        if len(string_number.strip()) == 0:
            return 0
        if len(string_number) >= 1:
            lst = list()
            for i in string_number.split(","):
                lst.append(int(i))
            return sum(lst)

        return 1
