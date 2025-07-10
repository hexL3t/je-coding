// GET to DOM elements
const gameContainer = document.querySelector(".container"),
    userResult = document.querySelector(".user-result img"),
    cpuResult = document.querySelector(".cpu-result img"),
    result = document.querySelector(".result"),
    optionImages = document.querySelectorAll(".option-img");

// console.log(gameContainer, userResult, cpuResult, result,optionImages);

// STEP ELEVEN
// Loop through each image element
optionImages.forEach((image, index) => {
    image.addEventListener("click", (e) => {
        image.classList.add("active");

        // STEP 15
       // userResult.src = "images/rock.png";
        //cpuResult.src = "images/rock.png";
       // result.textContent = "Wait....";

        // Loop through each option image again : STEP 13
       optionImages.forEach((image2, index2) => {
            //If the current index doesn't match the clicked index
            // Remove the "active" class from the other option images
            index !== index2 && image2.classList.remove("active");
        });

        // STEP 13 
        gameContainer.classList.add("start");

        // STEP 12 
        // Set a timeout to delay the result calculation, wrap the below in a timeOut()
        let time = setTimeout(() => {
            // STEP 13
        gameContainer.classList.remove("start");
        
            // STEP 11
        // Get the source of the clicked option image
        let imageSrc =  e.target.querySelector("img").src;
        // Set the user image to the clicked option image
        userResult.src = imageSrc;

        // Generate a random number between 0 and 2
        let randomNumber = Math.floor(Math.random() * 3);
        // Create and array of CPU image options
        let cpuImages = ["images/rock.png", "images/paper.png", "images/scissors.png"];
        // Set the CPU image to a random Option from the array
        cpuResult.src = cpuImages[randomNumber];

        // Assign a letter value to the CPU option (r = rock, p = paper, s = scissors)
        let cpuValue = ["R", "P", "S"][randomNumber];
        // Assign a letter value to the user option (r = rock, p = paper, s = scissors)
        let userValue = ["R", "P", "S"][index];

        // Create an object with all possible outcomes, start with Rock for User!
        let outcomes = {
            RR: "Draw",
            RP: "CPU",
            RS: "User",
            // Add the other outcomes
            PR: "User",
            PP: "Draw",
            PS: "CPU",
            SR: "CPU",
            SP: "User",
            SS: "Draw",
        }

        // Look up the outcome value based on user and CPU options
        let outcomeValue = outcomes[userValue + cpuValue];

        // Display the result
        result.textContent = userValue == cpuValue ? "Match Draw" 
        : `${outcomeValue} Won!!`;
        }, 2500);
    });
});