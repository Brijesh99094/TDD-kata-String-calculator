
from enum import Enum
import re


class IndexType(Enum):
    EVEN = 0
    ODD = 1


class StringCalculator:

    def getStringAndDelimiter(self, string):
        delimiter = "[,\\n]"

        splited_string = re.split("\n", string, maxsplit=1)
        if string.startswith("//"):
            string, delimiter = splited_string[1], splited_string[0][2:]
        elif string.startswith("0//"):
            string, delimiter = self.get_string_numbers_at_indices(
                IndexType.EVEN, splited_string)

        elif string.startswith('1//'):
            string, delimiter = self.get_string_numbers_at_indices(
                IndexType.ODD, splited_string)

        else:
            print("Invalid String")
        return string, delimiter

    def get_string_numbers_at_indices(self, index_type, splited_string):
        delimiter = splited_string[0][3:]
        lst = splited_string[1].split(delimiter)
        if IndexType.EVEN == index_type:
            string = delimiter.join(lst[0::2])
        else:
            string = delimiter.join(lst[1::2])
        return string, delimiter

    def add(self, string_number):
        if len(string_number.strip()) == 0:
            return 0

        if len(string_number) >= 1:
            string_number, delimiter = self.getStringAndDelimiter(
                string_number)
            lst = list()
            negative_values = list()
            self.get_valid_or_negative_numbers(
                string_number, delimiter, lst, negative_values)

            self.raise_exception_for_negative_values(negative_values)
        return sum(lst)

    def get_valid_or_negative_numbers(self, string_number, delimiter, lst, negative_values):
        for i in re.split(delimiter, string_number):
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
            elif int(i) > 1000:
                continue
            else:
                lst.append(int(i))

    def raise_exception_for_negative_values(self, negative_values):
        if (negative_values):
            s = ""
            for i in negative_values:
                s += (str(i)+',')
            s = s[0:len(s)-1]
            raise ValueError(s)


if __name__ == "__main__":
    sc = StringCalculator()
    # print(sc.add("0//;\n12;33;44;a;b;c"))
    # print(sc.add("1\n2,3,4,5\na,b,8\nl\n10"))
    # sc.add("-1,-2,3,-4")
    # print(sc.add("1,2,3,4\n5,6,7,8,9,10"))
    # print(sc.add("//;\n1;2;3;4;5"))
    # print(sc.add("1,2,3,-4,5"))`      `
    # print(sc.add("1,2,3,-4,5"))
