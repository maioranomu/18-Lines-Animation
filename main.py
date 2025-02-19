import os, time, random
def clear():
    time.sleep(0.1)
    os.system("cls")
truck1, truck2, truck3, b1, b2, b3, counter, s1, s2, s3, s4, sky1, sky2, sky3, sky4, c11, c12, c13, c14, c21, c22, c23, c24 = ("   ________________"),("  | ##### TRUCK  |o\\"), ("  |_________________|"), "_" * 2, "_" * 11, "_" * 100, " ", "(|)", "(/)", "(-)", "(\\)", " " * 20, " " * 20, " " * 20, " " * 20, "    ___  ___  ", " __/   \\/   \\ ", "/            \\", "\\____________/", "  ___  _____  ", " /   \\/     \\ ", "/            \\", "\\____________/"
sprites = [f"{b1}{s1}{b2}{s1}{b3}", f"{b1}{s2}{b2}{s2}{b3}", f"{b1}{s3}{b2}{s3}{b3}", f"{b1}{s4}{b2}{s4}{b3}"]
while True:
    for i in sprites:
        clear()
        counter += "_"
        if len(counter) % 10 == 0:
            cl, bc = random.randint(0, 2), random.randint(10, 14)
            if cl == 1:
                sky1, sky2, sky3, sky4 = sky1 + c11 + " " * bc, sky2 + c12 + " " * bc, sky3 + c13 + " " * bc, sky4 + c14 + " " * bc
            elif cl == 2:
                sky1, sky2, sky3, sky4 = sky1 + c21 + " " * bc, sky2 + c22 + " " * bc, sky3 + c23 + " " * bc, sky4 + c24 + " " * bc
        truck1, truck2, truck3, i = " " + truck1, " " + truck2, " " + truck3, counter + i
        print(f"{sky1}\n{sky2}\n{sky3}\n{sky4}\n{truck1}\n{truck2}\n{truck3}\n{i}")