from functools import partial

def logging(year, month, day, title, content):
    print("%s-%s-%s %s:%s" % (year, month, day, title, content))

def main():
    print("=== use partial function ===")
    f = partial(logging, "2021", "6", "17") # using partial function in functools module
    f("2021 spring", "end of semester")
    f("2021 summer", "vacation begins")

if __name__ == "__main__":
    main()