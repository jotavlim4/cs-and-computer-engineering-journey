for alyssa in range(1001):
    ben = max(alyssa - 20, 0) # para lidar com o caso de alyssa < 20
    cindy = alyssa * 2
    if alyssa + ben + cindy == 1000:
        print(f"alyssas sell's {alyssa} tickets")
        print(f"ben sell's {ben} tickets")
        print(f"cindy sell's {cindy} tickets")
        break

