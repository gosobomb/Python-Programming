for i in range(2, 10):
    print(f"#  {i}단  #", end=" ")
print()

for i in range(1, 10):
    for j in range(2, 10):
        print(f"{j}X  {i}= {i*j:>2}", end=" ")
    print()