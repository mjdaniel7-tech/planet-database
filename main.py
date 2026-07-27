# Planet Database

# Main Program

def main():

    planets = [

        "Mercury",

        "Venus",

        "Earth",

        "Mars",

        "Jupiter",

        "Saturn",

        "Uranus",

        "Neptune"

    ]

    print("Planet Database")

    print("=" * 30)

    for number, planet in enumerate(planets, start=1):

        print(f"{number}. {planet}")

if __name__ == "__main__":

    main(
  
