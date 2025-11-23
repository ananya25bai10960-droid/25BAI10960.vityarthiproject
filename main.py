from diamond import diamond
from spiral import spiral
from fractal_tree import fractal_tree
from circle import circle

def clear_screen():
    print("\n" * 60)

def main():
    while True:
        clear_screen()
        print("#########################################")
        print("#        ASCII PATTERN GENERATOR        #")
        print("#########################################\n")

        print("Choose a pattern:")
        print("1. Diamond")
        print("2. Spiral")
        print("3. Fractal Tree")
        print("4. Circle")
        print("5. Exit\n")

        choice = input("Enter choice (1-5): ")

        if choice == "1":
            size = int(input("Enter size (recommended 5–15): "))
            diamond(size)

        elif choice == "2":
            size = int(input("Enter size (recommended 10–25): "))
            spiral(size)

        elif choice == "3":
            level = int(input("Enter depth (recommended 3–6): "))
            fractal_tree(level)

        elif choice == "4":
            radius = int(input("Enter radius (recommended 5–15): "))
            circle(radius)

        elif choice == "5":
            print("\nGoodbye! ✨")
            break

        else:
            print("\nInvalid choice. Try again!")

        input("\nPress ENTER to return to menu...")

if __name__ == "__main__":
    main()
