ues = int(input("Enter number of UEs: "))
rbs = int(input("Enter number of Resource Blocks (RBs): "))
slots = int(input("Enter number of Time Slots: "))

allocation = []
ue_allocations = [0] * ues

for i in range(slots):
    row = []

    for j in range(rbs):
        ue = (i + j) % ues
        row.append(ue)
        ue_allocations[ue] += 1

    allocation.append(row)

print("\nRound Robin Allocation Matrix:\n")

for idx, r in enumerate(allocation[:10]):
    print(f"Slot {idx + 1}: {r}")

print("\nValidation:")
print("Total Slots =", len(allocation))
print("RBs per Slot =", len(allocation[0]))
print("UE IDs Range = 0 to", ues - 1)

print("\nUE Allocation Counts:")

for i in range(ues):
    print(f"UE {i}: {ue_allocations[i]}")