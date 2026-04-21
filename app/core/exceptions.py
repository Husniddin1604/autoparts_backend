import traceback


class AppException(Exception):
    def __init__(self, error: str, detail: str, status_code: int = 400):
        self.error = error
        self.detail = detail
        self.status_code = status_code

        # capture the stack at the time of raising the exception
        self.stack_trace = "".join(traceback.format_stack(limit=10))


class BusinessException(AppException):
    def __init__(self, detail: str):
        super().__init__(error=detail, detail="BusinessError", status_code=400)


class CustomValidationException(AppException):
    def __init__(self, detail: str):
        super().__init__(error=detail, detail="ValidationError", status_code=422)
