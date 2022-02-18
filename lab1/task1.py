from goto import with_goto


@with_goto
def task1():
    ignore = ["the", "on", "of", "in", "a", "an"]
    dic = dict()

    with open("rick.txt") as f:
        lines = f.readlines()

        j = 0
        label. jStart

        line = lines[j]
        words = line.split()

        i = 0
        label .iStart
        w = words[i]
        w = w.lower()
        if w in ignore:
            i += 1
            if i < len(words):
                goto .iStart
            else:
                goto.iEnd
        if w in dic:
            dic[w] += 1
        else:
            dic[w] = 1

        i += 1
        if i < len(words):
            goto .iStart

        label .iEnd

        j += 1
        if j < len(lines):
            goto. jStart

        label .jEnd

        dic = dict(sorted(dic.items(), key=lambda kv: kv[1]))
        keys = list(dic.keys())

        m = len(keys) - 1
        label .mStart

        print(keys[m], dic[keys[m]])

        if m > 0:
            m -= 1
            goto .mStart

        label .mEnd


task1()