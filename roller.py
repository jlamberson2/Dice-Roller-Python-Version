import random

#Used to roll for John's point buy
def roll_tower():
    statBlock = []
    for i in range(24):
        statBlock.append(random.randint(1, 6))
    
    statBlock.sort()

    statBlock = statBlock[6:]

    x = 0

    for i in statBlock:
        x += i
    
    return x

#Used to ensure that the minimum (currently set to 80) for Johns rolling method 
#Alpha is the roll
def tower_return():
    alpha = roll_tower()

    while(alpha < 80):
        alpha = roll_tower()
    
    return alpha


#Used for a regular stat block roll EX return [roll 1, roll 2, roll 3, roll 4, total], roll 1 = Exclusion roll after sort
def regular_roll():
    #Declare and fill stat block with rolls
    block = []
    for i in range(4):
        block.append(random.randint(1, 6))

    total_block = 0

    block.sort()

    #after the block sorts, exclude the first as this is 4D6 drop the lowest
    for i in range(4):
        if i > 0:
            total_block += block[i]
    
    block.append(total_block)

    return block

#Roll method reroll 1s, 4D6 drop the lowest, reroll 1s
def reroll_1s_roll():
    #Declare and fill stat block with rolls
    block = []
    for i in range(4):
        block.append(random.randint(1, 6))

    #Loop to reroll all 1's
    for i in range(4):
        if block[i] == 1:
            block[i] = random.randint(1,6)
    
    total_block = 0

    block.sort()
    
    #after the block sorts, exclude the first as this is 4D6 drop the lowest
    for i in range(4):
        if i > 0:
            total_block += block[i]
    
    block.append(total_block)
    return block

#Roll method to guarentee no 1s in the stat block
def no_1s_roll():
    #Declare and fill stat block with rolls
    block = []
    for i in range(4):
        block.append(random.randint(1, 6))

    ones_flag = True

    #while there are ones in the block, reroll them
    while(ones_flag):
        for i in range(4):
            if block[i] == 1:
                block[i] = random.randint(1,6)
        
        ones_flag = False
        for i in block:
            if i == 1:
                ones_flag = True
    
    block.sort()

    total_block = 0
    
    #TODO: add total to block
    #after the block sorts, exclude the first as this is 4D6 drop the lowest
    for i in range(4):
        if i > 0:
            total_block += block[i]
    
    block.append(total_block)
    return block

    