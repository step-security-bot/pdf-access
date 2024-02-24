# Standard Python Libraries
from pathlib import Path

# Third-Party Libraries
import fitz


class NiceBase:
    nice_name: str

    @classmethod
    def register(cls) -> str:
        return cls.nice_name


class PostProcessBase(NiceBase):
    # Subclasses should override this with their unique nice name
    nice_name: str

    @classmethod
    def apply(self, in_path: Path, out_path: Path, **kwargs):
        raise NotImplementedError(
            "Each post processor must implement the apply method."
        )


class TechniqueBase(NiceBase):
    # Subclasses should override this with their unique nice name
    nice_name: str

    @classmethod
    def apply(self, doc: fitz.Document, **kwargs) -> int:
        raise NotImplementedError("Each technique must implement the apply method.")
