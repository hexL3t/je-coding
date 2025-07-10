/*
  MAIN.JS
  This file makes the Rock Paper Scissors game work!
  It listens for clicks, picks a CPU move, and shows who wins.
*/

// 1. Grab the important parts of the page so we can change them later
const gameContainer = document.querySelector(".container"),
      userResult = document.querySelector(".user-result img"),
      computerResult = document.querySelector(".computer-result img"),
      result = document.querySelector(".result"),
      optionImages = document.querySelectorAll(".option-img");

// 2. Loop through each option image (rock, paper, scissors)
optionImages.forEach((image, index) => {
  // 3. When one is clicked...
  image.addEventListener("click", (e) => {
    image.classList.add("active"); // Highlight it

        // 14. Make sure the result's are the rock when shaking.
        userResult.src = "images/rock.png";
        computerResult.src = "images/rock.png";
        result.textContent = "Wait...";

         // 4. Remove the highlight from the other options
        optionImages.forEach((image2, index2) => {
            // If this image is NOT the one the user clicked...
            if (index !== index2) {
                // Remove the "active" highlight from that image
                image2.classList.remove("active");
            }
        });

        // 5. Start the game animation (shaking hands!)
        gameContainer.classList.add("start");

        // 6. Wait 2.5 seconds, then show results
        let time = setTimeout(() => {

            // Remove the "start" class after the delay
            gameContainer.classList.remove("start");  // Stop shaking

            // 7. Show the image the player picked
            let imgSrc = e.target.querySelector("img").src;
            // Set the user image to the clicked image option
            userResult.src = imgSrc;
            // 8. Let the computer randomly pick a number (0 to 2)
            let randomNumber = Math.floor(Math.random() * 3);
            // 9. Create a list of image files the computer can pick from
            let computerImages = ["images/rock.png","images/paper.png", 
                                  "images/scissors.png"];
            // Set Computer Images to a random option
            computerResult.src = computerImages[randomNumber];  // Show Computer's pick

             // 10. Get the letter versions of choices: R, P, S
            let computerValue = ["R", "P", "S"][randomNumber];
            // Get the User’s choice as a letter (R, P, S)
            let userValue = ["R", "P", "S"][index];
            // 11. Make a list of all win/draw outcomes
            let outcomes = {
                RR: "Draw",
                RP: "Computer",
                RS: "User",
                PR: "User",
                PP: "Draw",
                PS: "Computer",
                SR: "Computer",
                SP: "User",
                SS: "Draw",
            }
            // 12. Decide who wins by matching choices
            let outcomeValue = outcomes[userValue + computerValue];
            // 13. Show who won or if it's a draw
            result.textContent = userValue == computerValue ? "Match Draw" 
            : `${outcomeValue} Won!!`;
        }, 2500);
    });
});