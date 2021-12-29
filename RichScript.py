import math

try:
    from rich.console import Console
    from rich.table import Table
    from rich.style import Style


except:
    import pip
    pip.main (["install", "--user", "rich"])
    from rich.console import Console
    from rich.table import Table
    from rich.style import Style


x = list(map(float, input().rstrip().split()))

xbar = 0
third = []
fourth = []

svalue = 0.00

xbar = sum(x) / len(x)

third = [(k-xbar) for k in x]
    
fourth = [(j*j) for j in third] 

svalue = math.sqrt(sum(fourth)/(len(x) - 1))

table = Table(title="Table", style="red on black")

table.add_column("X", justify="right", style="cyan", no_wrap=True)
table.add_column("X_BAR", justify="right", style="cyan", no_wrap=True)
table.add_column("X - X_BAR", justify="right", style="cyan", no_wrap=True)
table.add_column("(X - X_BAR)^2", justify="right", style="cyan", no_wrap=True)

for r in range(len(x)):
    table.add_row(f"{x[r]}", f"{round(xbar, 3)}", f"{round(third[r], 3)}", f"{round(fourth[r], 3)}")


console = Console()
console.print(table)    
console1 = Console()
console1.print(f"XBAR = [b]{xbar}[/b]", style="magenta")
console2 = Console()
console2.print(f"Standard Deviation = [b]{str(round(svalue, 3))}[/b]", style="magenta")
