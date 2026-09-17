from operator import itemgetter
from re import fullmatch
from sys import exit


def main():

    try:
        with open("emails.txt", "r") as file:
            ledger = analyze(file)  # analyze returns ledger: dict
    except FileNotFoundError:
        exit("Emails.txt file not found")

    if not ledger:
        raise ValueError("Invalid .txt file")

    top = max(ledger, key=ledger.get)

    print(f"Top sender: {top} ({ledger[top]})\n")

    # itemgetter(1) does the same as lambda s: s[1], just highly optimized
    for key, value in sorted(ledger.items(), key=itemgetter(1), reverse=True):  
        print(f"{key:<40}{value}")
            


def analyze(file):
    ledger = {}

    for address in file:  #iterate line by line, address could be \n too
        address = validate(address.lower().strip())

        if not address:
            continue
        
        ledger[address] = ledger.get(address, 0) + 1

    return ledger


def validate(address):
    pattern = r"(\w+(?:\.\w+)*@\w+(?:\.\w+)*\.com)"

    if matches := fullmatch(pattern, address):
        return matches.group(1)
    
    return None


if __name__ == "__main__":
    main()
