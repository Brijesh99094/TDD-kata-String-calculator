class StringCalculator:

    def add(self, string_number):
        if len(string_number.strip()) == 0:
            return 0

        if len(string_number) >= 1:
            lst = list()

            for i in string_number.split(","):
                if not i.isdigit():
                    if len(i) == 1:
                        num = ord(i) - 96
                        lst.append(num)
                    else:
                        raise ValueError("Negative not allowed")
                else:
                    lst.append(int(i))
            return sum(lst)

        return 1
