# Usage

Let's try running a sinle line in the REPL

```python
from mathlamp_pocket.repl import REPL

console = REPL()#(1)!

result = console.run_line("1 + 1")

print(result)
```

1. Should be reused to share data (Ex: Variables) between evaluations.

