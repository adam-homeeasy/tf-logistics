# uEngage delivery disputes: every case that ends in a cancel or a refund

Owner: Adam. Build: Sovit + Pratyush. Ops: TF support.
Related: `RazorpayRoute_Plan/10_Refunds_Developer_Brief.md` (refund cases 2 to 7), `RouteA_Execution/TF_Owner_Dashboard_PRD_v2_23Sep2026.md` (section 5.5, section 13 "Needs attention"), `RazorpayRoute_Plan/Diner_Policies/05_Delivery_Policy.md`, `Logistics/09_Delivery_Provider_Swap_Plan.md`.
Written: 30 Sep 2026.

---

## 1. What this file covers

- Every case where **uEngage Flash** (the delivery service that books riders for TF restaurants) or **its rider** gets something wrong, and the diner ends up with a **cancelled order** or needs a **full or part refund**.
- Riders can be uEngage-managed or come from a partner behind Flash (Porter, Shadowfax, Rapido, Ola Logistics and others). For the diner and the restaurant it's the same thing: a uEngage task. Whether uEngage or its partner is at fault is uEngage's problem, not ours.
- Section 9 lists look-alike cases that feel like delivery problems but aren't uEngage's fault. They matter because they're where most arguments with uEngage will start.
- It also covers the two other ways an order can be delivered: by the **restaurant's own riders** (booked through Flash or not), and by **another delivery company not linked to uEngage**. Who pays for a mistake changes completely depending on who the rider is (section 1a).

## 1a. Three kinds of rider, and who carries the mistake

| Rider type | How the rider is booked | What uEngage charges the restaurant's wallet | Who carries a rider mistake | Who carries a system mistake (tracking, status, OTP, assignment) |
|---|---|---|---|---|
| **Type 1: uEngage partner rider (3PL)** | TF books through Flash, Flash picks a partner (Porter, Rapido, Shadowfax and others) | **₹65 for the first 3 km, then ₹12 per km** (5 km = ₹89, 8 km = ₹125). Confirm whether GST is on top | uEngage (claim) | uEngage (claim) |
| **Type 2: restaurant's own rider, run through Flash** | Flash assigns the restaurant's own staff rider using the rider app | **₹5 per delivery** | **Restaurant.** The rider is its employee. No uEngage claim | uEngage, but only for what its software did wrong. Most claims are just the ₹5 back, unless its failure caused a refund |
| **Type 3: rider outside uEngage** | The restaurant books another company directly (Porter, Rapido, Borzo, Shadowfax app, ONDC and so on), or sends its own rider without Flash | Nothing on the uEngage wallet | Restaurant first. It claims from that company under that company's terms | Restaurant / that company. TF can't see this delivery at all unless the restaurant updates it |

What this means in practice:

- **Every scenario card in section 7 assumes Type 1.** For Type 2 and Type 3, use the same diner outcome (the diner is treated the same whoever the rider is), but the claim changes as shown in the matrix in section 7G.
- **The diner never needs to know the rider type.** The restaurant is responsible for delivery to the diner (delivery policy section 1).
- **The delivery fee the diner paid and what the restaurant paid for delivery are different numbers.** A diner might pay ₹40 while the restaurant pays uEngage ₹89. Refunds (R1, R3) give back what the **diner** paid. Claims (C1, C3) get back what the **restaurant** paid.

## 2. The ground rules (apply to every scenario)

1. **The diner never waits for uEngage.** If the fault is clear, the diner gets their refund or replacement first. Getting the money back from uEngage happens afterwards, between the restaurant and uEngage.
2. **The restaurant pays the diner from held money.** Each order's money sits on hold in the restaurant's Razorpay linked account until delivery + 24 hours. The refund comes out of that (refund brief, case 2). The dashboard then logs a **uEngage claim** with the uEngage task id.
3. **If a delivery complaint is open, the money stays on hold.** Extend the transfer hold until the complaint is closed, even past delivery + 24 hours. A false "delivered" status must not release the money before we've checked (see UE-22, UE-30).
4. **The owner approves every refund** (PRD, "Refund request"). TF ops collects the evidence and suggests a decision. For clear cases before pickup (UE-01, UE-02, UE-07, UE-08), the system suggests "cancel + full refund" and the owner approves with one tap.
5. **Cancel the rider in the same step as the refund** (refund brief, fix for bug D6). A refunded order must never still be on its way.
6. **Evidence first, then blame.** Every claim to uEngage has a task id, timestamps and proof. No proof, no claim.

## 3. Money rules

### What the diner gets back

| Rule | When | Amount |
|---|---|---|
| **R1 Full refund** | The order never reaches the diner, or arrives unusable (spilled, tampered, spoiled). Refusing at the door counts only if it's for a rider-side reason we can check: seal broken or bag visibly damaged (UE-16, UE-18), rider unsafe or abusive (UE-27), rider demanding extra money (UE-26), or more than 60 minutes past the ETA (R4). Refusing for any other reason, like a change of mind, gets no refund | Everything they paid: food, taxes, packaging, delivery fee |
| **R2 Part refund** | Some items missing, spilled or damaged | Those items at the price actually paid (after any discount), plus their share of tax and packaging. Keep the delivery fee unless rule R3 also applies |
| **R3 Delivery fee back for lateness** | Delivered more than **30 minutes after the ETA shown at checkout**, and the lateness is on the rider or uEngage side | Delivery fee, refunded automatically, no request needed |
| **R4 Very late, diner refuses** | More than **60 minutes after the ETA**, rider-side delay, diner refuses at the door | Full refund (R1). The food comes back and is written off |
| **R5 Replacement** | The diner prefers fresh food over a refund, and the kitchen is open | Diner pays nothing extra. The second delivery's cost goes into the claim |

The diner picks refund or replacement. Default to refund if they don't answer within 15 minutes.

**Cancel or refund?** Before the food leaves the restaurant, the order is **cancelled** and refunded. Once the rider has picked it up, it isn't a cancellation any more: it's a **failed or faulty delivery**, and the diner gets a refund under R1 to R4.

### What the restaurant claims from uEngage

| Rule | When | Claim amount |
|---|---|---|
| **C1 Full claim** | Clear uEngage or rider fault | Amount refunded to the diner + delivery charge taken from the wallet for that task + any second task used for a replacement |
| **C2 Split claim** | Blame shared, for example a missing item where both the seal and the rider handling are unclear | 50% of the refund, unless evidence tips it one way |
| **C3 Charge reversal only** | uEngage failed but no food was wasted and no refund was needed (for example no rider found before cooking started) | Just the delivery charge, if any was taken |
| **C4 No claim** | Force majeure, or it's the restaurant's or the diner's fault | Nothing |
| **C5 Claim from another company** | Type 3 rider outside uEngage got it wrong | Refund + what the restaurant paid that company, under that company's claim process. Nothing to uEngage |

### Worked example (Type 1, 5 km order)

- Diner paid ₹540: food ₹470, GST ₹24, packaging ₹6, delivery fee ₹40.
- Restaurant paid uEngage ₹89 for the task (₹65 + 2 km × ₹12).
- Rider loses the order (UE-20). Diner gets **R1: ₹540**. If the restaurant sends a replacement instead, the second task is another ₹89.
- **C1 claim, refund route:** ₹540 + ₹89 = **₹629**.
- **C1 claim, replacement route:** cost of the second batch of food + ₹89 + ₹89.
- Same order with the restaurant's own rider through Flash (Type 2): no claim for the loss. At most **₹5** back if Flash's software was the cause.

**Important gap:** uEngage's public terms don't promise to pay for lost, damaged or stolen orders, and they exclude indirect losses. Today every claim depends on goodwill. Section 11 lists what to get in writing before scaling.

## 4. Evidence codes

Each scenario lists the evidence it needs, using these codes.

| Code | Evidence | Where it comes from |
|---|---|---|
| **E1** | uEngage task timeline: created, assigned, reached pickup, picked up, delivered or cancelled, with times and the cancel reason | uEngage webhook log in TF + uEngage dashboard |
| **E2** | Rider GPS trail for the whole task | uEngage (ask for it on every disputed task) |
| **E3** | Pickup proof: pickup OTP and photo | uEngage |
| **E4** | Delivery proof: delivery OTP, drop photo and drop GPS point | uEngage |
| **E5** | Rider's call log to the diner (number of calls, times, how long they rang) | uEngage masked-call log |
| **E6** | Rider details: name, phone, partner (Porter, Rapido and so on), vehicle number | uEngage |
| **E7** | Kitchen times: accepted, marked ready | TF order log / kitchen screen |
| **E8** | Handover photo at the counter: sealed bags, bag count | Restaurant (make this a standard step) |
| **E9** | Diner's photos or video, sent within the complaint window | WhatsApp |
| **E10** | Chat and call notes with the diner | TF support |
| **E11** | Payment id, refund id, bank reference (ARN) | Razorpay |

## 5. Diner messages

| Code | When | Message |
|---|---|---|
| **M1** | Cancelled before pickup | "Sorry, we couldn't get a rider for your order, so we've cancelled it. Your full ₹X is on its way back to the card or UPI you paid with. It usually shows in 5 to 7 working days." |
| **M2** | Delay, new rider being found | "Your food is ready. The rider had to drop out and we're getting you a new one now. We'll update you within 10 minutes." |
| **M3** | Full refund after pickup | "We're sorry, your order didn't reach you the way it should have. We've refunded the full ₹X to the card or UPI you paid with. It usually shows in 5 to 7 working days." |
| **M4** | Part refund | "Sorry about the {item}. We've refunded ₹X for it to the card or UPI you paid with." |
| **M5** | Replacement | "We're making a fresh {order or item} for you now, at no extra cost. New ETA: {time}." |
| **M6** | Checking | "Thanks for telling us. We're checking with the delivery partner and will get back to you by {time, within 2 hours}." |
| **M7** | Delivery fee back for lateness | "Your order came later than we promised, so we've refunded your delivery fee of ₹X." |
| **M8** | Rider asked for extra money | "You never owe anything at the door. If you paid the rider anything extra, tell us how much and we'll return it to you." |

## 6. Summary of all scenarios

| ID | What went wrong | Usual diner outcome | Claim |
|---|---|---|---|
| **A. Before pickup** ||||
| UE-01 | No rider found | Cancel, full refund (or restaurant delivers itself) | C1 if food was made, else C3 |
| UE-02 | Checkout said "we deliver here", then uEngage rejected the task | Cancel, full refund | C1 if food was made |
| UE-03 | Rider cancels before pickup, no replacement in time | Cancel, full refund, or late delivery + R3 | C1 |
| UE-04 | Rider assigned but never moves | Same as UE-03 | C1 |
| UE-05 | Rider reaches the restaurant very late, food goes cold | R3, or R2/R1 if food is spoiled | C1 |
| UE-06 | Rider refuses the order at the counter | Delay + R3, or cancel + R1 | C1 |
| UE-07 | uEngage or its partner cancels the task on its own | Cancel, full refund, or restaurant delivers itself | C1 |
| UE-08 | Partner pauses the zone for weather, strike or curfew | Cancel, full refund | C4 |
| **B. At pickup** ||||
| UE-09 | Rider takes the wrong order | Replacement or full refund for both diners | C1 |
| UE-10 | Marked "picked up" but never collected | Treat as UE-03 | C1 |
| UE-11 | Fake rider collects the order | Replacement or full refund | C1 |
| UE-12 | Rider leaves a bag behind | Send the bag, or R2 | C1 |
| UE-13 | Our order is batched with other drops and arrives very late | R3, or R4 | C1 |
| **C. On the way** ||||
| UE-14 | Rider drops out after pickup, handover goes wrong | R3 if delivered, R1 if lost | C1 |
| UE-15 | Accident or breakdown | R1 or replacement | C1 (handled gently, see card) |
| UE-16 | Food spilled or crushed | R2 or R1, or replacement | C1 |
| UE-17 | Food arrives cold or melted from a long ride or no bag | R2 or R1 | C1 |
| UE-18 | Seal broken, food missing or eaten | R1 or replacement | C1 |
| UE-19 | Rider detours or makes other stops | R3, or R4 | C1 |
| UE-20 | Rider disappears with the order | R1 or replacement | C1 |
| UE-21 | Rider goes to the wrong place although the address was right | R3, or R1 if never delivered | C1 |
| **D. At the door** ||||
| UE-22 | Marked "delivered" but the diner didn't get it | R1 or replacement | C1 |
| UE-23 | Handed to the wrong person or flat | R1 or replacement | C1 |
| UE-24 | Rider says the diner didn't answer, the diner says nobody called | R1 if the call log backs the diner | C1 |
| UE-25 | Rider won't come to the gate or the usual drop point | R1 or redelivery | C1 |
| UE-26 | Rider demands extra money | Pay back the extra (M8). R1 if the diner refused and the order went back | C1 |
| UE-27 | Rude, unsafe or drunk rider, diner refuses the order | R1, or the delivery fee back if they accepted it | C1 |
| UE-28 | Left at the door or with security without being asked, then lost | R1 or replacement | C1 |
| UE-29 | Wrong bag handed over from batched orders | Replacement or R1 for both diners | C1 |
| UE-30 | Rider takes the delivery OTP over the phone and marks it delivered early | Depends on what happens next: R1 if lost | C1 |
| **E. After delivery** ||||
| UE-31 | Missing item, unclear if it's the kitchen's or the rider's fault | R2 | C2 |
| UE-32 | Complaint after the restaurant's money was released | Same outcome, paid via recovery | Same as the scenario |
| UE-33 | Diner's bank raises a "not received" chargeback | Fight it or accept it | C1 if lost |
| UE-34 | Tracking wrong or frozen, diner cancels an order that's still coming | R1 if it can't be stopped, else deliver | C1 |
| **F. System and status errors** ||||
| UE-35 | uEngage sends a false "cancelled", TF auto-refunds, food arrives anyway | Diner keeps both. Money is lost | C1 |
| UE-36 | "Delivered" status never reaches TF, order stuck, diner wrongly told it's late or refunded | Case by case | C1 if we lost money |
| UE-37 | Two riders booked for one order | No diner impact. Wallet charged twice | C3 (reverse the duplicate) |
| **G. Restaurant's own rider through Flash (Type 2)** ||||
| OF-01 | Rider app crashes or stops syncing, status and tracking freeze | Depends on what follows | C3 (₹5), C1 if it caused a refund |
| OF-02 | Flash assigns the order to an own rider who is off duty or offline | Delay + R3, or R1 | C1 if Flash ignored the rider's offline status |
| OF-03 | No own rider free, and Flash doesn't fall back to a partner rider as set up | Delay + R3, or R1 | C1 if the fallback was switched on |
| OF-04 | Fallback to a partner rider works, but costs ₹65+ instead of ₹5 | No diner impact | C4 (it's the agreed price) |
| OF-05 | Own rider loses, damages, delays or mishandles the order | Same as the matching UE card | C4, restaurant carries it |
| OF-06 | Own rider misconduct (extra money, rude, tampering) | Same as UE-26, UE-27, UE-18 | C4, restaurant disciplines its staff |
| OF-07 | Own rider's delivery OTP or photo step fails in the Flash app | Depends on what follows | C1 if the failure made a refund necessary |
| OF-08 | Flash sends the own rider to the wrong map point | R3, or R1 | C1 if TF sent the right pin |
| **H. Rider outside uEngage (Type 3)** ||||
| XP-01 | Restaurant books another company but TF still has an active uEngage task | Two riders, wallet charged ₹65+ | C4, restaurant's own error. Cancel the uEngage task fast |
| XP-02 | Outside rider loses, damages or delays the order | Same as the matching UE card | C5, from that company |
| XP-03 | TF never gets "picked up" or "delivered", diner sees a stuck order | Diner calls, may cancel | C4 / C5 |
| XP-04 | Money stays on hold forever, or releases too early, because there's no delivered time | No diner impact | None |
| XP-05 | Chargeback with no delivery proof | Likely lose | C5 if the company can give proof, else restaurant |
| XP-06 | Outside company charges more than the diner's delivery fee, or charges on a cancel | No diner impact | Restaurant and that company |
| XP-07 | Restaurant's own rider delivers without Flash and no one records it | Same as XP-03 and XP-05 | C4 |
| **I. Rider behaviour bordering on crime (any rider type)** ||||
| CR-01 | Threatens the diner to pay extra | R1 + pay back any extra. Level 2 or 3 | C1 + formal complaint |
| CR-02 | Deliberately steals the order | R1 or replacement. Level 2 | C1 + formal complaint |
| CR-03 | Contaminates the food on purpose | R1, medical help if needed. Level 3 | C1 + formal complaint |
| CR-04 | Drunk or high on duty | R1 if refused. Level 2 | C1 |
| CR-05 | Verbal abuse, slurs, intimidation | R1 if refused, else fee back. Level 2 or 3 | C1 + formal complaint |
| CR-06 | Sexual harassment at the door | R1 + Level 3 steps | C1 + formal complaint |
| CR-07 | Physical assault | 112, R1 + Level 3 steps | C1 + formal complaint |
| CR-08 | Tries to get into the home | R1 + Level 3 steps | C1 + formal complaint |
| CR-09 | Contacts the diner after delivery | R1 + Level 3 steps, data breach check | C1 + formal complaint |
| CR-10 | Comes back to the address or follows the diner | R1 + Level 3 steps | C1 + formal complaint |
| CR-11 | Damages property | R1 if the order was affected. Level 2 | C1 + formal complaint |
| CR-12 | Payment trick at the door | Pay back what was paid, M11. Level 2 | C1 + formal complaint |
| CR-13 | Someone pretends to be the rider | R1 or replacement, Level 3 if unsafe | C1 + formal complaint |
| CR-14 | Threatens or attacks restaurant staff | Reassign or R1. Level 3 | C1 + formal complaint |
| CR-15 | Shares or photographs the diner or home | R1 + Level 3 steps, data breach check | C1 + formal complaint |
| CR-16 | Anything involving a child | R1 + Level 3 steps, police report is required | C1 + formal complaint |
| CR-17 | Complaint can't be checked or looks false | Level 3: still R1. Level 2: refund, no block on that alone | Case by case |

---

## 7. Scenario cards

Each card follows the same pattern: what happens, how we find out, what to check, the outcome, the claim, the diner message and what the system does.

### A. Before pickup (booking and rider assignment)

#### UE-01 No rider found after the order is accepted
- **What happens:** the restaurant accepts and starts cooking, then Flash can't assign any rider (in-house or partner).
- **How we find out:** no `assigned` status within X minutes of task creation (set to 10 minutes), or uEngage returns "no rider".
- **Check:** E1, E7.
- **Outcome:** delivery policy section 7. The restaurant delivers itself if it can, otherwise cancel + **R1**.
- **Claim:** **C1** if food was already made (claim the food cost + any charge). **C3** if cooking hadn't started.
- **Message:** M2 while retrying, then M1 if cancelled.
- **System:** retry assignment twice, then alert the kitchen screen + owner WhatsApp: "No rider for order N. Deliver yourself or cancel?" Cancel = `cancelTask` + full refund in one step. Reason code `DLV_NO_RIDER`.

#### UE-02 Checkout said "we deliver here", then uEngage rejects the task
- **What happens:** `getServiceability` said yes at checkout, but `createTask` after payment fails with "out of zone" or "not serviceable".
- **How we find out:** error on `createTask` in `dispatchOne`.
- **Check:** E1, the serviceability reply saved at checkout (save it, with a timestamp).
- **Outcome:** cancel + **R1**, or the restaurant delivers itself.
- **Claim:** **C1** if food was made, because uEngage's own check said yes.
- **Message:** M1.
- **System:** save the serviceability reply on the order. Reason code `DLV_SERVICEABILITY_MISMATCH`.

#### UE-03 Rider cancels before pickup and no one else comes in time
- **What happens:** a rider accepts and then drops out. Flash promises instant reassignment, but the new rider is very late or never comes.
- **How we find out:** E1 shows `assigned` then `rider_cancelled`, one or more times.
- **Check:** E1, E7 (was the food ready and waiting?).
- **Outcome:** if a rider still comes, deliver + **R3** if late. If none comes within 30 minutes of food ready, cancel + **R1**.
- **Claim:** **C1**.
- **Message:** M2, then M7 or M1.
- **System:** count rider drop-outs per task and show them on the order. Reason code `DLV_RIDER_CANCELLED_PRE_PICKUP`.

#### UE-04 Ghost rider: assigned but never moves
- **What happens:** the status says "assigned" but the rider's GPS doesn't move towards the restaurant.
- **How we find out:** ETA to the restaurant keeps growing. The kitchen sees no rider.
- **Check:** E1, E2, E6.
- **Outcome:** ask uEngage to reassign after 10 minutes of no movement. After that, same as UE-03.
- **Claim:** **C1**.
- **Message:** M2.
- **System:** flag "rider not moving" when the GPS is still for 8 minutes after assignment. Reason code `DLV_RIDER_NOT_MOVING`.

#### UE-05 Rider reaches the restaurant very late and the food goes cold
- **What happens:** food is ready on time, but the rider arrives 20+ minutes later. Fries go soggy, ice cream melts, the diner complains about "quality".
- **How we find out:** diner complaint about food quality + E1/E7 show a long gap between "ready" and "reached pickup".
- **Check:** E1, E7, E9. This is the case most often wrongly blamed on the kitchen.
- **Outcome:** **R3** as standard. **R2** or **R1** if the food is visibly spoiled (photo).
- **Claim:** **C1**. Evidence: ready time vs rider arrival time.
- **Message:** M7 or M4.
- **System:** record "rider wait time" (ready to pickup) on every order. Reason code `DLV_LATE_PICKUP`.

#### UE-06 Rider refuses the order at the counter
- **What happens:** the rider turns up and won't take the order: too big, too heavy, no bag, "too far", or wants extra cash from the restaurant.
- **How we find out:** restaurant reports it. E1 may show a rider cancel after `reached_pickup`.
- **Check:** E1, E6, restaurant's note.
- **Outcome:** reassign. If late, **R3**. If nobody comes within 30 minutes, cancel + **R1**.
- **Claim:** **C1**. Report the rider (E6).
- **Message:** M2, then M7 or M1.
- **System:** "Rider refused" button on the kitchen screen that notes the reason and triggers reassignment. Reason code `DLV_RIDER_REFUSED`.

#### UE-07 uEngage or its partner cancels the task on its own
- **What happens:** the task is cancelled by uEngage (timeout, partner SLA breach, partner pulled out) without anyone at TF or the restaurant asking for it. Sometimes no webhook is sent, so nobody knows until the diner calls.
- **How we find out:** `cancelled` webhook without a TF request, or a status check finds the task cancelled.
- **Check:** E1 (who cancelled and why).
- **Outcome:** rebook straight away if the food is still good. Otherwise the restaurant delivers itself, or cancel + **R1**.
- **Claim:** **C1**.
- **Message:** M2, then M1 or M3.
- **System:** poll the status of any task with no update in 10 minutes. Treat any cancel TF didn't request as an alert, never as an automatic refund (see UE-35). Reason code `DLV_PROVIDER_CANCELLED`.

#### UE-08 Delivery partner pauses a zone for weather, a strike or a curfew
- **What happens:** after the order is booked, riders stop running in that area.
- **Outcome:** delivery policy section 13: **R1** if we can't deliver.
- **Claim:** **C4**. Nobody's fault. Ask uEngage to reverse any task charge.
- **Message:** M1 or M3.
- **System:** reason code `DLV_FORCE_MAJEURE`. Pause delivery for that restaurant on the ordering page until riders are back.

### B. At pickup

#### UE-09 Rider picks up the wrong order
- **What happens:** two riders at the same counter, or one rider with two orders, take each other's bags. Two diners get the wrong food.
- **How we find out:** diner says "this isn't my order" with a photo.
- **Check:** E3 (the pickup OTP/photo should show which bag), E8, E9.
- **Outcome:** both diners get a replacement (**R5**) or **R1**.
- **Claim:** **C1**, if the pickup photo or OTP shows the rider took the wrong bag. If the restaurant handed over the wrong bag (the rider showed the right OTP), it's the restaurant's fault (section 9).
- **Message:** M5 or M3.
- **System:** print the order number and diner's first name large on every bag. Reason code `DLV_WRONG_PICKUP`.

#### UE-10 Rider marks "picked up" but never collected the food
- **What happens:** the status says picked up, but the bag is still on the counter.
- **How we find out:** restaurant sees the bag. E2 shows the rider wasn't at the restaurant.
- **Check:** E1, E2, E3 (no valid photo).
- **Outcome:** treat as UE-03.
- **Claim:** **C1**. Flag it as possible rider fraud.
- **System:** reason code `DLV_FAKE_PICKUP`.

#### UE-11 Someone else collects the order
- **What happens:** someone claiming to be the rider takes the bag, maybe by reading out an order number. The real rider arrives later.
- **Check:** E3 (who entered the pickup OTP), E6, restaurant CCTV if it has it.
- **Outcome:** replacement (**R5**) or **R1**.
- **Claim:** **C1** if the pickup OTP was checked and uEngage's system let it through. If the restaurant skipped the OTP, it's the restaurant's fault (section 9).
- **System:** the kitchen screen must require the pickup OTP before marking "handed over". Reason code `DLV_IMPOSTER_PICKUP`.

#### UE-12 Rider leaves a bag behind
- **What happens:** an order has 2+ bags, and the rider takes only one.
- **How we find out:** diner reports missing items. Restaurant finds a bag on the counter.
- **Check:** E8 (bag count at handover), E3.
- **Outcome:** send the missing bag with a new task if it's still good, otherwise **R2**.
- **Claim:** **C1** (the second task + any refund), if E8 shows the full bag count was handed over.
- **Message:** M5 or M4.
- **System:** show the bag count on the pickup screen. The rider confirms the count. Reason code `DLV_PARTIAL_PICKUP`.

#### UE-13 Our order gets batched with other drops and arrives very late
- **What happens:** Flash's "order clubbing" or the partner rider carries several orders. Ours is the last drop and arrives very late and cold.
- **Check:** E1, E2 (stops before ours).
- **Outcome:** **R3**. **R4** if the diner refuses it.
- **Claim:** **C1**.
- **Message:** M7.
- **System:** ask uEngage to switch off clubbing for TF restaurants, or cap it at 1 other drop. Reason code `DLV_BATCHED_LATE`.

### C. On the way

#### UE-14 Rider drops out after pickup and the handover to a new rider goes wrong
- **What happens:** the first rider cancels mid-route. Flash reassigns, but the food has to be handed from rider to rider, or goes back to the restaurant, or gets lost in between.
- **Check:** E1 (two riders on one task), E2, E6 for both riders.
- **Outcome:** if it arrives late, **R3**. If it's lost or spoiled, **R1** or replacement.
- **Claim:** **C1**.
- **Message:** M2, then M7, M3 or M5.
- **System:** reason code `DLV_RIDER_CANCELLED_POST_PICKUP`.

#### UE-15 Accident or vehicle breakdown
- **What happens:** the rider has an accident or the bike breaks down. The food is lost or very late.
- **Handling:** check the rider is okay first. Don't argue about blame on the day.
- **Outcome:** **R1** or replacement.
- **Claim:** **C1** (the diner shouldn't pay for this, and the restaurant shouldn't either). Raise it gently and later.
- **Message:** M3 or M5. Don't mention the accident to the diner. Say "a problem on the way".
- **System:** reason code `DLV_ACCIDENT_BREAKDOWN`.

#### UE-16 Food spilled or crushed from rough handling
- **What happens:** curry leaks, a cake is crushed, a drink spills. The bag was sealed and fine at handover.
- **Check:** E8 (sealed, upright), E9 (photo at the door), E4 (the drop photo sometimes shows the damage).
- **Outcome:** **R2** for what's damaged, **R1** if most of it is ruined, or replacement.
- **Claim:** **C1** if E8 shows good packing. If the packaging itself failed (lid not snapped on, thin container), it's the restaurant's fault (section 9).
- **Message:** M4, M3 or M5.
- **System:** reason code `DLV_SPILL_DAMAGE`.

#### UE-17 Food arrives cold or melted from a long ride or no bag
- **What happens:** the rider has no insulated bag, or the ride took too long. Ice cream melts, hot food arrives cold.
- **Check:** E1/E2 (ride time), E9, E6 (bag noted at pickup?).
- **Outcome:** **R2** for the items affected, **R1** if the whole order is unusable.
- **Claim:** **C1**.
- **System:** the restaurant can tick "rider has no delivery bag" at pickup, which is sent to uEngage. Reason code `DLV_TEMPERATURE`.

#### UE-18 Seal broken, food missing or eaten
- **What happens:** the diner gets a bag with a torn seal, missing items or food that's clearly been touched.
- **Check:** E8 (sealed at handover), E9 (photo of the broken seal), E6.
- **Outcome:** **R1** or replacement. Food safety comes first: never ask the diner to eat the rest.
- **Claim:** **C1**. Report the rider for tampering.
- **Message:** M3 or M5.
- **System:** reason code `DLV_TAMPERED`. Three reports against the same rider means ask uEngage to block them from TF orders.
- **If it looks deliberate** (food eaten, spat in or spiked), it's no longer this card. See CR-02 or CR-03.

#### UE-19 Rider detours or makes other stops
- **What happens:** GPS shows the rider went somewhere else first (personal stop, another platform's order).
- **Check:** E2.
- **Outcome:** **R3**, or **R4**.
- **Claim:** **C1**.
- **System:** reason code `DLV_DETOUR`.

#### UE-20 Rider disappears with the order
- **What happens:** picked up, then no movement, phone off, never delivered.
- **Check:** E1, E2, E5, E6.
- **Outcome:** after 30 minutes past the ETA with no contact, **R1** or replacement. Don't make the diner wait for uEngage to find the rider.
- **Claim:** **C1**.
- **Message:** M6, then M3 or M5.
- **System:** reason code `DLV_RIDER_ABSCONDED`.

#### UE-21 Rider goes to the wrong place although the address and pin were right
- **What happens:** the diner's address and pin are correct, but the rider goes to a different building or area, maybe because uEngage turned the address into the wrong map point.
- **Check:** the address and pin TF sent (save the exact request), E2, E4.
- **Outcome:** if the rider fixes it and delivers late, **R3**. If never delivered, **R1** or replacement.
- **Claim:** **C1** if TF sent the right pin. If TF sent wrong coordinates, that's TF's fault (section 9).
- **System:** always send the diner's pin coordinates to uEngage, not just the text address. Reason code `DLV_WRONG_LOCATION`.

### D. At the door

#### UE-22 Marked "delivered" but the diner didn't get it
- **What happens:** the status says delivered, the diner says nothing came. This is the most common delivery dispute.
- **Check:** E4 (was the delivery OTP entered, is there a drop photo, where was the drop GPS point?), E2, E5.
- **Decide:**
  - No OTP, no photo, or the drop point is far from the address: **uEngage's fault**. **R1** or replacement, **C1**.
  - OTP entered by the diner and the photo shows the door: the diner probably got it. Share the proof politely. No refund. If they push, see UE-33.
  - OTP entered but the rider was never near the address: see UE-30.
- **Message:** M6 first, then M3/M5, or the proof.
- **System:** keep the money on hold until this is closed (rule 3). Reason code `DLV_FALSE_DELIVERED`.

#### UE-23 Handed to the wrong person or flat
- **What happens:** the order is left with a neighbour, another flat, or someone at the gate who isn't the diner.
- **Check:** E4 (drop photo shows the wrong door), E2, E5.
- **Outcome:** try to get it back (the neighbour may have it). If not within 20 minutes, **R1** or replacement.
- **Claim:** **C1**.
- **System:** reason code `DLV_WRONG_HANDOVER`.

#### UE-24 Rider says the diner didn't answer, the diner says nobody called
- **What happens:** the rider marks "customer unreachable" and the food goes back. Our delivery policy says there may be no refund after two failed calls, so this turns into a dispute.
- **Check:** E5 is the judge. E2 (was the rider actually at the address when calling?).
- **Decide:**
  - Fewer than 2 calls, calls under 20 seconds, or the rider was far from the address: **rider's fault**. **R1** or redelivery at no cost, **C1**.
  - 2+ proper calls from the address: diner's side (section 9). No refund, as the policy says. Offer redelivery with a new delivery fee.
- **Message:** M3/M5, or explain with the call times.
- **System:** reason code `DLV_UNREACHABLE_DISPUTED`.

#### UE-25 Rider won't come to the gate or the usual drop point
- **What happens:** the rider asks the diner to walk far, won't enter an open society gate, or won't go to the usual drop point. The diner refuses and the order goes back.
- **Check:** E2, E5, E10. Is the building actually closed to riders? (Delivery policy section 2 and section 9.)
- **Outcome:** if the building allows riders and the rider still wouldn't go, **R1** or redelivery, **C1**. If the building doesn't allow riders and the diner was told, it's not uEngage's fault.
- **System:** reason code `DLV_REFUSED_LAST_MILE`.

#### UE-26 Rider demands extra money
- **What happens:** the rider asks for a "rain charge", "long distance", "floor charge" or a tip. Either the diner pays it, or refuses and the rider holds back the food.
- **Check:** E10, E5, E6.
- **Outcome:**
  - Diner paid extra: pay back exactly that amount as a goodwill refund on the order (M8). It can't come back from the rider through Razorpay, so the restaurant pays it and claims it.
  - Diner refused and the rider left with the food: **R1** or replacement.
- **Claim:** **C1** + report the rider. This goes against our "nothing extra at the door" promise, so it's serious.
- **System:** reason code `DLV_EXTRA_CASH_DEMANDED`.
- **If the rider threatens, blocks the door or uses a payment trick,** see CR-01 or CR-12.

#### UE-27 Rude, unsafe or drunk rider
- **What happens:** the diner feels unsafe or is abused. They refuse the order, or accept it but complain.
- **Outcome:** refused: **R1**. Accepted but complained: refund the delivery fee (R3 amount) as an apology.
- **Claim:** **C1** + report the rider (E6) and ask uEngage to block them from TF orders.
- **Handling:** take the diner's word on safety. Don't ask them to prove it.
- **System:** reason code `DLV_RIDER_CONDUCT`.
- **This card is Level 1 only** (rude, careless). Drunk, abusive, threatening or anything worse: see section 7I (CR-04 to CR-08).

#### UE-28 Left at the door or with security without being asked, then lost
- **What happens:** the diner didn't ask for contactless. The rider leaves it at the gate or door anyway, and it goes missing.
- **Check:** order note (did the diner ask for contactless?), E4, E5.
- **Outcome:** no contactless request: **R1** or replacement, **C1**. Contactless requested and left as asked: counts as delivered (delivery policy section 9), no refund.
- **System:** reason code `DLV_UNAUTHORISED_DROP`.

#### UE-29 Wrong bag handed over from batched orders
- **What happens:** the rider carries several orders and hands the diner someone else's bag.
- **Outcome:** both diners: replacement or **R1**.
- **Claim:** **C1**.
- **System:** same bag labels as UE-09. Reason code `DLV_WRONG_BAG_BATCHED`.

#### UE-30 Rider takes the delivery OTP over the phone and marks it delivered early
- **What happens:** the rider calls, asks for the OTP "to find the house", enters it and marks delivered before arriving. Then the order is late, lost or never arrives.
- **Check:** E4 (drop GPS point vs address), E2, E5 (call right before the OTP was entered).
- **Outcome:** if it never arrives: **R1** or replacement. If it arrives late: **R3**.
- **Claim:** **C1**. OTP misuse.
- **System:** tell diners in the tracking message: "Share your OTP only when the food is in your hand." Reason code `DLV_OTP_MISUSE`.

### E. After delivery

#### UE-31 Missing item, unclear if it's the kitchen's or the rider's fault
- **What happens:** one item is missing, the seal looks fine or there was no seal, and the restaurant says it was packed.
- **Check:** E8 (photo of items before sealing, if taken), E9, E3.
- **Outcome:** **R2** for the diner in all cases.
- **Claim:** **C2** (split), unless E8 proves it was packed (then **C1**) or there's no seal/handover photo (then the restaurant carries it).
- **System:** push restaurants to take a handover photo. It turns C2 into C1. Reason code `DLV_MISSING_UNCLEAR`.

#### UE-32 Complaint after the restaurant's money was already released
- **What happens:** any of the above, raised after delivery + 24 hours, once the money has gone to the restaurant.
- **Outcome:** same decision as the original scenario. Payment follows refund brief case 3 (from the linked account balance or a recovery from the next payout).
- **Claim:** same as the original scenario.
- **Note:** check the complaint window in the refund policy (`{refund_window_text}`) first. Outside it, a goodwill decision only.

#### UE-33 Diner's bank raises a "not received" chargeback
- **What happens:** instead of complaining to us, the diner disputes the payment with their bank.
- **Check:** E4, E2, E5, E11.
- **Decide:** strong delivery proof (OTP by the diner + drop photo + GPS at the address): send it to Razorpay and fight the chargeback. Weak or no proof: accept the chargeback.
- **Claim:** if we lose because uEngage's proof was missing, **C1** (refund amount + chargeback fee).
- **System:** refunds are blocked while a chargeback is open (refund brief case 6). Proof must be downloadable from uEngage within the chargeback reply window.

#### UE-34 Tracking wrong or frozen, diner cancels an order that's still coming
- **What happens:** the tracking link shows the rider stuck or in the wrong place. The diner panics and cancels. The food is actually on its way.
- **Outcome:** if the rider can still deliver, call the diner, explain and deliver + **R3** if late. If the diner insists on cancelling, **R1** and bring the food back.
- **Claim:** **C1** (their tracking caused the cancel).
- **System:** reason code `DLV_TRACKING_FAULT`.

### F. System and status errors

#### UE-35 uEngage sends a false "cancelled", TF auto-refunds, the food arrives anyway
- **What happens:** a webhook says "cancelled" (glitch, partner-side swap), TF refunds automatically, but the rider delivers. The diner gets food and a full refund.
- **Check:** E1 (cancel then delivered on the same task), E4.
- **Outcome:** don't ask the diner for money back. The money is lost.
- **Claim:** **C1**. Their wrong status caused the refund.
- **System:** **never refund automatically on a uEngage "cancelled" webhook.** Put it under "Needs attention" for a person to check. Reason code `DLV_FALSE_CANCEL_STATUS`.

#### UE-36 "Delivered" status never reaches TF
- **What happens:** the webhook is lost. TF shows "on the way" for hours. The diner gets "sorry, running late" messages, or the owner gives a refund thinking it's lost.
- **Check:** E1 from uEngage's dashboard, E4.
- **Outcome:** if a refund went out wrongly, treat as UE-35. If not, just fix the status.
- **Claim:** **C1** if money was lost.
- **System:** poll `trackTaskStatus` for any task over ETA + 15 minutes with no update. Reason code `DLV_STATUS_MISSING`.

#### UE-37 Two riders booked for one order
- **What happens:** a retry or a glitch creates two tasks. Two riders come. The wallet is charged twice.
- **Outcome:** no diner refund. Cancel the second task.
- **Claim:** **C3** (reverse the duplicate charge).
- **System:** send TF's order id as the unique reference on `createTask`. Reason code `DLV_DUPLICATE_TASK`.

### G. Restaurant's own rider through Flash (Type 2, ₹5 per delivery)

The rider works for the restaurant, so the restaurant carries anything the rider does wrong. uEngage only carries what its **software** did wrong: the rider app, assignment, tracking, status, OTP and photo steps, and map points. The diner outcome is the same as for Type 1.

#### Which UE cards can still be claimed from uEngage with an own rider

| UE cards | Type 2 claim |
|---|---|
| UE-01, UE-03, UE-04, UE-06 (no rider, drop-out, not moving, refused) | C4. It's the restaurant's own staff. Exception: Flash fallback to partners failed (OF-03) |
| UE-02 (serviceability said yes, then rejected) | C1 if the check and the rejection both came from Flash |
| UE-05, UE-13, UE-19 (late pickup, batching, detour) | C4. Exception: Flash batched the order against the restaurant's settings, then C1 |
| UE-07, UE-35, UE-36, UE-37 (system cancels, false status, lost status, duplicate) | Same as Type 1. These are software faults, so C1 or C3 |
| UE-08 (weather, strike) | C4 |
| UE-09 to UE-12, UE-14 to UE-18, UE-20, UE-22 to UE-31 (rider handling and door cases) | C4. Restaurant carries it |
| UE-21 (wrong place) | See OF-08 |
| UE-33 (chargeback) | C1 only if Flash didn't store the OTP, photo or GPS the rider captured |
| UE-34 (tracking wrong) | C1 if the tracking link was wrong while the rider app was sending the right location |

#### OF-01 Rider app crashes or stops syncing
- **What happens:** the Flash rider app freezes. Status stays on "assigned", the tracking link shows nothing, the OTP screen won't load. The diner thinks the order is lost.
- **Check:** E1, E2 (gaps in GPS), the rider's own account.
- **Outcome:** if delivered, fix the status by hand. If the diner cancelled because of the freeze, R1 (like UE-34).
- **Claim:** C3 (₹5 back) if nothing was lost. C1 if the freeze led to a refund.
- **System:** allow a manual "delivered" with a reason and a photo from the restaurant. Reason code `DLV_RIDER_APP_FAULT`.

#### OF-02 Flash gives the order to an own rider who is off duty or offline
- **What happens:** auto-assignment picks a rider marked offline, on leave or already on a long trip. Nobody comes.
- **Check:** E1, rider's attendance status in Flash at the time of assignment.
- **Outcome:** reassign. Late: R3. Nobody free: R1.
- **Claim:** C1 if Flash showed the rider as offline and still assigned them. C4 if the rider forgot to go offline.
- **System:** reason code `DLV_ASSIGNED_OFFLINE_RIDER`.

#### OF-03 No own rider free, and Flash doesn't fall back to a partner rider
- **What happens:** the restaurant set Flash to use partner riders when its own are busy. Flash waits for an own rider instead.
- **Check:** the restaurant's fallback setting in Flash, E1.
- **Outcome:** R3 if late, R1 if cancelled.
- **Claim:** C1 if the fallback was switched on. C4 if it wasn't.
- **System:** show the fallback setting on the TF owner dashboard so nobody has to guess. Reason code `DLV_FALLBACK_FAILED`.

#### OF-04 Fallback works, but the task costs ₹65+ instead of ₹5
- **What happens:** this isn't a mistake. When a partner rider takes over, the ₹65 + ₹12/km price applies.
- **Diner:** nothing changes. Don't charge them extra after payment (delivery policy section 4).
- **Claim:** C4.
- **System:** show "own rider ₹5" vs "partner rider ₹X" per order on the wallet page so the owner understands the spend. This avoids a false dispute with uEngage.

#### OF-05 Own rider loses, damages, delays or mishandles the order
- **Diner:** same outcome as the matching UE card (UE-14 to UE-25, UE-28 to UE-31).
- **Claim:** C4. The restaurant carries it and deals with its staff.
- **System:** same reason codes, with rider type "own". Rider watchlist still applies, so the owner can see repeat problems with its own staff.

#### OF-06 Own rider misconduct
- **What happens:** extra money demanded, rude behaviour, tampering (UE-26, UE-27, UE-18).
- **Diner:** same as the UE card. Safety first.
- **Claim:** C4. uEngage's terms also say rider job disputes are the restaurant's problem, not uEngage's.

#### OF-07 OTP or photo step fails in the Flash app
- **What happens:** the rider can't enter the delivery OTP or upload the drop photo, so they mark delivered without proof. Later the diner says they didn't get it (UE-22) or raises a chargeback (UE-33), and there's no proof.
- **Claim:** C1 if Flash's logs show the OTP or photo step failed. C4 if the rider skipped it.
- **System:** reason code `DLV_POD_FAULT`.

#### OF-08 Flash sends the own rider to the wrong map point
- **Same as UE-21.** C1 if TF sent the right pin and Flash's map sent the rider somewhere else.

### H. Rider outside uEngage (Type 3)

TF has no link to these deliveries. No task id, no webhook, no GPS, no OTP, no proof, unless the restaurant records it. The biggest risks are a stuck order status, money released at the wrong time, and losing chargebacks.

#### XP-01 Restaurant books another company while a uEngage task is still active
- **What happens:** the restaurant gets impatient, books Rapido or Porter directly, and forgets to cancel the Flash task. Two riders come. The uEngage wallet is charged ₹65+ for a task nobody needed.
- **Diner:** no impact, as long as only one rider hands over the food.
- **Claim:** C4, the restaurant's own error. Ask uEngage to waive the charge as goodwill only.
- **System:** a "Deliver another way" button on the kitchen screen that cancels the uEngage task and records the new rider type. Reason code `DLV_DOUBLE_BOOKED_OUTSIDE`.

#### XP-02 Outside rider loses, damages or delays the order
- **Diner:** same outcome as the matching UE card.
- **Claim:** C5, from that company, under its terms and time limits. Nothing to uEngage.
- **Evidence:** the restaurant must save the outside booking id, rider name and phone, and screenshots from that company's app. Without these the claim will fail.
- **System:** "Deliver another way" asks for the company name, booking id and rider phone. Reason code `DLV_OUTSIDE_PROVIDER`.

#### XP-03 TF never hears "picked up" or "delivered"
- **What happens:** the diner's tracking and WhatsApp updates stop at "ready". The diner calls or cancels, even if the rider is nearly there.
- **Outcome:** if the diner cancels because of the missing updates while food is on the way, R1 (like UE-34).
- **Claim:** C4 or C5.
- **System:** when a restaurant picks "Deliver another way", send the diner "Your order is on its way with our rider {name, phone}" and give the restaurant a "Delivered" button.

#### XP-04 The money hold has no delivered time
- **What happens:** the Razorpay hold is set to "delivered + 24 hours". With no delivered time, the money either stays on hold forever or releases on a fallback timer before a complaint can come in.
- **Diner:** no impact.
- **System:** for Type 3, use the restaurant's "Delivered" tap. If there's no tap, release at order time + 6 hours + 24 hours, and log it.

#### XP-05 Chargeback with no delivery proof
- **What happens:** the diner's bank raises "not received". TF has no OTP, photo or GPS.
- **Outcome:** without proof from the restaurant or the outside company, the chargeback is likely lost.
- **Claim:** C5 if the company has proof. Otherwise the restaurant carries it.
- **System:** ask the restaurant to upload a delivery photo when it taps "Delivered" on Type 3 orders.

#### XP-06 Outside company charges more than the diner's fee, or charges for a cancel
- **Diner:** no impact. Never charge the diner extra after payment.
- **Claim:** between the restaurant and that company. TF isn't involved.

#### XP-07 Restaurant's own rider delivers without Flash, and nobody records it
- **Same risks as XP-03, XP-04 and XP-05.** Restaurant carries everything (C4).
- **Recommendation:** if a restaurant has its own riders, run them through Flash (Type 2). ₹5 a delivery pays for itself with the first chargeback it helps win.

### I. Rider behaviour bordering on crime

The cards above treat rider behaviour as a service problem: refund, report, block after 3 complaints. That's right for rudeness. It's wrong for anything close to a crime. Here, **one incident is enough to act**, and the diner's safety comes before the money or the claim.

This section applies to **every rider type**. With the restaurant's own rider (Type 2 or 3), the restaurant is the employer, so it does what uEngage would do in the steps below: suspends the rider and works with the police. TF switches that restaurant to partner riders until the matter is closed.

#### Three levels

| Level | What it covers | Response |
|---|---|---|
| **1. Misconduct** | Rude, asks politely for a tip, careless handling, sloppy with the OTP | The normal cards (UE-26, UE-27 and so on). Refund if needed, report, block after 3 complaints |
| **2. Serious** | Threats, forcing extra money, stealing or deliberately eating the food, drunk or high on duty, verbal abuse or slurs, payment tricks | **Blocked from TF orders after one incident.** Written complaint to uEngage within 24 hours. Full refund. Help the diner report fraud |
| **3. Crime or safety** | Assault, sexual harassment, trying to get into the home, stalking, contacting the diner after delivery, misusing the diner's number, address or photos, spiking or contaminating food, anything involving a child | **The Level 3 steps below, straight away** |

If unsure between two levels, use the higher one.

#### Level 3 steps (in this order)

1. **Safety first.** If the diner, or anyone at the address, is in danger now, tell them to call **112**. Stay with them on call or WhatsApp. Don't ask for proof.
2. **Full refund at once (R1),** with no evidence asked for, plus a goodwill gesture from the restaurant (for example the next order free). Any payment for harm beyond that is a legal matter, never a refund line.
3. **Don't contact, confront or warn the rider.** Everything goes through uEngage or the police.
4. **Freeze the evidence the same day.** Ask uEngage in writing to keep E1 to E6 for the task (timeline, GPS trail, OTP and photos, call log, rider KYC) past their normal deletion time. Save TF's own order record, webhooks and the diner chat (E10). Ask the restaurant to keep any CCTV from pickup.
5. **Block the rider across all TF restaurants** in TF's own block list, and ask uEngage in writing to take the rider off TF orders. Don't wait for three complaints.
6. **Help the diner go to the police if they choose to.** Give them the order number, times, restaurant details and a short letter from the restaurant confirming the delivery. Share the rider's identity and KYC **only with the police, on their written request**, never with the diner directly. That keeps the restaurant and TF within data protection law.
7. **Escalate within 1 hour** to the TF lead, the restaurant owner and uEngage's escalation contact. Log it as a **safety incident**, which only those people can open.
8. **Check for a data breach.** If the rider used the diner's number, address or photos after the delivery, get a lawyer's view on whether it must be reported as a personal data breach. The restaurant is responsible for the diner's data. uEngage has promised to tell it about breaches within 24 hours.
9. **Follow up.** Call the diner within 24 hours, and again when uEngage or the police reply. Don't close the incident until they've had an answer.

**Helplines to give the diner:** 112 (emergency), 1091 (women's helpline), 1930 (online money fraud).

**Children:** if the victim of a sexual offence is under 18, Indian law (POCSO) requires anyone who learns of it to report it to the police. TF and the restaurant must report it themselves. It's not the family's choice to skip it.

**Fairness to the rider:** the rider is blocked from TF orders to protect diners, but TF never calls the rider a criminal, in public or to other restaurants. Only the police and courts decide that (see CR-17).

#### Level 3 diner messages

| Code | When | Message |
|---|---|---|
| **M9** | First reply to a safety complaint | "We're so sorry. Your safety comes first. If you're in danger right now, please call 112. We've taken this rider off our orders and refunded you in full. {Name} from our team will call you in the next 15 minutes." |
| **M10** | Diner wants to go to the police | "We'll help. Here are your order details and a letter from {restaurant}. If the police contact us, we'll give them everything we have about the rider." |
| **M11** | Payment trick | "Your order was already fully paid. Please don't pay anyone at the door or share any bank OTP. If you've paid or shared an OTP, call your bank now and report it on 1930." |

#### CR-01 Rider threatens the diner to make them pay extra
- **Level:** 2. Level 3 if there's violence or a threat of violence.
- **What happens:** a step beyond UE-26. The rider won't hand over the food, blocks the door or threatens the diner until they pay.
- **Diner:** R1 or replacement, plus back any money paid (M8).
- **Check:** E2, E5, E10, E9 if the diner recorded anything.
- **Claim:** C1 + formal complaint. Block after one incident.
- **System:** reason code `DLV_CRIME_EXTORTION`.

#### CR-02 Rider deliberately steals the order
- **Level:** 2.
- **What happens:** the rider picks up and keeps the food, marks it delivered or goes offline (a deliberate version of UE-20 or UE-22). A pattern across several orders proves it.
- **Diner:** R1 or replacement.
- **Check:** E1, E2, E3, E4.
- **Claim:** C1 + formal complaint. The restaurant can file a police complaint for theft if the value or pattern justifies it.
- **System:** reason code `DLV_CRIME_THEFT`.

#### CR-03 Rider contaminates the food on purpose
- **Level:** 3 (a health risk, not just tampering).
- **What happens:** signs the food has been spat in, spiked or had something added. Or the diner or a family member feels ill after an order with a broken seal.
- **Diner:** R1. Ask them not to eat it and to keep it, the bag and the seal. If anyone feels ill, get medical help first.
- **Check:** E8 (sealed at handover), E9, E3, E4, E6.
- **Claim:** C1 + formal complaint. Level 3 steps. Keep the food for the police if the diner reports it.
- **System:** reason code `DLV_CRIME_CONTAMINATION`.

#### CR-04 Rider drunk or high on duty
- **Level:** 2. Level 3 if it leads to abuse or danger.
- **Diner:** R1 if they refused the order. Delivery fee back if they took it.
- **Check:** E10, E6, restaurant's note if seen at pickup.
- **Claim:** C1. One-incident block. If the restaurant sees it at pickup, it refuses to hand over the order and asks uEngage for another rider (UE-06).
- **System:** reason code `DLV_CRIME_INTOXICATED`.

#### CR-05 Verbal abuse, slurs or intimidation
- **Level:** 2. Level 3 if it becomes threats of harm or targets the diner's gender, religion, caste or community.
- **Diner:** R1 if refused. Delivery fee back and an apology if accepted.
- **Claim:** C1 + formal complaint. One-incident block.
- **System:** reason code `DLV_CRIME_ABUSE`.

#### CR-06 Sexual harassment at the door
- **Level:** 3.
- **What happens:** sexual comments, gestures, exposure, touching, or asking for a phone number or a meeting.
- **Diner:** M9, R1 and the Level 3 steps. A woman from TF's team makes the follow-up call if the diner prefers.
- **Claim:** C1 + formal complaint. Ask uEngage to remove the rider from its platform, not just from TF orders.
- **System:** reason code `DLV_CRIME_SEXUAL_HARASSMENT`. Safety incident.

#### CR-07 Physical assault
- **Level:** 3.
- **What happens:** the rider hits, pushes or grabs the diner, a family member, a security guard or restaurant staff.
- **Diner:** 112 and medical help first. Then M9, R1 and the Level 3 steps.
- **Claim:** C1 + formal complaint. uEngage should cover any costs the restaurant has.
- **System:** reason code `DLV_CRIME_ASSAULT`. Safety incident.

#### CR-08 Rider tries to get into the home
- **Level:** 3.
- **What happens:** the rider pushes past the door, walks in uninvited, or insists on coming inside "to use the washroom" or "to collect payment".
- **Diner:** M9, R1 and the Level 3 steps.
- **Claim:** C1 + formal complaint.
- **System:** reason code `DLV_CRIME_TRESPASS`. Safety incident.

#### CR-09 Rider contacts the diner after the delivery
- **Level:** 3 (misuse of personal data).
- **What happens:** calls, WhatsApp messages, social media requests or friend requests from the rider after the order is closed. Only possible if the rider saw or saved the diner's real number or name.
- **Diner:** M9 and the Level 3 steps. R1 on the order, even if the delivery itself was fine.
- **Check:** screenshots from the diner, E5 (was calling masked?), E6.
- **Claim:** C1 + formal complaint. Step 8 (data breach check) applies.
- **System:** reason code `DLV_CRIME_DATA_MISUSE`. Push uEngage for masked calling and hiding the diner's details after the task is closed (section 11).

#### CR-10 Rider comes back to the address or follows the diner
- **Level:** 3 (stalking).
- **What happens:** the rider turns up again with no order, waits near the building, or follows the diner.
- **Diner:** 112 if happening now. M9 and the Level 3 steps. The restaurant can offer to pause delivery to that address, or send only its own trusted rider, until the diner feels safe.
- **Claim:** C1 + formal complaint. Ask uEngage to make sure the rider is never sent to that address again.
- **System:** reason code `DLV_CRIME_STALKING`. Flag the address so that rider can never be assigned there.

#### CR-11 Rider damages property
- **Level:** 2. Level 3 if done to threaten.
- **What happens:** damages a gate, car, doorbell or camera, or the restaurant's property at pickup.
- **Diner:** R1 on the order if it was affected. Repair costs are a matter between the diner and uEngage or the police, not a refund.
- **Claim:** C1 + formal complaint. Pass the diner's repair claim to uEngage.
- **System:** reason code `DLV_CRIME_PROPERTY_DAMAGE`.

#### CR-12 Payment trick at the door
- **Level:** 2 (fraud).
- **What happens:** the rider says "your payment failed" and asks the diner to pay again to their own UPI or QR code. Or they ask for an OTP that's really a bank or UPI OTP, not the delivery OTP.
- **Diner:** M11. Pay back anything they paid the rider (M8). If they shared a bank OTP, they must call their bank and 1930 at once. TF can't reverse that money.
- **Check:** E11 (the order was fully paid), E10, the diner's payment screenshot.
- **Claim:** C1 + formal complaint. One-incident block.
- **System:** reason code `DLV_CRIME_PAYMENT_FRAUD`. Every order message says "Your order is fully paid. Never pay anyone at the door."

#### CR-13 Someone pretends to be the rider to reach the diner
- **Level:** 3.
- **What happens:** a person who isn't the assigned rider (a fake rider, or someone the real rider passed the order to) turns up at the diner's door. Linked to UE-11, but the worry is about who now knows the diner's address.
- **Diner:** M9 and the Level 3 steps if the diner feels unsafe. R1 or replacement.
- **Check:** E6 (the rider photo and name sent to the diner vs who came), E3, E4.
- **Claim:** C1 + formal complaint. Passing tasks to another person breaks uEngage's KYC promise.
- **System:** reason code `DLV_CRIME_IMPERSONATION`. The rider photo and name should always go to the diner, so they can check who's at the door.

#### CR-14 Rider threatens or attacks restaurant staff
- **Level:** 3.
- **What happens:** at pickup, the rider gets violent over waiting time, a refused order or an argument.
- **Diner:** reassign or cancel with R1 (UE-06). Tell the diner "a problem at the restaurant", nothing more.
- **Restaurant:** staff safety first. 112 if needed. The restaurant can file a police complaint as the victim.
- **Claim:** C1 + formal complaint. One-incident block.
- **System:** reason code `DLV_CRIME_STAFF_THREAT`. Safety incident.

#### CR-15 Rider shares the diner's details, or photographs the diner or their home
- **Level:** 3.
- **What happens:** the rider takes photos beyond the normal drop photo (inside the home, of the diner), or shares the diner's address, phone or photos with others.
- **Diner:** M9 and the Level 3 steps. R1.
- **Check:** the drop photo in E4 (was it only the door or the bag?), anything the diner has seen shared.
- **Claim:** C1 + formal complaint. Step 8 (data breach check) applies.
- **System:** reason code `DLV_CRIME_DATA_MISUSE`. Ask uEngage to limit drop photos to the bag at the door.

#### CR-16 Anything involving a child
- **Level:** 3, always.
- **What happens:** the order is received by someone under 18, and the rider behaves inappropriately towards them in any way.
- **Diner:** speak to the parent or guardian. M9, R1 and the Level 3 steps.
- **Must do:** if it's sexual in any way, **TF and the restaurant report it to the police themselves** (POCSO). Don't wait for the family. Never contact the child directly.
- **Claim:** C1 + formal complaint. Ask uEngage to remove the rider from its platform.
- **System:** reason code `DLV_CRIME_CHILD_SAFETY`. Safety incident, restricted to the fewest people possible.

#### CR-17 A complaint we can't check, or that looks false
- **What happens:** a Level 2 or 3 complaint with no supporting evidence, or one that doesn't match E1 to E5 (for example the rider was never near the address). Sometimes it's a way to get a free meal.
- **Diner:** for Level 3, still refund in full and follow the safety steps. Getting a real case wrong is far worse than losing one meal. For Level 2 with nothing to back it up, refund the order but don't block the rider on that alone.
- **Rider:** block from TF orders while it's checked, but tell uEngage it's "not yet confirmed". Never share the accusation with other restaurants or in public.
- **Pattern check:** if the same diner makes repeated complaints that don't hold up, TF ops reviews it. The restaurant can decline future orders from that diner, with a reason logged.
- **System:** reason code `DLV_CRIME_UNVERIFIED`.

---

## 8. Decision flow for TF ops

1. **Is the diner safe?** If not (UE-15, or any case in section 7I), handle that first. For Level 3, follow the Level 3 steps and put everything else below on hold.
2. **Did the food leave the restaurant?** Check E1 + E3.
   - No: section A. Cancel or wait, then R1 or R3.
   - Yes: go to 3.
3. **Did it reach the right diner?** Check E4 + E2 + E5.
   - No or unclear: sections C and D. R1 or replacement.
   - Yes: go to 4.
4. **Was it in good shape and on time?** Check E9 + E1.
   - Damaged, missing or late: R2, R3 or R4.
5. **Who was the rider?** Type 1 partner rider, Type 2 own rider through Flash, or Type 3 outside uEngage (section 1a). The diner outcome stays the same, but the claim changes (section 7G and 7H).
6. **Whose fault?** Use the card. If it's in section 9, no uEngage claim.
7. **Owner approves** on the dashboard, cause "Delivery issue" + reason code + rider type. The refund goes out, the rider is cancelled if still active, and the claim is logged (to uEngage with the task id, or to the outside company with its booking id) with the evidence attached.
8. **Close the loop**: the owner marks the claim "Claimed", then "Received" (PRD section 13).

Target times: diner gets a first reply (M6) within **10 minutes**, a decision within **2 hours** in service hours.

## 9. Look-alike cases that are not uEngage's fault (no claim)

| Case | Whose fault | What happens |
|---|---|---|
| uEngage wallet too low, task rejected | Restaurant | R1 to the diner. Restaurant carries it. The wallet-low alert already exists |
| Kitchen late, rider waited | Restaurant | R3 if very late. No claim. E7 vs E1 proves it |
| Wrong or missing item packed | Restaurant | R2. No claim |
| Packaging failed (lid, thin box) though handling was fine | Restaurant | R2 or R1. No claim |
| Restaurant handed the wrong bag though the rider gave the right OTP | Restaurant | Replacement or R1. No claim |
| Restaurant skipped the pickup OTP and a fake rider took it | Restaurant | Replacement or R1. No claim |
| Diner gave a wrong or incomplete address or pin | Diner | No refund (policy). Offer redelivery for a fee |
| Diner didn't answer 2+ proper calls from the address | Diner | No refund (policy). E5 proves it |
| Diner asked for contactless and it was left as asked | Diner | Counts as delivered |
| TF sent the wrong coordinates to uEngage | TF | R1. TF carries it |
| TF refunded but didn't cancel the rider (bug D6) | TF | Diner keeps both. TF carries it |
| TF refunded twice (bug D5) | TF | TF carries it |
| Weather, strike, curfew | Nobody | R1. Ask for any task charge back |
| Restaurant's own rider (Type 2 or 3) got it wrong | Restaurant | Same diner outcome. No uEngage claim |
| Partner rider used as fallback costs ₹65+ instead of ₹5 | Nobody, agreed price | No claim (OF-04) |
| Restaurant booked an outside rider and left the uEngage task running | Restaurant | No claim (XP-01) |
| Outside company (Type 3) got it wrong | That company | Claim from that company (C5), not uEngage |

## 10. For the developers

### Reason codes (cause = "Delivery issue")

`DLV_NO_RIDER`, `DLV_SERVICEABILITY_MISMATCH`, `DLV_RIDER_CANCELLED_PRE_PICKUP`, `DLV_RIDER_NOT_MOVING`, `DLV_LATE_PICKUP`, `DLV_RIDER_REFUSED`, `DLV_PROVIDER_CANCELLED`, `DLV_FORCE_MAJEURE`, `DLV_WRONG_PICKUP`, `DLV_FAKE_PICKUP`, `DLV_IMPOSTER_PICKUP`, `DLV_PARTIAL_PICKUP`, `DLV_BATCHED_LATE`, `DLV_RIDER_CANCELLED_POST_PICKUP`, `DLV_ACCIDENT_BREAKDOWN`, `DLV_SPILL_DAMAGE`, `DLV_TEMPERATURE`, `DLV_TAMPERED`, `DLV_DETOUR`, `DLV_RIDER_ABSCONDED`, `DLV_WRONG_LOCATION`, `DLV_FALSE_DELIVERED`, `DLV_WRONG_HANDOVER`, `DLV_UNREACHABLE_DISPUTED`, `DLV_REFUSED_LAST_MILE`, `DLV_EXTRA_CASH_DEMANDED`, `DLV_RIDER_CONDUCT`, `DLV_UNAUTHORISED_DROP`, `DLV_WRONG_BAG_BATCHED`, `DLV_OTP_MISUSE`, `DLV_MISSING_UNCLEAR`, `DLV_TRACKING_FAULT`, `DLV_FALSE_CANCEL_STATUS`, `DLV_STATUS_MISSING`, `DLV_DUPLICATE_TASK`, `DLV_RIDER_APP_FAULT`, `DLV_ASSIGNED_OFFLINE_RIDER`, `DLV_FALLBACK_FAILED`, `DLV_POD_FAULT`, `DLV_DOUBLE_BOOKED_OUTSIDE`, `DLV_OUTSIDE_PROVIDER`, `DLV_CRIME_EXTORTION`, `DLV_CRIME_THEFT`, `DLV_CRIME_CONTAMINATION`, `DLV_CRIME_INTOXICATED`, `DLV_CRIME_ABUSE`, `DLV_CRIME_SEXUAL_HARASSMENT`, `DLV_CRIME_ASSAULT`, `DLV_CRIME_TRESPASS`, `DLV_CRIME_DATA_MISUSE`, `DLV_CRIME_STALKING`, `DLV_CRIME_PROPERTY_DAMAGE`, `DLV_CRIME_PAYMENT_FRAUD`, `DLV_CRIME_IMPERSONATION`, `DLV_CRIME_STAFF_THREAT`, `DLV_CRIME_CHILD_SAFETY`, `DLV_CRIME_UNVERIFIED`.

Every `DLV_CRIME_*` code also carries a **level** (2 or 3). Level 3 codes open a safety incident automatically.

Each code carries a default outcome (R1 to R5) and a default claim type (C1 to C5) from the cards above. The owner can change them before approving.

Every order also stores `rider_type`: `uengage_3pl`, `own_flash`, `own_direct` or `outside_provider`, plus `outside_provider_name` and `outside_booking_id` for Type 3. The default claim type for a reason code is looked up by reason code + rider type (matrix in section 7G).

### Changes to today's code

| # | Change | Why | Scenarios |
|---|---|---|---|
| 1 | Never refund automatically on a uEngage `cancelled` webhook. Put it under "Needs attention" | False cancels | UE-07, UE-35 |
| 2 | Poll `trackTaskStatus` for tasks with no update in 10 minutes, or over ETA + 15 | Lost webhooks, silent cancels | UE-07, UE-36 |
| 3 | Keep the Razorpay transfer on hold while a delivery complaint is open | False "delivered" releases money early | UE-22, UE-30 |
| 4 | Cancel the uEngage task in the same step as the refund | Bug D6 | All |
| 5 | Send TF's order id as the unique reference on `createTask` | Duplicate tasks | UE-37 |
| 6 | Save the serviceability reply, the exact `createTask` request (with pin coordinates) and every webhook, with timestamps | Proof for claims | UE-02, UE-21, all |
| 7 | Kitchen screen: pickup OTP required, bag count, "rider refused" and "no delivery bag" buttons, handover photo | Proof at pickup | UE-06, UE-11, UE-12, UE-17, UE-31 |
| 8 | Record rider wait time (ready to pickup) and rider drop-outs per task | Proves lateness is rider-side | UE-03, UE-05 |
| 9 | Auto-refund the delivery fee (R3) when delivered 30+ minutes after the checkout ETA and E1/E7 show a rider-side delay | Lateness rule | UE-05, UE-13, UE-19 |
| 10 | uEngage claim record: task id, reason code, claim type, amount, evidence links, status (To claim, Claimed, Received, Rejected) | PRD section 13 | All |
| 11 | Monthly claims export per restaurant (PRD PAY-SM-05) | Reconcile with uEngage | All |
| 12 | Rider watchlist: count complaints per rider (E6). Three strikes means ask uEngage to block them. Any Level 2 or 3 code blocks after one | Repeat offenders and serious cases | UE-18, UE-26, UE-27, section 7I |
| 13 | Store `rider_type` on every order. Read it from the Flash task (own rider or partner) | Claim type depends on it | Section 1a |
| 14 | Work out the expected task charge (₹5 own rider, ₹65 + ₹12 per km over 3 km for partners) and compare it with what the wallet was charged. Flag gaps | Catch wrong charges | OF-04, UE-37 |
| 15 | "Deliver another way" button: cancels the uEngage task, records company, booking id and rider phone, sends the diner a rider update, and shows "Delivered" with a photo upload | Type 3 deliveries have no data otherwise | XP-01 to XP-07 |
| 16 | Hold release for Type 3: restaurant's "Delivered" tap + 24 hours, fallback order time + 6 hours + 24 hours | No webhook to start the timer | XP-04 |
| 18 | TF-wide rider block list, keyed on rider phone and uEngage rider id, checked on every assignment. If a blocked rider is assigned, cancel and rebook automatically | One-incident blocks must work across all TF restaurants | Section 7I |
| 19 | Safety incident record, separate from normal refund requests. Only the TF lead, the restaurant owner and named ops staff can open it. Every view is logged | Sensitive details, possible police case | CR-03 to CR-16 |
| 20 | "Report a safety problem" link in every rider-assigned and delivered WhatsApp message. Goes straight to the on-duty TF person with an alert, not to the normal queue | Diner can raise it in seconds | Section 7I |
| 21 | Evidence freeze: one click sends uEngage the standard written request to keep E1 to E6 for that task, and locks TF's own records for that order from deletion | Police cases can take months | Level 3 step 4 |
| 22 | Address flag: a blocked rider can never be sent to an address linked to a Level 3 incident, even if uEngage unblocks them | Stalking | CR-10 |
| 17 | Show the restaurant's Flash fallback setting (own riders first, then partners) on the owner dashboard | Stops arguments about who should have delivered | OF-03 |

## 11. Get from uEngage in writing (before scaling past pilot restaurants)

1. **Claims clause:** which of the cases above uEngage pays back (lost, damaged, tampered, false delivered, rider refusal, extra cash demanded), how much (refund + task charge + food cost), how to file, the time limit, and how fast it's credited to the wallet.
2. **Partner riders:** uEngage takes the claim even when the rider came from Porter, Rapido, Shadowfax or another partner. TF doesn't chase the partners.
3. **Evidence on request:** timeline, GPS trail, pickup and delivery OTP and photo, masked-call log and rider details for any task, within 24 hours. Needed for chargebacks too.
4. **Webhooks for every status**, including cancels uEngage makes itself, with the reason and who cancelled.
5. **No charge on failed tasks:** no platform fee or partner fee when the task is cancelled, rejected or not delivered because of uEngage's side.
6. **Order batching:** the option to switch it off, or cap it, for TF restaurants.
7. **Rider blocking:** TF can have a named rider kept off its restaurants' orders.
8. **Time limits:** how long uEngage keeps GPS and call records (need at least 120 days for chargebacks).
9. **Prices in writing:** ₹5 per own-rider delivery, and ₹65 for the first 3 km + ₹12 per km for partner riders. Confirm whether GST is extra, how the km are measured (road or straight line, restaurant to diner), and whether cancelled tasks are charged.
10. **Rider checks:** police verification for every partner rider who delivers TF orders, not just KYC. Proof on request.
11. **Masked calling only,** and the diner's name, address and phone hidden in the rider app once the task closes.
12. **One-incident blocking** at TF's request for Level 2 and 3 cases, without needing uEngage's own investigation to finish first.
13. **24x7 escalation contact** at uEngage for safety incidents, with a reply within 1 hour.
14. **Evidence kept for police cases** on written request, for as long as the case is open.
15. **Cover for crime by their riders:** uEngage pays the restaurant's costs and defends it against claims when one of its riders (or someone the rider passed the task to) commits a crime on a TF order.
16. **Own-rider software faults:** for Type 2, uEngage pays back when its app, assignment, fallback or proof steps fail (OF-01, OF-02, OF-03, OF-07, OF-08), not just the ₹5.
