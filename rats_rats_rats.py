import math

# constants
YEAR = 365
FIRST_LITTER_DELAY = 105
LITTER_INTERVAL = 35
BABIES_PER_LITTER = 8
FEMALES_PER_LITTER = 4

# list of female birth days (df values)
df_list = [-105]  # include the original female as df=-105

# we simulate births by scheduling litters
female_birthdays = [-105]
new_females = [-105]

while new_females:
    next_gen = []
    for df in new_females:
        first = df + FIRST_LITTER_DELAY
        if first > YEAR:
            continue
        t = first
        while t <= YEAR:
            # add 4 new females born at time t
            next_gen.extend([t] * FEMALES_PER_LITTER)
            t += LITTER_INTERVAL
    if not next_gen:
        break
    df_list.extend(next_gen)
    new_females = next_gen

# now apply your equation exactly
total = 2 + BABIES_PER_LITTER * sum(
    max(0, math.floor((YEAR - (df + FIRST_LITTER_DELAY)) / LITTER_INTERVAL) + 1)
    for df in df_list
)

print(total)
