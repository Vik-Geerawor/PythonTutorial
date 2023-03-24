import traceback


def simple_exception():
    try:
        10 * (1/0)
    except ZeroDivisionError as err:
        print("Cannot divide by zero..!")


def multiple_handlers():
    while True:
        try:
            # NOTE: int() throws ValueError exception
            x = int(input("Enter a number: "))
            print(f"Well done..! {x} is an integer.")
            break
        except ValueError:
            print("Oops! That wasn't a number: Try again...")
        except KeyboardInterrupt:                   # NOTE: Ctrl+C throws this exception
            print("\nExiting. Good Bye..!")
            return -1


def exception_hierarchy():
    class B(Exception):
        """
        Description: is a type of exception
        """
        pass

    class C(B):
        """
        Description: inherits from class B
        i.e. an instance of C is of type B
        """
        pass

    class D(C):
        """
        Description: inherits from class C
        i.e. an instance of D is of type C and 
        ultimately of type B
        """
        pass

    for cls in [D, C, B]:
        try:
            # NOTE: Raise an [instance] of each exception
            raise cls()
        # NOTE: Which handle is executed depends on the type of exception
        except B:       # NOTE: any of the exceptions will be of type B
            print("B")  # NOTE: so any this handler will catch them all
        except C:
            print("C")
        except D:
            print("D")

    for cls in [B, C, D]:
        try:
            # NOTE: Raise an [instance] of each exception
            raise cls()
        except D:       # NOTE: an instance of B is not of type D
            print("D")
        except C:       # NOTE: or of type C
            print("C")
        except B:       # NOTE: but only of type B
            print("B")


def exception_args():
    class AboveTheLawError(Exception):
        _name: str

    def __init__(self, name) -> None:
        self._name = name

    class BelowTheLawError(Exception):
        _name: str

        def __init__(self, name) -> None:
            self._name = name

    above = AboveTheLawError("Oligarch")
    below = BelowTheLawError("Liberals")
    for cls in [above, below]:
        try:
            raise cls
        except AboveTheLawError as a:
            print(f"{a}: type={type(a)}; args={a.args}")
        except BelowTheLawError as b:
            print(f"{b}: type={type(b)}; args={b.args}")


def exception_return(file):
    try:
        with open(file, 'r', encoding="utf-8") as f:
            for line in f:
                try:
                    i = int(line.strip())
                    print(str(i))
                except ValueError:
                    print(f"Could not convert to integer: {line}", end='')
    except OSError as err:
        print("OS error:", err)
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        raise


def else_clause(file):
    """
    Description: else clause is executed if try clause is successful
    """
    f = None
    try:
        f = open(file, 'r')
    except OSError:
        print(f"File does not exist: {f}")
    else:
        print(f"{f} has {len(f.readlines())} lines")
        if f:
            f.close()


def raise_exception(word, fouls):
    class FoulError(Exception):
        def __init__(self, *args: object) -> None:
            super().__init__(*args)

    try:
        if word in fouls:
            raise FoulError(word)
    except FoulError:
        print(f"Mind you language..!")
        raise


def exception_chaining():
    try:
        1 / 0
    except ZeroDivisionError as err:
        i = int(err)        # NOTE: Unhandled exception, incl in preceding error
        print(f"{err}")
        print(f"__cause__: {err.__cause__}")
        if err.__context__:
            print(f"While handling: {err.__context__}")

    print(f"*** END TRY ***")


def finally_clause(file):
    """
    Description: finally clause is always executed
    """
    f = None
    try:
        with open(file, 'r') as f:
            pass
    except OSError as err:
        err.add_note("Notes add by Vik")
        # print(f"{err}")
        # print(f"{err=}")
        # print(f"File does not exist: {f}")

        # print(f"err.args: {err.args}")

        # if err.__context__:
        #     print(f"While handling: {err.__context__}")

        tblines = traceback.format_exception(type(err), err, err.__traceback__)
        tbmsg = ''.join(tblines)
        print(f"MyTraceback: {tbmsg}")
    else:
        print(f"{f} has {len(f.readlines())} lines")
        if f:
            f.close()
    finally:
        print(f"*** END FUNC ***")


if __name__ == "__main__":
    # simple_exception()
    # multiple_handlers()
    # exception_hierarchy()
    # exception_args()
    # exception_return("files/test.txt")
    # else_clause("files/test.txt")

    # foul_words = ["f**k", "a$$hole"]
    # raise_exception("f**k", foul_words)

    # exception_chaining()
    finally_clause("files/test1.txt")
