import traceback

def get_exception_trace(e: Exception) -> str:
    return ''.join(traceback.format_exception(type(e), e, e.__traceback__))
    