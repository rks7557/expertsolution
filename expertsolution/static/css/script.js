// Initialize AOS animations
document.addEventListener("DOMContentLoaded", function () {
  AOS.init({
    duration: 1000,
    once: true,
  });
});

// GST Calculator (optional if you want to move from inline to here)
const calculatorForm = document.getElementById("calculatorForm");
if (calculatorForm) {
  calculatorForm.addEventListener("submit", function (e) {
    e.preventDefault();
    const amount = parseFloat(document.getElementById("amount").value);
    const rate = parseFloat(document.getElementById("rate").value);

    if (isNaN(amount) || isNaN(rate)) {
      alert("Please enter valid amount and select GST rate.");
      return;
    }

    const gstAmount = (amount * rate) / 100;
    const totalAmount = amount + gstAmount;

    document.getElementById("gstAmount").textContent = gstAmount.toFixed(2);
    document.getElementById("totalAmount").textContent = totalAmount.toFixed(2);

    document.getElementById("result").style.display = "block";
  });
}

// Contact form submission (optional if you want to move from inline to here)
const contactForm = document.getElementById("contactForm");
if (contactForm) {
  contactForm.addEventListener("submit", function (e) {
    e.preventDefault();
    alert("Thank you for contacting us! We will get back to you shortly.");
    contactForm.reset();
  });
}
