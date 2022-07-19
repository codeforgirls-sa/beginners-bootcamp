# Slide 29
math = input("Are you good at math (yes/no)? ")
problemSolving = input("Are you good at solving problems (yes/no)? ")
communication = input("Are you good at communicating with people (yes/no)? ")
logic = input("Are you good at logical thinking (yes/no)? ")
if math == "yes" and problemSolving == "yes":
    print("You should be an engineer!")
elif communication == "yes" and problemSolving == "yes":
    print("You should work in marketing!")
elif logic == "yes" and problemSolving == "yes":
    print("You should be a programmer!")
