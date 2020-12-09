import sys

class ProgressBar():
    def __init__(self, total, barLength=20):
        self.__total = total
        self.__barLength = barLength
        self.__current = 0
        
    def update(self):
        self.__current += 1
        self.show(self.__current)

    def getCurrent(self):
        return self.__current

    def show(self, num):
        percent = float(num) * 100 / self.__total
        arrow = '-' * int(percent/100 * self.__barLength - 1) + '>'
        spaces = ' ' * (self.__barLength - len(arrow))
        print('Progress: [%s%s] %d %% %s/%s' % (arrow, spaces, percent, num, self.__total), end='\r')
        sys.stdout.flush()
