#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    
    def add(argv):
        argc = len(argv) - 1
        sum = 0

        if argc == 0:
            sum += sum

        else:
            for i in range(1, argc + 1):
                sum += int(argv[i])

        print("{:d}".format(sum))
add(sys.argv)
