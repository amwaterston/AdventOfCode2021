with open('input14.txt') as fp:
    template, _, *lines = [line.strip() for line in fp.readlines()]

    polys = {l.split(" -> ")[0]: l.split(" -> ")[1] for l in lines}
    letter_counts = {l : template.count(l) for l in set(list(template)) }
    pairs = {template[i] + template[i+1] : 1 for i in range(len(template) - 1)} #assumes all initial pairs are unique
    
    for i in range(40):
        new_pairs = {}
        for p in pairs.keys():
            if (polys[p] not in letter_counts): letter_counts[polys[p]] = 0 
            letter_counts[polys[p]] += pairs[p]

            p1 = p[0] + polys[p]
            p2 = polys[p] + p[1]
            if p1 not in new_pairs: new_pairs[p1] = 0 
            if p2 not in new_pairs: new_pairs[p2] = 0

            new_pairs[p1] += pairs[p]
            new_pairs[p2] += pairs[p]
        pairs = dict(new_pairs)

    print(max(letter_counts.values()) - min(letter_counts.values()))

