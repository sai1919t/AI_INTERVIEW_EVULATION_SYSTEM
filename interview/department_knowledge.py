# question_bank.py

DEPARTMENTS = {

# ======================================================
# ========================= CSE ========================
# ======================================================

"CSE": [

{"question": "What is a data structure?",
 "answers": [
     "A data structure is a method of organizing and storing data efficiently so operations like insertion, deletion and searching can be performed easily.",
     "It is a systematic way of arranging data in memory to improve performance and efficiency."
 ]},

{"question": "What is an algorithm?",
 "answers": [
     "An algorithm is a finite step by step procedure designed to solve a specific problem.",
     "It is a well defined sequence of logical instructions to accomplish a computational task."
 ]},

{"question": "Define time complexity.",
 "answers": [
     "Time complexity measures how the execution time of an algorithm increases with input size.",
     "It represents the growth rate of running time using Big O notation."
 ]},

{"question": "Define space complexity.",
 "answers": [
     "Space complexity is the amount of memory required by an algorithm during execution.",
     "It measures total memory consumption based on input size."
 ]},

{"question": "What is Big O notation?",
 "answers": [
     "Big O notation describes the worst case time complexity of an algorithm.",
     "It expresses the upper bound of algorithm growth rate."
 ]},

{"question": "What is a stack?",
 "answers": [
     "Stack is a linear data structure that follows Last In First Out principle.",
     "It allows insertion and deletion from one end called the top."
 ]},

{"question": "What is a queue?",
 "answers": [
     "Queue is a linear data structure that follows First In First Out principle.",
     "Elements are inserted at rear and removed from front."
 ]},

{"question": "What is a linked list?",
 "answers": [
     "A linked list is a dynamic data structure made of nodes connected by pointers.",
     "Each node contains data and a reference to the next node."
 ]},

{"question": "What is a binary tree?",
 "answers": [
     "A binary tree is a hierarchical data structure where each node has at most two children.",
     "It consists of root, left subtree and right subtree."
 ]},

{"question": "What is binary search?",
 "answers": [
     "Binary search is a searching technique that works on sorted arrays by dividing the search space in half.",
     "It repeatedly splits the array to locate the target efficiently."
 ]},

{"question": "What is recursion?",
 "answers": [
     "Recursion is a technique where a function calls itself to solve smaller subproblems.",
     "It requires a base condition to stop repeated calls."
 ]},

{"question": "What is an operating system?",
 "answers": [
     "An operating system is system software that manages hardware and software resources.",
     "It acts as an interface between user applications and hardware components."
 ]},

{"question": "What is a process?",
 "answers": [
     "A process is a program in execution containing code, data and execution state.",
     "It is an active instance of a running program."
 ]},

{"question": "What is a thread?",
 "answers": [
     "A thread is the smallest unit of CPU execution within a process.",
     "Threads share memory space but execute independently."
 ]},

{"question": "What is deadlock?",
 "answers": [
     "Deadlock is a condition where processes wait indefinitely for resources held by each other.",
     "It occurs due to circular wait and resource locking."
 ]},

{"question": "What is DBMS?",
 "answers": [
     "DBMS is software used to create, manage and manipulate databases.",
     "It ensures data security, consistency and integrity."
 ]},

{"question": "What is normalization?",
 "answers": [
     "Normalization is the process of organizing data to reduce redundancy in databases.",
     "It divides tables into smaller related tables to avoid anomalies."
 ]},

{"question": "What is primary key?",
 "answers": [
     "A primary key uniquely identifies each record in a table.",
     "It cannot contain null values and ensures uniqueness."
 ]},

{"question": "What is foreign key?",
 "answers": [
     "A foreign key is a field that links one table to another.",
     "It references the primary key of another table."
 ]},

{"question": "What is SQL?",
 "answers": [
     "SQL is Structured Query Language used to manage relational databases.",
     "It is used to insert, update, delete and retrieve data."
 ]},

{"question": "What is NoSQL?",
 "answers": [
     "NoSQL databases store non relational and unstructured data.",
     "They provide flexible schema and horizontal scalability."
 ]},

{"question": "What is cloud computing?",
 "answers": [
     "Cloud computing provides computing services over the internet on demand.",
     "It allows users to access storage and servers remotely."
 ]},

{"question": "What is artificial intelligence?",
 "answers": [
     "Artificial intelligence enables machines to simulate human intelligence.",
     "It allows systems to learn, reason and make decisions."
 ]},

{"question": "What is machine learning?",
 "answers": [
     "Machine learning is a subset of AI that enables systems to learn from data.",
     "It improves performance without being explicitly programmed."
 ]},

{"question": "What is deep learning?",
 "answers": [
     "Deep learning is a subset of machine learning based on neural networks.",
     "It uses multiple layers to learn complex patterns."
 ]},

{"question": "What is a compiler?",
 "answers": [
     "A compiler translates high level language into machine code.",
     "It converts source code into executable program."
 ]},

{"question": "What is an interpreter?",
 "answers": [
     "An interpreter executes code line by line.",
     "It translates source code at runtime."
 ]},

{"question": "What is computer network?",
 "answers": [
     "A computer network is a collection of connected devices that share data.",
     "It enables communication between multiple systems."
 ]},

{"question": "What is TCP?",
 "answers": [
     "TCP is a reliable transport protocol that ensures data delivery.",
     "It is connection oriented and provides error checking."
 ]},

{"question": "What is UDP?",
 "answers": [
     "UDP is a connectionless transport protocol.",
     "It is faster but does not guarantee data delivery."
 ]},

{"question": "What is IP address?",
 "answers": [
     "An IP address uniquely identifies a device on a network.",
     "It is used for communication between devices."
 ]},

{"question": "What is encryption?",
 "answers": [
     "Encryption converts readable data into unreadable format.",
     "It protects sensitive information using keys."
 ]},

{"question": "What is hashing?",
 "answers": [
     "Hashing converts data into fixed length hash value.",
     "It is used in password storage and fast retrieval."
 ]},

{"question": "What is virtualization?",
 "answers": [
     "Virtualization creates virtual machines on a single physical system.",
     "It allows multiple operating systems to run on one hardware."
 ]},

{"question": "What is REST API?",
 "answers": [
     "REST API is a web service architecture using HTTP methods.",
     "It allows communication between client and server."
 ]},

{"question": "What is multithreading?",
 "answers": [
     "Multithreading allows multiple threads to run concurrently.",
     "It improves performance and resource utilization."
 ]},

{"question": "What is load balancing?",
 "answers": [
     "Load balancing distributes traffic across multiple servers.",
     "It improves performance and reliability."
 ]},

{"question": "What is DevOps?",
 "answers": [
     "DevOps integrates development and operations teams.",
     "It improves deployment speed using automation."
 ]},

{"question": "What is blockchain?",
 "answers": [
     "Blockchain is a decentralized distributed ledger technology.",
     "It stores data securely in linked blocks."
 ]},

{"question": "What is cybersecurity?",
 "answers": [
     "Cybersecurity protects systems and data from cyber attacks.",
     "It ensures confidentiality, integrity and availability."
 ]},

{"question": "What is operating system scheduling?",
 "answers": [
     "Scheduling determines which process runs next.",
     "It improves CPU utilization and system efficiency."
 ]},

{"question": "What is paging?",
 "answers": [
     "Paging divides memory into fixed size pages.",
     "It reduces external fragmentation."
 ]},

{"question": "What is segmentation?",
 "answers": [
     "Segmentation divides memory into logical segments.",
     "It allows variable size memory allocation."
 ]},

{"question": "What is a microservice?",
 "answers": [
     "Microservice architecture divides application into small services.",
     "Each service runs independently."
 ]},

{"question": "What is agile methodology?",
 "answers": [
     "Agile is an iterative software development approach.",
     "It focuses on flexibility and continuous delivery."
 ]},

{"question": "What is unit testing?",
 "answers": [
     "Unit testing tests individual components of software.",
     "It ensures each module works correctly."
 ]},

{"question": "What is version control?",
 "answers": [
     "Version control tracks changes in source code.",
     "It allows collaboration among developers."
 ]},

{"question": "What is Docker?",
 "answers": [
     "Docker is a containerization platform.",
     "It packages applications with dependencies."
 ]},

{"question": "What is Git?",
 "answers": [
     "Git is a distributed version control system.",
     "It tracks and manages code changes."
 ]}

],

"ECE": [

{"question": "What is a semiconductor?",
 "answers": [
     "A semiconductor is a material whose conductivity lies between conductor and insulator.",
     "It is a material like silicon whose conductivity can be controlled."
 ]},

{"question": "What is intrinsic semiconductor?",
 "answers": [
     "An intrinsic semiconductor is a pure semiconductor without impurities.",
     "It is a semiconductor with equal number of electrons and holes."
 ]},

{"question": "What is extrinsic semiconductor?",
 "answers": [
     "An extrinsic semiconductor is doped with impurities to increase conductivity.",
     "It is formed by adding donor or acceptor atoms to pure semiconductor."
 ]},

{"question": "What is a diode?",
 "answers": [
     "A diode is a two terminal semiconductor device that allows current in one direction.",
     "It is a PN junction device used for rectification."
 ]},

{"question": "What is Zener diode?",
 "answers": [
     "A Zener diode operates in reverse breakdown region for voltage regulation.",
     "It is used to maintain constant output voltage."
 ]},

{"question": "What is a transistor?",
 "answers": [
     "A transistor is a three terminal semiconductor device used for amplification and switching.",
     "It controls current flow between collector and emitter."
 ]},

{"question": "What is BJT?",
 "answers": [
     "BJT is Bipolar Junction Transistor that uses both electrons and holes.",
     "It has emitter, base and collector terminals."
 ]},

{"question": "What is MOSFET?",
 "answers": [
     "MOSFET is a voltage controlled transistor.",
     "It is a Metal Oxide Semiconductor Field Effect Transistor."
 ]},

{"question": "What is rectifier?",
 "answers": [
     "A rectifier converts AC into DC.",
     "It uses diodes to allow one directional current."
 ]},

{"question": "What is amplifier?",
 "answers": [
     "An amplifier increases the amplitude of a signal.",
     "It strengthens weak input signals."
 ]},

{"question": "What is modulation?",
 "answers": [
     "Modulation is the process of varying a carrier signal according to message signal.",
     "It enables long distance communication."
 ]},

{"question": "What is demodulation?",
 "answers": [
     "Demodulation extracts original message signal from carrier wave.",
     "It is reverse process of modulation."
 ]},

{"question": "What is AM?",
 "answers": [
     "AM is Amplitude Modulation where amplitude of carrier varies.",
     "In AM only amplitude changes while frequency remains constant."
 ]},

{"question": "What is FM?",
 "answers": [
     "FM is Frequency Modulation where frequency of carrier varies.",
     "In FM amplitude remains constant."
 ]},

{"question": "What is bandwidth?",
 "answers": [
     "Bandwidth is range of frequencies a signal occupies.",
     "It is difference between highest and lowest frequency."
 ]},

{"question": "What is noise?",
 "answers": [
     "Noise is unwanted disturbance in signal.",
     "It affects signal quality in communication systems."
 ]},

{"question": "What is signal to noise ratio?",
 "answers": [
     "SNR is ratio of signal power to noise power.",
     "Higher SNR indicates better signal quality."
 ]},

{"question": "What is an oscillator?",
 "answers": [
     "An oscillator generates continuous periodic waveform.",
     "It produces signals without external input."
 ]},

{"question": "What is filter?",
 "answers": [
     "A filter allows certain frequencies and blocks others.",
     "It is used to remove unwanted frequency components."
 ]},

{"question": "What is multiplexer?",
 "answers": [
     "Multiplexer selects one input from multiple inputs.",
     "It is a combinational circuit."
 ]},

{"question": "What is demultiplexer?",
 "answers": [
     "Demultiplexer routes single input to multiple outputs.",
     "It performs opposite function of multiplexer."
 ]},

{"question": "What is logic gate?",
 "answers": [
     "Logic gate performs logical operations on binary inputs.",
     "Examples include AND OR NOT gates."
 ]},

{"question": "What is flip flop?",
 "answers": [
     "Flip flop is a memory element that stores one bit.",
     "It is a sequential circuit."
 ]},

{"question": "What is ADC?",
 "answers": [
     "ADC converts analog signal to digital signal.",
     "It samples continuous signal into binary form."
 ]},

{"question": "What is DAC?",
 "answers": [
     "DAC converts digital signal into analog signal.",
     "It produces analog output from binary input."
 ]},

{"question": "What is microprocessor?",
 "answers": [
     "Microprocessor is a programmable device that executes instructions.",
     "It contains CPU on a single chip."
 ]},

{"question": "What is microcontroller?",
 "answers": [
     "Microcontroller is a compact integrated circuit for embedded systems.",
     "It contains CPU memory and I O ports."
 ]},

{"question": "What is antenna?",
 "answers": [
     "An antenna transmits and receives electromagnetic waves.",
     "It converts electrical signals into radio waves."
 ]},

{"question": "What is impedance?",
 "answers": [
     "Impedance is opposition to AC current.",
     "It combines resistance and reactance."
 ]},

{"question": "What is resonance?",
 "answers": [
     "Resonance occurs when inductive and capacitive reactance are equal.",
     "It results in maximum current flow."
 ]},

{"question": "What is PCB?",
 "answers": [
     "PCB is Printed Circuit Board used to connect components.",
     "It mechanically supports and electrically connects electronic parts."
 ]},

{"question": "What is VLSI?",
 "answers": [
     "VLSI is Very Large Scale Integration.",
     "It integrates millions of transistors on a single chip."
 ]},

{"question": "What is digital signal?",
 "answers": [
     "Digital signal has discrete values.",
     "It is represented using binary numbers."
 ]},

{"question": "What is analog signal?",
 "answers": [
     "Analog signal varies continuously over time.",
     "It has infinite amplitude values."
 ]},

{"question": "What is GSM?",
 "answers": [
     "GSM is Global System for Mobile communication.",
     "It is standard for mobile networks."
 ]},

{"question": "What is LTE?",
 "answers": [
     "LTE is Long Term Evolution wireless standard.",
     "It provides high speed data communication."
 ]},

{"question": "What is WiFi?",
 "answers": [
     "WiFi is wireless networking technology.",
     "It allows devices to connect to internet wirelessly."
 ]},

{"question": "What is Bluetooth?",
 "answers": [
     "Bluetooth is short range wireless communication technology.",
     "It connects devices over small distances."
 ]},

{"question": "What is power amplifier?",
 "answers": [
     "Power amplifier increases power level of signal.",
     "It drives load devices like speakers."
 ]},

{"question": "What is CRO?",
 "answers": [
     "CRO is Cathode Ray Oscilloscope used to view waveforms.",
     "It displays voltage versus time graphically."
 ]},

{"question": "What is feedback?",
 "answers": [
     "Feedback returns part of output to input.",
     "It improves stability and performance."
 ]},

{"question": "What is negative feedback?",
 "answers": [
     "Negative feedback reduces gain but improves stability.",
     "It feeds output in opposite phase."
 ]},

{"question": "What is positive feedback?",
 "answers": [
     "Positive feedback increases gain.",
     "It can lead to oscillations."
 ]},

{"question": "What is PWM?",
 "answers": [
     "PWM is Pulse Width Modulation technique.",
     "It controls power by varying pulse width."
 ]},

{"question": "What is SMPS?",
 "answers": [
     "SMPS is Switch Mode Power Supply.",
     "It efficiently converts electrical power."
 ]},

{"question": "What is inverter?",
 "answers": [
     "Inverter converts DC into AC.",
     "It is used in backup power systems."
 ]},

{"question": "What is rectification?",
 "answers": [
     "Rectification is process of converting AC to DC.",
     "It is achieved using diodes."
 ]},

{"question": "What is sampling theorem?",
 "answers": [
     "Sampling theorem states signal must be sampled at twice its highest frequency.",
     "It prevents aliasing."
 ]},

{"question": "What is aliasing?",
 "answers": [
     "Aliasing occurs when sampling rate is too low.",
     "It causes distortion in reconstructed signal."
 ]}

],

"EEE": [

{"question": "What is Ohm's Law?",
 "answers": [
     "Ohms Law states that voltage is equal to current multiplied by resistance.",
     "It defines the relationship V equals I into R in an electrical circuit."
 ]},

{"question": "What is Kirchhoff's Current Law?",
 "answers": [
     "Kirchhoff Current Law states that sum of currents entering a node equals sum leaving it.",
     "It is based on conservation of charge."
 ]},

{"question": "What is Kirchhoff's Voltage Law?",
 "answers": [
     "Kirchhoff Voltage Law states that sum of voltages in a closed loop is zero.",
     "It follows conservation of energy principle."
 ]},

{"question": "What is resistance?",
 "answers": [
     "Resistance is opposition to flow of electric current.",
     "It limits current in a circuit and is measured in ohms."
 ]},

{"question": "What is capacitance?",
 "answers": [
     "Capacitance is the ability to store electric charge.",
     "It is measured in farads and stores energy in electric field."
 ]},

{"question": "What is inductance?",
 "answers": [
     "Inductance is property of a coil to oppose change in current.",
     "It stores energy in magnetic field."
 ]},

{"question": "What is power factor?",
 "answers": [
     "Power factor is ratio of real power to apparent power.",
     "It indicates efficiency of power usage in AC circuits."
 ]},

{"question": "What is transformer?",
 "answers": [
     "A transformer transfers electrical energy between circuits using electromagnetic induction.",
     "It steps up or steps down voltage levels."
 ]},

{"question": "What is DC motor?",
 "answers": [
     "A DC motor converts electrical energy into mechanical energy.",
     "It works on the principle of electromagnetic force."
 ]},

{"question": "What is AC motor?",
 "answers": [
     "An AC motor converts alternating current into mechanical energy.",
     "It operates using rotating magnetic field principle."
 ]},

{"question": "What is synchronous motor?",
 "answers": [
     "A synchronous motor runs at constant speed equal to synchronous speed.",
     "Its rotor rotates in sync with stator magnetic field."
 ]},

{"question": "What is induction motor?",
 "answers": [
     "An induction motor works on electromagnetic induction principle.",
     "It is widely used due to simple construction and low cost."
 ]},

{"question": "What is generator?",
 "answers": [
     "A generator converts mechanical energy into electrical energy.",
     "It works based on Faraday law of electromagnetic induction."
 ]},

{"question": "What is alternator?",
 "answers": [
     "An alternator is an AC generator.",
     "It produces alternating voltage."
 ]},

{"question": "What is circuit breaker?",
 "answers": [
     "A circuit breaker protects electrical circuits from overload.",
     "It interrupts current during fault conditions."
 ]},

{"question": "What is relay?",
 "answers": [
     "A relay is an electrically operated switch.",
     "It is used for protection and control in power systems."
 ]},

{"question": "What is earthing?",
 "answers": [
     "Earthing connects equipment to ground for safety.",
     "It prevents electric shock and protects equipment."
 ]},

{"question": "What is three phase system?",
 "answers": [
     "Three phase system uses three AC voltages separated by 120 degrees.",
     "It provides constant power delivery and higher efficiency."
 ]},

{"question": "What is single phase system?",
 "answers": [
     "Single phase system uses one alternating voltage.",
     "It is commonly used in domestic supply."
 ]},

{"question": "What is load?",
 "answers": [
     "Load is device that consumes electrical power.",
     "It converts electrical energy into useful work."
 ]},

{"question": "What is transmission line?",
 "answers": [
     "Transmission line carries electrical power over long distances.",
     "It connects generation and distribution systems."
 ]},

{"question": "What is distribution system?",
 "answers": [
     "Distribution system delivers electricity to consumers.",
     "It operates at lower voltage levels."
 ]},

{"question": "What is short circuit?",
 "answers": [
     "Short circuit occurs when low resistance path is created.",
     "It results in excessive current flow."
 ]},

{"question": "What is overload?",
 "answers": [
     "Overload occurs when current exceeds rated capacity.",
     "It causes overheating of equipment."
 ]},

{"question": "What is insulation?",
 "answers": [
     "Insulation prevents leakage of current.",
     "It protects conductors and ensures safety."
 ]},

{"question": "What is fuse?",
 "answers": [
     "Fuse protects circuit by melting during excess current.",
     "It breaks the circuit under fault conditions."
 ]},

{"question": "What is voltage regulation?",
 "answers": [
     "Voltage regulation is ability to maintain constant output voltage.",
     "It indicates voltage drop from no load to full load."
 ]},

{"question": "What is efficiency?",
 "answers": [
     "Efficiency is ratio of output power to input power.",
     "It indicates performance of electrical machine."
 ]},

{"question": "What is reactance?",
 "answers": [
     "Reactance is opposition to AC due to capacitance or inductance.",
     "It is frequency dependent resistance."
 ]},

{"question": "What is impedance?",
 "answers": [
     "Impedance is total opposition to AC current.",
     "It is combination of resistance and reactance."
 ]},

{"question": "What is skin effect?",
 "answers": [
     "Skin effect is tendency of AC current to flow on surface of conductor.",
     "It increases resistance at high frequency."
 ]},

{"question": "What is corona effect?",
 "answers": [
     "Corona is ionization of air around high voltage conductor.",
     "It causes power loss and noise."
 ]},

{"question": "What is power plant?",
 "answers": [
     "Power plant generates electrical energy.",
     "It converts mechanical or thermal energy into electricity."
 ]},

{"question": "What is thermal power plant?",
 "answers": [
     "Thermal power plant generates electricity using steam turbine.",
     "It uses coal or fuel to produce heat."
 ]},

{"question": "What is hydro power plant?",
 "answers": [
     "Hydro plant generates electricity using water flow.",
     "It converts hydraulic energy into electrical energy."
 ]},

{"question": "What is nuclear power plant?",
 "answers": [
     "Nuclear plant produces electricity using nuclear reactions.",
     "It generates heat from fission process."
 ]},

{"question": "What is renewable energy?",
 "answers": [
     "Renewable energy comes from natural sources like sun and wind.",
     "It is sustainable and eco friendly."
 ]},

{"question": "What is solar panel?",
 "answers": [
     "Solar panel converts sunlight into electrical energy.",
     "It works on photovoltaic principle."
 ]},

{"question": "What is wind turbine?",
 "answers": [
     "Wind turbine converts wind energy into electrical energy.",
     "It rotates blades to drive generator."
 ]},

{"question": "What is smart grid?",
 "answers": [
     "Smart grid uses digital communication in power system.",
     "It improves reliability and efficiency."
 ]},

{"question": "What is harmonic distortion?",
 "answers": [
     "Harmonics are unwanted frequency components.",
     "They distort waveform in power systems."
 ]},

{"question": "What is grounding?",
 "answers": [
     "Grounding connects electrical system to earth.",
     "It ensures safety and fault protection."
 ]},

{"question": "What is busbar?",
 "answers": [
     "Busbar is conductor used to distribute power.",
     "It collects and distributes current in switchgear."
 ]},

{"question": "What is substation?",
 "answers": [
     "Substation transforms voltage levels.",
     "It connects transmission and distribution systems."
 ]},

{"question": "What is surge?",
 "answers": [
     "Surge is sudden increase in voltage.",
     "It may damage electrical equipment."
 ]},

{"question": "What is lightning arrester?",
 "answers": [
     "Lightning arrester protects equipment from high voltage spikes.",
     "It safely diverts surge to ground."
 ]},

{"question": "What is load flow analysis?",
 "answers": [
     "Load flow analysis determines voltage and power in system.",
     "It analyzes steady state performance."
 ]},

{"question": "What is SCADA?",
 "answers": [
     "SCADA is Supervisory Control and Data Acquisition system.",
     "It monitors and controls power systems remotely."
 ]},

{"question": "What is electromagnetic induction?",
 "answers": [
     "Electromagnetic induction is generation of emf due to changing magnetic field.",
     "It is principle behind generators and transformers."
 ]}

],

"MECH": [

{"question": "What is thermodynamics?",
 "answers": [
     "Thermodynamics is the study of energy transfer in the form of heat and work.",
     "It deals with relationships between heat, work, temperature and energy."
 ]},

{"question": "State first law of thermodynamics.",
 "answers": [
     "First law states that energy cannot be created or destroyed but only converted.",
     "It is law of conservation of energy applied to thermodynamic systems."
 ]},

{"question": "State second law of thermodynamics.",
 "answers": [
     "Second law states that entropy of isolated system always increases.",
     "It defines direction of natural processes and limits efficiency."
 ]},

{"question": "What is entropy?",
 "answers": [
     "Entropy is measure of disorder in a system.",
     "It represents unavailable energy for work."
 ]},

{"question": "What is heat engine?",
 "answers": [
     "Heat engine converts heat energy into mechanical work.",
     "It operates between high and low temperature reservoirs."
 ]},

{"question": "What is internal combustion engine?",
 "answers": [
     "IC engine burns fuel inside combustion chamber.",
     "It converts chemical energy into mechanical energy."
 ]},

{"question": "What is external combustion engine?",
 "answers": [
     "External combustion engine burns fuel outside working cylinder.",
     "Steam engine is an example."
 ]},

{"question": "What is boiler?",
 "answers": [
     "Boiler is device that converts water into steam.",
     "It uses heat energy for steam generation."
 ]},

{"question": "What is turbine?",
 "answers": [
     "Turbine converts fluid energy into mechanical energy.",
     "It rotates due to impact of steam water or gas."
 ]},

{"question": "What is compressor?",
 "answers": [
     "Compressor increases pressure of gas.",
     "It reduces volume of air or gas."
 ]},

{"question": "What is pump?",
 "answers": [
     "Pump moves liquid from one place to another.",
     "It converts mechanical energy into hydraulic energy."
 ]},

{"question": "What is refrigeration?",
 "answers": [
     "Refrigeration is process of removing heat from low temperature region.",
     "It maintains temperature below surroundings."
 ]},

{"question": "What is air conditioning?",
 "answers": [
     "Air conditioning controls temperature humidity and air quality.",
     "It provides thermal comfort indoors."
 ]},

{"question": "What is stress?",
 "answers": [
     "Stress is internal resistance per unit area.",
     "It is force divided by cross sectional area."
 ]},

{"question": "What is strain?",
 "answers": [
     "Strain is deformation per unit length.",
     "It is ratio of change in length to original length."
 ]},

{"question": "What is Young's modulus?",
 "answers": [
     "Young modulus is ratio of stress to strain in elastic region.",
     "It measures stiffness of material."
 ]},

{"question": "What is shear stress?",
 "answers": [
     "Shear stress acts parallel to surface.",
     "It causes sliding deformation."
 ]},

{"question": "What is bending moment?",
 "answers": [
     "Bending moment causes beam to bend.",
     "It is product of force and perpendicular distance."
 ]},

{"question": "What is torsion?",
 "answers": [
     "Torsion is twisting of shaft due to torque.",
     "It produces shear stress in circular members."
 ]},

{"question": "What is fatigue?",
 "answers": [
     "Fatigue is failure due to repeated loading.",
     "It occurs below ultimate strength."
 ]},

{"question": "What is creep?",
 "answers": [
     "Creep is slow deformation under constant stress at high temperature.",
     "It occurs over long time."
 ]},

{"question": "What is casting?",
 "answers": [
     "Casting is manufacturing process where molten metal is poured into mold.",
     "It solidifies into desired shape."
 ]},

{"question": "What is welding?",
 "answers": [
     "Welding joins materials by melting edges.",
     "It creates strong permanent joint."
 ]},

{"question": "What is machining?",
 "answers": [
     "Machining removes material using cutting tools.",
     "It gives desired shape and finish."
 ]},

{"question": "What is lathe machine?",
 "answers": [
     "Lathe rotates workpiece against cutting tool.",
     "It is used for turning operations."
 ]},

{"question": "What is milling machine?",
 "answers": [
     "Milling machine removes material using rotating cutter.",
     "It performs slotting and shaping operations."
 ]},

{"question": "What is drilling?",
 "answers": [
     "Drilling creates circular holes in material.",
     "It uses rotating drill bit."
 ]},

{"question": "What is gear?",
 "answers": [
     "Gear transmits motion and power between shafts.",
     "It has toothed wheels."
 ]},

{"question": "What is bearing?",
 "answers": [
     "Bearing reduces friction between moving parts.",
     "It supports rotating shafts."
 ]},

{"question": "What is cam?",
 "answers": [
     "Cam converts rotary motion into reciprocating motion.",
     "It is used in engines."
 ]},

{"question": "What is flywheel?",
 "answers": [
     "Flywheel stores rotational energy.",
     "It smoothens fluctuations in speed."
 ]},

{"question": "What is brake?",
 "answers": [
     "Brake slows or stops motion.",
     "It converts kinetic energy into heat."
 ]},

{"question": "What is clutch?",
 "answers": [
     "Clutch connects and disconnects power transmission.",
     "It allows smooth gear shifting."
 ]},

{"question": "What is fluid mechanics?",
 "answers": [
     "Fluid mechanics studies behavior of liquids and gases.",
     "It analyzes pressure velocity and flow."
 ]},

{"question": "What is Bernoulli principle?",
 "answers": [
     "Bernoulli principle states pressure decreases as velocity increases.",
     "It applies to incompressible flow."
 ]},

{"question": "What is Reynolds number?",
 "answers": [
     "Reynolds number predicts flow type.",
     "It determines laminar or turbulent flow."
 ]},

{"question": "What is laminar flow?",
 "answers": [
     "Laminar flow is smooth and orderly fluid motion.",
     "It occurs at low Reynolds number."
 ]},

{"question": "What is turbulent flow?",
 "answers": [
     "Turbulent flow is irregular fluid motion.",
     "It occurs at high Reynolds number."
 ]},

{"question": "What is heat transfer?",
 "answers": [
     "Heat transfer is movement of thermal energy.",
     "It occurs by conduction convection and radiation."
 ]},

{"question": "What is conduction?",
 "answers": [
     "Conduction transfers heat through solids.",
     "It occurs due to molecular interaction."
 ]},

{"question": "What is convection?",
 "answers": [
     "Convection transfers heat through fluid motion.",
     "It involves bulk movement of molecules."
 ]},

{"question": "What is radiation?",
 "answers": [
     "Radiation transfers heat through electromagnetic waves.",
     "It does not require medium."
 ]},

{"question": "What is CAD?",
 "answers": [
     "CAD is Computer Aided Design software.",
     "It is used for designing mechanical components."
 ]},

{"question": "What is CAM?",
 "answers": [
     "CAM is Computer Aided Manufacturing.",
     "It automates production process."
 ]},

{"question": "What is CNC?",
 "answers": [
     "CNC is Computer Numerical Control machine.",
     "It automates machining operations."
 ]},

{"question": "What is robotics?",
 "answers": [
     "Robotics deals with design and application of robots.",
     "It integrates mechanics electronics and programming."
 ]},

{"question": "What is automation?",
 "answers": [
     "Automation uses control systems to operate machines.",
     "It reduces human intervention."
 ]},

{"question": "What is renewable energy in mechanical systems?",
 "answers": [
     "Renewable energy uses natural resources like wind and solar.",
     "It reduces environmental impact."
 ]},

{"question": "What is vibration?",
 "answers": [
     "Vibration is oscillatory motion of a body.",
     "It can be free or forced."
 ]}

],

"CIVIL": [

{"question": "What is civil engineering?",
 "answers": [
     "Civil engineering is the branch of engineering that deals with design construction and maintenance of infrastructure.",
     "It focuses on structures like buildings roads bridges and dams."
 ]},

{"question": "What is concrete?",
 "answers": [
     "Concrete is a composite material made of cement sand aggregate and water.",
     "It is widely used in construction for strength and durability."
 ]},

{"question": "What is cement?",
 "answers": [
     "Cement is a binding material used in construction.",
     "It reacts with water to form a hard mass."
 ]},

{"question": "What is aggregate?",
 "answers": [
     "Aggregate consists of sand gravel or crushed stone used in concrete.",
     "It provides bulk and strength to concrete."
 ]},

{"question": "What is water cement ratio?",
 "answers": [
     "Water cement ratio is ratio of water to cement in concrete mix.",
     "It affects strength and durability of concrete."
 ]},

{"question": "What is curing?",
 "answers": [
     "Curing is process of maintaining moisture in concrete.",
     "It helps in proper hydration and strength gain."
 ]},

{"question": "What is compressive strength?",
 "answers": [
     "Compressive strength is capacity of material to withstand compression.",
     "It is measured using compression test."
 ]},

{"question": "What is tensile strength?",
 "answers": [
     "Tensile strength is ability of material to resist tension.",
     "It measures resistance to pulling forces."
 ]},

{"question": "What is reinforcement?",
 "answers": [
     "Reinforcement is steel provided in concrete to resist tension.",
     "It improves structural strength."
 ]},

{"question": "What is beam?",
 "answers": [
     "Beam is horizontal structural member that carries loads.",
     "It resists bending moment and shear force."
 ]},

{"question": "What is column?",
 "answers": [
     "Column is vertical structural member.",
     "It transfers load from structure to foundation."
 ]},

{"question": "What is footing?",
 "answers": [
     "Footing is foundation element that spreads load to soil.",
     "It supports columns or walls."
 ]},

{"question": "What is foundation?",
 "answers": [
     "Foundation transfers structural load to ground.",
     "It ensures stability of structure."
 ]},

{"question": "What is shallow foundation?",
 "answers": [
     "Shallow foundation is constructed near ground surface.",
     "It is used when soil has good bearing capacity."
 ]},

{"question": "What is deep foundation?",
 "answers": [
     "Deep foundation transfers load to deeper soil layers.",
     "Pile foundation is an example."
 ]},

{"question": "What is soil bearing capacity?",
 "answers": [
     "Bearing capacity is maximum load soil can support.",
     "It determines size of foundation."
 ]},

{"question": "What is surveying?",
 "answers": [
     "Surveying is measurement of land and distances.",
     "It determines position of points on earth surface."
 ]},

{"question": "What is leveling?",
 "answers": [
     "Leveling determines difference in elevation.",
     "It measures height of points relative to datum."
 ]},

{"question": "What is contour?",
 "answers": [
     "Contour is imaginary line connecting equal elevations.",
     "It represents terrain shape on map."
 ]},

{"question": "What is retaining wall?",
 "answers": [
     "Retaining wall holds back soil.",
     "It prevents soil erosion and sliding."
 ]},

{"question": "What is slump test?",
 "answers": [
     "Slump test measures workability of concrete.",
     "It indicates consistency of fresh concrete."
 ]},

{"question": "What is mix design?",
 "answers": [
     "Mix design determines proportions of concrete ingredients.",
     "It ensures required strength and durability."
 ]},

{"question": "What is highway engineering?",
 "answers": [
     "Highway engineering deals with design and construction of roads.",
     "It ensures safe and efficient transportation."
 ]},

{"question": "What is traffic engineering?",
 "answers": [
     "Traffic engineering manages traffic flow.",
     "It improves road safety and efficiency."
 ]},

{"question": "What is pavement?",
 "answers": [
     "Pavement is durable road surface layer.",
     "It distributes vehicle loads to subgrade."
 ]},

{"question": "What is flexible pavement?",
 "answers": [
     "Flexible pavement uses asphalt layers.",
     "It distributes load gradually."
 ]},

{"question": "What is rigid pavement?",
 "answers": [
     "Rigid pavement uses concrete slab.",
     "It distributes load over wide area."
 ]},

{"question": "What is irrigation?",
 "answers": [
     "Irrigation supplies water to agricultural land.",
     "It improves crop production."
 ]},

{"question": "What is dam?",
 "answers": [
     "Dam is structure built across river to store water.",
     "It is used for irrigation and power generation."
 ]},

{"question": "What is canal?",
 "answers": [
     "Canal is artificial water channel.",
     "It carries water for irrigation."
 ]},

{"question": "What is environmental engineering?",
 "answers": [
     "Environmental engineering deals with pollution control.",
     "It protects environment and public health."
 ]},

{"question": "What is sewage?",
 "answers": [
     "Sewage is wastewater from domestic use.",
     "It requires treatment before disposal."
 ]},

{"question": "What is water treatment?",
 "answers": [
     "Water treatment removes impurities from water.",
     "It makes water safe for consumption."
 ]},

{"question": "What is BOD?",
 "answers": [
     "BOD is Biochemical Oxygen Demand.",
     "It measures organic pollution in water."
 ]},

{"question": "What is COD?",
 "answers": [
     "COD is Chemical Oxygen Demand.",
     "It indicates amount of oxidizable pollutants."
 ]},

{"question": "What is earthquake resistant structure?",
 "answers": [
     "Earthquake resistant structure withstands seismic forces.",
     "It uses ductile design principles."
 ]},

{"question": "What is load?",
 "answers": [
     "Load is force acting on structure.",
     "It can be dead load live load or wind load."
 ]},

{"question": "What is dead load?",
 "answers": [
     "Dead load is permanent static load of structure.",
     "It includes weight of structural components."
 ]},

{"question": "What is live load?",
 "answers": [
     "Live load is temporary load due to occupants.",
     "It varies over time."
 ]},

{"question": "What is shear force?",
 "answers": [
     "Shear force acts parallel to cross section.",
     "It causes sliding between sections."
 ]},

{"question": "What is bending moment?",
 "answers": [
     "Bending moment causes curvature in beam.",
     "It is product of force and distance."
 ]},

{"question": "What is truss?",
 "answers": [
     "Truss is structure of connected members forming triangles.",
     "It efficiently carries loads."
 ]},

{"question": "What is steel structure?",
 "answers": [
     "Steel structure uses steel components for construction.",
     "It offers high strength and durability."
 ]},

{"question": "What is brick masonry?",
 "answers": [
     "Brick masonry is construction using bricks and mortar.",
     "It forms walls and partitions."
 ]},

{"question": "What is plastering?",
 "answers": [
     "Plastering provides smooth surface finish.",
     "It protects walls from weather."
 ]},

{"question": "What is project management in civil engineering?",
 "answers": [
     "Project management plans and controls construction projects.",
     "It ensures completion within time and cost."
 ]},

{"question": "What is estimation?",
 "answers": [
     "Estimation calculates quantity and cost of materials.",
     "It helps in budgeting construction."
 ]},

{"question": "What is quantity surveying?",
 "answers": [
     "Quantity surveying measures quantities of work.",
     "It manages project costs."
 ]},

{"question": "What is green building?",
 "answers": [
     "Green building minimizes environmental impact.",
     "It promotes energy efficiency and sustainability."
 ]},

{"question": "What is smart city concept?",
 "answers": [
     "Smart city uses technology for efficient urban management.",
     "It improves quality of life using digital systems."
 ]}

]
}