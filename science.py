import time

elements = {"h" : "Hydrogen", "li" : "Lithium", "be" : "Beryllium", "na" : "Sodium", "mg" : "Magnesium", "k": "Potassium", "ca": "Calcium", "rb" : "Rubidium", "sr" : "Strontium", "cs" : "Caesium", "ba" : "Barium", "fr" : "Francium", "ra" : "Radium", "sc" : "Scandium", "ti" : "Titanium", "v" : "Vanadium", "cr" : "Chromium", "mn" : "Manganese", "fe" : "Iron", "co" : "Cobalt", "ni" : "Nickel", "cu" : "Copper", "zn" : "Zinc", "y" : "Yttrium", "zr" : "Zirconium", "nb" : "Niobium", "mo" : "Molybdenum", "tc" : "Technetium", "ru" : "Ruthenium", "rh" : "Rhdoium", "pd" : "Palladium", "ag" : "Silver", "cd" : "Cadmium", "lu" : "Lutetium", "hf" : "Hafnium", "ta" : "Tantalum", "w": "Tungsten", "re" : "Rhenium", "os" : "Osmium", "ir" : "Iridium", "pt" : "Platinum", "au" : "Gold", "hg" : "Mercury", "lr" : "Lawrencium", "rf" : "Rutherfordium", "db" : "Dubnium", "sg" : "Seaborgium", "bh" : "Bohrium", "hs" : "Hassium", "he" : "Helium", "b" : "Boron", "c" : "Carbon", "n" : "Nitrogen", "o" : "Oxygen", "f" : "Fluorine", "ne" : "Neon", "al" : "Aluminium", "si" : "Silicon", "p" : "Phosphorus", "s" : "Sulfur", "cl" : "Chlorine", "ar" : "Argon", "ga" : "Gallium", "ge" : "Germanium", "as" : "Arsenic", "se" : "Selenium", "br" : "Bromine", "kr" : "Krypton", "in" : "Indium", "sn" : "Tin", "sb" : "Antimony", "te" : "Tellurium", "i" : "Iodine", "xe" : "Xenon", "tl" : "Thallium", "pb" : "Lead", "bi" : "Bismuth", "po" : "Polonium", "at" : "Astatine", "rn" : "Radon", "u" : "Uranium"}

"""f = open("dictionary.txt", "r")
words = f.readlines()
f.close()
"""

phrases = []

while input("Would you like to add another phrase(Y/N)? ").lower() != "n":
    phrases.append(input("Enter a phrase: ").lower())

words = []

for phrase in phrases:
    for word in phrase.split(" "):
        words.append(word)

def permute(xs, low=0):
    if low + 1 >= len(xs):
        yield xs
    else:
        for p in permute(xs, low + 1):
            yield p        
        for i in range(low + 1, len(xs)):        
            xs[low], xs[i] = xs[i], xs[low]
            for p in permute(xs, low + 1):
                yield p        
            xs[low], xs[i] = xs[i], xs[low]

final = []
for word in words:
    possibles = []
    for e in elements:
        if e in word:
            possibles.append(e)

    exists = False
    for possible in possibles:
        if word[:len(possible)] == possible:
            exists = True

    if exists and len(possibles) < 8:
        for p in permute(possibles):
            w = ""
            ele = []
            for tw in p:
                w += tw
                ele.append(elements[tw])
                if w.strip() == word.strip():
                    f = ""
                    for t in ele:
                        f += t + " "
                    finalString = word + " " + f
                    if not finalString in final:
                        final.append(finalString)
                if len(w) > len(word):
                    break
    for string in final:
        print(string)
    if len(final) == 0:
        print("Sorry, the word \"" + word + "\" can't be represented by periodic elements.")
    final = []
    
