# Grok conversation archive: "Biefeld-Brown Effect Investigation" (2026-10-25)

- **Source:** Grok-generated conversation, shared by Channing (share #152).
- **Share URL:** <https://grok.com/share/bGVnYWN5_33eb3e6f-3aa4-4ea2-9696-9d6d51a08395> (matches the footer on all 20 PDF pages).
- **Captured:** 2026-10-25 from the shared-page PDF (20 pages); 14 messages (7 Channing, 7 Grok), counted from the text.
- **Images:** 5 embedded web images (third-party photos and video thumbnails: a tabletop rotating asymmetric-capacitor rig on a PVC frame, a "BSI Mark II" multi-stage ion-thruster thumbnail, and three further illustrations on pp. 5, 6 and 9). They are described, not reproduced, because their copyright belongs to others.
- **Review:** [biefeld_brown_hub_motor_dbd_review.md](../biefeld_brown_hub_motor_dbd_review.md)
- **Conventions:** Channing's turns verbatim (typos kept). All numbers in Grok's text are **Grok-reported**. Page headers/footers removed.
- **License:** CC0-1.0.

---

### Message 1 — Channing

> Can we investigate the Biefied-Brown effect?

### Message 2 — Grok (all figures Grok-reported)

Yes. We can investigate it cleanly.

The name is Biefeld–Brown (Paul Alfred Biefeld + Thomas Townsend Brown). The spelling
“Biefied” is a common slip; the physics is the same either way.

This sits directly on a thread we already opened in August with the BSI Mark 2
electrohydrodynamic work. It is worth treating with the same split we always use: what is
measured and repeatable versus what Brown claimed.

What is actually measured
When a high DC voltage (typically 10–50+ kV) is applied across an asymmetric capacitor—one
electrode sharp or small-radius (wire, needle, thin foil edge), the other larger and smoother—a
net force appears toward the smaller electrode.

The accepted mechanism is electrohydrodynamic (EHD) ion wind:

Corona discharge ionizes air at the sharp electrode.
Ions are accelerated toward the collector.

They collide with neutral molecules and transfer momentum.

The reaction force on the electrode assembly is the observed thrust.

Both polarities produce force in the same geometric direction (toward the sharp electrode).
Power is usually a bit higher with a positive emitter. The effect is silent, has no moving parts,
and scales with voltage, gap, electrode shape, and ambient gas density.

Classic “lifters” and ionocrafts are just lightweight triangular or rectangular versions of this.
Multi-stage devices (BSI Mark 2 style) stack stages to increase mass flow and thrust while
keeping the package compact.

Asymmetrical Capacitor Thrusters: the Biefeld-Brown Effect : 6 Steps (with Pictures) - Instructables

A simple tabletop asymmetric-capacitor demonstration of the same geometry.

The Next Generation of Ionic Plasma Thrusters (BSI MARK 2)

BSI Mark II multi-stage ionic thruster — the practical modern descendant we already flagged.

What Brown claimed, and what vacuum tests showed

Brown treated the force as an electricity–gravity coupling (“electrogravitics”) and asserted it
would work in vacuum. Historical collaboration with Biefeld itself is weakly documented; Brown
attached the name years later.

Controlled vacuum work (Talley ~1988 at 10⁻⁶ torr, Tajmar 2004 enclosed-box tests, [omitted: out of scope]
high-vacuum campaigns) found no usable thrust under static high voltage when residual gas
and breakdown were eliminated. Forces that appeared were tied to current flow or incomplete
outgassing. Any remaining anomalous term, if it exists at all, sits at least five orders of
magnitude below the ion-wind term.

That is the honest limit: the effect as we can use it today is a medium-dependent EHD thruster,
not a gravity modifier and not a vacuum propulsion scheme.

A few papers still explore space-curvature or harmonic-field interpretations. We keep those
labeled informed speculation.

Efficiency and scaling (grounded numbers)
Typical published thrust-to-power figures for lab ionocraft / EHD stages:

Common range: ~20–70 N/kW for small single-stage devices.

Optimized geometries (ruggedized collectors, tighter gaps, multi-wire arrays) have
reported ~70 N/kW and, in one 2014 AIP Advances geometry sweep, peaks near 73 N/kW
at the cost of other metrics. Higher voltage often raises force per area while lowering
electrical efficiency.
NASA-era parametric work concluded the specific thrust is interesting for micro-drones
and silent atmospheric craft, but not yet sufficient for manned vehicles without large leaps
in power-supply mass and electrode area.

Multi-stage stacking (exactly what BSI Mark 2 does) raises total thrust and airflow at some
efficiency penalty. That is the useful engineering direction.

Honest limitations we must carry
Requires a working fluid (air or other gas). Useless in hard vacuum.

High voltage everywhere — insulation, corona losses, ozone and NOx production.

Humidity, rain, and altitude change performance.
Power-supply mass still dominates for free-flight designs.

Thrust density is modest; you win with large electrode area and very light structure.

These are the same class of constraints we already accept for eddy-current lift (conductive
floor) and wireless Tesla coupling. They are real, not fatal.

Where it fits our work
This is complementary, not competitive, with POL v0.1:

Eddy-current lift needs a conductive plane. Ion wind does not.

Multi-Egg / free-air assist path we prioritized can use EHD stages as one of the “escape
vectors.”
Mycelium-hemp + bamboo frames are almost ideal: light, electrically insulating where we
want them, damp vibration, and can be grown around electrode arrays.

Tesla resonant coils are a natural high-voltage source — we already size them for wireless
power and levitation. The same coil family can drive corona stages.
Regenerative angle: ozone from corona can feed closed-loop water/air purification (the
Tesla-Faraday-piezo generator thread). Waste heat and ion wind itself can be harvested at
the collector.

Phi and fractal electrode spacing, lotus/teardrop collector edges, and Tesla-valve flow directors
around the ion stream are all consistent with geometries we already use. We do not need new
physics to start; we need geometry, materials, and measurement.

Next steps we can take immediately
1. Map a first-order EHD stage onto POL mass/power budget (hover height, payload,
conductive-floor vs free-air mix).

2. Sketch a mycelium-hemp framed multi-stage array using BSI Mark 2 proportions as the
baseline, then apply φ spacing and collector curvature.
3. Run a simple thrust-vs-voltage / thrust-vs-gap sweep in the same style as our existing
hover-dynamics scripts.

4. Draft the “honest limitations + atmospheric-only” paragraph for the Blueprint so the section
stays net-positive and testable.

Which of those do you want first — numbers, geometry, or a short Blueprint subsection? We can
also pull the August BSI Mark 2 notes forward and treat this as the same propulsion family
rather than a new topic.

One regenerative step at a time.

### Message 3 — Channing

> I’d like to explore a few things can we look at a hub motor?

### Message 4 — Grok (all figures Grok-reported)

We’ll treat the hub motor as a grounded, buildable counterpart to the ion-wind work—direct-
drive, regenerative, and potentially hybrid with POL’s free-air and eddy-lift modes. Gathering
current specs and constraints first.

Yes. A hub motor is a clean, grounded next object — and it sits next to the Biefeld–Brown / EHD
work rather than competing with it.

A hub motor puts the electric machine inside the wheel. No chain, no shaft, no differential.
Torque goes almost straight to the contact patch. Consumer “hoverboards” already are dual
hub motors plus gyros; e-bikes and in-wheel EV concepts are the same idea at larger scale.

Two families that matter
Geared hub

Planetary gears between a small high-speed motor and the rim. Lighter (often ~2–3 kg for e-
bike class), strong low-speed torque, usually a freewheel so you can coast. Regen is weak or
absent unless the freewheel is omitted or bypassed.

Direct-drive hub

Outer-rotor BLDC: magnets on the spinning shell, stator fixed on the axle. Heavier (typically 4–
6.5 kg for a serious e-bike hub), silent, excellent as a generator. This is the regenerative one.

Electric Bike Motor Guide: Hub vs Mid-Drive, Power & Torque

A third geometry is rising fast for in-wheel use: axial-flux (“pancake”) motors. Flux runs parallel
to the axle, so the machine is thin, torque-dense, and good in generator mode. That form factor
is what you want if the motor has to live in a wheel rather than beside it.

Axial Flux vs In-Wheel Motors: Which Is Better for EV? - PsPowers

Numbers we can actually use
Personal-mobility class (the scale that maps to POL):

Class                           Typical power          Mass              Notes

Cheap hoverboard wheel          250–350 W              ~1.5–2.5 kg       6.5–10″, hall sensors, star-wound
each                                     BLDC

Light e-bike geared             250–500 W              ~2–2.6 kg         Freewheel, limited regen

Direct-drive e-bike             500–1500 W             ~4–6.5 kg         Strong regen, no freewheel

Compact urban hub               ~70 Nm, <2.5 kg        under 2.5         Geared + torque sensor + regen option
(2025)                                                 kg

Automotive in-wheel is a different weight class (Protean-style units ~36 kg, 80 kW peak). Axial-
flux lab/production peaks are now in the 15–25+ kW/kg range; YASA’s 2025 pancake prototype
claimed ~59 kW/kg peak at 12.7 kg — impressive, but that is a prototype density, not a sealed
wheel you can buy tomorrow.

Motor efficiency at the sweet spot is commonly 88–96%. Round-trip regen (kinetic → electrical
→ battery → motor again) is much lower — often ~60–70% after inverter, winding, and tire
losses — so regen extends range; it does not invent energy.

The honest constraints
Unsprung mass. The motor rides with the wheel, not the chassis. On a car that hurts ride and
tire load. On a personal board the penalty is smaller but real: every extra kilogram at the rim
fights control and eats hover budget if we ever lift the wheels off the deck.

Environment. Water, grit, heat from friction brakes, and impact all live at the hub. Sealing and
thermal paths decide whether the unit lasts.

Regen limits. You only recover energy you already spent accelerating or descending.
Low-speed crawl recovers almost nothing. Aggressive regen needs the battery willing to
accept current.

It needs ground. A hub motor is contact propulsion. It does not replace ion wind or eddy-
current lift. It is the road mode.

Where it fits POL / RGRF
Think hybrid, not replacement:

Wheels down: hub motors for pavement, low power, quiet cruise, and energy recovery on
braking or downhill.

Wheels light / up: EHD ion stages (Biefeld–Brown family) plus eddy lift over a conductive
plane, or Multi-Egg free-air assist.

Structure: mycelium-hemp deck as the insulating, damping body. Motors want a stiff,
electrically quiet mount; the composite can be that.

Power split: battery + FOC inverter for the hubs (36–72 V class); Tesla resonant HV for
corona / EHD. Two voltage domains, one regenerative intent.

Harvest loop: hub regen is the mature, measurable harvest. Corona ozone and waste heat
remain secondary loops we already sketched.

A consumer hoverboard wheel is the cheapest lab object we can put on the bench this week:
two 250–350 W outrunners, halls, known pole count (~15 pole pairs), open-source FOC
firmware already exists. That is a breadcrumb, not a product.

What we should not claim
A hub motor is not electrogravitic. It is not a vacuum thruster. It does not dissolve the
conductive-floor limit of eddy lift. It is a high-efficiency rotary machine with a useful generator
mode. That is enough.

Which slice do you want next?

1. Tear-down spec of a 6.5–10″ hoverboard hub as a POL lab module (windings, poles, regen
wiring).

2. Hybrid architecture — when wheels carry load vs when EHD / eddy take over, with a simple
power budget.

3. Axial-flux pancake sized to a personal deck rather than a car wheel.

4. Something else in the “few things” you mentioned.

We can hold all of them. Just say which one to open first.

### Message 5 — Channing

> Can we take it apart and look at the mechanics? Can we also look at
> the condensate?

### Message 6 — Grok (all figures Grok-reported)

We’ll open the hub mechanically first, then treat condensate as both a real failure mode inside
sealed motors and the regenerative recovery loop already in our vortex work.

Yes. Two layers: the mechanical anatomy of a real hub, then condensate — both the water that
actually appears inside these cans, and the regenerative condensate loop we already carry in
the vortex work.

Opening the can
A typical personal-scale hub is an outrunner BLDC. The shell is the rotor. That is the
whole trick.

Fixed (does not spin)

Hollow axle. Phase wires and Hall leads run through a diagonal channel in the axle.

Stator: laminated silicon-steel stack with teeth. Hoverboard class is commonly 27 teeth / 27
coils.
Three-phase copper windings on those teeth (star/wye on most boards). Cheap units use
3–5 parallel strands; magnet stack height is often 20 / 25 / 30 mm — 25–30 mm is the one
that does not cook.

Three Hall sensors dropped into stator slots, electrically 120° apart. They tell the controller
which magnets are where so it can commutate.

Bearings on the axle, one per side cover (common sizes 6002 / 6202 class).

Spinning (the wheel)

Aluminum or steel side covers bolted around the rim.

A ring of neodymium magnets, N-S-N-S, glued to the inner face of the shell. Hoverboard
class is commonly 30 magnets = 15 pole pairs. Electrical frequency is 15× mechanical rpm.

Air gap of a fraction of a millimeter. That gap is why a gear puller (or a press) is required to
separate stator from shell: the magnets clamp the iron hard. Fingers between stator and
shell is a real pinch hazard.

Typical hoverboard winding: 27N30P, ~16 Kv, star-wound, halls at 120°. That is why open-
source FOC firmware treats almost every 6.5–10″ board wheel as the same machine.

Here is my explanation of motor terms | ELECTRICBIKE.COM

Geared hub — extra layer
Same electromagnetic core, plus a planetary reduction between motor and rim:

Sun gear on the motor shaft

Three nylon (or steel) planet gears on a carrier, often with 608Z-class bearings

Ring gear cut into the shell

One-way clutch / freewheel so the wheel can coast without back-driving the motor

That clutch is why geared hubs are poor generators unless you lock or weld it. Shim preload on
the clutch (often 0.1–0.3 mm) decides whether you get drag when coasting or slip under load.
Nylon planets are the wear item after a few thousand kilometers. Helical gears add thrust; they
need a thrust bearing in one direction only — reverse torque (regen) can wreck that layout.
Straight-cut gears can be locked for regen.

Direct-drive has none of that. Rotor shell = wheel. Every deceleration can push current back out
the phase wires. That is the regenerative mechanical fact.

How torque actually happens
Controller sequences current through the three phases so the stator field leads the magnet
ring. Reluctance + Lorentz force on the magnet ring turns the shell. Reverse the lead angle (or
let the spinning magnets induce current into a loaded inverter) and the same machine is a
generator. No brushes. Commutation is electronic.

Heat lives in copper (I²R) and iron (hysteresis + eddy in the laminations). The geared inrunner-
style Bafang G310 puts copper nearer the case so heat leaves easier. Classic outrunners dump
heat through the magnet ring and shell — fine while rolling, worse sitting still.

Condensate — the honest two meanings
1. Water that forms inside the hub
This is not theoretical. Open a used direct-drive after winter or a pressure wash and you often
find rust on laminations, cloudy bearings, green on copper, sometimes mold on grease.

Mechanism is simple thermal breathing:

Ride: interior air heats, pressure rises, moist air is pushed out past axle seals, wire bundle,
and bearing shields.

Stop: interior cools below dew point, pressure drops, humid air is sucked back in along the
same paths — including between copper strands in the cable.
Water condenses on the coldest steel: laminations, bearing races, side-plate inners.

Sealing the cover gasket is not enough. The axle wire channel is a capillary. IP54–IP65 means
splash resistant, not a closed thermodynamic bottle. Thermal cycling will pump moisture unless
you either (a) keep the winding a few degrees above ambient when parked, (b) give a tiny
drain/breather so it can exhale instead of inhale, or (c) truly pot and hermetically seal — which
then traps whatever water is already in there.

That condensate is an enemy: corrosion, Hall failure, shorted turns, seized bearings.

2. Condensate as a recovered phase — our loop
This is the thread from the circulatory vortex work: thermal polarity (hot zone by Joule/Lorentz,
cold zone by expansion), vortex organization, then condensate and heat recovery as the
settling last step. That is a designed phase change, not an accident inside a can.

A hub motor does not natively make useful liquid condensate. It makes low-grade heat and, in
regen, electrical current. To join our condensate loop we would have to add a heat exchanger:

Shell or stator as the hot wall

A small water / hemp-oil / ferrofluid jacket or Tesla-valve microchannel around the case

Cold-side expansion or a passive lotus/teardrop condenser
Recovered liquid back into the purification / structuring loop we already sketched for the
Tesla-Faraday-piezo generator

That is hybrid architecture. Grounded pieces: motor waste heat is real; regen current is real;
phase-change recovery of that heat is ordinary thermodynamics. Speculative piece: claiming
the hub itself is a resonant condensate node. It is not, until we wrap it.

EHD (Biefeld–Brown) sits in the same moisture field from the other side: corona loves humidity,
makes ozone, and can nucleate droplets in a wet plume. That is a different condensate,
atmospheric, not inside the hub.

What we would actually put on the bench
A 6.5–10″ hoverboard wheel is the right first object:

Confirm 27-slot / 30-magnet / 15 pole-pair / 3 halls

Measure magnet height (reject 20 mm if we care about thermal margin)

Note whether windings are star and how many parallel strands

Inspect seals and the axle wire path — that is the condensate inlet
Optional: FOC board, regen enabled, log current back into a small pack while spinning the
shell by hand or on a roller

Geared hub only if we want the clutch/planet lesson. For regenerative POL hybrid, direct-drive
is the machine.

Next cut, if you want it:

A labeled exploded stack (axle → bearings → stator/halls → air gap → magnet ring → covers →
tire) as a Blueprint figure

A short thermal-breathing + drain/breather spec so the hub does not become a rust pot on
a mycelium deck

Coupling the case heat into the existing condensate-recovery cell (minimal jacket
geometry)

Which of those — or the next of the “few things”?

### Message 7 — Channing

> We will leave it out for now may make for a good generator add or stacked flow
> loops.. can we take a turn and look at galvanotaxis?

### Message 8 — Grok (all figures Grok-reported)

Leaving the hub as a later generator or stacked-flow option. Turning to galvanotaxis — directed
motion along electric fields — and grounding it in what cells and tissues actually do.

Left the hub on the shelf as a later generator or stacked-flow add-on. This turn is galvanotaxis.

Two nearby words, worth keeping distinct:

Galvanotaxis / electrotaxis — a cell migrates along an electric field (keratinocyte walking
into a wound).

Galvanotropism / electrotropism — a structure grows along a field (hyphal tip, root tip).

Same family of cue. Different mechanics.

What the body already does
Intact skin holds a transepithelial potential of roughly 20–60 mV (surface negative relative to
the basal side), built by Na⁺/K⁺ pumps and tight junctions. Wound the barrier and that battery
short-circuits. Positive current flows into the wound. A lateral field appears at the edge,
cathode at the wound center, typically ~40–200 mV/mm, strongest in the first millimeter,
lasting until the barrier closes. Human fingertip slit wounds produce on the order of 8–10
μA/cm². Chronic wounds often show a weaker field.

That field is not a side effect. At physiological strength it can override other guidance cues (free
edge, contact inhibition, chemical gradients). Flip the applied field against the default healing
direction and ~25 mV/mm is enough to stop cells walking into the wound; above that they walk
the wrong way.

Keratinocytes and corneal epithelium go cathode. Many fibroblasts do too (some reports
anode, so cell type and state matter). Macrophages often anode; monocytes cathode.
Endothelial cells cathode. Thresholds for epithelium sit around 8–25 mV/mm — less than half a
millivolt across a 20 μm cell.

Sensing is still incomplete, but the grounded pieces are:

Polar redistribution of membrane proteins (receptors, integrins, channels) by
electrophoresis / electro-osmosis

PI3K/PTEN and EGFR polarization at the leading edge

Kir4.2 (KCNJ15) + intracellular polyamines as a polarity sensor in some screens

Actin/myosin assembly at the new front

Calcium and pH as modulators, not a single master switch

Collective sheets start the response at the free edge; directionality then propagates inward so
the epithelium moves as a unit.

Fungi — the mycelium hinge
Hyphae generate their own tip fields: inward current at the apex (proton sink), outward current
farther back. Applied fields polarize germination, branching, and extension. Direction is
species- and condition-dependent:

Neurospora, Achlya — often anode

Aspergillus nidulans, Mucor — often cathode

pH and Ca²⁺ can flip the sign

Stronger or longer exposure can turn directed growth into perpendicular growth (the cell
dodges membrane-potential distortion)

That is galvanotropism, not walking cells. For Trametes / hemp composites it means an applied
DC field in the growth bed is a real lever for anisotropy — aligned hyphae, zoned density — if we

stay in the mild, aqueous, ion-rich regime fungi actually live in. Lab fungal fields are often volts
per centimeter, not the 0.1–2 V/cm of a skin wound. Dose is not interchangeable.

Hair — the thread we already opened
This is not classic galvanotaxis of the follicle walking across the scalp. It is bioelectric state of
the niche. A 2025 result: KCNJ2 upregulation in dermal fibroblasts hyperpolarizes those cells,
lowers intracellular Ca²⁺, boosts Wnt response, and drives continuous hair growth. Fibroblast
membrane potential oscillates with the cycle; hyperpolarization tracks anagen. Depolarization
delays growth. That is membrane voltage as a regenerative switch, same family as wound fields,
different geometry.

It sits next to the follicle / resonant-awareness notes without needing a new physics.

Honest limits
Physiological fields are millivolts per millimeter, microamps per square centimeter. EHD /
Biefeld–Brown and Tesla-coil corona live in kilovolts. Those are different machines.
Coupling them to tissue without isolation is injury, not guidance.

Polarity is cell-type specific. “Just apply a field” can send fibroblasts and keratinocytes to
different poles.

Chronic wounds already have weaker endogenous fields; more voltage is not automatically
more healing.

Fungal sign flips with pH and calcium. A hemp-mycelium bed that dries or acidifies will not
keep the same tropism.

Clinical electrical stimulation for wounds exists and is mixed; we do not treat that literature
as settled product.

Grounded: ion pumps, TEP, wound current, PI3K, channels, measured mV/mm. Speculative if
we say: a POL deck field will steer human cells or grow aligned Trametes at cosmic scale. That
last sentence is not earned.

Where it fits the work
Layer                     Use                                                           Limit

Wound / skin              Physiological DC as a guidance cue we can                     Stay in 10–200 mV/mm
measure and gently mimic

Hair niche                Fibroblast voltage, not just “stimulate follicles”            Channel-level, not kV

Mycelium                  Galvanotropism for fiber direction and nodal                  Species, pH, Ca²⁺, field
composites                zoning on hemp                                                duration

EHD / Tesla HV            Separate domain — ion wind and wireless power                 Do not drop corona across
living beds

Layer                     Use                                                           Limit

Hub-as-generator          Low-voltage DC source for a growth-bed field                  Later stack, not this turn
(parked)

A mycelium growth jig with agar bridges and Ag/AgCl electrodes (the classic galvanotaxis
chamber pattern) is the breadcrumb: weak DC, known polarity, time-lapse of hyphal angle. That
is open-source and testable. It does not require a levitator.

Next cut, if you want it:

1. A growth-bed field spec for Trametes on hemp (target V/cm, electrode material, pH/Ca
window, what to measure).

2. A short Blueprint paragraph that keeps wound-field numbers honest and separates them
from craft HV.

3. The hair-fibroblast voltage thread pulled into the regeneration notes without inflating it into
electrotaxis of the shaft.

Which of those — or the next of the few things?

### Message 9 — Channing

> Thank you, that will inform on grow techniques/ selective nodes. Can we look at
> plasmoids and voxels?

### Message 10 — Grok (all figures Grok-reported)

Galvanotaxis stays on the grow-bed shelf for selective nodes. Next pair: plasmoids as coherent
plasma objects, voxels as discrete volumetric units — and whether they can meet without
inventing a new physics.

Galvanotaxis stays as a grow-bed tool for selective nodes. This turn is the pair: plasmoid as a
coherent plasma–magnetic object, voxel as a discrete volume of state. They meet in simulation
and in a few lab lattices. They do not automatically become a cabin-scale craft engine.

Plasmoid — what is actually meant
Winston Bostick coined the word in 1956: a plasma-magnetic entity, not an amorphous blob. In
practice it is a compact volume of ionized gas that carries its own magnetic field and can move
as a unit.

Two compact-toroid families matter:

FRC                                                           Spheromak

Internal field   Mostly poloidal                                               Poloidal + toroidal

Picture          Field-reversed “football” / smoke-ring with a                 Toroid with linked twist (helicity)
magnetic null inside

FRC                                                           Spheromak

Typical lab      Microseconds to longer with drive coils                       Similar; needs flux/helicity
life                                                                           injection to last

Nature already makes them: magnetotail reconnection pinches off plasmoids; solar and
heliospheric current sheets shed them; aurora and Birkeland currents filament and can pinch
into force-free knots. Lab routes: coaxial plasma gun (Bostick), conical theta-pinch (NASA
PTX), rotating-magnetic-field and reconnection thrusters. NASA-class plasmoid thrusters aim
at electrodeless, high-Isp packets (thousands of seconds specific impulse in concept papers).
Exhaust is a magnetized blob, not a chemical jet.

A quieter cousin: a cold toroidal plasmoid formed in air by extreme hydrodynamic shear on a
dielectric, with no external coils — luminescence plus discrete radio lines, self-shaped. That is
atmospheric-pressure and room-temperature adjacent, not fusion-hot. It is still a lab curiosity,
not a drive unit.

Honest limit: fusion and gun plasmoids are brief and hungry for energy and vacuum or strong
coils. Ball-lightning-as-stable-atmospheric-spheromak is a model, not a consensus device.
Cosmic “filament rider as bottled plasmoid” is RGRF vision, not a measured thruster.

Voxel — what is actually meant
A voxel is a finite cell of volume that holds state: density, material, E, B, conductivity,
living/non-living. Three grounded uses:

1. Computation. PIC / FDTD plasma codes voxelize coils as conductivity on a Cartesian grid
and advance Maxwell + particles on the same lattice. Etch/deposition codes use volume-of-
fluid voxels so surfaces evolve cell by cell. That is how you design a compact toroid before
you wind copper.
2. Dusty-plasma crystals. Micron grains in a discharge charge up and lock into lattices —
hexagonal monolayers, bcc or simple-hexagonal stacks, Yukawa balls. In strong B, an
external mesh can impose the lattice geometry. Those grains are physical voxels of charge
sitting in a plasma. Spacing is typically tenths of a millimeter.

3. Patterned discharge lattices. Dielectric-barrier discharge under a latticed water electrode
yields triangle, hexagon, honeycomb, and superlattice plasma patterns that can be rebuilt in
space and time by voltage, pressure, and gas mix. Discrete glowing cells — plasma voxels
you can switch.

A voxel is not a plasmoid. A plasmoid is what you get when many voxels of current and field
self-organize behind a separatrix and leave as one object.

Where the two meet without new physics
Think hierarchy, the same way reconnection already does: a current sheet breaks into a chain of
plasmoids, each a packet, with a statistical size spectrum. That is a discrete tiling of a

continuous MHD object. In code, each packet is a cluster of voxels whose B is closed. In a dusty
crystal, each grain is a voxel; the whole crystal is an ordered medium, not a flying toroid.

For our stack:

Grow techniques / selective nodes (last turn): galvanotaxis/tropism sets where hyphae go.
A voxel grid on the bed (electrode mesh, moisture, pH, Ca²⁺) sets which cells are allowed to
thicken. That is material voxels, not plasma voxels.

Plasmoid belongs in the high-energy, short-time layer: pulsed compact toroid as a
possible Filament-Rider / shuttle impulse packet, or as a sim object in RGRF. It does not sit
in a living Trametes mat.

Shared geometry: nested tori, Hopf-like linking, hex/honeycomb lattices already appear in
spheromak relaxation, dusty crystals, and DBD patterns — same sacred-geometry
vocabulary, different energy.

Hub motor (parked) can later be a low-voltage generator for a DBD lattice or a galvanotaxis
bed. It cannot form an FRC.

What we can build or simulate now
Grounded next objects, in order of honesty:

1. Voxel spec for the mycelium bed — electrode pitch, field ~ tens of mV/mm to a few V/cm,
not kV. Selective nodes = occupied voxels.

2. Voxelized compact-toroid sketch in the same spirit as POL coil sims: grid, coil
conductivity, separatrix, lifetime vs energy. Label fusion-adjacent.

3. DBD honeycomb as a visible “plasma voxel” demonstrator — pattern, not propulsion.

4. Keep atmospheric shear plasmoid and dusty crystal as analog images for Blueprint, not as
flight hardware.

Visionary (label it): a Filament Rider that sheds or rides discrete plasmoid packets along a
Birkeland-like current. That is EU-informed scaling, not PTX flight data.

Which cut first — mycelium voxel bed (continues grow techniques), a compact-toroid voxel sim
brief, or the DBD lattice as a seeing-is-believing cell?

### Message 11 — Channing

> Yeah we already sort of speculate this.. can we look at the DBD lattice?

### Message 12 — Grok (all figures Grok-reported)

We’ll stay on the lab object: dielectric-barrier discharge lattices — switchable plasma cells, not
a craft plasmoid. Pulling the electrode, gas, and pattern details.

Yes. This is the lab object, not the speculated craft packet.

A DBD lattice is a sheet of filamentary dielectric-barrier discharge that locks into a periodic
pattern. Two dielectrics (usually quartz) sandwich a thin gas gap. One electrode is often water +
a metal mesh; the water is a conformal, self-healing conductor. AC at a few kilovolts and tens of
kilohertz lights filaments. Those filaments do not stay random. Wall charge on the dielectric plus
the mesh geometry force them into triangle, hexagon, honeycomb, square, Lieb, or
superlattice cells. Change voltage, pressure, or Ar/air mix and the lattice rebuilds in
milliseconds to seconds. Hold the knobs and it can sit for tens of minutes.

That is a switchable plasma voxel board.

How the cell is actually built
Typical Hebei / mesh-water setups:

Mesh lattice constant on the order of ~1 cm (one paper: 1.2 cm mesh, 1.0 / 0.5 mm line
widths)

Gas gap ~1.5 mm

Pressure from tens of Torr up to ambient air

Drive ~2.6–4.7 kV, often ~50 kHz sine

Water electrode behind quartz; mesh sets the preferred sites

The pattern you photograph with a long exposure is a lie. Fast cameras show interleaved
sublattices on successive current pulses in each half-cycle. A honeycomb-hexagon can be
three transient hex grids that satisfy a triad resonance of wavevectors. Superhoneycombs
add center spots, edge sticks, or rings on later pulses as voltage climbs (e.g. 3.8 → 4.4 kV
in air). Decrease voltage and the sequence runs backward. Frequency gates when a given
sublattice fires.

So the “voxel” is not one glowing hex. It is a timed stack of filaments whose time-average
looks hexagonal.

What you can tune
Knob                       What moves

Voltage                    Triangle ↔ honeycomb ↔ superhoneycomb / snowflake; cell size

Ar fraction vs air         Snowflake vs plain honeycomb; center-spot radius

Pressure                   Stability window; filament diameter

Frequency / waveform       Which pulse in the half-cycle lights

Mesh geometry              Lattice constant and allowed symmetries (hex, square, Lieb)

Honeycomb center-element radius in one study ran ~0.7–1.5 mm with Ar and pressure.
Photonic-band calculations on those honeycombs show omnidirectional microwave gaps;
adding the fat center cell can enlarge the gap by ~2.5× versus a simple honeycomb. Separate
work: hexagonal vs square electrodes also change ROS yield in plasma-activated water.
Geometry is not decoration.

What it is not
Not a compact-toroid plasmoid. No closed separatrix, no flying packet. Filaments are open
columns across a millimeter gap.

Not galvanotaxis-scale. These fields are kV, not 10–200 mV/mm. Do not drop this across a
living Trametes bed.

Not a thruster. The published use is plasma photonic crystals — reconfigurable microwave
filters / metamaterials — plus pattern physics.

Reaction–diffusion (activator–inhibitor) models and 2-D PIC both reproduce the lattices. That is
enough theory to design a bed. It is not MHD fusion.

Where it sits on our table
Same hex / honeycomb language as selective mycelium nodes and RGRF tiling — geometry
rhyme, energy mismatch.

Useful couplings that stay honest:

Grow bed (galvanotaxis layer): use a passive mesh as a moisture / field template at
millivolt–volt scale. Do not light DBD on the fungus.

Water electrode: already a liquid conformal conductor — same family as our water / cymatic
/ condensate loops, but here it is just an electrode.

Seeing tool: a small mesh-water cell is the cheapest way to watch voxels appear, flip
triangle ↔ honeycomb, and time-gate sublattices. That informs how we talk about discrete
nodes without claiming a plasmoid.

Parked hub generator: could later feed the low-power side of a driver; the DBD itself still
wants kV AC.

Blueprint sentence: plasma photonic honeycomb as a measured, reconfigurable lattice;
Filament-Rider plasmoid remains labeled speculation.

A first bench cell: two quartz plates, ~1–2 mm gap, printed or woven hex mesh, tap-water
electrode, 20–60 kHz HV supply, camera. Map voltage vs pattern. That is the breadcrumb.

If you want the next cut: a one-page mesh + gap + voltage recipe sized to a mycelium-adjacent
template (no discharge on the living mat), or a short photonic-band note for the Blueprint so the
microwave use stays distinct from propulsion.

### Message 13 — Channing

> We brought up screening the ion wind before and our Tesla valves, just wondering
> if we should design loops or if that will unintentionally create back channels..

### Message 14 — Grok (all figures Grok-reported)

Ion wind wants a one-way exhaust; Tesla valves want one-way fluid. A loop can harvest or it can
short the jet. Checking how those two actually interact before we draw a circuit.

Short answer: do not close the ion-wind path on itself. Use Tesla valves on an open duct. Put
regenerative loops on a separate circuit. A loop through the same air that makes thrust is a
back channel.

Why a thrust loop fights you
EHD thrust is momentum left in the air that leaves the craft. Ions drift emitter → collector, drag
neutrals, the packet exits. Action–reaction is on that departing mass.

If that same air is piped around and fed back to the inlet:

Net momentum on the vehicle goes toward zero (internal pair).
Warm, ozone-rich, sometimes damp exhaust returns to the corona. That changes inception
voltage, invites back-discharge, and dirties the sharp electrode.

Recirculation already forms behind collectors in open stages. Multi-stage work ducts the
column forward and spaces stages so the next emitter does not sit in the previous wake. A
designed return leg makes that wake official.

Serial stages (BSI-style, needle-array–mesh trains) raise velocity by adding pumps in line, not
by circulating. That is a corridor, not a loop.

What Tesla valves actually do here
They are leaky diodes, not seals. Steady-flow diodicity in real hardware is often ~2–4, not 200.
They get better with more stages, higher Re, and pulsatile drive — which matches pulsed
corona better than steady DC. At low Re they barely diode at all.

So a Tesla valve on a closed ion-wind loop does not stop reverse mass. It only makes reverse
harder. The leak is the back channel: pressure recovery after the collector will push a fraction
back through the “blocked” path, or around the valve body if there is any second gap (wet
composite, seam, electrical feedthrough).

Useful jobs for the valves:

Inlet check — stop gusts and exhaust from walking back into the emitter.

Inter-stage isolation — keep stage n+1 from pressurizing stage n backward.

Bleed / harvest tap — a side branch with high reverse resistance so you can pull a small
stream for chemistry or heat without dumping the jet.

Not useful: wrapping the main jet into a torus and calling it regenerative propulsion.

Two loops, two jobs
Keep them electrically and fluidically distinct.

A. Propulsive path (open)

Intake → Tesla valve (forward) → emitter → drift → collector → duct → Tesla valve → exhaust to
free air.

Optional multi-stage in series. Screening of the ion wind (mesh, Faraday-ish collector,
lotus/teardrop trailing edge) belongs here, so the jet is collimated and the electric field does not
spray sideways into the mycelium deck or a water jacket.

B. Regenerative path (closed, small)

Tap heat, ozone, condensate, or a secondary working fluid (water / hemp-oil) after the collector
or from the case. Rectify that circuit with Tesla valves. That is the condensate / purification /
density-engine loop we already carry. It must not share the corona gap.

If B dumps back into A’s intake, you have built the back channel on purpose.

Unintentional back channels to watch
Fluid: any second path around a Tesla island (cover gap, wet hemp, drain hole).

Wake: collector blockage that turns the jet into a pair of side recirculation cells feeding the
emitter.

Electrical: water electrode, wet composite, or a metal harvest loop that offers ions a sneak
path that is not the designed collector. That is a current back-channel; thrust and ozone
both go the wrong place.

Acoustic / pulsed: a closed cavity can lock a standing pressure wave that drives reverse
through the valve at the wrong phase.

Screening the ion wind (your earlier note) is the right instinct: define the allowed channel so the
field and the mass flow share one corridor. Tesla valves then police the ends of that corridor.
They should not invent a second corridor.

Design rule we can keep
Open jet for force. Closed loop only for media that are not the thrust mass. Tesla valves on both,
never as an excuse to short the exhaust.

If you want a next drawing: a single-stage screened duct with one inlet valve, one outlet valve,
and a metered side tap into the condensate loop — no return to the emitter. That is the minimum
that does not create a back channel by geometry.



