

class StringCalculator:

    def add(self, string_number):
        if len(string_number.strip()) == 0:
            return 0
        if int(string_number) > 0:
            return (int(string_number))

        return 1
