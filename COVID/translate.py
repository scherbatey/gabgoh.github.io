with open("orig.txt") as f_orig, open("trans_ed.txt") as f_trans, open("bundle_orig.js") as f_js:
    lines_orig = [line.strip() for line in f_orig]
    lines_trans = [line.strip() for line in f_trans]
    lines_js = [line[:-1] for line in f_js]

i = 0

while i < len(lines_orig):
    found = False
    for j in range(0, len(lines_js)):
        p = lines_js[j].find(lines_orig[i])
        if p >= 0:
            q1 = lines_js[j].find('"')
            q2 = lines_js[j].find('"', q1 + 1)
            if q1 < 0 or q2 < 0:
                q1 = lines_js[j].find("'")
                q2 = lines_js[j].find("'", q1 + 1)
            else:
                pass
            if 0 <= q1 <= p < q2:
                lines_js[j] = lines_js[j].replace(lines_orig[i], lines_trans[i], 1)
                found = True
                break
            else:
                pass
    if found:
        i += 1
    else:
        print(f"Not found: {lines_orig[i]}")
        del lines_orig[i]
        del lines_trans[i]

# for orig, trans in zip(lines_orig, lines_trans):
#     print(f"{orig} -> {trans}")

with open("bundle.js", "w") as f:
    for line in lines_js:
        print(line, file=f)
