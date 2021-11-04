def display_ladder(steps):
  for i in range(steps):
    print("| |")
    print("*" * 3)

def create_ladder():
  display_ladder(int(input(("How many steps are left? "))))

create_ladder()