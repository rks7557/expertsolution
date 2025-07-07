// AOS Initialization (already present in HTML but just in case)
document.addEventListener("DOMContentLoaded", function () {
  AOS.init({ duration: 1000, once: true });

  // Newsletter form handler
  const newsletterForm = document.getElementById("newsletter-form");
  if (newsletterForm) {
    newsletterForm.addEventListener("submit", function (e) {
      e.preventDefault();
      alert("Thank you for subscribing!");
      newsletterForm.reset();
    });
  }

  // Contact form handler
  const contactForm = document.getElementById("contactForm");
  if (contactForm) {
    contactForm.addEventListener("submit", function (e) {
      e.preventDefault();
      alert("Message sent! We'll contact you soon.");
      contactForm.reset();
    });
  }

  // Language switcher
  const languageSwitch = document.getElementById("languageSwitch");
  if (languageSwitch) {
    languageSwitch.addEventListener("change", function () {
      alert("Language switch feature coming soon. Selected: " + this.value);
    });
  }
});

// GST Calculator logic (also included in HTML inline, optional to move here)
function calculateGST() {
  const amount = parseFloat(document.getElementById("amount").value);
  const rate = parseFloat(document.getElementById("gstRate").value);
  if (!amount || isNaN(amount)) return alert("Enter a valid amount");
  const gst = amount * (rate / 100);
  const total = amount + gst;
  document.getElementById("gstResult").innerText =
    `GST: ₹${gst.toFixed(2)}, Total: ₹${total.toFixed(2)}`;
}
