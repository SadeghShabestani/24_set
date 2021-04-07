import termcolor2

a = []
b = []

len_n = int(input(termcolor2.colored("Enter Number Value1:", color="blue")))

for i in range(len_n):
    a.append(int(input("Enter Number: ")))

len_m = int(input(termcolor2.colored("Enter Number Value2:", color="blue")))
for i in range(len_m):
    b.append(int(input("Enter Number: ")))

print(f"N:{set(a)}", end="\t")
print(f"M:{set(b)}")

set_a = set(a)
set_b = set(b)

result_a = set_a.intersection(set_b)
print(f"Common:{result_a}")

result_b = set_a.union(set_b)
print(f"Union:{result_b}")
