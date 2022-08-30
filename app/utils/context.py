from dataclasses import dataclass
@dataclass

class Contect:
    path: str
    fname: str
    train: object
    test: object
    id: str
    label: str
    
    @property # getter
    def path(self) -> str: return self._path # 안에 감춰진 path 
    
    @path.setter
    def path(self, path): self._path = path