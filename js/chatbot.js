// Toggle Chat Window

function toggleChat(){

let chat = document.getElementById("chatbot");

if(chat.style.display === "block"){
chat.style.display = "none";
}
else{
chat.style.display = "block";
}

}


// Send user message

function sendMessage(){

let input = document.getElementById("user-input");

let message = input.value;

if(message === "") return;

addMessage("You: " + message);

generateResponse(message.toLowerCase());

input.value = "";

}


// Add message to chat window

function addMessage(text){

let chatWindow = document.getElementById("chat-window");

let p = document.createElement("p");

p.innerText = text;

chatWindow.appendChild(p);

chatWindow.scrollTop = chatWindow.scrollHeight;

}


// Quick buttons

function quickQuestion(question){

addMessage("You: " + question);

generateResponse(question.toLowerCase());

}


// AI Response Generator

function generateResponse(message){

let response = "";


// Diabetes

if(message.includes("diabetes")){

response =
"Diabetes risk is influenced by diet, physical activity, and family history. Maintain a balanced diet, reduce sugar intake, and exercise regularly. Early lifestyle changes can significantly reduce risk. Remember: this information is for awareness only. Consult a healthcare professional for medical advice.";

}


// Anemia

else if(message.includes("anemia")){

response =
"Anemia risk may be linked to poor iron intake or family history. Include iron-rich foods like leafy vegetables, beans, and pulses in your diet. Vitamin C improves iron absorption. Regular hemoglobin tests help early detection.";

}


// Cancer or TB

else if(message.includes("cancer") || message.includes("tb")){

response =
"Cancer and tuberculosis risk can increase with smoking, alcohol use, and family history. Avoid tobacco, maintain a healthy lifestyle, and go for regular medical screenings. Early awareness improves prevention.";

}


// Preventive tips

else if(message.includes("preventive") || message.includes("tips")){

response =
"Preventive health tips: maintain a nutritious diet, stay physically active, avoid smoking and alcohol, maintain healthy weight, and follow regular health checkups.";

}


// Lifestyle

else if(message.includes("lifestyle")){

response =
"Healthy lifestyle habits include daily exercise, balanced meals, good sleep, hydration, and stress management. Small daily improvements can significantly reduce health risks.";

}


// Default response

else{

response =
"I can help explain Diabetes risk, Anemia risk, Cancer/TB risk, lifestyle advice, and preventive tips. Please ask about one of these topics.";

}


addMessage("PreCare Assistant: " + response);

}