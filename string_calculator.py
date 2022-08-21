
import re


class StringCalculator:

    def getStringAndDelimiter(self, string):
        delimiter = "[,\\n]"
        splited_string = re.split("\n", string, maxsplit=1)
        if string[0:2] == "//":
            splited_string = re.split("\n", string, maxsplit=1)
            string, delimiter = splited_string[1], splited_string[0][2:]
        elif string[0:3] == '0//':
            delimiter = splited_string[0][3:]
            lst = splited_string[1].split(delimiter)
            string = delimiter.join(lst[0::2])
        elif string[0:3] == '1//':
            delimiter = splited_string[0][3:]
            lst = splited_string[1].split(delimiter)
            string = delimiter.join(lst[1::2])
        else:
            print("Invalid String")
        return string, delimiter

    def add(self, string_number):
        if len(string_number.strip()) == 0:
            return 0

        if len(string_number) >= 1:
            string_number, delimiter = self.getStringAndDelimiter(
                string_number)
            lst = list()
            negative_values = list()
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

            if (negative_values):
                raise ValueError(negative_values)
        return sum(lst)


if __name__ == "__main__":
    sc = StringCalculator()
    # print(sc.add("0//;\n12;33;44;a;b;c"))
    # print(sc.add("1\n2,3,4,5\na,b,8\nl\n10"))
    # sc.add("-1,-2,3,-4")
    # print(sc.add("1,2,3,4\n5,6,7,8,9,10"))
    # print(sc.add("//;\n1;2;3;4;5"))
    # print(sc.add("1,2,3,-4,5"))`      `
    # print(sc.add("1,2,3,-4,5"))
