"""
Enhance Secondary 2 Science exercises to match Singapore MOE rigor
Focuses on: experimental design, data interpretation, application, scientific reasoning
Aligned with Singapore's practical science emphasis
"""

import json

# Load existing chapters
with open('chapters/science-sec2-chapters.json', 'r', encoding='utf-8') as f:
    chapters = json.load(f)

# Enhanced exercise data - more rigorous, inquiry-based
enhanced_exercises = {
    # CHEMISTRY CHAPTERS

    "chemical-changes-sec2": [
        # Easy
        ("Which observation confirms a chemical change has occurred?", ["New substance with different properties formed", "Change in shape only", "Change in size only", "Change in position"], 0, "mcq"),
        ("Burning of magnesium ribbon produces a white powder. This is an example of:", ["chemical change", "physical change", "both", "neither"], 0, "mcq"),
        ("In a chemical reaction, what happens to the total number of atoms?", "stays the same", None, "short"),
        ("Ice melting is a physical change because:", ["no new substance formed", "it is reversible", "only state changes", "all of the above"], 3, "mcq"),
        ("When iron rusts, it combines with:", ["oxygen", "hydrogen", "nitrogen", "carbon"], 0, "mcq"),

        # Medium
        ("A student heats 5.0g of copper carbonate. It decomposes to form 3.2g of copper oxide and carbon dioxide gas. Calculate the mass of CO₂ released.", ["1.8g", "8.2g", "2.0g", "3.2g"], 0, "mcq"),
        ("In Singapore's humid climate (80-90% humidity, 30°C), which factor most accelerates rusting of iron railings near the sea?", ["Salt spray providing ions for electron transfer", "High humidity only", "High temperature only", "Low oxygen levels"], 0, "mcq"),
        ("Hydrogen peroxide (H₂O₂) decomposes to form water and oxygen. If 34g H₂O₂ decomposes completely, what mass of products forms?", "34g", None, "short"),
        ("A closed container has 20g of reactants. After reaction, products weigh 20g. This demonstrates:", ["Law of Conservation of Mass", "Law of Constant Proportions", "Avogadro's Law", "Dalton's Law"], 0, "mcq"),
        ("Which combination would produce the most vigorous chemical reaction?", ["Concentrated acid + fine metal powder at high temperature", "Dilute acid + metal lump at room temperature", "Concentrated acid + metal lump at low temperature", "Dilute acid + fine powder at low temperature"], 0, "mcq"),

        # Hard
        ("Experiment: Heat 2.4g magnesium in air. Product weighs 4.0g. Calculate percentage by mass of oxygen in magnesium oxide.", ["40%", "60%", "50%", "66.7%"], 0, "mcq"),
        ("A hawker uses liquefied petroleum gas (LPG). In complete combustion, C₃H₈ + 5O₂ → 3CO₂ + 4H₂O. If 44g propane burns completely, what mass of water forms? (H=1, O=16, C=12)", ["72g", "44g", "132g", "18g"], 0, "mcq"),
        ("Zinc reacts with hydrochloric acid. Graph shows gas volume vs time. Why does the curve level off?", "reactant is used up", None, "short"),
        ("In a factory, ammonia (NH₃) is made from N₂ and H₂. If 28g N₂ reacts with excess H₂, what mass of NH₃ forms? (N=14, H=1)", ["34g", "28g", "17g", "68g"], 0, "mcq"),
        ("Thermal decomposition of calcium carbonate: CaCO₃ → CaO + CO₂. If 50g CaCO₃ decomposes, what volume of CO₂ at room conditions? (1 mole gas = 24L, Ca=40, C=12, O=16)", ["12L", "24L", "6L", "48L"], 0, "mcq")
    ],

    "oxidation-reduction-sec2": [
        # Easy
        ("Oxidation is defined as:", ["gain of oxygen or loss of electrons", "loss of oxygen", "gain of hydrogen", "gain of mass"], 0, "mcq"),
        ("When magnesium burns in oxygen: 2Mg + O₂ → 2MgO. Magnesium is:", ["oxidized", "reduced", "neither", "both"], 0, "mcq"),
        ("Complete combustion requires:", "sufficient oxygen", None, "short"),
        ("Iron rusting is an example of:", ["slow oxidation", "fast oxidation", "reduction", "decomposition"], 0, "mcq"),
        ("Which gas is produced during incomplete combustion of hydrocarbons?", ["Carbon monoxide (CO)", "Carbon dioxide (CO₂)", "Oxygen (O₂)", "Nitrogen (N₂)"], 0, "mcq"),

        # Medium
        ("Experiment: Heat copper(II) oxide with hydrogen gas. CuO + H₂ → Cu + H₂O. Which statement is correct?", ["Copper oxide is reduced, hydrogen is oxidized", "Both are oxidized", "Both are reduced", "Copper oxide is oxidized"], 0, "mcq"),
        ("Singapore's coastal MRT structures use galvanized steel. Zinc coating prevents rust by:", ["Acting as sacrificial anode (more reactive than iron)", "Preventing oxygen contact only", "Absorbing moisture", "Reflecting UV light"], 0, "mcq"),
        ("Methane burns: CH₄ + 2O₂ → CO₂ + 2H₂O. If only 1.5 moles O₂ available per mole CH₄, what forms?", ["Incomplete combustion with CO and soot", "Complete combustion", "No reaction", "Only water"], 0, "mcq"),
        ("A gas stove in poor ventilation produces CO. Why is this dangerous indoors?", "CO binds to hemoglobin preventing oxygen transport", None, "short"),
        ("In the reaction: Fe₂O₃ + 3CO → 2Fe + 3CO₂, which substance is the reducing agent?", ["CO", "Fe₂O₃", "Fe", "CO₂"], 0, "mcq"),

        # Hard
        ("Car exhaust contains harmful gases. Catalytic converter: 2CO + 2NO → 2CO₂ + N₂. In this reaction:", ["CO is oxidized, NO is reduced", "Both oxidized", "Both reduced", "CO is reduced, NO is oxidized"], 0, "mcq"),
        ("Experiment: Pass steam over heated iron. 3Fe + 4H₂O → Fe₃O₄ + 4H₂. If 5.6g Fe reacts (Fe=56), what volume H₂ at room temp? (1 mole = 24L)", ["4.8L", "2.4L", "9.6L", "1.2L"], 0, "mcq"),
        ("Hydrogen peroxide decomposes: 2H₂O₂ → 2H₂O + O₂. What happens to oxygen in H₂O₂?", "both oxidized and reduced (disproportionation)", None, "short"),
        ("Ship hulls use zinc blocks attached to steel. Over time zinc corrodes but steel doesn't. Explain using reactivity series.", ["Zinc more reactive, loses electrons preferentially", "Zinc less reactive", "Steel is non-metal", "Zinc prevents water contact"], 0, "mcq"),
        ("Industrial process removes sulfur from petroleum: H₂S + SO₂ → S + H₂O. Which element is both oxidized AND reduced?", ["Sulfur (in H₂S oxidized, in SO₂ reduced)", "Hydrogen", "Oxygen", "None"], 0, "mcq")
    ],

    "rate-of-reaction-sec2": [
        # Easy
        ("Rate of reaction is measured by:", ["change in concentration per unit time", "total amount of product", "temperature only", "color change only"], 0, "mcq"),
        ("Increasing temperature increases reaction rate because:", ["particles move faster and collide more frequently with greater energy", "color changes", "mass increases", "volume decreases"], 0, "mcq"),
        ("What is a catalyst?", "substance that speeds up reaction without being used up", None, "short"),
        ("Powdered marble reacts faster than marble chips with acid because:", ["greater surface area", "different chemical composition", "lower mass", "higher density"], 0, "mcq"),
        ("Which would slow down a reaction?", ["Lower temperature", "Higher concentration", "Catalyst added", "Smaller particle size"], 0, "mcq"),

        # Medium
        ("Experiment: Mg ribbon in HCl. Graph shows H₂ volume vs time for different concentrations. 2M acid produces steeper initial slope than 1M acid because:", ["More frequent collisions due to higher particle concentration", "Different products formed", "More heat produced", "Acid evaporates faster"], 0, "mcq"),
        ("Singapore hawker uses pressure cooker (120°C) vs normal pot (100°C). Cooking time reduces by ~50% because:", ["Rate approximately doubles every 10°C rise", "Pressure crushes food", "Water tastes different", "Food absorbs more water"], 0, "mcq"),
        ("Hydrogen peroxide decomposes slowly at room temperature but rapidly with MnO₂ catalyst. The catalyst works by:", "lowering activation energy", None, "short"),
        ("Sodium thiosulfate + HCl forms sulfur precipitate. Temperature increase from 20°C to 50°C affects rate how?", ["Increases by ~8 times (rate doubles every 10°C)", "Decreases", "No change", "Increases by 2 times only"], 0, "mcq"),
        ("Marble chips (CaCO₃) + HCl produces CO₂. Which factor does NOT affect the total volume of gas produced (assuming excess acid)?", ["Particle size of marble", "Mass of marble", "Concentration of acid", "Temperature"], 0, "mcq"),

        # Hard
        ("Experiment data: Zinc + acid. 1g zinc powder completes in 2 min. 1g zinc granules complete in 8 min. Calculate rate ratio (powder:granules).", ["4:1", "2:1", "8:2", "1:4"], 0, "mcq"),
        ("Industrial Haber process: N₂ + 3H₂ ⇌ 2NH₃. Uses 450°C and iron catalyst. Without catalyst, required temp would be ~900°C. The catalyst:", ["Lowers activation energy without changing equilibrium position", "Changes products formed", "Increases yield only", "Prevents reverse reaction"], 0, "mcq"),
        ("Graph shows [reactant] vs time for: A+B→C. Initial slope is 0.5 mol/L/s. After 10s, slope is 0.1 mol/L/s. Why does rate decrease?", "reactant concentration decreases", None, "short"),
        ("Enzyme experiment: 5cm³ H₂O₂ + catalase produces 50cm³ O₂ in 30s at 37°C. At 60°C, only 10cm³ O₂ in 30s. Explain.", ["Enzyme denatured at high temperature", "Reaction reversed", "More oxygen dissolved", "Pressure changed"], 0, "mcq"),
        ("Collision theory: For successful reaction, particles must collide with (1) correct orientation AND (2):", ["Sufficient activation energy", "Same mass", "Opposite charges", "High velocity only"], 0, "mcq")
    ],

    "reactivity-series-sec2": [
        # Easy
        ("Which metal is most reactive?", ["Potassium", "Copper", "Silver", "Gold"], 0, "mcq"),
        ("Metals above hydrogen in reactivity series:", "react with dilute acids to produce hydrogen", None, "short"),
        ("Zinc displaces copper from copper sulfate because:", ["Zinc more reactive than copper", "Zinc less reactive", "Both same reactivity", "Copper is non-metal"], 0, "mcq"),
        ("Least reactive metal:", ["Platinum", "Magnesium", "Iron", "Sodium"], 0, "mcq"),
        ("Which reaction occurs: Iron + copper sulfate →", ["Iron sulfate + Copper", "No reaction", "Iron oxide", "Copper oxide"], 0, "mcq"),

        # Medium
        ("Experiment: Add metals W, X, Y, Z to copper sulfate solution. W and X displace copper; Y and Z don't. Add W to X sulfate - displacement occurs. Reactivity order:", ["W > X > Cu > Y,Z", "X > W > Cu > Y,Z", "W > X > Y > Z > Cu", "Cu > W > X > Y,Z"], 0, "mcq"),
        ("Aluminium is extracted by electrolysis but iron by carbon reduction. This is because:", ["Aluminium more reactive than carbon", "Iron cheaper", "Aluminium melts easier", "Carbon reacts with aluminium"], 0, "mcq"),
        ("Which metal reacts vigorously with cold water?", "calcium", None, "short"),
        ("Singapore imports bauxite (Al₂O₃) for aluminium. Why not use carbon reduction like for iron?", ["Aluminium too reactive, carbon cannot reduce it", "Aluminium expensive", "Carbon unavailable", "Electrolysis faster"], 0, "mcq"),
        ("Metal X displaces Y from Y nitrate but not Z from Z chloride. Reactivity order:", ["Z > X > Y", "X > Y > Z", "Y > X > Z", "X > Z > Y"], 0, "mcq"),

        # Hard
        ("Experiment results: Metal A + water → vigorous reaction. Metal B + steam → slow reaction. Metal C + dilute HCl → no reaction. Metal D + conc. HCl when heated → reaction. Reactivity order:", ["A > B > D > C", "A > B > C > D", "B > A > D > C", "D > C > B > A"], 0, "mcq"),
        ("Thermite reaction: Fe₂O₃ + 2Al → 2Fe + Al₂O₃ releases enormous heat. This works because:", ["Aluminium more reactive, reduces iron oxide", "Iron more reactive", "Both same reactivity", "Oxygen escapes"], 0, "mcq"),
        ("Ship's steel hull has magnesium blocks attached. After 1 year, Mg corroded but steel intact. Explain.", "Mg more reactive acts as sacrificial anode", None, "short"),
        ("To extract metal from its oxide by carbon reduction, the metal must be:", ["Less reactive than carbon in reactivity series", "More reactive than carbon", "Equal reactivity to carbon", "Unreactive with oxygen"], 0, "mcq"),
        ("Displacement competition: Zn + CuSO₄ produces heat. Mg + ZnSO₄ produces more heat. Why?", ["Greater reactivity difference = more energy released", "Magnesium lighter", "Zinc is blue", "Copper catalyzes reaction"], 0, "mcq")
    ],

    "chemical-bonding-sec2": [
        # Easy
        ("Ionic bonding involves:", ["transfer of electrons from metal to non-metal", "sharing electrons", "gravitational attraction", "magnetic force"], 0, "mcq"),
        ("Sodium (2,8,1) forms Na⁺ by:", "losing 1 electron", None, "short"),
        ("Covalent bonding is:", ["sharing of electron pairs between non-metals", "transfer of electrons", "metallic lattice", "ionic attraction"], 0, "mcq"),
        ("Which has ionic bonding?", ["MgO", "CO₂", "H₂O", "CH₄"], 0, "mcq"),
        ("Water (H₂O) molecules have:", ["covalent bonds", "ionic bonds", "metallic bonds", "no bonds"], 0, "mcq"),

        # Medium
        ("Magnesium (2,8,2) + Oxygen (2,6) form MgO. Electron arrangement in Mg²⁺ and O²⁻:", ["Both achieve noble gas configuration (2,8)", "Mg: 2,8,0 O: 2,8", "Mg: 2,7 O: 2,7", "No change"], 0, "mcq"),
        ("Sodium chloride conducts electricity when molten or dissolved because:", ["Ions are free to move and carry charge", "Electrons flow through structure", "Melting creates new electrons", "Chlorine gas escapes"], 0, "mcq"),
        ("Diamond is very hard because:", "each carbon bonded to 4 others in giant covalent structure", None, "short"),
        ("Which property is NOT typical of ionic compounds?", ["Conduct electricity when solid", "High melting point", "Brittle", "Soluble in water"], 0, "mcq"),
        ("Methane (CH₄) is gas at room temperature but NaCl is solid because:", ["Covalent molecules have weak intermolecular forces; ionic has strong electrostatic forces", "Methane lighter", "NaCl has more atoms", "Carbon is non-metal"], 0, "mcq"),

        # Hard
        ("Experiment: Substance X melts at 801°C, conducts when molten but not when solid, shatters when hit. Substance Y melts at -78°C, never conducts, dissolves in petrol. Identify bonding types.", ["X: Ionic, Y: Covalent molecular", "X: Metallic, Y: Ionic", "X: Covalent, Y: Ionic", "Both ionic"], 0, "mcq"),
        ("Silicon dioxide (SiO₂) has high melting point (1610°C) but CO₂ is gas at room temp, though both are oxides of Group 14. Explain.", ["SiO₂ is giant covalent, CO₂ is simple molecular", "SiO₂ ionic, CO₂ covalent", "Silicon heavier", "Different number of bonds"], 0, "mcq"),
        ("Aluminium oxide (Al₂O₃) melting point 2072°C. Requires huge energy to separate ions because:", "strong electrostatic attraction in giant ionic lattice", None, "short"),
        ("Graphite conducts electricity but diamond doesn't, though both are carbon. This is because:", ["Graphite has delocalized electrons between layers", "Diamond has impurities", "Graphite is softer", "Diamond is transparent"], 0, "mcq"),
        ("Singapore's desalination plants remove NaCl from seawater. Why does NaCl dissolve in water?", ["Water molecules attract and surround ions, breaking ionic lattice", "NaCl reacts with water", "Salt evaporates", "Chlorine gas escapes"], 0, "mcq")
    ],

    # PHYSICS CHAPTERS

    "work-energy-power-sec2": [
        # Easy
        ("Work done = ", ["Force × Distance moved in direction of force", "Force × Time", "Mass × Velocity", "Energy / Time"], 0, "mcq"),
        ("Unit of work:", "Joule (J)", None, "short"),
        ("Power is defined as:", ["Rate of doing work or energy transfer", "Total work done", "Force applied", "Distance moved"], 0, "mcq"),
        ("If 100J work done in 5s, power = ", ["20W", "500W", "100W", "5W"], 0, "mcq"),
        ("Kinetic energy depends on:", ["Mass and velocity", "Mass only", "Velocity only", "Height"], 0, "mcq"),

        # Medium
        ("Student pushes box with 50N force for 4m horizontally. Work done:", ["200J", "50J", "12.5J", "54J"], 0, "mcq"),
        ("Crane lifts 500kg load 10m vertically in 20s. Power output (g=10m/s²):", ["2500W", "5000W", "50000W", "250W"], 0, "mcq"),
        ("Car moving at 20m/s has KE = 400kJ. Find mass.", "2000 kg", None, "short"),
        ("Singapore MRT train brakes from 30m/s to rest. If mass = 40,000kg, kinetic energy converted to heat:", ["18,000,000J", "1,200,000J", "600,000J", "30,000J"], 0, "mcq"),
        ("Gravitational potential energy = mgh. A 2kg book on 1.5m shelf has GPE (g=10m/s²):", ["30J", "20J", "15J", "3J"], 0, "mcq"),

        # Hard
        ("Roller coaster car (500kg) at top of 30m hill (v=0). At bottom, v=20m/s. Energy lost to friction (g=10m/s²):", ["50,000J", "150,000J", "100,000J", "200,000J"], 0, "mcq"),
        ("Motor lifts 200kg elevator 15m in 10s. If 25% energy wasted as heat, total power input (g=10m/s²):", ["4000W", "3000W", "5000W", "2000W"], 0, "mcq"),
        ("Pendulum: At highest point has GPE=100J, KE=0. At lowest point, KE=80J. Energy lost per swing:", "20J", None, "short"),
        ("Hydroelectric dam: water falls 50m at rate 1000kg/s. Maximum power generated (g=10m/s²):", ["500kW", "50kW", "5000kW", "5MW"], 0, "mcq"),
        ("Efficiency = (useful energy output / total energy input) × 100%. Machine uses 500J, does 350J useful work. Efficiency:", ["70%", "35%", "85%", "50%"], 0, "mcq")
    ],

    "moments-sec2": [
        # Easy
        ("Moment of force = ", ["Force × Perpendicular distance from pivot", "Force × Time", "Mass × Distance", "Force / Distance"], 0, "mcq"),
        ("Unit of moment:", "Newton-metre (Nm)", None, "short"),
        ("For balanced seesaw, principle states:", ["Clockwise moment = Anticlockwise moment", "Weights are equal", "Distances are equal", "Forces are parallel"], 0, "mcq"),
        ("10N force acts 0.5m from pivot. Moment = ", ["5 Nm", "10 Nm", "20 Nm", "0.5 Nm"], 0, "mcq"),
        ("To increase moment, you can:", ["Increase force or increase distance", "Decrease force", "Decrease distance", "Use lighter object"], 0, "mcq"),

        # Medium
        ("Uniform beam 4m long weighs 100N. Pivoted at center. 50N load placed 1m from pivot on right. Where to place 200N on left for balance?", ["0.25m from pivot", "0.5m", "1m", "2m"], 0, "mcq"),
        ("Door handle 0.8m from hinge. To open door requiring 40 Nm moment, force needed:", ["50N", "32N", "80N", "5N"], 0, "mcq"),
        ("Wheelbarrow: Load 300N at 0.5m from wheel. Lifting force applied 1.5m from wheel. Force needed:", "100N", None, "short"),
        ("Singapore HDB window: 60cm wide, hinged on left. 30N force closes it. If force applied at 40cm from hinge, moment produced:", ["12 Nm", "18 Nm", "30 Nm", "1200 Nm"], 0, "mcq"),
        ("Principle of moments states system is balanced when:", ["Sum of clockwise moments = Sum of anticlockwise moments", "All forces equal", "All distances equal", "No forces acting"], 0, "mcq"),

        # Hard
        ("Uniform plank 6m long, mass 20kg, pivoted 2m from left end. 50kg person stands at left end. For balance, what mass at right end? (g=10m/s²)", ["60kg", "50kg", "80kg", "40kg"], 0, "mcq"),
        ("Crane jib: 10m boom, pivot at base. 5000N load at end. Counterweight 8000N placed where from pivot for balance?", ["6.25m opposite side", "5m", "10m", "12.5m"], 0, "mcq"),
        ("Ladder 8m long, 200N weight, leans against wall at 60°. Person 600N stands 6m up ladder. Moment about base:", "2880 Nm", None, "short"),
        ("Beam 5m long, weight 100N (acts at center). Supported at 1m from left, 1m from right. Reaction forces if balanced:", ["Left: 30N, Right: 70N", "Both 50N", "Left: 70N, Right: 30N", "Left: 40N, Right: 60N"], 0, "mcq"),
        ("Steering wheel radius 20cm. Driver applies 50N at edge. Gears multiply moment by factor 15. Moment at wheels:", ["150 Nm", "10 Nm", "1500 Nm", "15 Nm"], 0, "mcq")
    ],

    "kinetic-particle-theory-sec2": [
        # Easy
        ("According to kinetic particle theory, particles in solids:", ["vibrate about fixed positions", "move freely", "have no energy", "don't move at all"], 0, "mcq"),
        ("State with particles farthest apart:", "gas", None, "short"),
        ("Particles in liquids:", ["Can move past each other but close together", "Fixed positions", "Very far apart", "Don't touch"], 0, "mcq"),
        ("Boiling point of water at standard pressure:", ["100°C", "0°C", "50°C", "212°C"], 0, "mcq"),
        ("Melting is change from:", ["Solid to liquid", "Liquid to gas", "Gas to liquid", "Liquid to solid"], 0, "mcq"),

        # Medium
        ("Evaporation occurs because:", ["Highest energy particles escape from liquid surface", "All particles have same energy", "Temperature is 100°C", "Pressure is low"], 0, "mcq"),
        ("Singapore's humid air (90% humidity) slows clothes drying because:", ["Air already saturated, less evaporation of water", "Temperature too high", "Wind speed too high", "Clothes heavier"], 0, "mcq"),
        ("Heating curve shows temperature constant during boiling because:", "energy used to overcome intermolecular forces not to increase temperature", None, "short"),
        ("Dry ice (solid CO₂) at -78°C becomes gas without liquid phase. This is called:", ["Sublimation", "Evaporation", "Condensation", "Freezing"], 0, "mcq"),
        ("Pressure increases when gas compressed because:", ["Particles collide more frequently with container walls", "Particles get bigger", "Particles slow down", "Attractive forces increase"], 0, "mcq"),

        # Hard
        ("Experiment: Heat ice from -10°C to steam at 110°C. Temperature stays constant at 0°C and 100°C. During these plateaus:", ["Energy breaks bonds (latent heat) without temperature change", "No heat absorbed", "Particles stop moving", "Heating stops"], 0, "mcq"),
        ("Gas diffusion: Ammonia (NH₃, mass 17) and HCl (mass 36.5) from opposite ends of tube. Where do they meet?", ["Closer to HCl end (lighter NH₃ faster)", "Exact center", "Closer to NH₃ end", "At both ends"], 0, "mcq"),
        ("Brownian motion of smoke particles observed under microscope is evidence for:", "random motion of invisible air molecules", None, "short"),
        ("At 27°C, gas in cylinder at 200kPa. If heated to 127°C at constant volume, new pressure: (Use T in Kelvin: 27°C=300K, 127°C=400K)", ["266.7 kPa", "300 kPa", "400 kPa", "200 kPa"], 0, "mcq"),
        ("Explains why smell spreads faster on hot day:", ["Higher kinetic energy means faster particle movement", "More particles in air", "Lower pressure", "Wind"], 0, "mcq")
    ],

    "sound-sec2": [
        # Easy
        ("Sound travels through medium by:", ["Vibrations of particles", "Light waves", "Heat transfer", "Magnetic fields"], 0, "mcq"),
        ("Sound cannot travel in:", "vacuum", None, "short"),
        ("Speed of sound is fastest in:", ["Solids", "Liquids", "Gases", "Vacuum"], 0, "mcq"),
        ("Frequency measured in:", ["Hertz (Hz)", "Decibels (dB)", "Metres (m)", "Seconds (s)"], 0, "mcq"),
        ("Pitch of sound depends on:", ["Frequency", "Amplitude", "Speed", "Medium"], 0, "mcq"),

        # Medium
        ("Thunder heard 3 seconds after lightning. Distance to lightning (speed of sound ≈ 330m/s):", ["990m", "330m", "110m", "3300m"], 0, "mcq"),
        ("Ultrasound has frequency:", ["Above 20,000 Hz (above human hearing)", "Below 20 Hz", "20-20,000 Hz", "Exactly 1000 Hz"], 0, "mcq"),
        ("Echo from cliff returns after 4s. Distance to cliff (v = 340m/s):", "680m", None, "short"),
        ("Singapore uses ultrasound for medical imaging because:", ["High frequency gives better resolution and doesn't damage tissue", "It's louder", "Cheaper", "Faster"], 0, "mcq"),
        ("Loudness of sound depends on:", ["Amplitude of vibration", "Frequency", "Wavelength", "Speed"], 0, "mcq"),

        # Hard
        ("Sonar on ship sends pulse, echo returns in 0.5s. Seabed depth if speed of sound in water = 1500m/s:", ["375m", "750m", "1500m", "500m"], 0, "mcq"),
        ("String vibrates at 256 Hz. If you double the tension (keeping length and mass same), new frequency approximately:", ["362 Hz (increases by √2)", "512 Hz", "128 Hz", "256 Hz"], 0, "mcq"),
        ("Doppler effect: Ambulance siren approaching has frequency:", "higher than when stationary", None, "short"),
        ("Musical note: fundamental 440Hz, next harmonic 880Hz, then 1320Hz. This shows:", ["Harmonics are integer multiples of fundamental", "Random frequencies", "All frequencies same", "Decreasing pattern"], 0, "mcq"),
        ("Noise level: 80dB is how many times more intense than 60dB? (Decibel scale is logarithmic: 10dB increase = 10× intensity)", ["100 times", "20 times", "1.33 times", "10 times"], 0, "mcq")
    ],

    "magnetism-sec2": [
        # Easy
        ("Materials attracted to magnets:", ["Iron, cobalt, nickel", "Aluminium, copper", "Wood, plastic", "All metals"], 0, "mcq"),
        ("Magnetic poles:", "North and South", None, "short"),
        ("Like poles:", ["Repel each other", "Attract each other", "No effect", "Merge together"], 0, "mcq"),
        ("Earth acts as a:", ["Giant magnet", "Electric field", "Gravity source only", "Heat source"], 0, "mcq"),
        ("Magnetic field lines go from:", ["North to South outside magnet", "South to North", "Both ways equally", "Straight lines only"], 0, "mcq"),

        # Medium
        ("Iron filing pattern around bar magnet shows:", ["Magnetic field lines from N to S", "Random arrangement", "Circular patterns", "No pattern"], 0, "mcq"),
        ("Plotting compass points North because:", ["Earth's magnetic South pole is near geographic North", "Gravity", "Wind direction", "Light from sun"], 0, "mcq"),
        ("Induced magnetism means:", "temporary magnetism in magnetic material near permanent magnet", None, "short"),
        ("To demagnetize steel bar, you can:", ["Heat above Curie temperature or hammer it", "Cool it down", "Keep in magnetic field", "Polish it"], 0, "mcq"),
        ("Electromagnet advantage over permanent magnet:", ["Can be switched on/off and strength adjusted", "Stronger always", "Cheaper", "Lighter"], 0, "mcq"),

        # Hard
        ("Singapore MRT uses electromagnetic brakes. When power cut, electromagnets OFF. This causes:", ["Magnetic brakes engage by spring force for safety", "Train accelerates", "Nothing happens", "Train explodes"], 0, "mcq"),
        ("Solenoid with 200 turns carries 3A. To double magnetic field strength, you can:", ["Double current to 6A OR double turns to 400", "Halve current", "Reverse current direction", "Use AC instead of DC"], 0, "mcq"),
        ("Magnetic relay: small current in coil switches large current in circuit. This demonstrates:", "electromagnetic switching and amplification", None, "short"),
        ("Right-hand grip rule for solenoid: fingers curl in current direction, thumb points to:", ["North pole of electromagnet", "South pole", "Current direction", "Wire direction"], 0, "mcq"),
        ("Lodestone (natural magnet) is mineral:", ["Magnetite (Fe₃O₄)", "Hematite", "Quartz", "Copper oxide"], 0, "mcq")
    ],

    # BIOLOGY CHAPTERS

    "photosynthesis-sec2": [
        # Easy
        ("Photosynthesis equation: 6CO₂ + 6H₂O →", "C₆H₁₂O₆ + 6O₂", None, "short"),
        ("Chlorophyll is found in:", ["Chloroplasts", "Mitochondria", "Nucleus", "Cell wall"], 0, "mcq"),
        ("Gas produced during photosynthesis:", ["Oxygen", "Carbon dioxide", "Nitrogen", "Hydrogen"], 0, "mcq"),
        ("Light energy is converted to:", ["Chemical energy in glucose", "Heat only", "Sound", "Kinetic energy"], 0, "mcq"),
        ("Photosynthesis mainly occurs in:", ["Leaves", "Roots", "Stem only", "Flowers"], 0, "mcq"),

        # Medium
        ("Experiment: Place plant in dark for 24h, then illuminate leaf partially with stencil. After testing with iodine, only illuminated part turns blue-black. This shows:", ["Light is necessary for starch production", "Dark needed for photosynthesis", "Iodine causes starch formation", "All parts photosynthesize equally"], 0, "mcq"),
        ("Singapore Gardens by the Bay uses LED grow lights (red + blue). Why these colors?", ["Chlorophyll absorbs red and blue light most efficiently", "Cheaper", "Brighter to human eyes", "Plants are green"], 0, "mcq"),
        ("Limiting factor: On sunny day with adequate water, increasing temperature from 20°C to 30°C increases rate. Why?", "higher temperature increases enzyme activity", None, "short"),
        ("Variegated leaf (green and white patches). After starch test, only green parts blue-black because:", ["Chlorophyll needed to produce starch", "White parts are dead", "Green parts stored starch from roots", "Iodine doesn't work on white parts"], 0, "mcq"),
        ("Stomata close at night because:", ["No photosynthesis, so CO₂ not needed; prevents water loss", "Temperature too low", "Light damages them", "Oxygen harmful at night"], 0, "mcq"),

        # Hard
        ("Graph: Light intensity vs rate. Initially linear, then plateaus. At plateau, limiting factor is:", ["CO₂ concentration or temperature, not light", "Light intensity", "Water only", "Chlorophyll amount"], 0, "mcq"),
        ("Hydroponics experiment: Bubbling CO₂ through water around roots has no effect on photosynthesis rate. Why?", ["CO₂ must enter through stomata in leaves, not roots", "Plants don't need CO₂", "Water blocks CO₂", "Roots absorb all CO₂"], 0, "mcq"),
        ("Compensation point is when:", "rate of photosynthesis equals rate of respiration", None, "short"),
        ("Greenhouse in Singapore: High light, 35°C, 400ppm CO₂. To increase yield, best to:", ["Increase CO₂ to 1000ppm (light and temp already high)", "Increase temperature to 45°C", "Decrease CO₂", "Add more light only"], 0, "mcq"),
        ("Destarching: Keep plant in dark 48h before experiment. Purpose:", ["Ensure all starch used up so new starch formed is from the experiment", "Kill plant", "Remove chlorophyll", "Increase photosynthesis rate"], 0, "mcq")
    ],

    "transport-in-plants-sec2": [
        # Easy
        ("Xylem transports:", ["Water and mineral salts from roots to leaves", "Sugars", "Oxygen", "Proteins"], 0, "mcq"),
        ("Phloem transports:", "sugars from leaves to other parts", None, "short"),
        ("Root hair cells increase:", ["Surface area for absorption", "Photosynthesis rate", "Seed production", "Flower color"], 0, "mcq"),
        ("Transpiration is:", ["Loss of water vapor from leaves", "Uptake of water", "Production of oxygen", "Food making"], 0, "mcq"),
        ("Water enters root by:", ["Osmosis", "Active transport", "Diffusion of water vapor", "Evaporation"], 0, "mcq"),

        # Medium
        ("Experiment: Place shoot in water with dye. After 24h, xylem vessels are stained. This shows:", ["Xylem transports water upwards", "Phloem transports dye", "All cells absorb dye equally", "Dye is toxic"], 0, "mcq"),
        ("Singapore's high humidity (80-90%) affects transpiration by:", ["Reducing rate because smaller water potential gradient", "Increasing rate", "No effect", "Stopping it completely"], 0, "mcq"),
        ("Transpiration pull: Water column in xylem is under tension because:", "cohesion between water molecules and adhesion to xylem walls", None, "short"),
        ("Wilting occurs when:", ["Transpiration exceeds water absorption rate", "Too much water absorbed", "Plant grows", "Photosynthesis stops"], 0, "mcq"),
        ("Guard cells control stomata opening. In daylight, guard cells:", ["Turgid due to water uptake, stomata open", "Flaccid, stomata close", "Die", "No change"], 0, "mcq"),

        # Hard
        ("Potometer measures transpiration rate. In 30min, air bubble moves 5cm in capillary tube (radius 1mm). Volume water lost (πr²h):", ["0.157 cm³", "5 cm³", "50 cm³", "1.57 cm³"], 0, "mcq"),
        ("Translocation experiment: Remove ring of bark (phloem) from tree trunk. Above ring swells, below shrinks. This shows:", ["Phloem transports sugars downward; removing it blocks transport", "Xylem blocked", "Tree growing", "Bark regenerates"], 0, "mcq"),
        ("Active transport in roots requires:", "ATP from respiration to move minerals against concentration gradient", None, "short"),
        ("Mass flow hypothesis: Sugar loading in leaf phloem creates high pressure. Water follows by osmosis, pushing solution to sink. This requires:", ["Living phloem cells and energy", "Dead xylem only", "No energy", "Transpiration only"], 0, "mcq"),
        ("Guttation: Water droplets on leaf edges in morning. Occurs when:", ["High humidity prevents transpiration but root pressure forces water out", "Transpiration very high", "Photosynthesis active", "Plant crying"], 0, "mcq")
    ],

    "respiration-sec2": [
        # Easy
        ("Aerobic respiration equation: C₆H₁₂O₆ + 6O₂ →", "6CO₂ + 6H₂O + energy (ATP)", None, "short"),
        ("Respiration occurs in:", ["All living cells", "Only muscle cells", "Only plant cells", "Only when exercising"], 0, "mcq"),
        ("Energy from respiration stored in:", ["ATP molecules", "Glucose", "Oxygen", "Water"], 0, "mcq"),
        ("Aerobic respiration requires:", ["Oxygen", "Carbon dioxide", "Light", "Nitrogen"], 0, "mcq"),
        ("Anaerobic respiration in humans produces:", ["Lactic acid", "Alcohol", "Oxygen", "Glucose"], 0, "mcq"),

        # Medium
        ("Experiment: Germinating seeds in thermos produce heat. This shows:", ["Respiration releases energy as heat", "Seeds are cold-blooded", "Thermos generates heat", "No respiration in seeds"], 0, "mcq"),
        ("Marathon runner after race has muscle pain. Caused by:", ["Lactic acid buildup from anaerobic respiration", "Excess oxygen", "Too much glucose", "Aerobic respiration"], 0, "mcq"),
        ("Yeast in bread dough: C₆H₁₂O₆ → 2C₂H₅OH + 2CO₂ + energy. This is:", "anaerobic respiration (fermentation)", None, "short"),
        ("Aerobic vs anaerobic: aerobic produces:", ["38 ATP vs 2 ATP (much more efficient)", "Same energy", "Less energy", "No ATP"], 0, "mcq"),
        ("Mitochondria called 'powerhouse' because:", ["Site of aerobic respiration producing ATP", "Produce electricity", "Store energy", "Generate heat only"], 0, "mcq"),

        # Hard
        ("Singapore hawker making lontong: soaks beans in water overnight. Respiration rate increases initially then decreases. Why decrease?", ["Oxygen in water depleted, anaerobic respiration less efficient", "Beans die", "Temperature drops", "Too much energy"], 0, "mcq"),
        ("Athlete breathes heavily after race. Oxygen debt means:", ["Oxygen needed to break down lactic acid accumulated during anaerobic respiration", "Borrowed oxygen", "Lung damage", "Excess oxygen intake"], 0, "mcq"),
        ("Respiratory quotient RQ = CO₂ produced / O₂ consumed. For glucose, RQ = 1. For fats, RQ = 0.7. Person with RQ = 0.85 is:", "respiring mixture of carbohydrates and fats", None, "short"),
        ("Cyanide poisoning blocks electron transport chain in mitochondria. Effect:", ["Aerobic respiration stops, no ATP produced, rapid death", "Anaerobic increases compensation", "No effect", "More energy produced"], 0, "mcq"),
        ("Germinating seeds: Mass decreases over time despite taking in water. Why?", ["Respiration converts glucose to CO₂ + H₂O, CO₂ released reduces mass", "Seed shrinking", "Water evaporates", "Decomposition"], 0, "mcq")
    ],

    "human-transport-sec2": [
        # Easy
        ("Heart pumps:", ["Blood around the body", "Air to lungs", "Food to stomach", "Nutrients only"], 0, "mcq"),
        ("Red blood cells carry:", "oxygen", None, "short"),
        ("Arteries carry blood:", ["Away from heart", "To heart", "Only to lungs", "Only to brain"], 0, "mcq"),
        ("Veins have:", ["Valves to prevent backflow", "No valves", "Thicker walls than arteries", "Carry only pure blood"], 0, "mcq"),
        ("Double circulation means:", ["Blood passes through heart twice per circuit", "Two hearts", "Two types of blood", "Blood flows both ways"], 0, "mcq"),

        # Medium
        ("Pulmonary artery is unusual because it carries:", ["Deoxygenated blood from heart to lungs", "Oxygenated blood to body", "Blood to heart", "Nutrients to lungs"], 0, "mcq"),
        ("Blood pressure in arteries is high because:", ["Heart pumps blood forcefully and artery walls are elastic", "Arteries are thin", "Gravity", "Oxygen content high"], 0, "mcq"),
        ("Capillaries have walls one cell thick because:", "allow efficient diffusion of materials between blood and tissues", None, "short"),
        ("Hemoglobin combines with oxygen in lungs, releases in tissues because:", ["Higher O₂ concentration in lungs, lower in respiring tissues", "Temperature difference", "pH same everywhere", "Pressure difference"], 0, "mcq"),
        ("White blood cells defend against:", ["Pathogens by phagocytosis and antibody production", "Oxygen transport", "Blood clotting", "Nutrient transport"], 0, "mcq"),

        # Hard
        ("Athlete training in Singapore (30°C, humid). Heart rate increases from 60 to 140 bpm. Stroke volume 70mL. Cardiac output at 140bpm:", ["9.8 L/min", "4.2 L/min", "140 L/min", "70 L/min"], 0, "mcq"),
        ("Coronary arteries supply heart muscle. Blockage causes heart attack because:", ["Heart muscle cells deprived of O₂ and glucose, cannot produce ATP, die", "Blood can't leave heart", "Valves fail", "Brain affected"], 0, "mcq"),
        ("Fetal circulation: Blood bypasses lungs via foramen ovale. At birth, this closes because:", "lungs start working pressure changes cause flap to seal", None, "short"),
        ("Blood doping: Inject extra red blood cells before competition. Advantage:", ["More O₂ carried to muscles improving endurance", "More white cells", "Faster clotting", "Lower heart rate"], 0, "mcq"),
        ("Tissue fluid formation: High pressure at arteriole end forces fluid out. At venule end, low pressure and high protein concentration draws fluid back. If lymphatic vessels blocked:", ["Tissue swelling (edema) as fluid accumulates", "No effect", "Blood pressure rises only", "Dehydration"], 0, "mcq")
    ],

    "coordination-response-sec2": [
        # Easy
        ("Nervous system includes:", ["Brain, spinal cord, nerves", "Heart and blood vessels", "Lungs and airways", "Stomach and intestines"], 0, "mcq"),
        ("Stimulus is:", "a change in environment that is detected", None, "short"),
        ("Receptors detect:", ["Stimuli", "Responses", "Energy only", "Nothing"], 0, "mcq"),
        ("Reflex actions are:", ["Automatic and rapid responses", "Slow and thought out", "Voluntary only", "Learned behaviors"], 0, "mcq"),
        ("Hormones are transported by:", ["Blood", "Nerves", "Air", "Lymph only"], 0, "mcq"),

        # Medium
        ("Reflex arc pathway: Stimulus → receptor → sensory neuron → relay neuron → motor neuron → effector. In knee-jerk reflex, relay neuron is:", ["In spinal cord (CNS)", "In muscle", "In skin", "Not present"], 0, "mcq"),
        ("Pupil reflex: Bright light causes pupil to constrict. Advantage:", ["Protects retina from damage by excess light", "See better in dark", "Increases light entry", "No advantage"], 0, "mcq"),
        ("Synapse: Impulse crosses gap by:", "neurotransmitter chemical diffusion", None, "short"),
        ("Hot object touched: Hand withdraws before feeling pain. This shows:", ["Reflex faster than conscious thought; spinal cord involved", "No pain receptors", "Brain very fast", "Muscles act alone"], 0, "mcq"),
        ("Adrenaline hormone during stress increases:", ["Heart rate, breathing rate, glucose release for fight-or-flight", "Digestion", "Sleep", "Bone growth"], 0, "mcq"),

        # Hard
        ("Nerve impulse speed ~100 m/s. If toe to brain is 2m, time for pain signal:", ["0.02 seconds (20 ms)", "2 seconds", "0.2 seconds", "200 seconds"], 0, "mcq"),
        ("Diabetes: Pancreas fails to produce insulin. Result:", ["Blood glucose remains high after meals, glucose in urine", "Low blood sugar", "High blood pressure only", "Oxygen deficiency"], 0, "mcq"),
        ("Myelin sheath on neurons functions to:", "insulate and speed up impulse transmission", None, "short"),
        ("Singapore driver reacts to red light. Response time = 0.2s, driving at 20m/s. Thinking distance:", ["4m", "20m", "0.2m", "100m"], 0, "mcq"),
        ("Hormones vs nerves: Hormones are:", ["Slower, longer-lasting, target multiple organs via blood", "Faster, short-lived, precise", "Same speed", "Only in plants"], 0, "mcq")
    ]
}

print("Enhancing Science exercises to Singapore MOE standards...\n")

# Update chapters with enhanced exercises
for chapter in chapters:
    chapter_id = chapter["id"]
    if chapter_id in enhanced_exercises:
        exercises = []
        for q_num, q_data in enumerate(enhanced_exercises[chapter_id], 1):
            difficulty = "easy" if q_num <= 5 else ("medium" if q_num <= 10 else "hard")

            prompt, choices_or_answer, answer_or_none, q_type = q_data

            if q_type == "short":
                exercise = {
                    "id": f"{chapter_id.replace('-sec2', '')}-q{q_num}",
                    "type": "short",
                    "difficulty": difficulty,
                    "prompt": prompt,
                    "prompt_zh": f"[{chapter['title']} - 问题 {q_num}]",
                    "answer": choices_or_answer,
                    "validator": "exact",
                    "hint": "Apply scientific method: observe, hypothesize, experiment, analyze, conclude.",
                    "hint_zh": "运用科学方法:观察、假设、实验、分析、结论。"
                }
            else:  # mcq
                exercise = {
                    "id": f"{chapter_id.replace('-sec2', '')}-q{q_num}",
                    "type": "mcq",
                    "difficulty": difficulty,
                    "prompt": prompt,
                    "prompt_zh": f"[{chapter['title']} - 问题 {q_num}]",
                    "choices": choices_or_answer,
                    "answer": answer_or_none,
                    "hint": "Consider the scientific principles and Singapore context in the question.",
                    "hint_zh": "考虑问题中的科学原理和新加坡背景。"
                }

            exercises.append(exercise)

        chapter["exercises"] = exercises
        print(f"✓ {chapter['title']} ({chapter['tag']}): Enhanced with rigorous MOE-standard exercises")

# Save enhanced chapters
with open('chapters/science-sec2-chapters.json', 'w', encoding='utf-8') as f:
    json.dump(chapters, f, indent=2, ensure_ascii=False)

print(f"\n✅ All Science exercises enhanced to Singapore MOE Secondary 2 standards!")
print(f"\n📊 Enhancement features:")
print(f"  • Experimental design and data interpretation")
print(f"  • Calculation-based questions")
print(f"  • Application to Singapore context")
print(f"  • Scientific reasoning and analysis")
print(f"  • Conceptual understanding emphasis")
