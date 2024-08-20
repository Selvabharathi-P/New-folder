import argparse

def hello(name, language):
    greeting = {
        "German":"Hallo",
        "English":"Hello",
        "Spanish":"Hola"
    }

    msg = f"{greeting[language] }  {name}"
    print(msg)

if (__name__) == "__main__":
    parser = argparse.ArgumentParser(
        description = "Provides a personalized greeting",
        )

    parser.add_argument(
        "-n", "--name", required=True, metavar="name", help="Name of the person to greet", 
        )

    parser.add_argument(
        "-l", "--lang", metavar="language", help="Language to greet", required=True, choices=["English", "Spanish", "German"],
        )

    args = parser.parse_args()
    
    hello(args.name, args.lang)
