import itertools


def jaccard_distance(base, target):
    set1 = set(base.split())
    set2 = set(target.split())
    return float('%.2f' % ((len(set1 | set2) - len(set1 & set2)) / len(set1 | set2)))


def dice_coefficient_distance(base, target):
    set1 = set(base.split())
    set2 = set(target.split())
    return float('%.2f' % (1 - (2*len(set1 & set2) / (len(set1)+len(set2)))))


target_1 = "assent chore champion dairy aural baron"
target_2 = "ascent chord champagne diary oral barn"
target_3 = "assent ascent chore champion dairy aural baron chord champagne diary oral barn"
target_4 = "assent chore champagne diary aural barren"
target_5 = "accent chord champion dairy aural baron"
target_6 = "ascent core champion dirty rural barn"
targets = [target_1, target_2, target_3, target_4, target_5, target_6]

targets_combinations = list(itertools.combinations(targets, 3))
print(len(targets_combinations))
jd_result = list()
for combination in targets_combinations:
    a, b, c = combination
    d_ab = jaccard_distance(a, b)
    d_ac = jaccard_distance(a, c)
    d_bc = jaccard_distance(b, c)
    triangle_inequality = (d_ab+d_ac >= d_bc) & (d_ab+d_bc >= d_ac) & (d_bc+d_ac >= d_ab)
    print(d_ab, d_ac, d_bc, triangle_inequality)
    # print((d_ab+d_ac >= d_bc) & (d_ab+d_bc >= d_ac) & (d_bc+d_ac >= d_ab))
    jd_result.append(triangle_inequality)
print(False not in jd_result)

dj_result = list()
print("---------")
for combination in targets_combinations:
    a, b, c = combination
    d_ab = dice_coefficient_distance(a, b)
    d_ac = dice_coefficient_distance(a, c)
    d_bc = dice_coefficient_distance(b, c)
    triangle_inequality = (d_ab+d_ac >= d_bc) & (d_ab+d_bc >= d_ac) & (d_bc+d_ac >= d_ab)
    print(d_ab, d_ac, d_bc, triangle_inequality)
    dj_result.append(triangle_inequality)
print(False not in dj_result)