import random

li = [
"김효진",
"김소정",
"신동헌",
"서정권",
"김종혁",
"전예준",
"김동준",
"박세지",
"조용현",
"한예원",
"장은영",
"홍예지",
"김동윤",
"신유경",
"송유나",
"최진영",
"윤혜진",
"백재원",
"류지웅",
"김상준"
]

random.shuffle(li)

print([li[i] for i in range(4)])
print([li[i] for i in range(4,8)])
print([li[i] for i in range(8,12)])
print([li[i] for i in range(12,16)])
print([li[i] for i in range(16,20)])