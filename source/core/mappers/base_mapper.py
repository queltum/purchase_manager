from typing import Any
from abc import ABC, abstractmethod

class BaseMapper(ABC):
	@staticmethod
	@abstractmethod
	def to_view(model: Any) -> Any:
		pass

	@staticmethod
	@abstractmethod
	def to_model(view: Any) -> Any:
		pass