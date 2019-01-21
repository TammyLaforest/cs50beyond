const questions = [
    {
        question: "What is Athena's favorite animal?",
        options: ["jellyfish", "penguins", "otters"],
        answer: "otters"
    },
    {
        question: "What is 10 + 10?",
        options: ["8", "20", "28", "30"],
        answer: "20"
    }
];

const numquestions = questions.length;
let question_number = 0;
let correct = 0;

 
	document.addEventListener("DOMContentLoaded", () => {
    load_question();
    document.querySelector("#numquestions").innerHTML = numquestions;
    document.querySelector("#correct").innerHTML = correct;

});
 
function load_question() {
    
    document.querySelector("#question").innerHTML = questions[question_number].question;
    const options = document.querySelector("#options");
    options.innerHTML = "";
    document.querySelector("#correct").innerHTML = correct;

    

    // When document is loaded, load first question. 
    // When question_number increments, load a new question
    for (const option of questions[question_number].options) {
        options.innerHTML += `<button class="option">${option}</button>`;
    }

 	// Add listener for click to call function checkCorrect
    document.querySelectorAll(".option").forEach(option => {
        option.onclick = () => {
 
		if (option.innerHTML === questions[question_number].answer) 
		{
			option.style.background = "lightgreen";
			correct++;
		}
		else 
		{
			option.style.background = "red";

		}
		
		question_number++;
		
		if (question_number < numquestions)
		{	
			
			setTimeout(load_question, 1000);

		}
		else
		{
			setTimeout(()=> {document.querySelector("#quizdiv").classList.add("hide");
			document.querySelector("#winword").innerHTML = "You got " + correct + " out of " + numquestions + " right.";}, 1000);
			
		}



}
	  });
};



// If answer correct, increment score

// move to next question after answered

// When game is over, show game over screen displaying final score