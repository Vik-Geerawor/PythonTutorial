def scope_demo():
    """
    Order of Precedence: LEGB (Local Enclosed Global Builtin)
    """
    x = "What x am I?"

    def func_a():
        x = "I'm local x"

    def func_b():
        nonlocal x
        x = "I'm nonlocal x"

    def func_c():
        global x
        x = "I'm global x"

    func_a()                        # NOTE: local namespace - to the func
    print(f"After func a: {x}")
    func_b()                        # NOTE: nonlocal namespace - outside the func
    print(f"After func b: {x}")
    func_c()                        # NOTE: global namespace - inside the module
    print(f"After func c: {x}")


if __name__ == "__main__":
    # scope_test()
    scope_demo()

    print(f"outter call = {x}")
