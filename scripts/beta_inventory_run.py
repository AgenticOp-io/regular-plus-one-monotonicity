from fractions import Fraction

from scripts.beta_full_inventory import inventory


def main() -> None:
    print("full inventory with fork+k3path", flush=True)
    for an in [Fraction(1, 10), Fraction(1, 20), Fraction(1, 40)]:
        Ds, _ = inventory(an)
        a = float(an)
        print(
            f"a={an} Da_tot={Ds['total']*a:.6f} p64={Ds['p64']*a:.6f} "
            f"c35={Ds['c35']*a:.6f} k4={Ds['k4']*a:.6f} k3={Ds['k3xw']*a:.6f}",
            flush=True,
        )


if __name__ == "__main__":
    main()
