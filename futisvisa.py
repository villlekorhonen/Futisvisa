import csv
import random
tulos = 0
kierros = 0

def tarkastus(kysymys, vastaus):
    global tulos, kierros
    
    if kysymys.lower() == vastaus.lower():
        print("Oikein!")
        tulos += 1
        kierros += 1
    else:
        print("Väärin!")
        kierros += 1

def nayta_tulos():
    if tulos <= kierros and tulos >= 8:
        print("Loistavaa, olet futisnero niin kuin Litti!")
    elif tulos < 8 and tulos >= 5:
        print("Hyvä, ymmärrät futiksesta yhtä paljon kuin Pasi Rautiainen!")
    elif tulos < 5 and tulos >= 2:
        print("Välttävää, Tietosi tarvitsevat päivitystä kuin Mixu Paatelaisen pelikirja!")
    elif tulos < 2 and tulos >= 0:
        print("Ai,ai..Raadat kuin Sakke Saarinen, mutta tulosta ei tule!")
    print(f"Tuloksesi: {tulos}/{kierros}")
    print(f"{tulos/kierros*100}% kysymyksistä oli oikein!")

if __name__ == "__main__":

    

    with open("Futisvisa.csv") as csvfile:
        
        csvreader = csv.reader(csvfile, delimiter=';')

        data = [[cell.strip() for cell in row] for row in csvreader]
        
        for _ in range(10): 
            rand_row = random.choice(data)
            kysymys = rand_row[0] 
            vastaus = rand_row[1] 
            vastaus_kayttajalta = input(kysymys + " ")
            tarkastus(vastaus_kayttajalta, vastaus)
        
nayta_tulos()



