# MoM: delivery partner call (Pro Routing platform), 30 Sep 2026

Meeting: `meeting-e0653c35-4b01-44ab-87b0-a77b1c41e3bb` (about 32 min).
Filed as: uEngage meeting. Note: in the call the partner calls its platform **"Pro Routing"** (a delivery aggregator that books riders from many delivery companies (LSPs) over ONDC). Its pricing is live per order, not the fixed uEngage Flash rate card in `Logistics/10_uEngage_Delivery_Dispute_Scenarios.md` (section 1a).
Related: `Logistics/10_uEngage_Delivery_Dispute_Scenarios.md`.

**Attendees**
- TF: TF lead (ran the commercial and serviceability questions), Pratyush (wallet question), TF tech.
- Partner: Arjuna (demo and commercials), partner tech lead (API, wallet, live price checks).

Names are taken from the transcript. Please correct any that are wrong.

---

## 1. Summary

- The partner showed its dashboard. For TF it would be an **API integration**: orders go in automatically from TF.
- **Commercials:** ₹3 platform fee per successful order + GST. LSP delivery charges are passed through **with no markup**. **No setup fee and no upfront payment.**
- **Pricing is dynamic:** a live quote for every order based on pickup and drop lat-long. This needs a code change on our side, because today we charge a fixed rate (first 3 km, then per km).
- **Serviceability:** Bhubaneswar and Kolkata already have LSPs. **Cuttack has none today.** A live test to a Cuttack drop returned no LSP.
- **Wallet:** each restaurant gets its own account, API key and prepaid wallet. TF asked whether the wallet could show inside the TF owner dashboard. The partner will check with its tech team. A month-end invoice is also possible. **No decision yet.**
- **Next:** the partner sends an onboarding form, then a sandbox (pre-prod) API account, then testing, then the agreement, then go-live. TF wants to start around **10 Oct** (Bhubaneswar and Kolkata first).

---

## 2. Dashboard demo (what the partner showed)

| Area | What it does |
|---|---|
| **Stores** | Add each restaurant or outlet: store ID, phone, name, address. |
| **Orders** | Bill number, order amount, pickup OTP. Drop = customer phone, name, address. With the API this is automatic. Pickup OTP and drop OTP can each be switched on or off. |
| **Wallet** | One login and one wallet per restaurant, set up at onboarding. The restaurant recharges it. Each order takes off the LSP delivery charge + ₹3 platform fee + GST. The dashboard shows every deduction. |
| **Refunds for failed deliveries** | Checked at **month end**. If genuine, the money goes back to the wallet **only once the LSP refunds the partner**. |
| **Reports** | Daily, weekly, monthly, quarterly. Delivered, cancelled by client, cancelled by system or LSP, averages. LSP report (charges, and which LSP does well at which distance). Raw data download for audits. Monthly invoices. Views by client, city and LSP. |
| **Issues** | Raise an issue on the dashboard, or paste the bill number in the shared WhatsApp group and ops raises it for you. Ops works **7 am to 12 midnight**. The issues page shows the resolution and any refund to the wallet. |
| **Manage users** | **Admin:** gets an OTP on the admin number at every login. **Staff:** no OTP of their own, so they have to ask the admin for it. |
| **Editable configs** | The partner sets these for us. |
| **Search order** | Look up any order by order ID. |
| **Support** | By email to the ops team. |

---

## 3. Discussion and outcomes

### 3.1 Wallet and billing

- **Ask (Pratyush):** can the partner's wallet be copied into the TF owner dashboard (next to deliveries and KDS), so owners see their balance and recharge there? Restaurant owners don't want to manage lots of URLs and logins.
- **Partner:** they would have to check with their tech team. Other setups they already run:
  - A master dashboard that shows each sub-account's activity but doesn't touch the wallets (Maruti, for its dealers).
  - A client that pays **one monthly invoice** for all its restaurants.
- **Partner tech:** every restaurant can have **its own account and API key**. The integration is the same for all, with the API key changed per restaurant. The owner or store manager runs each account.
- **TF view:** paying and managing on behalf of restaurants is fine at 10 outlets, tough at 15 and a nightmare at 100. A custom build usually costs money and time. **Only do the wallet integration if it's cheap and fast.** Otherwise go with what exists now and revisit when we have scale. A month-end invoice based on deliveries was raised as a fallback, and the partner said it's possible.
- **Outcome:** open. Waiting for the partner's tech answer on wallet mirroring (cost and time).

### 3.2 Commercials

- ₹3 per successful order + GST. LSP charges at cost, the same as shown in the dashboard. No setup fee, no upfront payment, no other charges.
- TF plans to add the ₹3 to the restaurant's order, so in the end the diner pays it.
- The partner offered to let TF add a further ₹2 per order as TF's commission (₹3 to the partner, ₹2 to TF). **TF: no plans to add anything right now.**
- Partner background: runs food deliveries for Swiggy, plus hyperlocal work for Zepto, BigBasket and others. FIFO and gig models.
  - **Gig model** = riders based at one location doing back-to-back runs. **Not needed now**, maybe later.
  - **On-demand** = book a rider per order through the API. **This is what TF needs.**

### 3.3 Serviceability (live check on the call)

- Serviceability works on **pin code or lat-long**. Lat-long is preferred.
- **Bhubaneswar and Kolkata:** LSPs already live.
- **Cuttack:** no LSP today. The partner says it could onboard one in about a week, but it **depends on ONDC**. First they'd check whether any current LSP covers Cuttack, otherwise they'd onboard a new one. **TF treats Cuttack as the secondary plan.**
- **Test 1:** pickup location 2 to DLF Cyber City. **Porter and Loadshare** were available. The LSP distance came back as **about 17–18 km (about 35 min)**, but Google Maps showed **about 7 km** by road.
  - Partner's explanation: each LSP works out distance with its own maps (OSRM, Google, Ola Maps). The partner just shows the price the LSP quotes.
- **Test 2:** pickup location 2 to drop location 1 (Cuttack), about 19 km. **No LSP available.** Cuttack is not serviceable today.
- An earlier short test (about 1 km) returned several LSPs with prices, including Porter and Borzo.
- **Distance cap:** possible per account (for example, no orders over 10 km).
- **Tracking:** the LSP provides the tracking link. The partner also gives rider lat-long, so we can show it on our own map.

### 3.4 Pricing and LSP selection (tech)

- Today our delivery cost is a fixed rule (X for the first 3 km, Y per km after that). With this partner it's a **live quote for every order** (pickup lat-long + drop lat-long gives the price), because LSPs can add surcharges. **This changes our code.**
- The partner's quote API returns each available LSP with its price. **API docs to be shared.**
- **How an LSP is chosen:**
  - **Fixed LSP:** we choose one LSP. If it doesn't assign a rider, the partner **does not** try the others.
  - **"Fastest agent" (recommended by the partner):** the order goes to every LSP that serves the area. The first one to assign a rider gets the order, at that LSP's price.

### 3.5 Sandbox

- Every UI screen and API works in sandbox.
- No real rider is assigned. To test that step, send the partner the order ID and they'll assign a dummy rider.

---

## 4. Action items

| # | Action | Owner | Due |
|---|---|---|---|
| 1 | Check the lat-longs shared on the call and email back which LSPs serve each one | Partner (Arjuna) | TBC |
| 2 | Look for Cuttack cover: check current LSPs first, otherwise start onboarding a new LSP (depends on ONDC) and give a date | Partner | TBC (about 1 week, as they said) |
| 3 | Check with tech whether the wallet can be mirrored in the TF owner dashboard (recharge + balance), and what it costs and how long it takes | Partner | TBC |
| 4 | Share API documentation (quote API, order API, "fastest agent" mode) | Partner tech | TBC |
| 5 | Send the onboarding form | Partner (Arjuna) | TBC |
| 6 | Fill in the onboarding form, then get a sandbox API account | TF | After #5 |
| 7 | Read the docs and scope the change from fixed-rate to live-quote pricing | TF tech | Before go-live |
| 8 | Decide on billing: each restaurant has its own wallet, a mirrored wallet, or a month-end invoice | TF lead | After #3 |
| 9 | Test in sandbox (ask the partner for a dummy rider by order ID), then sign the agreement, then go to production | TF + Partner | Target start about **10 Oct 2026** (Bhubaneswar + Kolkata) |

---

## 5. Risks and questions to settle before signing

1. **Distance mismatch:** the LSP quoted about 17–18 km where Google shows about 7 km. The diner or restaurant would pay for the LSP's distance. Set an account-level km cap, and compare quotes against our own distance on test orders.
2. **Dynamic price vs what the diner sees:** decide what the diner is shown when the live quote is different from what we'd expect, and what happens if the quote goes up between checkout and booking.
3. **"Fastest agent" pricing:** the price is whichever LSP assigns first, not the cheapest. Confirm when the final price is locked and how it's reported back to us.
4. **Refunds are slow:** a failed delivery is only credited at month end, and only after the LSP pays out. This affects the diner-first refund rule in file 10 (section 2). The restaurant carries the cost until then.
5. **Ops hours 7 am to 12 midnight:** late-night orders have no live ops support.
6. **Staff login:** staff need the admin's OTP to log in, which adds friction for store managers.
7. **Cuttack** depends on ONDC LSP onboarding, with no firm date.
8. **Wallet friction:** one wallet and one login per restaurant is the thing TF is trying to avoid.
9. **Still to confirm:** GST on LSP charges, what the ₹3 is charged on (successful orders only? what about cancellations after a rider is assigned?), the agreement terms, and SLA or penalty terms.
