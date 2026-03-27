
# =========================================================
# FILES
# =========================================================
USERS_FILE = "users.json"
SUPPORT_FILE = "support.json"
PINS_FILE = "epins.json"
WITHDRAWALS_FILE = "withdrawals.json"
TRANSACTIONS_FILE = "transactions.json"
TEAM_FILE = "team.json"

PACKAGE_RULES = {
    "Free": {
        "price": 0,
        "pins": 0,
        "direct_income": 0,
        "bonus_pool": 0,
        "company_profit": 0,
        "server_expense": 0,
        "level_income": {},
        "royalty_allowed": False,
        "referral_limit": 2,
        "withdrawal": False
    },
    "Starter": {
        "price": 99,
        "pins": 1,
        "direct_income": 30,
        "bonus_pool": 20,
        "company_profit": 40,
        "server_expense": 9,
        "level_income": {},
        "royalty_allowed": True,
        "referral_limit": None,
        "withdrawal": True
    },
    "Growth": {
        "price": 299,
        "pins": 3,
        "direct_income": 90,
        "bonus_pool": 60,
        "company_profit": 120,
        "server_expense": 29,
        "level_income": {
            1: 10
        },
        "royalty_allowed": True,
        "referral_limit": None,
        "withdrawal": True
    },
    "Pro": {
        "price": 599,
        "pins": 7,
        "direct_income": 180,
        "bonus_pool": 120,
        "company_profit": 240,
        "server_expense": 59,
        "level_income": {
            1: 10,
            2: 5,
            3: 3
        },
        "royalty_allowed": True,
        "referral_limit": None,
        "withdrawal": True
    }
}

# =========================================================
# DEFAULT SESSION STATE
# =========================================================

import streamlit as st
import json
import os
import random
import uuid
from datetime import datetime

# =========================================
# PAGE CONFIG
# =========================================

st.set_page_config(
    page_title="UniQueMarketing - Premium MLM Portal",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================
# SESSION INITIALIZE
# =========================================

if "page" not in st.session_state:
    st.session_state.page = "login"

if "user_logged_in" not in st.session_state:
    st.session_state.user_logged_in = False

if "admin_logged_in" not in st.session_state:
    st.session_state.admin_logged_in = False

if "user_data" not in st.session_state:
    st.session_state.user_data = None

# =========================================================
# FILE HELPERS
# =========================================================
def ensure_file(file_path, default_data):
    if not os.path.exists(file_path):
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(default_data, f, indent=4)

def load_json(file_path, default_data):
    ensure_file(file_path, default_data)
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return default_data

def save_json(file_path, data):
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def setup_files():


    default_users = [
        {
            "user_id": "UQM001",
            "username": "demo",
            "name": "Demo User",
            "email": "demo@example.com",
            "phone": "9000000001",
            "password": "user123",
            "status": "Active",
            "join_date": str(datetime.now().date()),
            "bank_name": "",
            "account_number": "",
            "ifsc": "",
            "account_holder": "",
            "package": "Starter",
            "wallet": 0,
            "wallet_balance": 0,
            "total_earned": 0,
            "direct_referrals": 0,
            "active_direct_referrals": 0,
            "royalty_eligible": False,
            "sponsor_id": "",
            "is_active": True
        },
        {
            "user_id": "UQM002",
            "username": "abe",
            "name": "Abe",
            "email": "abe@example.com",
            "phone": "9000000002",
            "password": "user123",
            "status": "Active",
            "join_date": str(datetime.now().date()),
            "bank_name": "",
            "account_number": "",
            "ifsc": "",
            "account_holder": "",
            "package": "None",
            "wallet": 0,
            "wallet_balance": 0,
            "total_earned": 0,
            "direct_referrals": 0,
            "active_direct_referrals": 0,
            "royalty_eligible": False,
            "sponsor_id": "",
            "is_active": True
        },
        {
            "user_id": "UQM003",
            "username": "user",
            "name": "User Account",
            "email": "user@gmail.com",
            "phone": "9000000003",
            "password": "user123",
            "status": "Active",
            "join_date": str(datetime.now().date()),
            "bank_name": "",
            "account_number": "",
            "ifsc": "",
            "account_holder": "",
            "package": "None",
            "wallet": 0,
            "wallet_balance": 0,
            "total_earned": 0,
            "direct_referrals": 0,
            "active_direct_referrals": 0,
            "royalty_eligible": False,
            "sponsor_id": "",
            "is_active": True
        }
    ]

    ensure_file(USERS_FILE, default_users)
    ensure_file(SUPPORT_FILE, [])
    ensure_file(PINS_FILE, [])
    ensure_file(WITHDRAWALS_FILE, [])
    ensure_file(TRANSACTIONS_FILE, [])
    ensure_file(TEAM_FILE, [])

setup_files()

# =========================================================
# DATA HELPERS
# =========================================================
def load_users():
    return load_json(USERS_FILE, [])

def load_epins():
    return load_json(PINS_FILE, [])

def save_users(users):
    save_json(USERS_FILE, users)

def generate_user_id(users):
    next_num = len(users) + 1
    return f"UQM{next_num:03d}"

def generate_user_id_uuid():
    return "USR" + uuid.uuid4().hex[:6].upper()


def register_user(name, sponsor_id=None, users_db=None):
    if users_db is None:
        users_db = []

    user_id = generate_user_id_uuid()
    new_user = {
        "user_id": user_id,
        "name": name,
        "package": "Free",
        "is_active": False,
        "status": "Inactive",
        "join_date": str(datetime.now().date()),
        "wallet": 0,
        "wallet_balance": 0,
        "total_earned": 0,
        "direct_referrals": 0,
        "active_direct_referrals": 0,
        "total_team": 0,
        "active_team": 0,
        "royalty_eligible": False,
        "sponsor_id": sponsor_id if sponsor_id else ""
    }
    users_db.append(new_user)
    return new_user


def generate_referral_link(user_id):
    return f"https://yourdomain.com/register?ref={user_id}"


def get_sponsor_from_ref(ref_code, users_db):
    sponsor = next((u for u in users_db if u.get("user_id") == ref_code), None)
    return sponsor.get("user_id") if sponsor else None


def save_epins(epins):
    save_json(PINS_FILE, epins)


def create_activation_pin(length=6):
    epins = load_epins()
    existing = {str(pin.get("pin_code", "")) for pin in epins if isinstance(pin, dict)}
    for _ in range(100):
        pin_code = "".join(random.choices("0123456789", k=length))
        if pin_code not in existing:
            epins.append({
                "pin_code": pin_code,
                "used": False,
                "used_by": "",
                "created_at": str(datetime.now()),
                "used_at": ""
            })
            save_epins(epins)
            return True, pin_code
    return False, "Could not generate unique PIN"

def get_wallet_balance(user):
    return user.get("wallet", user.get("wallet_balance", 0))

def set_wallet_balance(user, amount):
    user["wallet"] = amount
    user["wallet_balance"] = amount


def generate_pins_for_user(user_id, package_name, count):
    epins = load_epins()
    existing = {str(pin.get("pin_code", "")) for pin in epins if isinstance(pin, dict)}
    generated = []

    for _ in range(count):
        for _ in range(100):
            pin_code = "".join(random.choices("0123456789", k=6))
            if pin_code not in existing:
                existing.add(pin_code)
                epins.append({
                    "pin_code": pin_code,
                    "used": False,
                    "used_by": "",
                    "created_for": user_id,
                    "package": package_name,
                    "created_at": str(datetime.now()),
                    "used_at": ""
                })
                generated.append(pin_code)
                break

    save_epins(epins)
    return generated


def activate_user(user, package_name):
    rules = PACKAGE_RULES.get(package_name, PACKAGE_RULES["Free"])

    user["package"] = package_name
    user["is_active"] = package_name != "Free"
    user["status"] = "Active"

    if rules["pins"] > 0:
        generate_pins_for_user(user["user_id"], package_name, rules["pins"])


def can_refer(user):
    if user.get("package") == "Free":
        return user.get("direct_referrals", 0) < 2
    return True


def give_direct_income(sponsor, package_name):
    amount = PACKAGE_RULES.get(package_name, PACKAGE_RULES["Free"])["direct_income"]
    amount = amount or 0
    balance = get_wallet_balance(sponsor) + amount
    set_wallet_balance(sponsor, balance)
    sponsor["total_earned"] = sponsor.get("total_earned", 0) + amount


def get_upline(joined_user_id, users_db, level):
    current = next((u for u in users_db if u.get("user_id") == joined_user_id), None)
    for _ in range(level):
        if current is None:
            return None
        sponsor_id = current.get("sponsor_id", "")
        current = next((u for u in users_db if u.get("user_id") == sponsor_id), None)
    return current


def give_level_income(joined_user, package_name, users_db):
    level_rules = PACKAGE_RULES.get(package_name, PACKAGE_RULES["Free"]).get("level_income", {})

    for level, income in level_rules.items():
        upline = get_upline(joined_user.get("user_id"), users_db, level)
        if upline and upline.get("is_active"):
            balance = get_wallet_balance(upline) + income
            set_wallet_balance(upline, balance)
            upline["total_earned"] = upline.get("total_earned", 0) + income


system_bonus_pool = 0

def add_to_bonus_pool(package_name):
    global system_bonus_pool
    system_bonus_pool += PACKAGE_RULES.get(package_name, PACKAGE_RULES["Free"]).get("bonus_pool", 0)


def update_royalty_eligibility(user):
    if (
        user.get("is_active")
        and user.get("package") in ["Starter", "Growth", "Pro"]
        and user.get("active_direct_referrals", 0) >= 2
    ):
        user["royalty_eligible"] = True
    else:
        user["royalty_eligible"] = False


def distribute_royalty(users_db):
    global system_bonus_pool

    eligible_users = [
        u for u in users_db
        if u.get("royalty_eligible") is True
    ]

    if not eligible_users:
        return

    share = system_bonus_pool / len(eligible_users)
    for user in eligible_users:
        balance = get_wallet_balance(user) + share
        set_wallet_balance(user, balance)
        user["total_earned"] = user.get("total_earned", 0) + share

    system_bonus_pool = 0


def process_new_activation(new_user, package_name, sponsor, users_db):
    activate_user(new_user, package_name)

    if sponsor and sponsor.get("is_active"):
        sponsor["direct_referrals"] = sponsor.get("direct_referrals", 0) + 1
        sponsor["active_direct_referrals"] = sponsor.get("active_direct_referrals", 0) + 1

        give_direct_income(sponsor, package_name)
        give_level_income(new_user, package_name, users_db)
        update_royalty_eligibility(sponsor)

    add_to_bonus_pool(package_name)


def activate_account(username, pin_code):
    users = load_users()
    epins = load_epins()
    pin_code = str(pin_code).strip()

    pin = next((pin for pin in epins if str(pin.get("pin_code", "")).strip() == pin_code), None)
    if not pin:
        return False, "Invalid PIN"

    if pin.get("used", False):
        return False, "PIN already used"

    user = None
    for u in users:
        if not isinstance(u, dict):
            continue
        if str(u.get("username", "")).strip() == username or str(u.get("user_id", "")).strip() == username:
            user = u
            break

    if not user:
        return False, "User not found"

    if user.get("status") == "Active":
        return False, "Account already active"

    sponsor = next((u for u in users if u.get("user_id") == user.get("sponsor_id")), None)
    process_new_activation(user, user.get("package", "Free"), sponsor, users)

    pin["used"] = True
    pin["used_by"] = user.get("user_id", "")
    pin["used_at"] = str(datetime.now())

    save_users(users)
    save_epins(epins)
    return True, "Account activated successfully"

def find_user(identifier, password):
    users = load_users()

    identifier = str(identifier).strip()
    password = str(password).strip()

    if not isinstance(users, list):
        return None

    for user in users:
        if not isinstance(user, dict):
            continue

        user_id = str(user.get("user_id", "")).strip()
        username = str(user.get("username", "")).strip()
        email = str(user.get("email", "")).strip()
        phone = str(user.get("phone", "")).strip()
        user_password = str(user.get("password", "")).strip()

        if identifier in [user_id, username, email, phone] and user_password == password:
            return user

    return None


def update_current_user(updated_user):
    users = load_users()
    for i, u in enumerate(users):
        if u["user_id"] == updated_user["user_id"]:
            users[i] = updated_user
            break
    save_users(users)
    st.session_state.user_data = updated_user

# =========================================================
# GLOBAL CSS
# =========================================================
def inject_css():
    st.markdown("""
<style>
:root {
    --primary: #6d5dfc;
    --secondary: #8b5cf6;
    --dark1: #0b1220;
    --dark2: #16213e;
    --dark3: #1e293b;
}

/* Full app background + default text */
html, body, [data-testid="stAppViewContainer"] {
    background: #ffffff !important;
    color: #111827 !important;
}

/* All general text */
p, label, span, div, h1, h2, h3, h4, h5, h6 {
    color: #111827 !important;
}

/* Input + text fields */
input, textarea {
    color: #111827 !important;
    background-color: #ffffff !important;
    -webkit-text-fill-color: #111827 !important;
}

/* Streamlit text input wrapper */
[data-baseweb="input"] input {
    color: #111827 !important;
    background-color: #ffffff !important;
    -webkit-text-fill-color: #111827 !important;
}

/* Placeholder */
input::placeholder,
textarea::placeholder {
    color: #6b7280 !important;
    opacity: 1 !important;
}

/* Buttons */
button {
    color: #111827 !important;
}

/* Package cards */
.package-card {
    border: 1px solid #e5e7eb;
    border-radius: 20px;
    padding: 24px;
    background: #ffffff;
    transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
    margin-bottom: 16px;
}

.package-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 18px 45px rgba(15, 23, 42, 0.08);
}

.package-selected {
    background: #eef2ff;
    border-color: #6366f1;
}

.package-icon {
    font-size: 42px;
    margin-bottom: 16px;
}

.package-name {
    font-size: 20px;
    font-weight: 700;
    margin-bottom: 8px;
}

.package-price {
    font-size: 30px;
    font-weight: 800;
    margin-bottom: 10px;
}

.package-desc {
    color: #475569;
    margin-bottom: 18px;
}

.package-badge {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    background: #f3e8ff;
    color: #7c3aed;
    padding: 6px 14px;
    border-radius: 999px;
    font-size: 12px;
    font-weight: 700;
    margin-bottom: 12px;
}

/* Tabs / radio / misc text */
.stMarkdown, .stText, .stCaption, .st-emotion-cache-ue6h4q {
    color: #111827 !important;
}
</style>
""", unsafe_allow_html=True)

inject_css()

# =========================================================
# UI HELPERS
# =========================================================
def show_top_banner(text):
    st.markdown(f'<div class="banner">{text}</div>', unsafe_allow_html=True)

def render_sidebar():
    user = st.session_state.user_data

    st.sidebar.markdown("""
    <div class="brand-box">
        <div class="brand-title">💼 UniQueMarketing</div>
        <div class="brand-sub">Premium MLM Portal</div>
    </div>
    """, unsafe_allow_html=True)

    st.sidebar.markdown(f"""
    <div class="user-box">
        <div class="user-small">LOGGED IN AS</div>
        <div class="user-name">{user.get("name", "User")}</div>
        <div class="user-id">{user.get("user_id", "")}</div>
    </div>
    """, unsafe_allow_html=True)

    st.sidebar.markdown("### Navigation")

    if user and user.get("status") != "Active":
        menu_items = [
            ("activate_account", "🔑 Activate Account"),
        ]
    else:
        menu_items = [
            ("dashboard", "🏠 Dashboard"),
            ("profile", "👤 Profile"),
            ("transfer_epin", "🎫 Transfer E-Pin"),
            ("withdraw", "💸 Withdraw"),
            ("income_reports", "📊 Income Reports"),
            ("team", "👥 My Team"),
            ("support", "🆘 Support"),
        ]

    for key, label in menu_items:
        if st.sidebar.button(label, key=f"menu_{key}", use_container_width=True):
            st.session_state.page = key
            st.rerun()

    st.sidebar.markdown("<br>", unsafe_allow_html=True)

    if st.sidebar.button("🚪 Sign Out", use_container_width=True):
        st.session_state.user_logged_in = False
        st.session_state.user_data = None
        st.session_state.page = "login"
        st.rerun()

# =========================================================
# AUTH PAGES
# =========================================================
def show_login():
    st.markdown('<div class="login-wrap">', unsafe_allow_html=True)
    st.markdown('<div class="login-title">💼 UniQueMarketing</div>', unsafe_allow_html=True)
    st.markdown('<div class="login-sub">Premium MLM Portal Login</div>', unsafe_allow_html=True)

    identifier = st.text_input("User ID / Username / Email / Phone")
    password = st.text_input("Password", type="password")

    c1, c2, c3 = st.columns(3)

    with c1:
        if st.button("Login", use_container_width=True):
            user = find_user(identifier, password)
            if user:
                st.session_state.user_logged_in = True
                st.session_state.admin_logged_in = False
                st.session_state.user_data = user
                st.session_state.page = "dashboard"
                st.success("Login successful")
                st.rerun()
            else:
                st.error("Invalid login credentials")

    with c2:
        if st.button("Register", use_container_width=True):
            st.session_state.page = "register"
            st.rerun()

    with c3:
        if st.button("Admin Login", use_container_width=True):
            st.session_state.page = "admin_login"
            st.rerun()

    st.markdown('<div class="small-note">Demo User ID: UQM003 | Password: user123</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

def show_register():
    st.markdown('<div class="login-wrap">', unsafe_allow_html=True)
    st.markdown('<div class="login-title">📝 Register</div>', unsafe_allow_html=True)
    st.markdown('<div class="login-sub">Create your new member account</div>', unsafe_allow_html=True)

    query_params = st.experimental_get_query_params()
    default_sponsor = query_params.get("ref", [""])[0] if query_params.get("ref") else ""

    name = st.text_input("Full Name")
    username = st.text_input("Username")
    email = st.text_input("Email")
    phone = st.text_input("Phone")
    password = st.text_input("Password", type="password")
    sponsor_id = st.text_input("Sponsor User ID (optional)", value=default_sponsor)
    package = st.selectbox("Select Package", list(PACKAGE_RULES.keys()), index=list(PACKAGE_RULES.keys()).index("Free"))

    c1, c2 = st.columns(2)

    with c1:
        if st.button("Create Account", use_container_width=True):
            users = load_users()

            for u in users:
                if u["username"] == username:
                    st.error("Username already exists")
                    st.markdown('</div>', unsafe_allow_html=True)
                    return
                if u["email"] == email:
                    st.error("Email already exists")
                    st.markdown('</div>', unsafe_allow_html=True)
                    return
                if u["phone"] == phone:
                    st.error("Phone already exists")
                    st.markdown('</div>', unsafe_allow_html=True)
                    return

            if not name or not username or not email or not phone or not password:
                st.error("Please fill all fields")
            else:
                sponsor_value = sponsor_id.strip()
                if sponsor_value:
                    sponsor = next((u for u in users if str(u.get("user_id", "")).strip() == sponsor_value), None)
                    if not sponsor:
                        st.error("Sponsor User ID not found")
                        st.markdown('</div>', unsafe_allow_html=True)
                        return
                else:
                    sponsor = None

                new_user = {
                    "user_id": generate_user_id(users),
                    "username": username,
                    "name": name,
                    "email": email,
                    "phone": phone,
                    "password": password,
                    "status": "Inactive",
                    "join_date": str(datetime.now().date()),
                    "bank_name": "",
                    "account_number": "",
                    "ifsc": "",
                    "account_holder": "",
                    "package": package,
                    "wallet": 0,
                    "wallet_balance": 0,
                    "total_earned": 0,
                    "direct_referrals": 0,
                    "active_direct_referrals": 0,
                    "royalty_eligible": False,
                    "sponsor_id": sponsor_value if sponsor else "",
                    "is_active": False
                }
                users.append(new_user)
                save_users(users)
                st.success(f"Account created successfully. Your User ID is {new_user['user_id']}")
                if sponsor:
                    st.info(f"Sponsor registered as {sponsor_value}")
                st.info("Your account is currently inactive. Ask admin for an activation PIN, then login to activate.")

    with c2:
        if st.button("Back to Login", use_container_width=True):
            st.session_state.page = "login"
            st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

def show_admin_login():
    st.markdown('<div class="login-wrap">', unsafe_allow_html=True)
    st.markdown('<div class="login-title">🛠 Admin Login</div>', unsafe_allow_html=True)
    st.markdown('<div class="login-sub">Portal management access</div>', unsafe_allow_html=True)

    admin_user = st.text_input("Admin Username", key="admin_user")
    admin_pass = st.text_input("Admin Password", type="password", key="admin_pass")

    c1, c2 = st.columns(2)

    with c1:
        if st.button("Login as Admin", use_container_width=True):
            if admin_user == "admin" and admin_pass == "admin123":
                st.session_state.admin_logged_in = True
                st.session_state.user_logged_in = False
                st.session_state.page = "admin_dashboard"
                st.success("Admin login successful")
                st.rerun()
            else:
                st.error("Invalid admin credentials")

    with c2:
        if st.button("Back", use_container_width=True):
            st.session_state.page = "login"
            st.rerun()

    st.markdown('<div class="small-note">Admin Username: admin | Password: admin123</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# =========================================================
# USER PAGES
# =========================================================
def show_dashboard():
    show_top_banner("🏠 Dashboard")

    st.markdown('<div class="section-title">📦 Business Packages</div>', unsafe_allow_html=True)

    package_icons = {
        "Free": "🆓",
        "Starter": "🌟",
        "Growth": "📈",
        "Pro": "👑"
    }

    packages = []
    for package_name, rule in PACKAGE_RULES.items():
        price = f"₹{rule['price']}"
        desc = f"Pins: {rule['pins']} · Direct: ₹{rule['direct_income']} · Withdraw: {'Yes' if rule['withdrawal'] else 'No'}"
        packages.append((package_icons.get(package_name, "🔹"), price, package_name, desc))

    cols = st.columns(4)
    current_package = st.session_state.user_data.get("package", "Free")
    for col, pkg in zip(cols, packages):
        icon, price, title, desc = pkg
        is_current = current_package == title
        card_classes = "package-card package-selected" if is_current else "package-card"
        badge_html = "<div class='package-badge'>Most Popular</div>" if title == "Pro" else ""
        html = (
            f'<div class="{card_classes}">'
            f'<div class="package-icon">{icon}</div>'
            f'{badge_html}'
            f'<div class="package-name">{title}</div>'
            f'<div class="package-price">{price}</div>'
            f'<div class="package-desc">{desc}</div>'
            '</div>'
        )

        with col:
            st.markdown(html, unsafe_allow_html=True)
            action_label = "Current Package" if is_current else "Select Package"
            if st.button(action_label, key=f"activate_{title}", use_container_width=True):
                if not is_current:
                    user = st.session_state.user_data
                    user["package"] = title
                    update_current_user(user)
                    st.success(f"Package changed to {title}")
                    st.experimental_rerun()

    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown('<div class="section-title">🔗 Your Referral Link</div>', unsafe_allow_html=True)
    user = st.session_state.user_data
    referral_link = generate_referral_link(user.get("user_id", ""))
    st.code(referral_link, language="text")

    st.markdown('<div class="section-title">📈 Quick Statistics</div>', unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    user = st.session_state.user_data

    with c1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">👥 Team Members</div>
            <div class="metric-value">0</div>
            <div class="metric-sub">0 Active</div>
        </div>
        """, unsafe_allow_html=True)

    current_package = user.get("package", "Free")
    st.markdown(f"<div style='margin-top:16px; font-weight:600;'>Current Package: {current_package}</div>", unsafe_allow_html=True)

    with c2:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">📊 Total Transactions</div>
            <div class="metric-value">0</div>
            <div class="metric-sub">This Month</div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">📅 Member Since</div>
            <div class="metric-value">{user.get("join_date","-")}</div>
            <div class="metric-sub">Account Created</div>
        </div>
        """, unsafe_allow_html=True)

def show_profile():
    user = st.session_state.user_data
    show_top_banner("👤 Your Profile")

    c1, c2 = st.columns(2)

    with c1:
        st.markdown('<div class="card"><h2>Personal Information</h2></div>', unsafe_allow_html=True)
        name = st.text_input("Full Name", value=user.get("name", ""), key="profile_name")
        user_id = st.text_input("User ID", value=user.get("user_id", ""), disabled=True)
        email = st.text_input("Email", value=user.get("email", ""), key="profile_email")
        phone = st.text_input("Phone", value=user.get("phone", ""), key="profile_phone")
        status = st.text_input("Account Status", value=user.get("status", "Active"), disabled=True)
        join_date = st.text_input("Join Date", value=user.get("join_date", ""), disabled=True)

    with c2:
        st.markdown('<div class="card"><h2>Bank Details</h2></div>', unsafe_allow_html=True)
        bank_name = st.text_input("Bank Name", value=user.get("bank_name", ""), key="bank_name")
        account_number = st.text_input("Account Number", value=user.get("account_number", ""), key="account_number")
        ifsc = st.text_input("IFSC Code", value=user.get("ifsc", ""), key="ifsc")
        account_holder = st.text_input("Account Holder Name", value=user.get("account_holder", ""), key="account_holder")

        if st.button("💾 Save Bank Details", use_container_width=True):
            user["name"] = name
            user["email"] = email
            user["phone"] = phone
            user["bank_name"] = bank_name
            user["account_number"] = account_number
            user["ifsc"] = ifsc
            user["account_holder"] = account_holder
            update_current_user(user)
            st.success("Profile updated successfully")

def show_transfer_epin():
    show_top_banner("🎫 Transfer E-Pin")

    st.markdown('<div class="section-title">Transfer E-Pin to another member</div>', unsafe_allow_html=True)

    recipient = st.text_input("Recipient User ID")
    pin_code = st.text_input("E-Pin Code")

    if st.button("Transfer E-Pin", use_container_width=True):
        if recipient and pin_code:
            st.success(f"E-Pin {pin_code} transferred to {recipient}")
        else:
            st.error("Please enter recipient ID and E-Pin")


def show_activate_account():
    user = st.session_state.user_data
    show_top_banner("🔑 Activate Your Account")

    st.markdown('<div class="section-title">Enter your activation PIN to activate your account.</div>', unsafe_allow_html=True)

    pin_code = st.text_input("Activation PIN")

    if st.button("Activate Account", use_container_width=True):
        if not pin_code:
            st.error("Please enter your activation PIN")
            return

        ok, msg = activate_account(user.get("username", ""), pin_code)
        if ok:
            user["status"] = "Active"
            update_current_user(user)
            st.success(msg)
            st.experimental_rerun()
        else:
            st.error(msg)


def show_withdraw():
    user = st.session_state.user_data
    show_top_banner("💸 Withdraw Funds")

    st.markdown('<div class="section-title">Request Withdrawal</div>', unsafe_allow_html=True)

    st.info(f"Available Wallet Balance: ₹{user.get('wallet', 0)}")

    amount = st.number_input("Enter Withdrawal Amount", min_value=0, step=100)

    if st.button("Submit Withdrawal Request", use_container_width=True):
        if amount <= 0:
            st.error("Enter a valid amount")
            return

        if amount > user.get("wallet", 0):
            st.error("Insufficient wallet balance")
            return

        withdrawals = load_json(WITHDRAWALS_FILE, [])
        withdrawals.append({
            "user_id": user["user_id"],
            "name": user["name"],
            "amount": amount,
            "status": "Pending",
            "date": str(datetime.now())
        })
        save_json(WITHDRAWALS_FILE, withdrawals)
        st.success("Withdrawal request submitted successfully")

def show_income_reports():
    show_top_banner("📊 Income Reports")

    st.markdown('<div class="section-title">Income Summary</div>', unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("Direct Income", "₹0")
    with c2:
        st.metric("Level Income", "₹0")
    with c3:
        st.metric("Total Income", "₹0")

    st.markdown('<div class="section-title">Recent Transactions</div>', unsafe_allow_html=True)
    transactions = load_json(TRANSACTIONS_FILE, [])

    if transactions:
        st.dataframe(transactions, use_container_width=True)
    else:
        st.info("No transactions available")

def show_team():
    show_top_banner("👥 My Team")

    st.markdown('<div class="section-title">Team Overview</div>', unsafe_allow_html=True)

    team_data = load_json(TEAM_FILE, [])
    if team_data:
        st.dataframe(team_data, use_container_width=True)
    else:
        st.info("No team members added yet")

def show_support():
    user = st.session_state.user_data
    show_top_banner("🆘 Support & Help")

    subject = st.text_input("Subject")
    message = st.text_area("Describe your issue")

    if st.button("Submit Support Ticket", use_container_width=True):
        if subject and message:
            tickets = load_json(SUPPORT_FILE, [])
            tickets.append({
                "user_id": user["user_id"],
                "name": user["name"],
                "subject": subject,
                "message": message,
                "date": str(datetime.now()),
                "status": "Open"
            })
            save_json(SUPPORT_FILE, tickets)
            st.success("Support ticket submitted successfully")
        else:
            st.error("Please fill subject and message")

# =========================================================
# ADMIN PAGE
# =========================================================
def show_admin_dashboard():
    st.title("🛠 Admin Dashboard")
    st.success("Admin panel active")

    users = load_users()
    withdrawals = load_json(WITHDRAWALS_FILE, [])
    tickets = load_json(SUPPORT_FILE, [])
    epins = load_epins()

    active_users = [u for u in users if isinstance(u, dict) and u.get("status") == "Active"]
    inactive_users = [u for u in users if isinstance(u, dict) and u.get("status") != "Active"]
    unused_pins = [p for p in epins if isinstance(p, dict) and not p.get("used", False)]

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.metric("Total Users", len(users))
    with c2:
        st.metric("Active Users", len(active_users))
    with c3:
        st.metric("Inactive Users", len(inactive_users))
    with c4:
        st.metric("Unused PINs", len(unused_pins))

    st.markdown("---")
    st.subheader("User Access Control")
    col1, col2 = st.columns([2, 1])

    with col1:
        if inactive_users:
            user_options = [f"{u.get('name', '')} ({u.get('username','')}) - {u.get('user_id','')}" for u in inactive_users]
            selected_user = st.selectbox("Select inactive user to activate", user_options)
        else:
            selected_user = None
            st.info("No inactive users available for activation.")

        pin_code = st.text_input("Activation PIN for selected user")

        if st.button("Activate Selected User", use_container_width=True):
            if not selected_user:
                st.error("No inactive user selected")
            elif not pin_code:
                st.error("Please enter an activation PIN")
            else:
                selected_username = selected_user.split("(")[1].split(")")[0].strip()
                ok, msg = activate_account(selected_username, pin_code)
                if ok:
                    st.success(msg)
                    users = load_users()
                    inactive_users = [u for u in users if isinstance(u, dict) and u.get("status") != "Active"]
                    epins = load_epins()
                else:
                    st.error(msg)

    with col2:
        if st.button("Generate Activation PIN", use_container_width=True):
            ok, msg = create_activation_pin()
            if ok:
                st.success(f"New PIN generated: {msg}")
            else:
                st.error(msg)

        st.markdown("#### Latest activation pins")
        if unused_pins:
            pin_table = [{"PIN": p.get("pin_code"), "Used": p.get("used"), "Used By": p.get("used_by"), "Created At": p.get("created_at")} for p in unused_pins]
            st.dataframe(pin_table, use_container_width=True)
        else:
            st.info("No unused activation PINs available.")

    st.markdown("---")
    st.markdown("## Users List")
    if users:
        st.dataframe(users, use_container_width=True)
    else:
        st.info("No users found")

    st.markdown("## Withdrawal Requests")
    if withdrawals:
        st.dataframe(withdrawals, use_container_width=True)
    else:
        st.info("No withdrawal requests")

    st.markdown("## Support Tickets")
    if tickets:
        st.dataframe(tickets, use_container_width=True)
    else:
        st.info("No support tickets")

    if st.button("Logout Admin", use_container_width=True):
        st.session_state.admin_logged_in = False
        st.session_state.page = "login"
        st.rerun()

# =========================================================
# USER PORTAL ROUTER
# =========================================================
def show_user_portal():
    render_sidebar()

    user = st.session_state.user_data
    if user and user.get("status") != "Active":
        show_activate_account()
        return

    current_page = st.session_state.page

    if current_page == "dashboard":
        show_dashboard()
    elif current_page == "profile":
        show_profile()
    elif current_page == "transfer_epin":
        show_transfer_epin()
    elif current_page == "withdraw":
        show_withdraw()
    elif current_page == "income_reports":
        show_income_reports()
    elif current_page == "team":
        show_team()
    elif current_page == "support":
        show_support()
    else:
        show_dashboard()

# =========================================================
# MAIN ROUTING
# =========================================================
if st.session_state.admin_logged_in:
    show_admin_dashboard()

elif st.session_state.user_logged_in:
    show_user_portal()

else:
    if st.session_state.page == "admin_login":
        show_admin_login()
    elif st.session_state.page == "register":
        show_register()
    else:
        show_login()