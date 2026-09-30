# DotPe — Product & Business Model Teardown

**Target:** https://dotpe.in (DotPe Private Limited, Gurugram · CIN U72200HR2019PTC080437)
**Date of evidence:** 30 Sep 2026
**Lens:** Feature map, business model and positioning
**Feeding into:** Table Foundry F&B work. It covers DotPe as a vendor our restaurant clients use or evaluate, as a growing competitor to TF's growth and marketing services (through Amello and Horizon), and as a reference model for productizing restaurant-growth judgment.

> Evidence key: **[O]** = observed directly (site fetch, page source, HTTP headers). **[P]** = press or filing aggregator. **[C]** = competitor-authored (biased, and DotPe hasn't confirmed it). **[I]** = my inference.

---

## 1. Overview

DotPe started in 2020 as a payments-led offline-to-online (O2O) land grab for Indian SMBs. It was founded by Shailaz Nag, who also founded PayU, with Gyanesh Sharma and Anurag Gupta. It has since narrowed to **restaurant and F&B tech**, and in 2025–26 it is renaming itself as **"the AI brain for restaurants."** [P]

The arc in four phases:

| Phase | Years | What they were | Evidence |
|---|---|---|---|
| 1. O2O land grab | 2020–21 | Free "Digital Showroom" catalog and ordering app for any shop, with payments attached. Reached 7.5M sign-ups in about a year. | Forbes India Jul 2021; Business Standard Feb 2022 [P] |
| 2. F&B wedge | 2021–22 | QR dine-in ordering and direct online ordering, pitched as "freedom from the 20% aggregator commission." Wins included McDonald's India, Barista and Haldiram's. **Acquired Rista POS (Sep 2021, all cash, ~1,500 merchants).** | Inc42, YourStory, Forbes India [P] |
| 3. Enterprise F&B consolidation | 2022–25 | Series B of $58M led by Temasek at a ~$245–250M valuation. Rista became the operating core. Revenue grew but losses stayed large. | Entrackr, Tofler [P] |
| 4. AI rebrand | 2025–26 | Five-product stack: **Rista** (POS core), **SOVA** (AI host and ordering), **Sovi** (guest memory and CRM), **Amello** (AI Growth OS), **Horizon** (ad tech built on POS data). About 55,000 restaurant outlets. | amello.ai [O]; LinkedIn and aggregators [P] |

**Bottom line [I]:** DotPe is a well-funded but sub-scale restaurant POS company. It has roughly the same revenue as Petpooja with far larger losses. Its bet is that AI growth products on top of Rista data will earn more per outlet than POS subscriptions alone. The public website hasn't caught up with this strategy.

---

## 2. Feature Map

### 2.1 Core workflow (restaurant, as sold today)

1. **Onboard.** Sales-led: a "Request Demo" form, then a sales call. There's no self-serve signup on dotpe.in. [O]
2. **Set up the menu once** in Rista. It pushes channel-specific menus, prices, combos and stock-outs to dine-in, QR, the web store and Swiggy/Zomato/Amazon Food through two-way sync. [O]
3. **Take orders** from POS billing, the waiter app, QR scan-to-order and scan-to-pay, the branded web store, and aggregator orders pulled into the same queue. [O]
4. **Run the kitchen.** A KDS synced to POS tickets. [O]
5. **Fulfil.** Delivery management sends orders to third-party logistics partners at "pre-negotiated rates" across 26,000+ pincodes. [O] (The retail page states this; F&B delivery is likely the same engine. [I])
6. **Get paid.** Integrated payments and digital bills over WhatsApp. [O]
7. **Grow.** CRM segments, tiered loyalty, SMS/WhatsApp campaigns and Facebook/Google Ads from the dashboard [O]. Amello handles AI content, reviews and Google Business Profile [O], and Horizon runs data-backed ads [P].
8. **Measure.** Reports, scheduled reports and kitchen-efficiency metrics [O]. Amello sends weekly reports that tie actions to traffic, orders and retention [O].

### 2.2 Feature inventory

| Area | Feature | Status |
|---|---|---|
| **POS / billing (Rista)** | Multi-brand invoicing, partial or credit payments, WhatsApp e-bills, mobile/tablet-first cloud POS | [O] |
| **Menu** | Central menu with outlet-level status, channel-wise variants and combos, auto stock-out tied to raw materials | [O] |
| **Inventory** | Supply tracking by channel, branch and brand; item-level cost ledger; wastage, damage and theft logs; multi-location | [O] |
| **Front of house** | Waiter app, reservations, waitlist, queue management, live table occupancy, call-center reservations for chains | [O] |
| **Kitchen** | KDS synced to POS, kitchen-efficiency reports | [O] |
| **Direct ordering** | QR scan-to-menu, scan-to-order, scan-to-pay; branded web store and Digital Showroom; custom domain in under 5 minutes | [O] |
| **Aggregators** | Two-way integration with Swiggy, Zomato and Amazon Food (orders, menu, pricing, inventory, deals) | [O] |
| **Delivery** | 3PL aggregation, 26k+ pincodes, pre-negotiated rates | [O] (retail page) |
| **Payments** | Integrated payments, payment links and reminders over SMS/WhatsApp | [O] |
| **CRM / loyalty** | Behavioral segmentation, tiered loyalty, branch-level deals, abandoned-cart campaigns | [O] |
| **Marketing** | SMS and WhatsApp marketing; Facebook and Google Ads from the dashboard | [O] |
| **Amello (AI Growth OS)** | Menu and sales analysis, AI replies to reviews, on-brand content with approval flow, Instagram/Facebook posting, GBP and local SEO, retention messaging, weekly impact report, a chat to "ask your restaurant." Runs on Gemini, Claude and ChatGPT. | [O] amello.ai |
| **SOVA (AI host)** | Conversational ordering that answers menu questions, recommends, handles dietary filters and remembers preferences, across channels | [P] |
| **Sovi** | Guest memory and relationship layer for repeat business | [P] |
| **Horizon (ad tech)** | Turns POS data into targeted marketing and performance analytics | [P]. dotpehorizon.in had an **expired SSL certificate** on 30 Sep 2026 [O] |
| **Capital / lending** | "DotPe Capital" credit lines appear only on dotpe.tech, whose ownership is unclear (see §6). The Series B announcement stated plans for lending and B2B neobanking. | [P]/unverified |
| **Retail / services** | Online store themes, marketing suite, WhatsApp for Business, invoicing and ePOS. These are phase-1 pages that look like legacy. | [O] |
| **Ops promise** | "99.5% uptime guaranteed", 24/7 support, monthly updates | [O] |

### 2.3 Notable UX and GTM decisions

- **Demo-gated everything.** No pricing appears on any DotPe-owned page. That signals enterprise and mid-market sales with negotiated deals. [O]
- **The lead form mixes two ICPs.** Business categories include Salon, Bakery, Clothing, Home Decor, eCommerce and Services next to F&B, and the role field lists Owner, Store Manager, Accounts and Sales. The form still qualifies for the 2020 SMB business, not the 2026 enterprise-restaurant one. [O]
- **Anti-aggregator framing is the hook.** The strongest homepage proof is "reduced 3rd-party commission by 98%." Rista's proof is "75% fewer online-order cancellations" (Thick Shake Factory). [O]
- **AI sits on a separate brand.** Amello has its own domain, login (work.amello.ai) and voice. It's only linked from the dotpe.in nav as "Try Amello." This looks like a hedge: the AI brand can sell to non-Rista restaurants later. [I]

### 2.4 Tech and build signals (dotpe.in)

- A **static HTML site** (`index.html`, `f-b-page.html` …) using Bootstrap 5.3.5, **two copies of jQuery (1.11 and 3.7.1)**, Owl Carousel and WOW.js. The demo form posts to `curl.php`, a PHP proxy into the CRM. [O]
- Tracking: Google Tag Manager (GTM-P2H6MMKK), GA, and **two Meta pixels**. Pixels on paid social suggest demo-lead campaigns. [O]
- Good hygiene: strict CSP, HSTS and X-Frame-Options are set. Last modified 28 Sep 2026, so someone maintains it. [O]
- **The footer "Terms" link (`merchantacquistiontandc.html`) returns 404.** [O]
- Rista's Android app is `com.dotpos` and the Digital Showroom app is `com.digitaldukaan` (the original "Digital Dukaan" name). [P]

---

## 3. Business Model & Positioning

### 3.1 Revenue lines

DotPe publishes no revenue split, so this is reconstructed:

| # | Revenue line | Mechanism | Confidence |
|---|---|---|---|
| 1 | **Rista POS SaaS** | Subscription per outlet with enterprise pricing through demos. Likely the largest and most stable line. | [I] high. The product is clear; the price isn't disclosed. |
| 2 | **Direct-order take rate** | Commission per order on QR and web-store orders, reported as **1–3%** ("very low single digits" in DotPe's own words to Forbes). There's a free tier for basic QR. | Founder quote [P] plus [C] figures |
| 3 | **Payments spread** | Payment processing margin. **PayU owns 22.6%** fully diluted and is the likely gateway partner. | [P] stake; [I] economics |
| 4 | **Delivery margin** | Resale of 3PL delivery at "pre-negotiated" rates, with the spread or a platform fee kept. | [I] |
| 5 | **Marketing credits** | SMS and WhatsApp campaign credits, and managed ad spend. | [I] |
| 6 | **Amello / Horizon** | AI Growth OS subscription (undisclosed price) and ad tech, likely a managed-spend or performance fee. | [O] product exists; [I] pricing |
| 7 | **Digital Showroom Pro** | A paid 12-month plan for the SMB store, sold through resellers such as Ministry of POS. | [P] |
| 8 | **Capital** | Lending or credit lines, probably with an NBFC partner. | Stated intent only [P] |

**How the model works [I]:** DotPe gets into restaurants with a free or low-cost direct-ordering product ("cut aggregator commissions"). It keeps them with Rista, since switching POS is expensive. It then tries to make money through payments, delivery, marketing and now AI. The commission model (line 2) is also its main weakness: competitors frame it as "the better you do, the more you pay" (Bill Feeds, dineomAI) [C].

### 3.2 Financials

All figures in INR crore.

| FY | Revenue | Expenses | Net loss | Notes |
|---|---|---|---|---|
| FY22 | 17 (total) | 120.4 | (103.3) | [P] thekredible, citing RoC filings |
| FY23 | 36.9 total / 24 from operations | 108 | (~71) | Employee cost ~24, ads ~5 [P] |
| FY24 | 56.1 | n/a | n/a | [P] aggregator snippet |
| FY25 | **75–100 band, +47.7% YoY (≈₹83 cr implied)** | n/a | **Unclear.** Tofler shows operating margin **−146%** but net margin **+49%**. | [P] Tofler. The net-profit sign likely reflects a one-off gain or a data error; check it against the MCA filing before quoting. |

- **Capital raised:** ≈$93.5M (Seed $8M Feb 2020; Series A $27.5M Mar 2021 led by Google with PayU and Info Edge; Series B $58M Sep 2022 led by Temasek with MUFG, Naya and existing investors). Last valuation was about $250M. [P]
- **Headcount:** 815 in 2025 fell to about 656 in 2026 (−20%); another tracker says 551. [P] Revenue per employee is about ₹12–15 lakh (~$15–18k), which is low for SaaS. [I]
- **Unit economics:** ₹83 cr ÷ ~55,000 outlets ≈ **₹15k per outlet per year**, close to Petpooja's list price for POS alone. So DotPe earns little extra from payments and marketing today. That gap is the reason for the AI stack. [I]

**Benchmark: Petpooja** (bootstrapped until its $15.5M Series C). FY25 revenue ₹101 cr, loss ₹21.4 cr, 1 lakh+ restaurants [P]. DotPe has about 80% of Petpooja's revenue, raised about 6× the capital, and has historically lost 3–5× as much. **Petpooja is winning on efficiency; DotPe is betting on AI features to catch up.** [I]

### 3.3 ICP signals

- **Stated ICP (dotpe.in):** "75 lakh+ businesses," covering F&B, retail and services. [O] This number hasn't changed since Feb 2022 and counts free Digital Showroom sign-ups, so it's a vanity metric. [I]
- **Real ICP (Rista, Amello and the logos):** organized, multi-outlet F&B chains, often multi-brand, across QSR, casual and fine dining, cloud kitchens, cinemas, airports and hotels. Logos: McDonald's, PVR, Social, Haldiram's, Blue Tokai, Burger Singh, Biryani Blues, Farzi Cafe, Nirula's, Mad Over Donuts, Frozen Bottle, Thick Shake Factory, Drunken Monkey, Giani, Frankie. [O]
- **Buyer roles:** founder or co-founder, and e-commerce or ops heads (the testimonials come from an AVP E-commerce and a co-founder). [O]
- **Amello's ICP:** "restaurants of all sizes," owners with no data skills. It claims 50,000+ restaurants, which probably counts the Rista base [I]. That makes it a separate funnel toward smaller owners.

### 3.4 Positioning and differentiation

- **Claimed category:** first "O2O commerce," then "restaurant POS," now "AI-native restaurant OS" or "AI brain for restaurants." [P]
- **Wedge vs Zomato and Swiggy:** direct ordering and customer data ownership versus 20–25% commissions. [P]
- **Wedge vs Petpooja and Posist:** one vendor for POS, ordering, payments, marketing and AI; enterprise references; Google and Temasek backing. [I]
- **Awards:** "India's Best POS" (ET Hospitality World 2022) and "Tech Startup of the Year" (MSME India 2022). Both are four years old. [O]

### 3.5 Growth loops

- **Paid social into demo requests** (Meta pixels and GTM). [O]
- **Enterprise logo referrals.** Chain restaurant operators follow each other. [I]
- **Content SEO on Amello** (`/blog`, `/marketing-ideas`). This is the only real content engine in the group. [O]
- **Land and expand across products.** Rista sells SOVA, Sovi, Amello and Horizon. [I]
- **The original viral loop is dormant.** The Digital Showroom loop (merchant shares a store link, customers order, other merchants see it) no longer appears in DotPe's messaging. [I]

---

## 4. Strengths / Weaknesses

### Strengths
- **Real enterprise F&B references** (McDonald's, PVR, Haldiram's, Social). Chains rarely switch POS vendors without serious diligence. [O]
- **Complete stack under one login:** POS, KDS, reservations, inventory, aggregator sync, QR, payments and CRM. Enterprise buyers value having one vendor. [O]
- **Deep, practical inventory features** (item-level cost ledger, wastage and theft logs, auto stock-out) with credible testimonials. [O]
- **An AI roadmap anchored in proprietary POS data.** An AI host and a growth OS that read real sales data are more defensible than AI tools with no data. [I]
- **Strong investors and a PayU link,** which suits payments and lending. [P]

### Weaknesses
- **Burn and efficiency.** It has a long history of losses larger than revenue, headcount is shrinking, and FY25 operating margin was around −146%. A good reason to check vendor stability before recommending it to a client. [P/I]
- **The front door and the strategy don't match.** dotpe.in still sells salons and home décor with a four-year-old metric, a broken T&C link and a jQuery site. Meanwhile the real strategy lives on amello.ai and LinkedIn. [O]
- **Brand sprawl.** dotpe.in, amello.ai, dotpehorizon.in (expired cert) and dotpe.tech (unclear) split the buyer's attention. Rista, SOVA, Sovi, Amello and Horizon are five names for one stack. [O]
- **Commission pricing works against the merchant.** Competitors already attack it. [C]
- **Competitor-reported gaps:** limited offline mode, a KDS behind specialist tools, weaker multi-branch and complex-GST handling. These are unverified but match a POS built on an ordering app. [C]
- **Amello is at an early stage.** Reported early usage: 82 regular owners in month one, against a target of 100. [P]

---

## 5. Synthesis for Table Foundry

### 5.1 Borrow
- **Close the attribution loop.** Amello's weekly report links actions to traffic, orders and retention. TF campaign and offer work should end with the same kind of sales-linked scorecard, not a list of deliverables.
- **Put a number on aggregator dependency.** The "98% lower third-party commission" proof is the strongest line on their site. TF could produce a "direct vs aggregator economics" sheet for every client (share of orders, effective commission, contribution per order).
- **Buy a platform, don't build one.** DotPe bought Rista instead of building a POS. The same applies to TF's logistics work: plug into uEngage, Flexirider or other 3PLs and ONDC instead of building rider operations.
- **Ask-your-restaurant chat on client data.** Amello's chat is a strong format for owner updates on WhatsApp.

### 5.2 Avoid / gaps to exploit
- **Metrics nobody can check** (75 lakh+). TF proof should be client-level and dated.
- **Too many product names.** Sell one named system, not five sub-brands.
- **Lock-in to one POS.** Amello, Horizon and SOVA read Rista data first. Chains running Petpooja, Posist or UrbanPiper are unserved by them.
- **Vendor risk for clients.** When a TF client evaluates DotPe/Rista, add a data-portability and exit clause, and confirm the real per-outlet and per-order fees in writing.

### 5.3 Differentiate
- **Don't compete on software parity.** TF should never build POS, payments or lending. The better position is a **POS-agnostic growth and ops judgment layer**: brand, menu engineering, offer design, delivery operations and dispute handling. It should work on top of whatever stack the client already runs.
- **Human-led where it matters.** Amello automates content; TF should own strategy, offers and brand decisions, with the AI doing execution.
- **Logistics expertise.** DotPe treats delivery as resold 3PL capacity. This repo's uEngage Flash SOPs, dispute scenarios and Flexirider model show TF can go deeper on the delivery P&L (SLA breaches, dispute recovery, rider-model economics).

### 5.4 Pattern-match: a service niche worth productizing
**Restaurant growth marketing is a fragmented, judgment-heavy service niche. Amello is DotPe trying to productize it.** That confirms TF's thesis: expert rules (offer design, campaign timing, menu mix, aggregator-vs-direct decisions, delivery dispute handling) can become a **scored, config-driven engine sold in tiers**. DotPe is coming at this from the software side and is still early (82 owners in month one), so a services-first player with a sharper engine has a window.

### 5.5 Build spec draft: "TF Restaurant Growth Engine" (POS-agnostic)

**Core loop:** ingest data → score → recommend → execute → attribute → re-score, every week.

**v1 must-haves**
- Data ingestion from CSV/API exports of any POS (Petpooja, Rista, Posist), aggregator payout reports (Swiggy/Zomato) and Google Business Profile or review exports.
- A 0–100 scorecard with sub-scores for direct-order share, effective aggregator commission, repeat rate, menu contribution mix, review velocity and rating, and delivery SLA or dispute loss.
- A rules engine that maps each weak sub-score to a TF playbook (offer, campaign, menu change, 3PL dispute SOP), with an expected rupee impact.
- A weekly owner report over WhatsApp: three actions, what changed, and rupee impact against a baseline.
- A delivery-dispute module built on the existing `Logistics/10_uEngage_Delivery_Dispute_Scenarios.md`, covering claim templates and recovered amounts.

**v2 nice-to-haves**
- A chat to "ask your restaurant" on client data.
- Cross-client benchmarks by format and city (anonymized).
- ONDC and direct-channel launch playbook with economics modeling.
- Tiered packaging: Diagnostic (one-off), Growth (monthly retainer), Growth + Ops (retainer plus a share of recovered or saved money).

**Explicit non-goals**
- No POS, KDS, payments processing, lending or consumer ordering app.
- No per-order commission pricing: use flat retainers plus a share of savings.
- No "we serve everyone" positioning: F&B only.

---

## 6. Sources

| Source | Used for | Type |
|---|---|---|
| https://dotpe.in/ (HTML, headers, `js/main.js`) | Products, claims, logos, nav, tech stack, form fields, CSP, last-modified | [O] |
| https://dotpe.in/f-b-page.html | F&B modules, aggregator integrations, uptime claim | [O] |
| https://dotpe.in/retail.html | Delivery (26k pincodes), online store | [O] |
| https://dotpe.in/services.html | CRM, SMS/WhatsApp, Ads suite | [O] |
| https://dotpe.in/rista-restaurant-management-software.html | Rista modules, logos, testimonials, awards | [O] |
| https://dotpe.in/press-media.html | Funding and merchant-count press | [O] |
| https://dotpe.in/merchantacquistiontandc.html | **404** on 30 Sep 2026 | [O] |
| https://amello.ai/ | Amello product, LLM providers, 50k+ restaurants claim | [O] |
| https://www.dotpehorizon.in/ | Expired SSL cert, so contents not read | [O] |
| https://dotpe.tech/ | "DotPe Capital," Digital Showroom. **Unclear ownership:** placeholder "Brand A–E" logos and a Lovable-style build. Weighted low. | [O]/unverified |
| [Forbes India, Jul 2021](https://www.forbesindia.com/article/take-one-big-story-of-the-day/dotpe-meet-the-unlikely-freedom-fighter-battling-zomatoswiggy-for-riled-restaurants/69011/1) | Founders, "very low single digit" commission, 20k restaurants, Haldiram's | [P] |
| [Inc42: Rista acquisition](https://inc42.com/buzz/retail-tech-startup-dotpe-acquires-rista-marks-foray-into-pos-space/) · [YourStory](https://yourstory.com/2021/09/o2o-commerce-platform-dotpe-enters-pos-space-with-rista-acquisition) | Rista deal, ~1,500 merchants, all-cash | [P] |
| [Entrackr: Series B](https://entrackr.com/2022/09/exclusive-google-backed-dot-raises-58-mn-round-led-by-temasek/) · [Inc42](https://inc42.com/buzz/google-backed-dotpe-raises-54-5-mn-from-temasek-mufg-bank-others/) · [PRNewswire: Series A](https://www.prnewswire.com/in/news-releases/offline-to-online-merchant-platform-dotpe-secures-27-5-million-series-a-funding-from-payu-info-edge-ventures-and-google-835406994.html) · [PYMNTS](https://www.pymnts.com/news/investment-tracker/2022/indian-commerce-platform-dotpe-raises-58m-to-add-financial-services/) | Rounds, investors, valuation, PayU 22.6%, lending plans | [P] |
| [thekredible: FY23](https://thekredible.com/blogs/dotpe-records-a-spike-in-revenue-to-rs-37-cr-in-fy23-expenses-total-to-rs-108-cr/) (via search snippet; page blocked) | FY22 and FY23 P&L | [P] |
| [Tofler](https://www.tofler.in/dotpe-private-limited/company/U72200HR2019PTC080437) · [Tracxn](https://tracxn.com/d/legal-entities/india/dotpe-private-limited/__Tdsa-nOhgbu7jEj0S0yprZaH9jFYsF-MlM2Ea8hVOb0) | FY24 and FY25 revenue band, growth, margins | [P] |
| [Revelio Labs](https://www.reveliolabs.com/companies/dotpe/employees) · [Crustdata](https://profiles.crustdata.com/company/dotpe) · [LeadIQ](https://leadiq.com/c/dotpe/5e3fdf3d626d3b6fe06f716f) | Headcount, AI product names, 55k outlets, Amello early usage | [P] |
| [Entrackr: Petpooja Series C](https://entrackr.com/news/petpooja-raises-155-mn-series-c-at-over-3x-valuation-premium-10512396) and search results | Petpooja benchmark | [P] |
| [Bill Feeds: DotPe vs Bill Feeds](https://billfeeds.com/blog/dotpe-vs-billfeeds.html) · [dineomAI: DotPe alternatives](https://dineomai.com/blog/dotpe-alternatives) | 1–3% commission, weaknesses | [C] |
| [Ministry of POS listing](https://ministryofpos.com/product/dotpe-digital-showroom-website-development-pro-plan-12-months-subscription/) | Digital Showroom Pro plan exists (price not retrievable: 403) | [P] |

**Couldn't verify:** actual Rista per-outlet pricing, Amello pricing, FY24 and FY25 net loss, whether DotPe Capital is live, Horizon's commercial model, and the Play Store rating or review themes (page didn't render). The quickest way to close the pricing gaps is a demo request posing as a 5–10 outlet chain. The P&L gaps close with the MCA filings (Tofler "All financials", ₹349).
