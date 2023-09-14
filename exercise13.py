def main():
    R = float(input("Please enter the length of row, in feet: "))
    E = float(input("Please enter the amount of space used by an end post assembly, in feet: "))
    S = float(input("Please enter the amount of space between the vines, in feet: "))
    V = (R - 2 * E) / S
    print('\nNumber of grapevines that will fit in the row:', V)

main()
