def calc_venit(venit):
    print(f"Venit:{venit}")
    print("Recomandarile noastre:")
    print(f"Cheltuieli uzuale:  {venit / 2}")
    print(f"Recreere:  {venit * 0.3}")
    print(f"Economii si datorii:  {venit * 0.2}")

calc_venit(int(input()))