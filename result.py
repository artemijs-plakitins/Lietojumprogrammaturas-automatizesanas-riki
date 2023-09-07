def main():
    dollars = dollars_to_float(input("How much was the meal? ").rstrip())
    percent = percent_to_float(input("What percentage would you like to tip? ").rstrip())
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    t = d.rstrip()
    t1 = t.replace ("$","")
    r = float (t1)
    return (r)

def percent_to_float(p):
    m = p.rstrip()
    m1 = m.replace("%","")
    c = float (m1) / 100
    return (c)

main()