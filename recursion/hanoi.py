

def hanoi(n, source = "A", through = "B", dest = "C"):
  if n == 0:
    return 
  hanoi(n-1, source, dest, through)
  print(f"{source} --> {dest}")
  hanoi(n-1, through, source, dest)
 
hanoi(4)
