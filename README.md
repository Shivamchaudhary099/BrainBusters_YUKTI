<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Medical HealthCare</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<!-- Google Font -->
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap" rel="stylesheet">

<!-- Font Awesome Icons -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">

<style>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Poppins', sans-serif;
}

body {
    background: linear-gradient(120deg, #e3f2fd, #ffffff);
    color: #333;
}

/* Header */
header {
    background: linear-gradient(135deg, #0077b6, #00b4d8);
    padding: 18px;
    text-align: center;
    color: white;
    font-size: 26px;
    font-weight: 700;
    letter-spacing: 1px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
}

/* Hero Section */
.hero {
    height: 80vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center; 
    padding: 20px;
}

.hero h1 {
    font-size: 42px;
    margin-bottom: 10px;
    color: #0077b6;
}

.hero p {
    margin-bottom: 20px;
    font-size: 18px;
}

/* Search Box */
.search-box {
    width: 100%;
    max-width: 520px;
    display: flex;
    background: white;
    border-radius: 50px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.1);
    overflow: hidden;
    margin-bottom: 20px;
}

.search-box input {
    flex: 1;
    padding: 15px 20px;
    border: none;
    outline: none;
    font-size: 16px;
}

.search-box button {
    padding: 15px 25px;
    border: none;
    background: linear-gradient(135deg, #0077b6, #023e8a);
    color: white;
    cursor: pointer;
    font-weight: 600;
    transition: 0.3s;
}

.search-box button:hover {
    background: linear-gradient(135deg, #023e8a, #0077b6);
}

/* Hero Buttons */
.hero-btn {
    padding: 12px 22px;
    margin: 8px;
    border: none;
    border-radius: 25px;
    background: linear-gradient(135deg, #0077b6, #00b4d8);
    color: white;
    font-size: 16px;
    cursor: pointer;
    transition: 0.3s;
}

.hero-btn:hover {
    transform: translateY(-3px);
}

/* Services Section */
.services {
    padding: 70px 20px;
    text-align: center;
}

.services h2 {
    margin-bottom: 40px;
    color: #0077b6;
    font-size: 32px;
}

/* Cards */
.cards {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 25px;
}

.card {
    background: white;
    padding: 30px 20px;
    width: 260px;
    border-radius: 16px;
    box-shadow: 0 8px 25px rgba(0,0,0,0.08);
    transition: 0.4s;
}

.card:hover {
    transform: translateY(-10px);
}

.card i {
    color: #0077b6;
    margin-bottom: 15px;
}

.card h3 {
    margin-bottom: 10px;
    color: #0077b6;
}

/* Emergency Floating Button */
.emergency-btn {
    position: fixed;
    bottom: 20px;
    right: 20px;
    background: red;
    color: white;
    padding: 18px;
    border-radius: 50%;
    font-size: 22px;
    box-shadow: 0 5px 20px rgba(0,0,0,0.3);
    text-decoration: none;
    animation: pulse 1.5s infinite;
}

@keyframes pulse {
    0% { transform: scale(1); }
    50% { transform: scale(1.1); }
    100% { transform: scale(1); }
}

/* Footer */
footer {
    background: linear-gradient(135deg, #0077b6, #023e8a);
    color: white;
    text-align: center;
    padding: 18px;
    margin-top: 40px;
    font-size: 14px;
}

/* Responsive */
@media(max-width: 768px) {
    .hero h1 {
        font-size: 28px;
    }
    .cards {
        flex-direction: column;
        align-items: center;
    }
}
</style>
</head>

<body>

<header>
    🏥 Medical HealthCare
</header>

<section class="hero">
    <h1>Your Health, Our Priority</h1>
    <p>Find doctors, services and instant emergency support in one place.</p>

    <div class="search-box">
        <input type="text" placeholder="Search doctors, services, diseases...">
        <button><i class="fa fa-search"></i> Search</button>
    </div>

    <div>
        <button class="hero-btn">Book Appointment</button>
        <button class="hero-btn">Emergency Help</button>
    </div>
</section>

<section class="services">
    <h2>Our Services</h2>
    <div class="cards">
        <div class="card">
            <i class="fa-solid fa-stethoscope fa-2x"></i>
            <h3>General Checkup</h3>
            <p>Comprehensive health checkups for all ages.</p>
        </div>
        <div class="card">
            <i class="fa-solid fa-truck-medical fa-2x"></i>
            <h3>Emergency Care</h3>
            <p>24/7 emergency medical support.</p>
        </div>
        <div class="card">
            <i class="fa-solid fa-user-doctor fa-2x"></i>
            <h3>Specialist Doctors</h3>
            <p>Experienced professionals in every field.</p>
        </div>
        <div class="card">
            <i class="fa-solid fa-pills fa-2x"></i>
            <h3>Online Pharmacy</h3>
            <p>Order medicines with fast home delivery.</p>
        </div>
    </div>
</section>

<section class="services">
    <h2>Our Top Doctors</h2>
    <div class="cards">
        <div class="card">
            <h3>Dr. Rahul Sharma</h3>
            <p>Cardiologist</p>
        </div>
        <div class="card">
            <h3>Dr. Priya Verma</h3>
            <p>Neurologist</p>
        </div>
        <div class="card">
            <h3>Dr. Aman Singh</h3>
            <p>Orthopedic Specialist</p>
        </div>
    </div>
</section>

<section class="services">
    <h2>Contact Us</h2>
    <p>Email: support@medicalhealthcare.com</p>
    <p>Phone: +91 98765 43210</p>
    <p>Location: Prayagraj, India</p>
</section>

<a href="tel:102" class="emergency-btn">
    <i class="fa-solid fa-phone"></i>
</a>

<footer>
    © 2026 Medical HealthCare | All Rights Reserved
</footer>

</body>
</html>

On Sat, 14 Feb 2026, 7:45 pm Shivam, <shivamchaudhary18109@gmail.com> wrote:
