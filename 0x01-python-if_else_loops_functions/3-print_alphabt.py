for i in range(97, 123):
    if chr(i) == 'e' or chr(i) == 'q':
        continue
    else:
        print("{0}".format(chr(i)), end="")
