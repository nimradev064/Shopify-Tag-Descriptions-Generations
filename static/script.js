// static/script.js

function renderCards() {
    fetch('/all-tags/')
    .then(response => response.json())
    .then(products => {
        const container = document.getElementById('card-container');
        products.forEach(product => {
            const cardHTML = `
                <div class="card">
                    <img src="${product.image}" alt="${product.title}">
                    <div class="card-body">
                        <div class="card-title">${product.title}</div>
                        <div class="card-description">${product.description}</div>
                        <div class="card-tags">${product.apps}</div>
                    </div>
                </div>
            `;
            container.innerHTML += cardHTML;
        });
    })
    .catch(error => console.error('Error fetching products:', error));
}

document.addEventListener('DOMContentLoaded', renderCards);
