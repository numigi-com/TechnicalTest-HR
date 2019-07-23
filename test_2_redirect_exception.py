def redirect_exception(source, target):
    """ Redirect an exception type of `source` type to `target` type.
    :param exception source: Type of exception that will be redirected.
    :param exception target: Type of exception that the source will be redirected to.
    """

    def redirectFunction(func):
        try:
            return func()
        except source as srcError:
            print("Oops!  division by zero!.  Try again...")
            raise target('%s' % (srcError,))

    return redirectFunction


@redirect_exception(ZeroDivisionError, ValueError)
def divide_by_zero():
    return 1 / 0
    # Should raise a ValueError


if __name__ == "__main__":
    divide_by_zero()
