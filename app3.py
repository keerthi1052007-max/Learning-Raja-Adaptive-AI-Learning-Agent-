import streamlit as st
import pandas as pd
import os, time, random
from datetime import date, timedelta
from openai import OpenAI, RateLimitError

def ai_mood(xp):
    if xp >= 300:
        return "😎 GOD TIER"
    elif xp >= 150:
        return "🔥 LOCKED IN"
    elif xp >= 50:
        return "🙂 WARMING UP"
    else:
        return "😴 SLEEP MODE"


# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Adaptive AI Learning Platform-THE LEARNING RAJA😎",
    page_icon="🎓",
    layout="wide"
)

# ================= UI STYLES =================
st.markdown("""
<style>

/* ================= BASE APP ================= */
.stApp {
    color: white;
    background: linear-gradient(-45deg, #020617, #020617, #0f172a, #020617);
    background-size: 400% 400%;
    animation: gradientBG 14s ease infinite;
}

@keyframes gradientBG {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* ================= HEADER ================= */
.header {
    background:linear-gradient(135deg,#38bdf8,#22c55e);
    padding:28px;
    border-radius:24px;
    color:black;
    font-size:38px;
    font-weight:900;
    text-align:center;
    box-shadow: 0 0 25px rgba(34,197,94,0.4);
}

/* ================= CARDS ================= */
.card {
    background:rgba(255,255,255,0.08);
    padding:20px;
    border-radius:18px;
    margin-bottom:15px;
    transition: all 0.3s ease;
}
.card:hover {
    transform: translateY(-6px) scale(1.02);
    box-shadow:
        0 0 15px rgba(56,189,248,0.6),
        0 0 40px rgba(34,197,94,0.4),
        0 0 70px rgba(168,85,247,0.3);
}

/* ================= XP CARD ================= */
.xp {
    background:linear-gradient(135deg,#facc15,#fb7185);
    color:black;
    font-size:26px;
    font-weight:800;
    text-align:center;
    padding:14px;
    border-radius:16px;
    box-shadow: 0 0 25px rgba(250,204,21,0.45);
}

/* ================= COLORFUL BOXES ================= */
.hero-box {
    background: linear-gradient(135deg,#6366f1,#22c55e,#38bdf8);
    border-radius: 26px;
    padding: 55px;
    box-shadow: 0 0 35px rgba(56,189,248,0.45);
}

.study-break {
    background: linear-gradient(135deg,#fb7185,#facc15);
    color: black;
    border-radius: 22px;
    padding: 30px;
    box-shadow: 0 0 30px rgba(250,204,21,0.45);
}

.einstein-box {
    background: linear-gradient(135deg,#a855f7,#ec4899);
    color: white;
    border-radius: 22px;
    padding: 32px;
    box-shadow: 0 0 30px rgba(236,72,153,0.5);
}

/* ================= GOD MODE GLASS ================= */
.glass {
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(18px);
    border-radius: 22px;
    border: 1px solid rgba(255,255,255,0.15);
}

.glass:hover {
    box-shadow:
        0 0 15px rgba(56,189,248,0.6),
        0 0 40px rgba(34,197,94,0.4),
        0 0 70px rgba(168,85,247,0.3);
    transform: translateY(-6px) scale(1.02);
}

/* ================= SIDEBAR ================= */
.sidebar-title {
    font-size: 28px;
    font-weight: 900;
    text-align: center;
    margin-bottom: 15px;
}

/* ================= XP PROGRESS BAR ================= */
.xp-bar {
    width: 100%;
    background: rgba(255,255,255,0.15);
    border-radius: 999px;
    overflow: hidden;
}
.xp-fill {
    height: 14px;
    background: linear-gradient(135deg,#22c55e,#38bdf8);
    animation: loadXP 1.5s ease;
}
@keyframes loadXP {
    from { width: 0%; }
}

/* ================= GOD BUTTON ================= */
.god-btn button {
    background: linear-gradient(135deg,#facc15,#fb7185,#a855f7);
    font-size: 26px;
    font-weight: 900;
    padding: 22px 46px;
    border-radius: 999px;
    box-shadow: 0 0 40px rgba(250,204,21,0.6);
    transition: all 0.3s ease;
}
.god-btn button:hover {
    transform: scale(1.15) rotate(-1deg);
    box-shadow: 0 0 70px rgba(168,85,247,0.8);
}

</style>
""", unsafe_allow_html=True)


# ================= OPENAI =================
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ================= HEADER =================
st.markdown("""
<div class="header">
🎓 LEARNING RAJA😎-Adaptive AI Learning Platform<br>
<span style="font-size:17px">Learn • Practice • Master • Certify</span>
</div>
""", unsafe_allow_html=True)

# ================= DATA =================
# ================= COMPLETE SYLLABUS DATA =================

# ================= COMPLETE SCHOOL + COLLEGE SYLLABUS =================

grades = [
    "6th","7th","8th","9th","10th","11th","12th",
    "BSc_1st_Year","BSc_2nd_Year","BSc_3rd_Year",
    "BTech_1st_Year","BTech_2nd_Year","BTech_3rd_Year","BTech_4th_Year"
]

subjects = [
    "Maths","Physics","Chemistry","Biology","Computer Science"
]

syllabus = {

# ================= MATHS =================
"Maths": {
    "6th": ["Knowing Our Numbers","Whole Numbers","Playing with Numbers",
            "Basic Geometrical Ideas","Understanding Elementary Shapes",
            "Integers","Fractions","Decimals","Data Handling",
            "Mensuration","Algebra","Ratio and Proportion"],

    "7th": ["Integers","Fractions and Decimals","Data Handling",
            "Simple Equations","Lines and Angles",
            "The Triangle and its Properties","Congruence of Triangles",
            "Comparing Quantities","Rational Numbers","Perimeter and Area",
            "Algebraic Expressions","Exponents and Powers",
            "Symmetry","Visualising Solid Shapes"],

    "8th": ["Rational Numbers","Linear Equations in One Variable",
            "Understanding Quadrilaterals","Practical Geometry",
            "Data Handling","Squares and Square Roots",
            "Cubes and Cube Roots","Comparing Quantities",
            "Algebraic Expressions and Identities","Mensuration",
            "Exponents and Powers","Direct and Inverse Proportions",
            "Factorisation","Introduction to Graphs","Playing with Numbers"],

    "9th": ["Number Systems","Polynomials","Coordinate Geometry",
            "Linear Equations in Two Variables","Introduction to Euclid’s Geometry",
            "Lines and Angles","Triangles","Quadrilaterals",
            "Areas of Parallelograms and Triangles","Circles",
            "Constructions","Heron’s Formula",
            "Surface Areas and Volumes","Statistics","Probability"],

    "10th": ["Real Numbers","Polynomials",
             "Pair of Linear Equations in Two Variables",
             "Quadratic Equations","Arithmetic Progressions",
             "Triangles","Coordinate Geometry","Trigonometry",
             "Applications of Trigonometry","Circles","Constructions",
             "Areas Related to Circles","Surface Areas and Volumes",
             "Statistics","Probability"],

    "11th": ["Sets","Relations and Functions","Trigonometric Functions",
             "Principle of Mathematical Induction",
             "Complex Numbers and Quadratic Equations",
             "Linear Inequalities","Permutations and Combinations",
             "Binomial Theorem","Sequences and Series",
             "Straight Lines","Conic Sections",
             "Introduction to Three Dimensional Geometry",
             "Limits and Derivatives","Mathematical Reasoning",
             "Statistics","Probability"],

    "12th": ["Relations and Functions","Inverse Trigonometric Functions",
             "Matrices","Determinants","Continuity and Differentiability",
             "Applications of Derivatives","Integrals",
             "Applications of Integrals","Differential Equations",
             "Vector Algebra","Three Dimensional Geometry",
             "Linear Programming","Probability"],

    "BSc_1st_Year": ["Algebra","Trigonometry","Differential Calculus","Matrices"],
    "BSc_2nd_Year": ["Integral Calculus","Differential Equations",
                      "Vector Analysis","Probability"],
    "BSc_3rd_Year": ["Real Analysis","Complex Analysis","Numerical Methods"],

    "BTech_1st_Year": ["Limits and Continuity","Differentiation",
                        "Applications of Derivatives","Integrals",
                        "Differential Equations","Matrices",
                        "Eigen Values and Vectors"],
    "BTech_2nd_Year": ["Vector Calculus","Laplace Transforms",
                        "Fourier Series","Probability","Statistics",
                        "Numerical Methods"],
    "BTech_3rd_Year": ["Complex Analysis","Operations Research",
                        "Optimization Techniques","Graph Theory"],
    "BTech_4th_Year": ["Advanced Statistics","Data Analysis",
                        "Applied Mathematics"]
},

# ================= PHYSICS =================
"Physics": {
    "6th": ["Motion and Measurement of Distances",
            "Light Shadows and Reflections",
            "Electricity and Circuits","Fun with Magnets"],

    "7th": ["Heat","Motion and Time",
            "Electric Current and its Effects","Light"],

    "8th": ["Force and Pressure","Friction",
            "Sound","Light","Some Natural Phenomena"],

    "9th": ["Motion","Force and Laws of Motion",
            "Gravitation","Work and Energy","Sound"],

    "10th": ["Light – Reflection and Refraction",
             "The Human Eye and the Colourful World",
             "Electricity","Magnetic Effects of Electric Current",
             "Sources of Energy"],

    "11th": ["Physical World and Measurement","Units and Measurements",
             "Motion in a Straight Line","Motion in a Plane",
             "Laws of Motion","Work Energy and Power",
             "Centre of Mass and Rotational Motion",
             "Gravitation","Mechanical Properties of Solids",
             "Mechanical Properties of Fluids",
             "Thermal Properties of Matter","Thermodynamics",
             "Kinetic Theory","Oscillations and Waves"],

    "12th": ["Electrostatics","Current Electricity",
             "Magnetic Effects of Current","Magnetism and Matter",
             "Electromagnetic Induction","Alternating Current",
             "Electromagnetic Waves","Ray Optics and Optical Instruments",
             "Wave Optics","Dual Nature of Radiation and Matter",
             "Atoms","Nuclei","Semiconductor Electronics",
             "Communication Systems"],

    "BSc_1st_Year": ["Mechanics","Properties of Matter","Oscillations","Optics"],
    "BSc_2nd_Year": ["Electricity and Magnetism","Thermal Physics","Electronics"],
    "BSc_3rd_Year": ["Quantum Mechanics","Solid State Physics","Nuclear Physics"],

    "BTech_1st_Year": ["Engineering Mechanics","Waves and Oscillations",
                        "Optics","Modern Physics","Semiconductor Physics"],
    "BTech_2nd_Year": ["Electromagnetism","Electronic Materials",
                        "Quantum Mechanics Basics"],
    "BTech_3rd_Year": ["Solid State Physics","Nano Physics","Nuclear Physics"],
    "BTech_4th_Year": ["Advanced Materials","Applied Physics"]
},

# ================= CHEMISTRY =================
"Chemistry": {
    "6th": ["Sorting Materials into Groups",
            "Separation of Substances","Changes Around Us",
            "Water","Air Around Us"],

    "7th": ["Acids Bases and Salts","Physical and Chemical Changes"],

    "8th": ["Synthetic Fibres and Plastics",
            "Materials Metals and Non-metals",
            "Coal and Petroleum","Combustion and Flame",
            "Chemical Effects of Electric Current"],

    "9th": ["Matter in Our Surroundings",
            "Is Matter Around Us Pure",
            "Atoms and Molecules","Structure of the Atom"],

    "10th": ["Chemical Reactions and Equations",
             "Acids Bases and Salts",
             "Metals and Non-metals",
             "Carbon and its Compounds",
             "Sources of Energy"],

    "11th": ["Some Basic Concepts of Chemistry",
             "Structure of Atom",
             "Classification of Elements and Periodicity",
             "Chemical Bonding and Molecular Structure",
             "States of Matter","Thermodynamics",
             "Equilibrium","Redox Reactions",
             "Hydrogen","s-Block Elements",
             "Some p-Block Elements",
             "Organic Chemistry – Basic Principles",
             "Hydrocarbons","Environmental Chemistry"],

    "12th": ["Solid State","Solutions","Electrochemistry",
             "Chemical Kinetics","Surface Chemistry",
             "p-Block Elements","d and f Block Elements",
             "Coordination Compounds",
             "Haloalkanes and Haloarenes",
             "Alcohols Phenols and Ethers",
             "Aldehydes Ketones and Carboxylic Acids",
             "Amines","Biomolecules",
             "Polymers","Chemistry in Everyday Life"],

    "BSc_1st_Year": ["Physical Chemistry I","Atomic Structure","Periodic Table"],
    "BSc_2nd_Year": ["Organic Chemistry I","Hydrocarbons",
                      "Alcohols and Ethers"],
    "BSc_3rd_Year": ["Physical Chemistry II",
                      "Inorganic Chemistry","Analytical Techniques"],

    "BTech_1st_Year": ["Atomic Structure","Chemical Bonding",
                        "Spectroscopy","Water Technology",
                        "Polymers","Nanomaterials"],
    "BTech_2nd_Year": ["Electrochemistry","Corrosion","Fuels and Combustion"],
    "BTech_3rd_Year": ["Polymer Science","Industrial Chemistry"],
    "BTech_4th_Year": ["Green Chemistry","Nano Chemistry"]
},

# ================= BIOLOGY =================
"Biology": {
    "6th": ["Food Where Does It Come From","Components of Food",
            "Getting to Know Plants","Body Movements",
            "The Living Organisms","Garbage In Garbage Out"],

    "7th": ["Nutrition in Plants","Nutrition in Animals",
            "Respiration in Organisms",
            "Transportation in Animals and Plants",
            "Reproduction in Plants"],

    "8th": ["Crop Production and Management",
            "Microorganisms Friend and Foe",
            "Conservation of Plants and Animals",
            "Cell Structure and Functions",
            "Reproduction in Animals",
            "Reaching the Age of Adolescence",
            "Pollution of Air and Water"],

    "9th": ["The Fundamental Unit of Life","Tissues",
            "Diversity in Living Organisms",
            "Why Do We Fall Ill",
            "Natural Resources",
            "Improvement in Food Resources"],

    "10th": ["Life Processes","Control and Coordination",
             "How Do Organisms Reproduce",
             "Heredity and Evolution",
             "Our Environment",
             "Management of Natural Resources"],

    "11th": ["The Living World","Biological Classification",
             "Plant Kingdom","Animal Kingdom",
             "Cell: Structure and Function",
             "Plant Physiology","Human Physiology"],

    "12th": ["Reproduction","Genetics","Evolution",
             "Biotechnology","Ecology","Environmental Issues"],

    "BSc_1st_Year": ["Cell Biology","Diversity of Living Organisms"],
    "BSc_2nd_Year": ["Genetics","Microbiology","Biochemistry"],
    "BSc_3rd_Year": ["Biotechnology","Ecology","Evolution"],

    "BTech_1st_Year": ["Cell Biology","Biochemistry"],
    "BTech_2nd_Year": ["Genetics","Microbiology"],
    "BTech_3rd_Year": ["Biotechnology","Molecular Biology"],
    "BTech_4th_Year": ["Bioinformatics","Industrial Biotechnology"]
},

# ================= COMPUTER SCIENCE =================
"Computer Science": {
    "6th": ["Computer – A Friendly Machine",
            "Parts of Computer","Uses of Computer",
            "Introduction to Internet"],

    "7th": ["Number System","Computer Memory",
            "Operating System","Introduction to Programming"],

    "8th": ["Computer Networks","Cyber Safety",
            "HTML","Problem Solving"],

    "9th": ["Introduction to Python","Data Types",
            "Flow of Control","Introduction to Data Handling",
            "Cyber Ethics"],

    "10th": ["Python Programming","Lists and Dictionaries",
             "Functions","File Handling","Database Concepts"],

    "11th": ["Computer System","Data Representation",
             "Python Programming","Flow of Control",
             "Functions","Lists","Dictionaries","File Handling"],

    "12th": ["Data Structures","Stacks and Queues",
             "Searching and Sorting",
             "Database Management Systems","SQL Queries",
             "Computer Networks","Cyber Security"],

    "BSc_1st_Year": ["Computer Fundamentals","C Programming"],
    "BSc_2nd_Year": ["Data Structures","OOP","DBMS"],
    "BSc_3rd_Year": ["Operating Systems","Computer Networks",
                      "Software Engineering","Mini Project"],

    "BTech_1st_Year": ["C Programming","Python Programming","Problem Solving"],
    "BTech_2nd_Year": ["Data Structures","OOP","Java","DBMS"],
    "BTech_3rd_Year": ["Operating Systems","Computer Networks",
                        "Software Engineering"],
    "BTech_4th_Year": ["Artificial Intelligence","Machine Learning",
                        "Cloud Computing","Cyber Security","Major Project"]
}

}


# ================= SESSION INIT =================
def init(k,v):
    if k not in st.session_state:
        st.session_state[k]=v

init("page","Welcome")
init("points",{})
init("quiz_no",{})
init("quiz_scores",{})
init("quiz_active",{})
init("questions",{})
init("q_index",{})
init("answered",{})
init("streak",{})
init("last_date",{})
init("performance",{})   # ⭐ subject-wise performance

# ================= AI MCQ =================
def parse_mcq(text):
    qs=[]
    for b in text.split("\n\n"):
        try:
            q=b.split("Explanation:")[0].strip()
            e=b.split("Explanation:")[1].split("Answer:")[0].strip()
            a=b.split("Answer:")[1].strip()
            qs.append((q,a,e))
        except:
            pass
    return qs

def gen_mcq(subject,topic,diff,n=10):
    prompt=f"""
Create {n} {diff} MCQs on {topic} ({subject}).

Format:
Question
A) ...
B) ...
C) ...
D) ...
Explanation: ...
Answer: A
"""
    for _ in range(3):
        try:
            r=client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role":"user","content":prompt}]
            )
            qs=parse_mcq(r.choices[0].message.content)
            if len(qs)>=n: return qs[:n]
        except RateLimitError:
            time.sleep(20)
    return []

# ================= ROUTER =================
def go(p):
    st.session_state.page=p
    st.rerun()

# ================= WELCOME =================
if st.session_state.page == "Welcome":

    # ================= CRAZY CSS =================
    st.markdown("""
    <style>
    @keyframes glow {
        0% { box-shadow: 0 0 10px #22c55e; }
        50% { box-shadow: 0 0 25px #38bdf8; }
        100% { box-shadow: 0 0 10px #22c55e; }
    }
    @keyframes wobble {
        0% { transform: rotate(0deg); }
        25% { transform: rotate(1deg); }
        50% { transform: rotate(-1deg); }
        75% { transform: rotate(1deg); }
        100% { transform: rotate(0deg); }
    }
    .glow {
        animation: glow 2s infinite;
    }
    .wobble {
        animation: wobble 0.6s infinite;
    }
    </style>
    """, unsafe_allow_html=True)

    # ================= GIANT HERO =================
    st.markdown("""
    <div class="card glow" style="text-align:center; padding:55px;">
        <h1 style="font-size:68px;">🤯 LEARNING RAJA</h1>
        <p style="font-size:30px;">
            The only AI that teaches you <br>
            <b>and</b> roasts you till you succeed 🔥
        </p>
        <p style="font-size:18px; opacity:0.75;">
            Warning: Studying may cause intelligence.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # ================= ROTATING JOKES =================
    jokes = [
        "📚 I opened my book… my confidence closed.",
        "😴 Studying without breaks is illegal in 42 countries (trust me).",
        "🤓 Teacher: ‘Revise once’ • Brain: formats itself",
        "🧠 Brain during lecture: NASA • Brain during exam: Calculator.exe stopped",
        "🔥 Syllabus so big even Google said ‘bro chill’",
        "💀 My motivation went to buy milk and never came back"
    ]

    roasts = [
        "➗ Maths: Solve for x. Lose peace.",
        "⚡ Physics: Gravity works. Grades don’t.",
        "🧪 Chemistry: Bonding issues everywhere.",
        "🧬 Biology: 400 terms, 1 exam, 0 mercy.",
        "💻 CS: One semicolon away from enlightenment."
    ]

    # Session-based rotation
    if "joke_idx" not in st.session_state:
        st.session_state.joke_idx = 0

    joke = jokes[st.session_state.joke_idx % len(jokes)]
    roast = roasts[st.session_state.joke_idx % len(roasts)]
    st.session_state.joke_idx += 1

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown(f"""
        <div class="card wobble">
            <h2 style="font-size:42px;">😂 AI STUDY BREAK</h2>
            <p style="font-size:28px; line-height:1.7;">
                {joke}
            </p>
            <hr>
            <p style="font-size:24px;">
                {roast}
            </p>
            <p style="font-size:18px; opacity:0.7;">
                +5 XP if you didn’t cry reading this
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card" style="text-align:center;">
            <h2 style="font-size:36px;">🧠 EINSTEIN MODE</h2>
            <p style="font-size:26px;">
                “Education is not learning facts,<br>
                it’s surviving exams.”
            </p>
            <p style="font-size:18px; opacity:0.8;">
                — Definitely Einstein 😎
            </p>
        </div>
        """, unsafe_allow_html=True)

    # ================= FAKE AI LOADING =================
    with st.spinner("🤖 Learning Raja is calculating your future success..."):
        time.sleep(1.2)

    # ================= FINAL CTA =================
    st.markdown("<div class='god-btn'>", unsafe_allow_html=True)
    if st.button("🚀 OKAY RAJA, MAKE ME A TOPPER"):
        st.balloons()
        go("Details")
    st.markdown("</div>", unsafe_allow_html=True)




# ================= DETAILS =================
elif st.session_state.page == "Details":

    # ===== FUN CSS (DETAILS ONLY) =====
    st.markdown("""
    <style>
    .big-input label {
        font-size:22px !important;
        font-weight:700 !important;
    }
    .helper-text {
        font-size:18px;
        opacity:0.85;
        margin-top:-10px;
        margin-bottom:20px;
    }
    </style>
    """, unsafe_allow_html=True)

    # ===== HERO CARD =====
    st.markdown("""
    <div class="card" style="text-align:center; padding:45px;">
        <h1 style="font-size:52px;">🧾 Tell Me About You</h1>
        <p style="font-size:24px;">
            No judging. Except your syllabus. 😌
        </p>
        <p style="font-size:18px; opacity:0.75;">
            (This helps me roast you accurately)
        </p>
    </div>
    """, unsafe_allow_html=True)

    # ===== INPUTS =====
    st.markdown('<div class="big-input">', unsafe_allow_html=True)
    name = st.text_input("👤 Your Name")
    st.markdown("<div class='helper-text'>Don’t worry, I won’t tell your teacher 😄</div>", unsafe_allow_html=True)

    grade = st.selectbox("🎓 Your Grade", grades)
    st.markdown("<div class='helper-text'>Choose wisely… your future depends on it 🔮</div>", unsafe_allow_html=True)

    subject = st.selectbox("📘 Favorite Subject", subjects)
    st.markdown("<div class='helper-text'>Or the one that scares you the most 😈</div>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # ===== FUN FACT STRIP =====
    facts = [
        "🧠 Fun fact: Your brain loads slower when exams are near.",
        "📚 Fun fact: Studying 1 hour now saves 10 hours of panic later.",
        "🔥 Fun fact: Toppers were once confused too.",
        "😴 Fun fact: Sleep is also part of the syllabus."
    ]

    st.markdown(
        f"""
        <div class="card" style="text-align:center;">
            <p style="font-size:20px;">
                {random.choice(facts)}
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # ===== CONTINUE BUTTON =====
    st.markdown("<br>", unsafe_allow_html=True)
    if name and st.button("🚀 CONTINUE (I’M READY)"):
        uid = name.replace(" ", "_")
        st.session_state.user = name
        st.session_state.grade = grade
        st.session_state.subject = subject

        st.session_state.points.setdefault(uid, 0)
        st.session_state.quiz_no.setdefault(uid, 1)
        st.session_state.quiz_scores.setdefault(uid, [])
        st.session_state.streak.setdefault(uid, 0)
        st.session_state.last_date.setdefault(uid, None)
        st.session_state.performance.setdefault(uid, {})

        go("Dashboard")
# ================= CONTEXT =================
# ================= CONTEXT =================
else:
    name = st.session_state.user
    grade = st.session_state.grade
    uid = name.replace(" ", "_")

    # ✅ DYNAMIC SUBJECT SELECTION (NEW)
    subject = st.selectbox(
        "📘 Subject",
        subjects,
        key="active_subject"
    )

    # ✅ TOPIC DEPENDS ON SUBJECT + GRADE
    # Get topics strictly from syllabus
    topics = syllabus.get(subject, {}).get(st.session_state.grade)

    if topics is None:
        st.error("❌ No syllabus found for this class & subject")
        topic = None
    else:
        topic = st.selectbox("📚 Change Topic", topics)



    with st.sidebar:
        

        st.markdown(
            "<div class='glass sidebar-title'>⚙ LEARNING CONTROL</div>",
            unsafe_allow_html=True
        )

        st.markdown(
            f"<div class='glass'><h3>👤 {name}</h3>🎓 {grade}</div>",
            unsafe_allow_html=True
        )

        st.markdown(
            f"<div class='xp'>🏆 {st.session_state.points[uid]} XP</div>",
            unsafe_allow_html=True
        )

        new_grade = st.selectbox(
            "🎓 Change Class",
            grades,
            index=grades.index(grade)
        )
        if new_grade != grade:
            st.session_state.grade = new_grade
            st.rerun()

        subject = st.selectbox("📘 Change Subject", subjects)

        topic = st.selectbox(
            "📚 Change Topic",
            syllabus.get(subject, {}).get(
                st.session_state.grade, ["General"]
            )
        )

        st.divider()

        if st.button("🏠 Dashboard"): go("Dashboard")
        if st.button("🤖 AI Tutor"): go("Tutor")
        if st.button("📝 Quiz"): go("Quiz")
        if st.button("🧪 Mock Test"): go("Mock")
        if st.button("🎓 Final Test"): go("Final")
        if st.button("🏆 Leaderboard"): go("Leaderboard")
        if st.button("🚪 Log Out"):
            go("Logout")


        

# ================= DASHBOARD =================
if st.session_state.page=="Dashboard":
    today=date.today()
    mins=st.number_input("⏱ Study minutes today",10,600,30)

    if st.button("Log Study"):
        last=st.session_state.last_date[uid]
        if last==today-timedelta(days=1):
            st.session_state.streak[uid]+=1
            st.session_state.points[uid]+=20
            st.success("🔥 Streak continued +20 XP")
        elif last!=today:
            st.session_state.streak[uid]=1
        st.session_state.last_date[uid]=today

    c1,c2,c3=st.columns(3)
    c1.metric("XP",st.session_state.points[uid])
    c2.metric("🔥 Streak",st.session_state.streak[uid])
    c3.metric("🎯 Quizzes",len(st.session_state.quiz_scores[uid]))
   # ===== AI MOOD =====
    xp = st.session_state.points[uid]
    mood = ai_mood(xp)

    st.markdown(
        f"<div class='badge'>🤖 AI Mood: {mood}</div>",
        unsafe_allow_html=True
    )

    # ===== XP PROGRESS BAR =====
    progress = min((xp % 100), 100)

    st.markdown(f"""
    <div class="xp-bar">
        <div class="xp-fill" style="width:{progress}%"></div>
    </div>
    <p style="text-align:center; margin-top:6px;">
    ⚡ {progress}/100 XP to next level
    </p>
    """, unsafe_allow_html=True)


    # ===== SUBJECT PERFORMANCE GRAPH =====
    # ===== SMART + FUN SUBJECT PERFORMANCE GRAPH =====
    st.subheader("📊 Subject-wise Performance (AI Roast Edition 😈)")

    perf = st.session_state.performance.get(uid, {})

    subject_avg = {}
    status_msg = {}

    for sub in subjects:
        if sub in perf and len(perf[sub]) > 0:
            avg = sum(perf[sub]) / len(perf[sub])
            subject_avg[f"{sub} 📘"] = avg

            # 🔥 AI commentary
            if avg >= 80:
                status_msg[sub] = "🔥 Topper vibes!"
            elif avg >= 50:
                status_msg[sub] = "😌 Doing okay… for now"
            else:
                status_msg[sub] = "😬 Needs attention ASAP"
        else:
            subject_avg[f"{sub} ❌"] = 0
            status_msg[sub] = "🫣 Not attempted yet (AI judging silently)"

    # DataFrame
    df = pd.DataFrame.from_dict(
        subject_avg,
        orient="index",
        columns=["Average Score"]
    )

    # Graph
    st.bar_chart(df)

    # ===== FUN COMMENTARY SECTION =====
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### 🤖 AI Coach Commentary")

    for sub, msg in status_msg.items():
        st.markdown(f"- *{sub}* → {msg}")



# ================= AI TUTOR =================
elif st.session_state.page=="Tutor":
    q=st.text_input("Ask your doubt")
    if st.button("Ask AI"):
        r=client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role":"user","content":f"Explain {topic} for {grade}: {q}"}]
        )
        st.markdown(r.choices[0].message.content)

# ================= QUIZ =================
elif st.session_state.page == "Quiz":
    qn = st.session_state.quiz_no[uid]
    st.subheader(f"Quiz {qn} / 5")

    if qn > 5:
        st.success("All quizzes completed 🎉")
    else:
        if not st.session_state.quiz_active.get(uid, False):
            if st.button("▶ Start Quiz"):
                diff = "easy" if qn < 3 else "medium"
                st.session_state.questions[uid] = gen_mcq(subject, topic, diff)
                st.session_state.q_index[uid] = 0
                st.session_state.quiz_active[uid] = True
                st.session_state.score = 0
                st.session_state.answered[uid] = False
                st.rerun()

        if st.session_state.quiz_active.get(uid):
            i = st.session_state.q_index[uid]
            q, a, e = st.session_state.questions[uid][i]

            # ✅ CLEAN THE AI ANSWER (CRITICAL FIX)
            correct = a.strip().replace("*", "").replace("(", "").replace(")", "")
            correct = correct.split()[0]  # keeps only A / B / C / D

            st.markdown(f"### Question {i+1}/10")
            st.markdown(q)

            choice = st.radio(
                "Answer",
                ["A", "B", "C", "D"],
                key=f"{uid}_{i}"
            )

            if not st.session_state.answered[uid] and st.button("Submit"):
                st.session_state.answered[uid] = True

                if choice == correct:
                    st.balloons()
                    st.success("Correct! 🎉")
                    st.session_state.score += 1
                    st.session_state.points[uid] += 10
                else:
                    st.error(f"Wrong | Correct: {correct}")

            # ✅ SHOW EXPLANATION + NEXT BUTTON
            if st.session_state.answered[uid]:
                st.info(e)

                if st.button("Next ➡"):
                    st.session_state.q_index[uid] += 1
                    st.session_state.answered[uid] = False

                    # ✅ QUIZ FINISHED
                    if st.session_state.q_index[uid] == 10:
                        acc = st.session_state.score * 10
                        st.session_state.quiz_scores[uid].append(acc)

                        # subject-wise performance tracking
                        st.session_state.performance.setdefault(uid, {})
                        st.session_state.performance[uid].setdefault(subject, [])
                        st.session_state.performance[uid][subject].append(acc)

                        st.session_state.quiz_no[uid] += 1
                        st.session_state.quiz_active[uid] = False
                        st.success(f"🎯 Quiz completed | {acc}%")

                    st.rerun()

# ================= MOCK =================
elif st.session_state.page == "Mock":

    if st.session_state.quiz_no[uid] <= 5:
        st.warning("🔒 Complete 5 quizzes to unlock Mock Test")
        st.stop()

    st.subheader("🧪 Mock Test (Timed – Exam Mode ⏱)")

    MOCK_DURATION = 20 * 60  # 20 minutes

    if "mock_active" not in st.session_state:
        st.session_state.mock_active = False

    if not st.session_state.mock_active:
        if st.button("▶ Start Mock Test"):
            st.session_state.mock_questions = gen_mcq(
                subject=subject,
                topic=topic,
                diff="hard",
                n=20
            )
            st.session_state.mock_index = 0
            st.session_state.mock_score = 0
            st.session_state.mock_start_time = time.time()
            st.session_state.mock_active = True
            st.rerun()

    if st.session_state.mock_active:
        elapsed = int(time.time() - st.session_state.mock_start_time)
        remaining = MOCK_DURATION - elapsed

        mins, secs = divmod(max(0, remaining), 60)
        st.markdown(f"## ⏱ Time Left: {mins:02d}:{secs:02d}")

        if remaining <= 0:
            score = st.session_state.mock_score * 5
            st.error("⏰ Time’s up! Mock auto-submitted.")

            st.session_state.last_mock_analysis = {
                "total": 20,
                "correct": st.session_state.mock_score,
                "wrong": 20 - st.session_state.mock_score,
                "accuracy": round((st.session_state.mock_score / 20) * 100, 2),
                "subject": subject,
                "topic": topic
            }

            st.session_state.performance.setdefault(uid, {})
            st.session_state.performance[uid].setdefault(subject, [])
            st.session_state.performance[uid][subject].append(score)

            st.session_state.mock_active = False
            go("MockAnalysis")

        i = st.session_state.mock_index
        q, a, e = st.session_state.mock_questions[i]

        correct = a.strip().split()[0]

        st.markdown(f"### Question {i+1}/20")
        st.markdown(q)

        choice = st.radio(
            "Answer",
            ["A", "B", "C", "D"],
            key=f"mock_{uid}_{i}"
        )

        if st.button("Submit"):
            if choice == correct:
                st.success("✅ Correct")
                st.session_state.mock_score += 1
            else:
                st.error(f"❌ Wrong | Correct: {correct}")

            st.info(e)

            if st.button("Next ➡"):
                st.session_state.mock_index += 1

                if st.session_state.mock_index == 20:
                    score = st.session_state.mock_score * 5

                    st.session_state.last_mock_analysis = {
                        "total": 20,
                        "correct": st.session_state.mock_score,
                        "wrong": 20 - st.session_state.mock_score,
                        "accuracy": round((st.session_state.mock_score / 20) * 100, 2),
                        "subject": subject,
                        "topic": topic
                    }

                    st.session_state.performance.setdefault(uid, {})
                    st.session_state.performance[uid].setdefault(subject, [])
                    st.session_state.performance[uid][subject].append(score)

                    st.session_state.mock_active = False
                    go("MockAnalysis")

                st.rerun()


        
# ================= FINAL =================
elif st.session_state.page == "Final":

    if not st.session_state.mock_completed.get(uid, False):
        st.warning("🔒 Complete Mock Test to unlock Final Exam")
        st.stop()


    st.subheader("🎓 FINAL TEST (Board / Semester Mode ⏱)")

    FINAL_DURATION = 40 * 60  # ⏱ 40 minutes

    # INIT
    if "final_active" not in st.session_state:
        st.session_state.final_active = False

    # START FINAL
    if not st.session_state.final_active:
        if st.button("▶ Start Final Test"):
            st.session_state.final_questions = gen_mcq(
                subject=subject,
                topic=topic,
                diff="hard",
                n=40
            )
            st.session_state.final_index = 0
            st.session_state.final_score = 0
            st.session_state.final_start_time = time.time()
            st.session_state.final_active = True
            st.rerun()

    # RUN FINAL
    if st.session_state.final_active:
        elapsed = int(time.time() - st.session_state.final_start_time)
        remaining = FINAL_DURATION - elapsed

        mins, secs = divmod(max(0, remaining), 60)
        st.markdown(f"## ⏱ Time Left: {mins:02d}:{secs:02d}")

        # ⏰ TIME UP
        if remaining <= 0:
            score = round((st.session_state.final_score / 40) * 100, 2)
            st.error("⏰ Time’s up! Final auto-submitted.")

            st.session_state.last_final_analysis = {
                "total": 40,
                "correct": st.session_state.final_score,
                "wrong": 40 - st.session_state.final_score,
                "accuracy": score,
                "subject": subject,
                "topic": topic
            }

            st.session_state.performance.setdefault(uid, {})
            st.session_state.performance[uid].setdefault(subject, [])
            st.session_state.performance[uid][subject].append(score)

            st.session_state.final_active = False
            go("FinalAnalysis")

        # QUESTIONS
        i = st.session_state.final_index
        q, a, e = st.session_state.final_questions[i]

        correct = a.strip().split()[0]

        st.markdown(f"### Question {i+1}/40")
        st.markdown(q)

        choice = st.radio(
            "Answer",
            ["A", "B", "C", "D"],
            key=f"final_{uid}_{i}"
        )

        if st.button("Submit"):
            if choice == correct:
                st.success("✅ Correct")
                st.session_state.final_score += 1
            else:
                st.error(f"❌ Wrong | Correct: {correct}")

            st.info(e)

            if st.button("Next ➡"):
                st.session_state.final_index += 1

                # FINISH
                if st.session_state.final_index == 40:
                    score = round((st.session_state.final_score / 40) * 100, 2)

                    st.session_state.last_final_analysis = {
                        "total": 40,
                        "correct": st.session_state.final_score,
                        "wrong": 40 - st.session_state.final_score,
                        "accuracy": score,
                        "subject": subject,
                        "topic": topic
                    }

                    st.session_state.performance.setdefault(uid, {})
                    st.session_state.performance[uid].setdefault(subject, [])
                    st.session_state.performance[uid][subject].append(score)

                    st.session_state.final_active = False
                    go("FinalAnalysis")

                st.rerun()


# ================= LEADERBOARD =================
elif st.session_state.page=="Leaderboard":
    df=pd.DataFrame(
        sorted(st.session_state.points.items(),key=lambda x:x[1],reverse=True),
        columns=["Student","XP"]
    )
    st.table(df)