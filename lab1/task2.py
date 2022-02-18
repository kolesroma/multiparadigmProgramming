from goto import with_goto


@with_goto
def task2():
    dic = dict()

    with open("text.txt") as f:
        lines = f.readlines()

        j = 0
        label.jStart

        line = lines[j]
        words = line.split()

        i = 0
        label.iStart
        w = words[i]
        w = w.lower()

        page_num = j // 45
        if w in dic:
            dic[w].add(page_num)
        else:
            dic[w] = {page_num}

        i += 1
        if i < len(words):
            goto.iStart

        label.iEnd

        j += 1
        if j < len(lines):
            goto.jStart

        label.jEnd

        dic_sorted = sorted(dic)

        e = 0
        label .eStart

        if len(dic[dic_sorted[e]]) > 100:
            e += 1
            goto .eStart

        print(dic_sorted[e], dic[dic_sorted[e]])

        e += 1
        if e < len(dic_sorted):
            goto .eStart

        label .eEnd


task2()