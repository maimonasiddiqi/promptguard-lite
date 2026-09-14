class PromptGuardError(Exception):
    def __init__(self,message,snippet=None,context=None):
        super().__init__(message)
        self.snippet=snippet
        self.context=context
class InjectionRiskError(PromptGuardError):
    pass
class MalformedInputError(PromptGuardError):
    pass
class PatternCompileError(PromptGuardError):
    pass
class DetectorRegistrationError(PromptGuardError):
    pass


