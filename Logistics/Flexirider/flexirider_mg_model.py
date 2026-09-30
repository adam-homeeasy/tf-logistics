"""Flexirider MG model, v2 (30 Sep 2026).
Flexirider bill a month = max(MG, their fee x deliveries).
INPUTS: [ADAM] = told by Adam, [ASK] = unknown, confirm with Flexirider, [GUESS] = placeholder."""
MG = 25000                 # [ADAM] Rs a month; ex-GST or incl-GST? [ASK]
GST = 0.18                 # [ADAM] GST on top; 18% rate itself [ASK/CA]
UE_OWN = 5                 # [ADAM] uEngage, restaurant's own riders, Rs per delivery + GST
def ue_3pl(km):            # [ADAM] uEngage via its logistics partners: Rs65 up to 3 km, Rs12/km after, + GST
    return 65 + 12*max(0, km-3)

print("uEngage 3PL price by distance (ex-GST / incl GST)")
for km in (2,3,4,5,6,8):
    p=ue_3pl(km); print(f"  {km} km: Rs{p} / Rs{p*(1+GST):.2f}")

print("\nCase 1: Flexirider fee is software only, restaurant's own riders (compare with uEngage Rs5)")
for fee in (5,):
    print(f"  deliveries a month to use up MG at Rs{fee}: {MG/fee:,.0f}")
    for d in (250,500,1000,2000,3000,5000):
        b=max(MG,fee*d); print(f"  {d:>5}/month: bill Rs{b:,} | per delivery Rs{b/d:.2f} vs uEngage Rs{UE_OWN} | extra over uEngage Rs{b-UE_OWN*d:,}")

print("\nCase 2: MG counts full delivery charges (Flexirider books 3PL riders), priced like uEngage 3PL")
for km in (3,4,5):
    p=ue_3pl(km); print(f"  avg {km} km (Rs{p}): deliveries to use up MG = {MG/p:,.0f}")
for d in (100,200,300,400):
    for km in (3,5):
        p=ue_3pl(km); short=max(0,MG-p*d)
        print(f"  {d}/month at {km} km: charges Rs{p*d:,}, shortfall TF pays Rs{short:,}")
