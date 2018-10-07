def minion_game(string):
    p1Letters = "AEIOU"
    p2Letters = "BCDFGHJKLMNPQRSTVWXYZ"
    p1Score = 0
    p2Score = 0
    
    
    p1Input = raw_input()
    
    while p1Input != string:
        if p1Input[0] not in p1Letters:
            p1Input = raw_input()
        p1Score += string.count(p1Input)
        print(string.count(p1Input))
        p1Input = raw_input()

    p2Input = raw_input()
    
    while p2Input != string:
        if p2Input[0] not in p2Letters:
            p2Input = raw_input()
        p2Score += string.count(p2Input)
        print(string.count(p2Input))
        p2Input = raw_input()
        
    if p1Score > p2Score:
        return "Player One Won!"
    elif p2Score > p1Score:
        return "Player Two Won!"
    return "Its a Draw!"
