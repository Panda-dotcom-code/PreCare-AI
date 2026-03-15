function calculateRisk(){

let age = document.getElementById("age").value;
let diet = document.getElementById("diet").value;
let activity = document.getElementById("activity").value;
let smoking = document.getElementById("smoking").value;

let diabetes = document.getElementById("diabetes").checked;
let anemia = document.getElementById("anemia").checked;
let cancer = document.getElementById("cancer").checked;
let tb = document.getElementById("tb").checked;

let fatigue = document.getElementById("fatigue").checked;
let weight = document.getElementById("weight").checked;
let cough = document.getElementById("cough").checked;

let score = 0;


/* AGE */

if(age > 45){
score += 20;
}
else if(age > 30){
score += 10;
}


/* DIET */

if(diet === "Poor"){
score += 15;
}
else if(diet === "Moderate"){
score += 8;
}


/* ACTIVITY */

if(activity === "Low"){
score += 15;
}
else if(activity === "Medium"){
score += 7;
}


/* SMOKING */

if(smoking === "Yes"){
score += 20;
}


/* FAMILY HISTORY */

if(diabetes) score += 15;
if(anemia) score += 10;
if(cancer) score += 15;
if(tb) score += 10;


/* SYMPTOMS */

if(fatigue) score += 10;
if(weight) score += 15;
if(cough) score += 10;


/* LIMIT */

if(score > 100){
score = 100;
}


/* RISK LEVEL */

let level = "";

if(score <= 20){
level = "Low";
}
else if(score <= 50){
level = "Moderate";
}
else{
level = "High";
}


/* DISPLAY RESULT */

document.getElementById("riskPercent").innerText = score + "%";
document.getElementById("riskLevel").innerText = level;
let diabetesRisk = score * 0.8;
let anemiaRisk = score * 0.6;
let cancerRisk = score * 0.4;

document.getElementById("diabetesBar").style.width = diabetesRisk + "%";
document.getElementById("anemiaBar").style.width = anemiaRisk + "%";
document.getElementById("cancerBar").style.width = cancerRisk + "%";

}