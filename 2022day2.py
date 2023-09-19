
with open("2022day2.txt", "r") as input:
    data = input.read()

list = data.split()

theirScore = "ABC"
myScore = "XYZ"
total = 0
for i in range(len(list)):
    if i%2==0:
        theirs = list[i]
        theirIndex = theirScore.index(theirs)
        mine = list[i+1]
        myIndex = myScore.index(mine)
        


        total += myIndex + 1

        if myIndex == theirIndex:
            total += 3
        elif myIndex == 0 and theirIndex == 2 or myIndex == 1 and theirIndex == 0 or myIndex == 2 and theirIndex == 1:
            total += 6


print(f"Part 1 Answer: {total}")


###################### Part 2 ################
theirScore = "ABC"
resultScore = "XYZ"
total2 = 0
for i in range(len(list)):
    if i%2 == 0:
        theirs = list[i]
        result = list[i+1]
        theirIndex = theirScore.index(theirs)
        resultIndex = resultScore.index(result)

        total2 += resultIndex * 3
        
        if resultIndex == 0:
            if theirIndex == 0:
                total2 += 3
            elif theirIndex == 1:
                total2 += 1
            else:
                total2 += 2
        elif resultIndex == 1:
            total2 += theirIndex + 1
        else:
            if theirIndex == 0:
                total2 += 2
            elif theirIndex == 1:
                total2 += 3
            else:
                total2 += 1

print(f"Part 2 Answer: {total2}")

    
