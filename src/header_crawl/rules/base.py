from abc import ABC, abstractmethod

class HeaderRule(ABC):
    @property
    @abstractmethod
    def rule_name(self) -> str:
        """Name of the rule"""
        pass

    @abstractmethod
    def evaluate(self, headers: dict) -> str | None:
        """
        Evaluate logic.
        Returns a string message if notable, or None if nothing to report.
        """
        pass
