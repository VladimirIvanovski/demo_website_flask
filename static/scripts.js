// Get the buttons
const noButton = document.getElementById("no-button");
const yesButton = document.getElementById("yes-button");
const heartsContainer = document.getElementById("hearts-container");

// Function to move the 'No' button to a random position within the viewport
function moveNoButton() {
    // Set the position of the 'No' button to fixed if not already
    if (noButton.style.position !== 'fixed') {
        const buttonRect = noButton.getBoundingClientRect();
        noButton.style.position = 'fixed';
        noButton.style.top = `${buttonRect.top}px`;
        noButton.style.left = `${buttonRect.left}px`;
    }

    // Calculate random positions within the viewport boundaries
    const maxX = window.innerWidth - noButton.offsetWidth;
    const maxY = window.innerHeight - noButton.offsetHeight;

    const randomX = Math.floor(Math.random() * maxX);
    const randomY = Math.floor(Math.random() * maxY);

    // Update the position of the 'No' button
    noButton.style.left = `${randomX}px`;
    noButton.style.top = `${randomY}px`;
}

// Attach event listener for 'No' button to move on hover
noButton.addEventListener("mouseover", () => {
    moveNoButton();
});

// Attach event listener for 'Yes' button
yesButton.addEventListener("click", () => {
    // Update the container to display the desired message
    document.querySelector(".container").innerHTML = `
        <h1 class="thank-you-message">Фала тии мамо  ❤️</h1>
    `;
    createHearts();
});

// Function to create floating hearts
function createHearts() {
    for (let i = 0; i < 30; i++) {
        const heart = document.createElement("div");
        heart.className = "heart";
        heart.style.left = Math.random() * 100 + "vw";
        heart.style.animationDelay = Math.random() * 2 + "s";
        heart.style.backgroundColor = `hsl(${Math.random() * 360}, 70%, 80%)`;
        heartsContainer.appendChild(heart);
        setTimeout(() => heart.remove(), 4000); // Remove hearts after animation
    }
}
