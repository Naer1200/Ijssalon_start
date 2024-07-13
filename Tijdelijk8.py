from helper import decoreer

prijzen = {
    "aardbei" : "3",
    "vanille" : "4",
    "chocolade" : "5"
    
    }

aanbieding = prijzen ["vanille"] * 0,8
aanbieding = 3 * 0.8

reclame_tekst = f"Vandag in de aanbiding vanille-ijs, 1 liter - slechts € {aanbieding:.16f}"

reclame_tekst2 = reclame_tekst[:60]

reclame_tekst3 = reclame_tekst2.upper()

reclame_tekst4 = reclame_tekst3.split()

for el in reclame_tekst4 :
    if len(el) > 4:
        print(el.upper())
    else:
        print(el.lower())
       
        decoreer("Aanbieding")
        print(reclame_tekst2) 
        
        print(aanbieding) 