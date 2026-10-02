---
name: "sag-graphify"
description: "Build, update and query a Graphify knowledge graph of everything about Stratcon Agara Global (SAG): people and current titles, services, clients, case studies, permits, meetings, decks and internal systems. Use for any question about SAG's people, history, clients or documents, or when asked to graph, map, index or connect SAG material."
---

# SAG Graphify

A Graphify (github.com/Graphify-Labs/graphify) workflow for PT Stratcon Agara Global, with SAG's knowledge built in. It does two jobs:

1. **Answer** questions about SAG. Query `graphify-out/` first if it exists. If it does not, answer from sections 3 to 12 below and say which source each fact came from.
2. **Build or update the graph** over SAG's documents (section 14 onward), using the authority rules in section 2 so stale titles and numbers never win.

Facts were compiled on 1 Oct 2026 from the SAG BOOK (June 2026), the Business Cards zip (30 Sep 2026), the Company Overview and FDE Team one-pager (Sep 2026), meeting records of 15 and 30 Sep 2026, the other Business-Docs files (old company profile PDF, Thryve deck, whiteboard photo, Taikai reference list) and the working notes in the SAG project. Re-verify anything that looks old.

The graph is a navigation aid, not proof that a claim is true. Check consequential claims against the original source.

## 1. Quick answers

- SAG = PT Stratcon Agara Global. Indonesian strategic advisory and government-relations firm, HQ South Tangerang (cards print "Bintaro, Indonesia, 15220"). Tagline: "Navigating complexity, delivering simplicity." Web stratconagaraglobal.com. Corporate mail corporate@stratconagaraglobal.com.
- Title questions: use section 3 (business cards). Never use the SAG BOOK for a current title.
- Number questions: use section 5; where sources disagree, the rule is in section 2.
- "Who handles X" questions: section 3 plus the expert bench in section 8.

## 2. Source authority (read before resolving any conflict)

Newest and most official wins. Tag the older claim as superseded; do not average or merge.

| Rank | Source | Date | Use it for | Do not use it for |
|---|---|---|---|---|
| 1 | Business Cards.zip (8 cards, Downloads/Business-Docs) | 30 Sep 2026 | Names, honorifics, titles, work email, phone | Anything beyond contact and title |
| 2 | Company Overview, FDE Team one-pager, recent MoMs | Sep 2026 | Headline stats, team description, current deals | Titles (see rank 1) |
| 3 | SAG BOOK (Corporate Profile, Complete Edition, 2026; also in project as `SAG BOOK.pdf` and `Pre-Company profile.docx`) | compiled June 2026 | History, services, track record, case studies, bios, methodology | Current titles; headline stats where the Overview differs |
| 4 | SAG working files (`sag/PROJECT.md`, `README.md`, `docs/`, older SAG-app docs) | Feb to Mar 2026 | How the internal operating model and Document Control were first designed | Names and roles (several differ from today) |
| 4a | Current SAG-app Document Control docs (`SAG-app/docs/document-control/PRODUCT_OBJECTIVES.md` for the current target; `SHARED_WORKSPACE_SETUP.md` for the dated implementation status, 15 Sep 2026, local-tested, not cloud-accepted) | Sep 2026 | What Document Control should do now and what has been built | Older SAG OS plans are historical designs only |
| 5 | Raw transcripts (Fireflies, Otter) | per meeting | Raw material for MoMs | Names or terms until corrected (section 4) |

Known conflicts and the ruling:

| Item | Says | Ruling |
|---|---|---|
| Andi Prasetyo's title | Card: Chairman. Book: President Director (and "founder"). PROJECT.md: Managing Director ("Om Andi"). Overview: Consulting Partner | Chairman. The legal board title (director vs commissioner) is a separate question and is unresolved. No source document has been located: the RUPS deed of 28 Apr 2026 in Downloads/Business-Docs belongs to PT Andalan Travel Nusantara, a client, not to SAG, and does not establish SAG's board titles. The user will look for SAG's own deed of establishment or latest amendment later. Do not guess a legal title; ask before using one in a legal document |
| Ahmed Khalifa's title | Card: Technical Manager. Book: Strategic Project Engineer (earlier: International Business Consultant). First Infrastructure & Transport deck draft: Project Engineer | Technical Manager |
| Monzer Tarig's title | Card: Strategic Project Manager. Book: Corporate Development Specialist. First Infrastructure & Transport deck draft: Strategic Corporate Development Specialist | Strategic Project Manager (the 15 Sep Bitera MoM already uses this) |
| Radka Prasetyo | Card: Director. Book: "Director" and "Managing Director / Principal Consultant" | Director |
| Diovandi's title | Card: Strategic Technical Advisor. An earlier evidence index (24 Sep) said the post-internship title was open | Strategic Technical Advisor |
| Engagements | Overview and book chapters 7: 46. Book chapter 9 and the older green "SAG -Company Profile.pdf": 47 | 46 (keep the 47 as a contradicted node) |
| Jobs enabled | Overview: 10,000+. Book: "well over ten thousand" and once "tens of thousands" | 10,000+ |
| Leadership | Overview shows "five consulting partners"; the cards show eight staff with different titles | Cards for titles; the other three Consulting Partners (section 3b) have no card in the zip; the user confirmed their title is simply "Consulting Partner" |
| Bitera site area | The 15 Sep MoM records 8,200 m²; the user earlier believed 8.2 hectares | 8,200 m², per the MoM (confirmed by the user, 2 Oct 2026). Keep 8.2 ha only as a superseded node |
| Service lines | Five taxonomies exist (section 6) | Keep all as separate nodes; link equivalents; never merge |

## 3. People

### 3a. Current team (Business Cards, 30 Sep 2026)
Cards are two-sided. Front: name, title, email, phone, office "Bintaro, Indonesia, 15220", QR code. Back: yellow shield logo, "Stratcon Agara Global — Consultancy", tagline, web address.

| Name as printed | Title on card | Email | Phone |
|---|---|---|---|
| Mr. Andi Prasetyo | Chairman | Andi.prasetyo@stratconagaraglobal.com | +62 819 19021412 |
| Mr. Jhonshan Jusli | Deputy Chairman | Jhonshan.jusli@stratconagaraglobal.com | +62 813 88666611 |
| Eng. Radka Andafa Prasetyo | Director | Radka.prasetyo@stratconagaraglobal.com | +62 819 231001 |
| Eng. Ahmed Y. S. Khalifa | Technical Manager | Ahmed.khalifa@stratconagaraglobal.com | +62 812 10020646 |
| Eng. Monzer T. M. Ahmed | Strategic Project Manager | Monzer.tarig@stratconagaraglobal.com | +62 812 12292247 |
| Diovandi Basheera Putra | Strategic Technical Advisor | Diovandi.putra@stratconagaraglobal.com | +62 821 23354935 |
| Talita Mediva | Legal Specialist | Talita.mediva@stratconagaraglobal.com | +62 851 62707969 |
| Yandra Samudra | Import & Export Specialist | Yandra.samudra@stratconagaraglobal.com | +62 816 1985575 |

Notes:
- Print the honorific exactly as on the card ("Mr.", "Eng."). Diovandi, Talita and Yandra carry none.
- Emails follow `Firstname.lastname@`, but Monzer's is `Monzer.tarig@` (his middle name, while his card name ends in "Ahmed"), so copy emails from the table instead of building them from a name.
- The FDE (Forward Deployed Engineering) team has four members: Diovandi, Radka, Ahmed and Monzer, supported by the rest of SAG. See section 9.
- Cards are the only source for phone numbers. Only put phones on documents where a contact panel is wanted.

### 3b. People named elsewhere (no card in the zip; Consulting Partner titles confirmed)
| Person | Source | What it says |
|---|---|---|
| Eka Trisny Edyanti N, S.H. | Company Overview | Consulting Partner. Senior Advisor, PT Contemporary Brump Indonesia; Trisakti law graduate; 25+ years in corporate leadership, marketing and stakeholder relations |
| Radityo Adi Nugroho, S.E. | Company Overview | Consulting Partner. 17 years at the Presidential Protocol Bureau, State Secretariat; former Head of Institutional Relations, Indonesia Deposit Insurance Corporation (LPS) |
| Henry Thenoch | Company Overview | Consulting Partner. Chemical and environmental engineer (Ohio State); director in hazardous waste, e-waste and EV-battery recycling; ex-GM, Coca-Cola bottling Sulawesi |
| Michael Jordy Lorenzo ("Jordy") | SAG BOOK; an AGM business card exists in the Drive | Corporate Development Manager (confirmed by the user, 1 Oct 2026). Book adds "Strategic Projects Lead". An AGM card also exists |
| Rahmatullah Aba ("Uncle Rahmat") | SAG BOOK; PROJECT.md | Tax affairs expert; founder of PT Justo Accountant Solusi; CFO of Koperasi Agri Energi Indonesia; ex-EY, Crowe, RSM |
| Jamal Mukaddas | SAG BOOK | Environmental, GIS and forestry expert; AMDAL team leader (KTPA/ATPA); 80+ UKL-UPL and AMDAL documents in the Riau Islands |
| "Uncle Johnson" = Jhonshan Jusli | PROJECT.md; user confirmation 1 Oct 2026 | Same person as Jhonshan Jusli (card title Deputy Chairman). The Feb 2026 operating model gave him a field due diligence role; that is a historical design role, not a card title |
| Parga / Pargata | PROJECT.md (AVG sea cucumber deal); 30 Sep Kadin attendee list | Same person (confirmed by the user, 2 Oct 2026). Link the two names with `alias_of` |

Do not include HR records (probation, contracts, BPJS, internship paperwork) in the graph. They live in the Drive `Employee` folder and are excluded in section 14.

### 3c. External people who recur
| Person | Organisation | Context |
|---|---|---|
| Mr. Handoko | SEECON | SEECON side of the 30 Sep pilot meeting |
| Mr. Putra | Kadin | Kadin side, 30 Sep; has worked closely with Mr. Andi, including on CATL. Not Diovandi Basheera Putra |
| Mr. Andrew Soetanto | AMANTRA / Kadin | Advisory Board member at AMANTRA; wore a Kadin uniform at the 30 Sep meeting |
| Andrew Pradipta | Bitera Data Center | Business development manager, 15 Sep call |

## 4. Aliases and transcript mishearings (use these to merge nodes)

| Written or heard | Means |
|---|---|
| Mr. Andi, Pak Andi, Om Andi, Mas Andi, "Mr. Andi" | Andi Prasetyo (SAG Chairman). In the 30 Sep SEECON transcript, "Speaker 2" is Mr. Andi when speaking as the SAG senior and Mr. Handoko when speaking for SEECON. Do not create global alias links from "Speaker 2" to a named person |
| Uncle Johnson, Om Johnson | Jhonshan Jusli (confirmed by the user, 1 Oct 2026) |
| Monza, Monza Tarig, Monzer Tarig, Monzer T. M. Ahmed, Monzer Tarig Abdalla Mohamedahmed | Monzer |
| Ahmed Youssef / Yousef / Yousef Saeed / Yousef Saheed Khalifa, Ahmed Y. S. Khalifa | Ahmed Khalifa |
| Talitha Mediva, Talita Mediva | Talita Mediva |
| Dio, Dio Basheera Putra, DBP | Diovandi Basheera Putra |
| si con, "konser", SEECON, Seecons | SEECON. "Konser" is uncertain. Seecons Engineering is the same company as SEECON (confirmed by the user, 1 Oct 2026); merge into one node with the alias |
| CCP, "CCP" in transcripts, CECEP | CECEP (China's leading renewable-energy company; data-centre cooling and power partner) |
| Kadin | Indonesian Chamber of Commerce and Industry |
| Amantra | Advisory platform that guides foreign investors in data centres, energy, cold storage, AI and ERP; Andrew Soetanto sits on its advisory board |
| Brump, Brunp, BRUNP | Guangdong BRUNP Recycling Technology (CATL group). Do not claim that PT Contemporary Brump Indonesia is the same legal entity; the spelling similarity is not evidence |
| Taikun vs Taikai | Two different companies: PT Taikun Petrochemical (client) and Shandong Taikai Transformer (feasibility study) |
| Galang Batang, Bintan KEK | Galang Batang Special Economic Zone, Bintan, Riau Islands |
| RDM, Rekind Daya Mamuju | PT Rekind Daya Mamuju, Mamuju power station |
| AGM | PT Agara Global Maritim, a separate company in the SAG Group; see section 11 |

## 5. Company facts

**Identity.** Strategic advisory, government relations and ESG firm for foreign and domestic investors. 20+ years of practice. Core conviction: compliance is a strategic asset, not a cost centre. The book describes an "advisory arc" of five stages: pre-entry intelligence, market entry, compliance management, stakeholder engagement, long-term advisory. Sector focus (book): energy and renewables, infrastructure, industrial development, agriculture and agribusiness, sustainable forestry, mining and minerals, petrochemicals, manufacturing.

**Headline numbers (Overview, Sep 2026).**
| Metric | Value | Note |
|---|---|---|
| Years | 20+ | |
| Client engagements | 46 | across 12+ sectors |
| Service lines | 8 | |
| Permit and licence types | 20+ | OSS, AMDAL, PBG, TUKS and more |
| Languages | 5 | EN, ID, ZH, AR, DE |
| Authorities navigated | 7+ | ministries, agencies, KEK administrators |
| Client investment facilitated | IDR 1.5T+ | |
| Client savings | IDR 200 to 600B | risk avoided plus revenue unlocked; an estimate |
| Industrial plant permitted | 700K+ m² | 105 building permits, 5 facilities, Galang Batang |
| Strategic project value advised | USD 33B | CATL, BRUNP, Antam; the value of the projects, not money through SAG |
| Jobs enabled | 10,000+ | mostly outside Java |
| Provinces (book) | 5 | Riau Islands to Papua |

**Documented engagement values (book ch. 9).** Galang Batang KEK programme Rp10.0bn contracted plus Rp10.0bn government retribution; PT Dermaga Prima Sukses Investment coal terminal Rp5.75bn quoted; full AMDAL, coal-terminal class, Rp2.3bn; PT Jingdong Industrials Rp2.1bn (1,750 t jumbo bags); PT Garuda Ark Engineering Rp200.5m; PT Gaoshi Rp35m plus per-kg fees. Pricing benchmarks: steel-import PERTEK about Rp175/kg with a ten-working-day target, PI about Rp50/kg.

**Fee model.** Fixed fees quoted up front, usually milestone-tied: part on signing, the larger share on the technical approval, the balance on the import permit.

**Brand.** Graphite & Slate design package; yellow shield logo; use the `sag-brand` skill for any SAG document or deck. Cards appear to use a serif display name with a sans body (stationery), while documents and decks use Plus Jakarta Sans per `sag-brand`. Do not "correct" one to match the other without asking. The older green "SAG -Company Profile.pdf" (11 pages, black shield logo) and the Thryve deck (yellow shield, green) are earlier styles.

## 6. Services

SAG has used five different service taxonomies. Model each as its own set of nodes, linked by `equivalent_to` edges.

**A. Eight service lines (book ch. 3, "One firm, the whole journey").** 1 Company Formation & Business Licensing; 2 Import Facilitation & Trade Compliance; 3 Environmental Permitting & Assessment; 4 Construction & Building Permits; 5 Port, Marine & Energy Facilities; 6 Certification & Sustainability (ESG); 7 Strategic & Regulatory Advisory; 8 Ongoing Compliance & Administration.

**B. Five core services (book ch. 3).** Market Entry & Strategic Consulting; Technical & Engineering Services; End-to-End Regulatory Support; Open-Door Market Entry for Global Investors; Operations, Logistics & Supply Chain Advisory.

**C. Overview's eight lines (Sep 2026).** Market Entry & Strategic Consulting; End-to-End Regulatory & Licensing Support; Environmental Permitting & AMDAL; Construction & Building Permits (PBG, SLF, SLO); Import Facilitation & Trade Compliance; Port, Marine & Energy Facilities; Certification, ESG & Carbon Advisory; Ongoing Compliance & Administration.

**D. Priority order for the Infrastructure & Transport profile deck** (whiteboard photo, for PT MITJ; maximum 15 slides at that point): 1 ESG (community outreach, green infrastructure, renewable energy); 2 FDE, Forward Deployed Engineering (ICT solutions, digital infrastructure); 3 Stakeholder management (investor coordination, procurement first, then funds); 4 Permits & licensing (EV permits); 5 Supply chain (EV charging stations, cable supply); 6 Strategic advisory; 7 Roadmap coordination (land clearing and purchasing); 8 Government relations (Transportation, Economy, Home Affairs, Industry, Energy & Mineral Resources, Manpower). The board also sketches SAG as the intermediary between MITJ and the Ministry. That deck keeps these eight and does not add Overview's formal lines.

**E. Four lines of the older green company profile** (`SAG -Company Profile.pdf`, image-only): Market Entry & Strategic Consulting; End-to-End Regulatory Support; Operations & Supply Chain Advisory; Technical & Engineering Services.

**Distinctive capabilities.** Bilingual Indonesian-Chinese practice; KEK strategy (Galang Batang); mega-scale building permits under PP 16/2021 with STRA/STRI-certified calculations and SONDIR/DCPT soil tests; TERSUS/TUKS terminal permitting and ISPS Code certification; ASI, ISO, GRS, MSC, R2v3 and GMP readiness; carbon accounting and CCS advisory (a practice in development); transaction consulting (M&A, JV, due diligence).

**Methodology.** Delivery sequence: Map, Sequence, Stress-test, Cost, Track. Four-phase core: deep diagnosis, strategic design, precision execution, continuous calibration. ESG four-stage: Assessment, Alignment, Action Plan, Execution. Risk mapping across regulatory, stakeholder, operational and reputational risk. Execution principles: clarity of scope, accountable senior owner, government-first sequencing, adaptive management, transparent reporting. Seven values (book ch. 8): absolute discretion; predictive risk mitigation; end-to-end "Open-Door" excellence; strategic connectedness; alignment with national development goals; passion for results; long-term client alliances.

## 7. Track record

**The 46 engagements (book ch. 7).** Names only; scope in parentheses where the book gives it.
1 JAPFA (ESG strategy, social licence, conflict resolution) · 2 Strategy Source, CA USA · 3 Sampoerna Strategic Group (social programmes, education) · 4 Philip Morris International · 5 Inner City, CA USA · 6 British American Tobacco (regulatory affairs lead) · 7 PT Jasa Marga Tbk (fibre-optic commercialisation) · 8 CATL · 9 The Ritz-Carlton Group · 10 PT Kimia Farma Tbk · 11 PT Jingdong Industrials Indonesia, JD.ID (incorporation, PERTEK and PI, 1,750 t jumbo bags) · 12 PT Taikun Petrochemical (RKL-RPL Rinci, PERTEK, PKKPRL) · 13 PT Gaoshi Building Material Technology (NIB/SIINas/INSW, IUI, PKKPR, UPL, PERTEK and PI; five correction rounds cleared) · 14 PT Perdagangan Cakrawala Abadi, PCA (steel PERTEK under API-P, about 2,665 t) · 15 PT RDM, Rekind Daya Mamuju · 16 PT Rekayasa Industri (corn-to-fuel stakeholder work) · 17 ANTAM-IBC-CBL (CATL, Brunp, Lygend nickel JV, Halmahera) · 18 BRUNP Recycling (Buli, East Halmahera) · 19 PT Hutan Papua Berdikari (AMDAL, carbon accounting) · 20 PT Mega Rimba Papua (PBPH forest utilisation licence) · 21 Furen Ltd · 22 PT Migu Jaya Perkasa · 23 PT Blue Ocean Hardware Indonesia · 24 PT Nanshan Fashion Bintan Indonesia (SPP, SLO) · 25 PT Garuda Ark Engineering (API-P, PERTEK, PI, B3 storage framework) · 26 PT Medical Galang Batang (hospital) · 27 PT Bintan Alumina Indonesia (28 buildings, 550,882 m²) · 28 PT Bintan Harbour Energy (72 buildings, 150,866 m²) · 29 PT Tidezen New Textile Materials · 30 PT Baraaka Bangun Indonesia · 31 Brasali Group · 32 Namicoh · 33 Ihara MFG Co Ltd · 34 PT Dermaga Prima Sukses Investment, DPSI (coal terminal, East Kalimantan: KKPR, AMDAL, PERTEK, TUKS, BUP) · 35 Hoyu · 36 Meiyume · 37 PT Jiechengsuda Trading Indonesia, JTI (5,000 t jumbo-bag PERTEK; nine PKKPR) · 38 Galenium Pharmacia · 39 Boehringer Ingelheim · 40 PT Akasha International Tbk · 41 Hainan Seafort Healthcare Ltd (BPOM, 100% foreign-owned) · 42 PT Sky Industri Indonesia · 43 PT Langkah Maju Mesinindo · 44 PT Shandong Zhengtai Construction Indonesia · 45 PT Win Power Indonesia · 46 North Seattle College (student-support digitalisation, about 40% faster service).

Gotcha: CECEP, Tongkun Group, Xinfengming, Nanshan Group, YTO Group and Bentoel are named in the book's narrative and in the Overview's "trusted by" strip but are **not** in the numbered 46. Create `client_of` edges for them, but do not count them toward 46.

**The 14 case studies (book ch. 7).**
| # | Theme | Case | Key facts |
|---|---|---|---|
| 1 | Environmental | Corn biomass-to-fuel, Mamuju (Rekind, RDM, PLN) | Field assessment and pilot; proved corn cobs can become fuel |
| 2 | Environmental | CATL and BRUNP facilities, Buli, East Halmahera | Stakeholder engagement, regulatory insight, ESG support |
| 3 | Environmental | PT Indonesia Puqing Recycling Technology, Morowali | US$71M, 133,000 m², BRUNP 70% / GEM 15% / IMIP 15%; 20,000 t/yr design; at least 98.5% recovery (design values, not audited) |
| 4 | Environmental | Sustainable forestry and natural carbon capture, Papua (Hutan Papua Berdikari) | Reforestation, carbon accounting, community social licence |
| 5 | Social | North Seattle College student-support digitalisation (ctcLink) | Radka Prasetyo's work; about 40% efficiency gain |
| 6 | Social | PPPs for national nutrition and agriculture (JAPFA Foundation) | Andi Prasetyo's work at JAPFA |
| 7 | Social | Education philanthropy foundation | 25,000+ scholarships; client left unnamed; a delivery-model case, not an engagement |
| 8 | Social | National child-nutrition campaign (JAPFA Foundation) | 55,288 students, 3,955 teachers, 290 schools, 18 provinces; JAPFA's own 2014 figures |
| 9 | Social | Community agri-energy cooperative for biomass co-firing (PT RDM) | Feasibility and business case; forward-looking projections |
| 10 | Social | Koperasi Agri Energi Indonesia (KAEI) | 7 ha pilot at Kalukku since Feb 2020; 55,000 ha plan; 250 MW co-firing plus 10 MW biomass; about IDR 7bn sought; 92.5% of gross profit to members; projections only |
| 11 | Governance | Industrial IoT for Industry 4.0, PT Siemens Indonesia | Delivered by Ahmed Khalifa and Monzer Tarig during a Siemens engineering internship; Node-RED dashboard and alerting |
| 12 | Governance | Responsible marketing standards roadmap (international tobacco group) | Andi Prasetyo's contribution |
| 13 | Governance | Digital toll-road infrastructure, fibre-optic use and broadband (PT Jasa Marga) | 24-core planning concept, 8 internal and 16 commercial; Jakarta-Bandung and Jagorawi corridors; concept figures, not audited |
| 14 | Governance | Pictorial health warning regulation (Philip Morris International and Ministry of Health) | Contributed to Indonesia's first pictorial warnings, Government Regulation 109/2012, in force 2014; names Andi Prasetyo |

The Thryve ESG deck re-uses seven of these as its Case Studies 1 to 7 (Papua forestry; Mamuju corn biomass; CATL and BRUNP Buli; RDM agri-energy cooperative; JAPFA child nutrition; responsible marketing for a tobacco group; Jasa Marga toll-road digital infrastructure).

**Flagship programmes.** Galang Batang KEK, Bintan: 105 building permits, 5 facilities, 700,000+ m², managed concurrently; the shift of building-permit authority from the regional government to the KEK administrator was tracked and managed. DPSI coal terminal at the Nanshan Chemical Industrial Park. CATL, BRUNP and Antam, Halmahera. JAPFA CSR redesign. Planned Nanshan/Huazhang recycling park, Bintan: five million tonnes a year of scrap and e-waste, permitting and quota in scoping.

**Pipeline and growth (book ch. 9).** Water-treatment opportunities in Morocco and Tunisia; oil and gas connection in Libya; early-stage Sudan; ISPS certification as a turnkey package; ASI certification for Bintan alumina; carbon markets, CCS and climate finance (practice in development); CECEP renewable facilitation (active relationship). Climate anchor: Indonesia net-zero 2060.

## 8. Expert bench and network (SAG BOOK, June 2026)

**Nine key experts (book ch. 6):** Andi Prasetyo; Radka Prasetyo; Jhonshan Jusli; Jamal Mukaddas; Rahmatullah Aba; Talita Mediva; Ahmed Khalifa; Monzer Tarig; Michael Jordy Lorenzo. Titles in the book are out of date for the first eight (section 2). Bios worth keeping: Andi, senior advisor to CATL on sustainable development and strategic relations, sustainability consultant to PT Rekind Daya Mamuju, former Commissioner at Seecons Engineering (= SEECON), JAPFA Foundation and tobacco-industry corporate-affairs background; Jhonshan, ex-JAPFA stakeholder relations, renewable energy and biomass at Koperasi Agri Energi Indonesia, GRI-certified; Radka, ESG and FDI facilitation, earlier CATL engineering-risk intern and IT roles at Seattle-area colleges; Talita, ex-Supreme Court registry (civil chamber), then legal counsel and litigator (Bank BTN due diligence, Hasnur Group due diligence); Ahmed and Monzer, Siemens Indonesia IoT work (Siemens SITRAIN certifications).

**Specialist bench:** Engineering and Infrastructure (11 named plus 9 vendor disciplines); Environmental Studies (6 named plus 2 vendor); Social and Urban Planning (4 named); Quality, Safety and Procurement (4 vendor disciplines). Named AMDAL team leaders include Ir. Nursyamsi Suleman, Ir. Sulbi and Sutran, M.Ling.

**Institutional network (four corridors, book ch. 5).**
1. Investment, legal and fiscal: BKPM and the OSS-RBA system, Ministry of Law (AHU), DJP and Customs, Ministry of Finance and Danantara.
2. Trade, industrial and energy: Ministry of Industry, Ministry of Trade, ESDM and PLN.
3. Spatial, environmental and structural: Ministry of Environment (AMDAL units), ATR/BPN, Ministry of Public Works, Sea Transportation (Hubla).
4. Human capital, security and oversight: Ministry of Manpower, Immigration, Presidential Staff Office, TNI.
Diplomatic network: 16 senior contacts; four resident embassies in Jakarta (Morocco, Tunisia, Libya, Sudan) and twelve Indonesian missions abroad. The book names individual officials. In the graph, create nodes for the institutions; create person nodes for officials only as `claimed_contact` edges sourced to "SAG BOOK ch. 5" and tag them INFERRED. They are SAG's own access claims, not verified relationships, and officeholders change.

## 9. FDE team (Forward Deployed Engineering)

Four SAG engineers (Diovandi, Radka, Ahmed, Monzer) who work on client projects: SAG handles permits, government relations and the technical proposal; the team adds working systems. Approach: Systems, then AI/agentic, then Product. First systems were for SAG itself: AI-assisted permit-document handling, Document Control with legal and director sign-off, meeting transcription into action items. Initial offerings: permit-tracking agent (maps licences by KBLI, sequences the critical path, flags rule changes); SAG AI operations system (ERP, CRM, HR, Document Control); site-safety and compliance monitoring (CCTV AI and sensors). Positioning stated in the 30 Sep notes: builders and implementers for small and mid-size players, not competing with Nvidia or AWS-scale "AI factories". Source: SAG_AI_FDE_Team.pdf (Sep 2026) and individual FDE master profiles in the `SAG FDE Team` folder (these hold personal career detail; keep out of the graph unless asked).

## 10. Current activity (Sep to Oct 2026)

| Thread | What it is | Status and facts |
|---|---|---|
| SAG x SEECON | Pilot discussion on AI agentic tools for a highway-construction consultancy | 30 Sep 2026, 14:16 WIB, in person. Idea: match SEECON's expert bank (talent pool) and technical proposals to bid requirements. Jasa Marga and Public Works integration problems used as examples. MoM `SAG_x_SEECON_MoM_30Sep2026` (v0.9, ref SAG-SEE-MOM-001), prepared by Diovandi |
| SAG x Kadin | Meeting right after SEECON, 30 Sep | SAG: Mr. Andi, Pargata, Diovandi, Ahmed, Monzer. Kadin: Mr. Putra and Mr. Andrew Soetanto (AMANTRA). Topics: foreign-investor guidance, AI data-centre ecosystem (CECEP cooling and power up to 300 MW; Runjian International for GPU and AI), FDE positioning. MoM `SAG_x_Kadin_MoM_30Sep2026`; source notes titled "Indonesia AI Infrastructure and Investment Strategy"; the raw speaker-labelled transcript (anonymous Speaker 1 to 3) is also staged and was extracted in the graph |
| SAG x Bitera Data Center | Introductory online call, 15 Sep 2026 | Bitera runs about 20 MW, scaling to 32 MW; second Jakarta site, up to about 60 MW, power, cooling and construction scope for SAG and consortium partners. First deployment of the SAG system in Indonesia. Site area: 8,200 m², per the MoM (confirmed by the user, 2 Oct 2026). Ref SAG-BDC-MOM-001 v1.0, prepared by Monzer |
| SAG company profile, Infrastructure & Transport | 24-slide Claude Slides deck, started for PT MITJ (Moda Integrasi Transportasi Jabodetabek), now a general compro | Brief in project doc `claude/MITJ_profile_brief.md`; whiteboard photo in Business-Docs; a first-version text (v1) also exists with older titles for Ahmed and Monzer. Cable partner is PT Damai Cable Indonesia (confirmed by the user, 2 Oct 2026); internal only, never named on client-facing service pages (see `sag-brand`). Open: practice-area reporting lines. EV-charging partner is Bescore |
| SAG x Thryve | ESG & Sustainability deck (`SAGxThryve.pdf`, 20 pages) | Precedent for a sector-specific deck; its closing pages hold the "Our ESG Clients" logo set (Rekind Daya Mamuju, JAPFA, a forestry-company logo, BRUNP Recycling, PLN, an institutional crest, CATL, BAT, Jasa Marga). Contact on the cover is Ahmed Khalifa. Seven case studies, five "Why choose us" points |
| Taikai feasibility study | AI-assisted sales department for Shandong Taikai Transformer's Indonesian operation, WCT Jakarta, Sep 2026 | Versions v1 to v3 plus a critique in `sag/docs`. Taikai's own overseas reference list (Indonesian nickel, aluminium and industrial-park transformer projects since 2019) is staged and extracted |
| China-Indonesia fisheries matchmaking | Online exchange and project matchmaking session (banner in Business-Docs) | Hosts: Indonesia's Ministry of Trade and the Yuanhong Functional Area administrative committee, Fuzhou New Area; executive organisers include the China-Indonesia Two-Way Investment Cooperation Service Center; co-organiser China ASEAN Marine Product Exchange. Related to the AGM seafood thread |
| Data-centre pipeline | CECEP data-centre group (Future Clients-Projects); Bitera; Amantra | See above |
| Seafood and AGM | Sea-cucumber export (Maluku to China) | See section 11 |

## 11. AGM (separate entity)

PT Agara Global Maritim, a SAG Group company: start-up seafood venture exporting dried sea cucumber from Maluku to China (harvester and sea-cucumber teaser PDFs, Indonesia-China seafood meeting notes). It has its own brand skill (`agm-brand`, Seafood and Marine editions). Keep AGM nodes in a separate community; link to SAG with `part_of_group` only. Do not apply SAG titles to AGM people. A navy ship-in-crescent-and-star logo (two image files, white and navy versions) sits in Business-Docs; it is AGM's (confirmed by the user, 2 Oct 2026).

## 12. Internal operating model (design from Feb to Mar 2026)

Source: `sag/PROJECT.md`, `README.md`, `docs/` and older SAG-app docs. Treat names and roles here as historical; for what Document Control should do now use the current `PRODUCT_OBJECTIVES.md`, and for implementation status `SHARED_WORKSPACE_SETUP.md` (local-tested on 15 Sep 2026, not cloud-accepted; release one excludes fees).
- **Three offices.** Front (origination, outbound leads on a 70/30 maritime-and-energy model, partner onboarding protocol SPOP); Middle (four sector pods: Industrial and Manufacturing, Maritime and ESG, Digital Infrastructure, Government Relations and AMDAL); Back (legal/AMDAL gate, tax and fiscal gate, field due diligence gate, Document Control engine).
- **System layer.** SAG-app: Cloudflare D1 `DOCS` database (23-table design), Google Shared Drive for files, Telegram and WhatsApp alert bots, 48-hour review SLA, status path intake_draft, pending_legal, pending_director, accepted.
- **Evidence caution.** Design documents are not proof of production deployment; the FDE evidence index says so explicitly.

## 13. Standing editorial rules for SAG materials

Decided while building external SAG profiles. Apply to other external SAG material unless the user says otherwise.
- Andi Prasetyo: mention as little as possible; SAG materials focus on SAG as a whole. Where the SAG BOOK names him (for example the PMI / Ministry of Health case), keep the book's wording.
- Land-clearing history: word it as "SAG legacy" (Jagorawi toll road, 1978) with no names, and never use the phrase "eminent domain".
- Galang Batang: no photographs, for privacy; list facility types instead of names.
- Closing contact on profile decks: the corporate mailbox only, no named person.
- Where sources conflict on a figure, follow the Company Overview (for example 46 engagements).
- Client logos on case studies are supplied by the user or taken from the SAGxThryve ending pages; do not source them elsewhere.

## 14. Corpus map and what to leave out

Graphify sends non-code files (docs, PDFs, images) to a model for extraction, so decide what goes in before running it. Build from a dedicated folder (suggested: `sag/sag-graph/`) holding copies or extracts, not from a whole drive.

| Tier | Include | Where it lives |
|---|---|---|
| 1 Authoritative | `people_registry.md` (write section 3a into it; the card PDFs have **no text layer**, so `pdftotext` returns nothing and they must be rendered with `pdftoppm -r 220` and read by vision, or transcribed once), Company Overview, FDE Team one-pager, SAG BOOK / `Pre-Company profile.md`, this skill's sections 2 and 4 | Downloads/Business-Docs; project doc `SAG BOOK.pdf` |
| 2 Activity | MoMs (Bitera, SEECON, Kadin), cleaned transcripts (after fixing section 4 mishearings), deck briefs, Taikai study and reference list, AI-infrastructure notes, SAGxThryve and company-profile PDFs (`SAG -Company Profile.pdf` and some Thryve pages are image-only; read by vision and write the notes to a text file), whiteboard photo | Downloads/Business-Docs; `Claude outputs`; project docs |
| 3 Internal design | `sag/PROJECT.md`, `README.md`, `docs/*.md`, `meeting-mind/*.md`, SAG-app `docs/` (current Document Control docs are rank 4a, section 2) | `sag`, `SAG-app` |
| 4 Opt-in only | Client folders (`Clients/*`), checklists and templates in `Dokumen Contoh`, price lists | Drive mirror `sag/Stratcon Agara Global` |

Create `.graphifyignore` at the corpus root (git syntax):
```
# Personal, HR, legal and financial: never send to a model
**/Employee/**
**/Employment*/**
**/*PKWT*
**/*Internship*
**/*Assessment Practical Training*
**/*BPJS*
**/*WLKP*
**/*RUPS*
**/*Akta*
**/*Berita Acara*
**/Legal Documents/**
**/Contracts/**
**/Certificates/**
**/*KTP*
**/*Passport*
**/*NPWP*
# Bulk or binary
**/*.m4a
**/*.mp3
**/*.ai
**/*.idml*
**/node_modules/**
**/.env*
**/.work/**
# Opt-in tier (remove a line to include that client)
**/Clients/**
**/Future Clients*/**
```
Audio recordings should be transcribed first and the transcript fixed per section 4, then added. Left out of the 1 Oct 2026 Business-Docs pass on purpose: the PKWT draft, the Berita Acara file, personal profile documents, the RUPS deed (it is Andalan's), transformer catalogues and a research paper unrelated to SAG, and the price and checklist spreadsheets (tier 4).

## 15. Build the graph

Requirements: Python 3.10+, `pip install graphifyy` (double y) or `uv tool install graphifyy`, then `graphify install`. For `.docx` and `.xlsx` install the office extra: `pip install "graphifyy[office]"`. In the cloud workspace add `--break-system-packages`. On the user's computer, run it with the device shell so files are not copied around; if the shell has no network for pip, install in the cloud workspace and work on staged copies.

1. Prepare the corpus folder and `.graphifyignore` (section 14). Write `people_registry.md` from section 3a and an `aliases.md` from section 4 so those facts are EXTRACTED text, not guesses.
2. First build: `/graphify <corpus-path> --mode deep`. Deep mode gives richer INFERRED edges, which is useful for a corpus that is mostly prose. Expect a prompt to narrow the scope above about 500 files or 2M words; narrow by tier rather than by date.
3. Semantic extraction runs through subagents. They must be `general-purpose` agents; read-only agent types silently drop their results.
4. Re-run after changes with `/graphify <corpus-path> --update` (changed files only). Add `--directed` if you want edge direction kept for "holds_title" style queries.
5. Outputs in `graphify-out/`: `graph.json` (query it), `graph.html` (explore), `GRAPH_REPORT.md` (god nodes, surprising links, suggested questions), `cache/`. Optional: `--obsidian`, `--wiki`, `--svg`.
6. To combine with other graphs: `graphify merge-graphs a.json b.json`.
7. **Preserve what was curated.** Before overwriting `graph.json`, archive the current one in `graphify-out/archive/` under a dated name. If a person has curated the graph (removed unsupported links), add new material on top of the curated `graph.json` instead of rebuilding from raw extracts, and do not re-add links they removed (1 Oct 2026: the "Speaker 2" aliases, BRUNP/Brump equivalence, Kadin/Accenture equivalence).
8. If `graph.html` shows "vis is not defined", the CDN script was blocked; inline vis-network into the page and re-check it in a headless browser.

**Node types to steer extraction toward:** Person, Organisation (SAG, client, government body, partner), Service, Engagement, Case study, Document, Meeting, Permit or regulation, Place or zone (KEK, province), Sector, Metric.

**Relationship vocabulary:** `holds_title` (card, current), `held_title` (book or older file, superseded), `supersedes`, `alias_of`, `contradicts`, `equivalent_to`, `works_at`, `client_of`, `delivered_for`, `advises`, `partner_of`, `part_of_group`, `attended`, `prepared_by`, `requires_permit`, `located_in`, `claimed_contact`, `mentions`.

**Confidence rules.** EXTRACTED: stated in a document and sourced to it (everything in section 3a). INFERRED: a reasonable link the text implies. AMBIGUOUS: uncertain or conflicting (title conflicts until resolved). Never invent edges, and never create an identity link from an anonymous transcript speaker label to a named person. If two sources disagree, keep both claims and add a `contradicts` edge plus a `supersedes` edge pointing from the higher-ranked source.

**Post-build checks.** Run these after a build. Each should come back as described; if one does not, fix the aliases or registry and re-run with `--update`.
- `graphify explain "Andi Prasetyo"` shows Chairman as current and "President Director" as superseded.
- `graphify explain "Ahmed Khalifa"` and `"Monzer"` show Technical Manager and Strategic Project Manager.
- `graphify explain "Jhonshan Jusli"` lists "Uncle Johnson" as an alias and Deputy Chairman as his only current title.
- `graphify path "Diovandi Basheera Putra" "SEECON"` finds the 30 Sep meeting.
- `graphify path "Andi Prasetyo" "CATL"` finds the advisor role and the Kadin link, with no duplicate Andi node.
- `graphify query "CCP"` lands on CECEP, not on a separate organisation.
- Engagement count nodes say 46, and CECEP is a client but not one of the 46.
- No node sourced from an excluded path (Employee, Contracts, Legal Documents).

## 16. Answering from the graph

- Broad questions: `graphify query "<question>"`. Tracing a specific chain: add `--dfs`. Cap long answers with `--budget N`.
- "How are X and Y connected": `graphify path "X" "Y"`. "What is X": `graphify explain "X"`.
- Always cite the source file and its date, and when a fact comes from the SAG BOOK say it is the June 2026 book, because titles and some numbers there are out of date.
- If the graph and section 3a disagree on a title, section 3a wins; report the mismatch and offer to rebuild.

## 17. Keeping this skill current

- When a new card batch, MoM or profile arrives, update sections 3, 10 and 2 (conflicts), then propose the full updated SKILL.md so the saved skill replaces the old one.
- Open items to resolve: the legal board titles for Andi Prasetyo and Jhonshan Jusli (no source located; the RUPS deed in Downloads/Business-Docs is PT Andalan Travel Nusantara's, not SAG's; the user will look for SAG's own deed later). Resolved 2 Oct 2026: Parga = Pargata; Bitera site area = 8,200 m² (per the MoM); cable partner = PT Damai Cable Indonesia (internal only); the ship logo is AGM's. Resolved 1 Oct 2026: Seecons Engineering = SEECON; Jordy = Corporate Development Manager; other Consulting Partners keep the title Consulting Partner; Uncle Johnson = Jhonshan Jusli.