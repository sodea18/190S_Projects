print("Solve: SLAYER + SLAYER + SLAYER = LAYERS")
slayer = int(input("What is your guess? ")) 

correctLayers = (slayer % 100000) * 10 + (slayer // 100000) #what layers should be if user solution is correct
actualLayers = slayer * 3 #layers based on user input

print(f'{correctLayers} == {actualLayers} -> {(correctLayers == actualLayers)}')
#checks if layers calculated from user input matches what would be the correct solution 