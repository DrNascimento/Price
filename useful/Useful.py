

class Useful:
    @staticmethod
    def is_number(val):
        try:
            float(val)
        except ValueError:
            return False
        return True

