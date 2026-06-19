print('''
  a pirate's treasure map
    ___
    ).x)
   (:_(
  
  Finrod




                                                                      



         __________
        /\____;;___\
       | /         /
       `. ())oo() .
        |\(%()*^^()^\
       %| |-%-------|
      % \ | %  ))   |
      %  \|%________|
ejm97  %%%%

       {}           {}
         \  _---_  /
          \/     \/
           |() ()|
            \ + /
ejm 96     / HHH  \
          /  \_/   \
        {}          {}
                           ___________
                ___________)%{}%%%%%%/
               /{}%%%%%%%%/%%/%%%%%%/
              /%%\% _---_/ \/%%%%%%/
             /%%%%\/    /()|%%%%%%/
            /%%%%%|()  /+ /%%%%%%/
           /%%%%%%%\ +/HH%%\%%%%/
          /%%%%%%/%HH/_/%%%\%%%/
 ejm97   /%%%%%%/%%\/%%%%%%{}%/
        /%%%%%{}%%%/
       /
      /
     /
    /
   /


'''
)

print("Welcome to Treasure island.\n Your mission is to find the treasure")
direction = input("Left or Right? ").lower()

if direction == 'right':
    print("Game over.")
else:
    swim_wait = input("Swim or Wait? ").lower()
    if swim_wait == 'swim':
        print("Game over.")
    else:
        door_choice = input("Which door? Red, Blue or Yellow ").lower()
        if door_choice == 'yellow':
            print("You win!")
        else:
            print("Game over.")
