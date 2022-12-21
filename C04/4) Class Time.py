class time:
    def __init__(self, hour, minute, second):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def __add__(self, other):
        __sum1 = (self.__hour * 60 * 60) + (self.__minute * 60) + (self.__second)
        __sum2 = (other.__hour * 60 * 60) + (other.__minute * 60) + (other.__second)
        __sum_time = __sum1 + __sum2
        __hour_conv = int(__sum_time / 3600)
        __min_conv = int((__sum_time % 3600) / 60)
        __sec_conv = int((__sum_time % 3600) % 60)
        return "{0} hours, {1} minutes, {2} seconds".format(__hour_conv, __min_conv, __sec_conv)

# hour1 = int(input("Enter the first hour"))
# minuite1 = int(input("Enter the first seconds"))
# seconds1 = int(input("Enter the first second"))
# hour1 = int(input("Enter the second hour"))
# minuite1 = int(input("Enter the second seconds"))
# seconds1 = int(input("Enter the second second"))

t1 = time(2, 10, 30)
t2 = time(5, 40, 23)

print(t1+t2)
