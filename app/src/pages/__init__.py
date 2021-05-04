from .page1 import Page1
from .page2 import Page2
from ..utils import Page

from typing import Dict, Type


PAGE_MAP: Dict[str, Type[Page]] = {
    "Salary distribution": Page1,
    "Scatter plot of stats": Page2,
}

__all__ = ["PAGE_MAP"]