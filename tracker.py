# Budget ah smart ah pirikkum program di
def budget_split(total):
    needs = total * 0.5
    wants = total * 0.3
    savings = total * 0.2
    print(f"Total: {total} di Muthu")
    print(f"1. Needs ku (Mobile/Laptop): Rs {needs}")
    print(f"2. Wants ku (IKEA/Style): Rs {wants}")
    print(f"3. Savings: Rs {savings}")

budget = int(input("Budget sollu di: "))
budget_split(budget)