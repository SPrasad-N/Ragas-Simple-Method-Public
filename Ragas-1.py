
# Program for knowing info about Raga.

import playsound

Ragas = {
    "Yaman" : [
        " Aaroh : 'Ni Re Ga Ma Dha Ni Sa' ",
        " Avaroh : Sa' Ni Dha Pa Ma Ga Re Sa ",
        " Vadi : Ni Sa ",
        " Samvadi : Ma Ga "
    ],
    "Kedar" : [
        " Aaroh : Sa Re Ga Ma Pa Dha Ni Sa ",
        " Avaroh : Sa Ni Dha Pa Ma Ga Re Sa ",
        " Vadi : Ni Sa ",
        " Samvadi : Ma Ga "
    ],
}

Raga_name = input("Enter the name of Raag:\n")

Raga_capital = Raga_name.capitalize()

if Raga_capital in Ragas:
    print(f"\n{Raga_capital} -")
    for items in Ragas[Raga_capital]:
        print(items)
    print("\nDo you want to play the audio?\nIf yes type y otherwise n.")
    play_audio = input(" Play? : ")
    if play_audio == "y":
        playsound.playsound(f"Raga/{Raga_capital}.mp3")
        exit()
    else:
         print("Exited Successfully!")
         exit()

else:
    print("Wrong input or Raga unavailable")
