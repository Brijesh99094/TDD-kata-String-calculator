
class StringCalculator:

    def add(self, string_number):
        if len(string_number.strip()) == 0:
            return 0

        if len(string_number) >= 1:
            lst = list()
            negative_values = list()
            for i in string_number.split(","):
                if not i.isdigit():
                    if len(i) == 1:
                        num = ord(i) - 96
                        lst.append(num)
                    else:
                        #raise ValueError("Negative not allowed")
                        negative_values.append(int(i))
                elif int(i) < 0:
                    negative_values.append(int(i))
                    #raise ValueError("Negative value not allowed")
                else:
                    lst.append(int(i))

            if (negative_values):
                raise ValueError(negative_values)
            return sum(lst)

        return 1
