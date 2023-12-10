input = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""


input = input.split("\n")
combos = []

def get_combos(curr, length, springs):
    if not springs:
        print(curr)
        #combos += curr
        return 
    
    sp = springs[0]
    rest = springs[1:]
    spring = f"{'#' * (sp-1)}."


    for p in range(len(curr), length-sp):
        spaces = "." * p
        next = f"{curr}{spaces}{spring}"
        get_combos(next, length, rest)


def get_possible(mask, springs):
    mask = f"{mask}."
    print(mask, springs)

    get_combos("", len(mask), springs)

    for combo in combos:
        pass

    return 0

res = 0

for line in input:
    mask, springs = line.split()
    sp_list = [int(c)+1 for c in springs.split(",")]
    #res += get_possible(mask, sp_list)

print(res)


get_combos("", 10, [4,2,2])


