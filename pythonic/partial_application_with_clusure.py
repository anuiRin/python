def partial(func, *partial_args):

    def wrapper(*extra_args):
        args = list(partial_args)
        args.extend(extra_args) # add arguments to the list when declaring and using closure.

        return func(*args)
    return wrapper # use inner function as return value. This means that it is closure.

def logging(year, month, day, title, content):
    print("%s-%s-%s %s:%s" % (year, month, day, title, content))

def main():
    print("=== use logging function ===")
    logging("2021", "6", "17", "2021 spring", "end of semester")
    logging("2021", "6", "17", "2021 summer", "vacation begins")

    print("=== use partial function ===")
    f = partial(logging, "2021", "6", "17")
    f("2021 spring", "end of semester")
    f("2021 summer", "vacation begins")
    # Partial applications can be used to increase readability.

if __name__ == "__main__":
    main() # we can expect to print same values.
