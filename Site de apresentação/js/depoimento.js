// Sample testimonials data
const testimonials = [
    {
        id: 1,
        name: "Maria Clara",
        profession: "Analista de Marketing",
        testimonial: "Consegui 3 entrevistas em uma semana usando o sistema! A análise da IA me mostrou habilidades que nem sabia que tinha.",
        rating: 5,
        avatar: "MC"
    }
];

// Mobile Menu Toggle
document.querySelector('.mobile-menu').addEventListener('click', function() {
    const navLinks = document.querySelector('.nav-links');
    navLinks.style.display = navLinks.style.display === 'flex' ? 'none' : 'flex';
});

// Rating System
const ratingStars = document.querySelectorAll('.rating-star');
const ratingInput = document.getElementById('rating');

ratingStars.forEach(star => {
    star.addEventListener('click', function() {
        const value = this.getAttribute('data-value');
        ratingInput.value = value;
        
        // Update star appearance
        ratingStars.forEach(s => {
            if (s.getAttribute('data-value') <= value) {
                s.classList.add('active');
            } else {
                s.classList.remove('active');
            }
        });
    });
    
    // Hover effect
    star.addEventListener('mouseover', function() {
        const value = this.getAttribute('data-value');
        ratingStars.forEach(s => {
            if (s.getAttribute('data-value') <= value) {
                s.style.color = '#ffc107';
            } else {
                s.style.color = '#555';
            }
        });
    });
    
    star.addEventListener('mouseout', function() {
        const currentValue = ratingInput.value;
        ratingStars.forEach(s => {
            if (s.getAttribute('data-value') <= currentValue) {
                s.style.color = '#ffc107';
            } else {
                s.style.color = '#555';
            }
        });
    });
});


// Function to display testimonials
function displayTestimonials() {
    const container = document.getElementById('testimonials-container');
    container.innerHTML = '';
    
    testimonials.forEach(testimonial => {
        const stars = '★'.repeat(testimonial.rating) + '☆'.repeat(5 - testimonial.rating);
        
        const testimonialHTML = `
            <div class="testimonial-card" style="animation: fadeInUp 0.5s ease forwards;">
                <p class="testimonial-text">${testimonial.testimonial}</p>
                <div class="testimonial-author">
                    <div class="author-avatar">${testimonial.avatar}</div>
                    <div class="author-info">
                        <h4>${testimonial.name}</h4>
                        <p>${testimonial.profession}</p>
                        <div class="testimonial-rating">${stars}</div>
                    </div>
                </div>
            </div>
        `;
        
        container.innerHTML += testimonialHTML;
    });
}

// Form submission
document.getElementById('testimonial-form').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const name = document.getElementById('name').value;
    const profession = document.getElementById('profession').value;
    const rating = document.getElementById('rating').value;
    const testimonialText = document.getElementById('testimonial').value;
    
    if (rating === '0') {
        alert('Por favor, selecione uma avaliação.');
        return;
    }
    
    // Create new testimonial object
    const newTestimonial = {
        id: testimonials.length + 1,
        name: name,
        profession: profession,
        testimonial: testimonialText,
        rating: parseInt(rating),
        avatar: name.split(' ').map(n => n[0]).join('').toUpperCase()
    };
    
    // Add to testimonials array
    testimonials.unshift(newTestimonial);
    
    // Update display
    displayTestimonials();
    
    // Reset form
    this.reset();
    ratingInput.value = '0';
    ratingStars.forEach(star => {
        star.classList.remove('active');
        star.style.color = '#555';
    });
    
    // Show success message
    alert('Obrigado pelo seu depoimento! Ele será revisado e em breve aparecerá em nossa página.');
});

// Initialize testimonials on page load
document.addEventListener('DOMContentLoaded', displayTestimonials);