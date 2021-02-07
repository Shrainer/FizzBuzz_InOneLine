#for i in range(1, 101):
#	print(f"{str(i) * (bool((i % 3) * (i % 5)))}{'Fizz' * (not bool(i % 3))}{'Buzz' * (not bool(i % 5))}")	

# help me PLEASE!!!

print("\n".join([f"{str(i) * (bool((i % 3) * (i % 5)))}{'Fizz' * (not bool(i % 3))}{'Buzz' * (not bool(i % 5))}" for i in range(1, 101)]))