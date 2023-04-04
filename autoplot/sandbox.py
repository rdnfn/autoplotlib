from sys import addaudithook


def run(code: str, global_vars: dict = None, local_vars: dict = None):
    """Run code in a sandboxed environment.

    Args:
        code (str): Python code to run.
    global_vars (dict, optional): Global
        variables. Defaults to None.
    local_vars (dict, optional): Local
        variables. Defaults to None.
    """

    if global_vars is None:
        global_vars = {}
    if local_vars is None:
        local_vars = {}

    def block_mischief(event, arg):
        if "WRITE_LOCK" in globals() and (
            (event == "open" and arg[1] != "r")
            or event.split(".")[0] in ["subprocess", "os", "shutil", "winreg"]
        ):
            raise IOError("File write is forbidden by autoplot sandbox.")

    addaudithook(block_mischief)

    global WRITE_LOCK
    WRITE_LOCK = True
    exec(code, global_vars, local_vars)
    del WRITE_LOCK
