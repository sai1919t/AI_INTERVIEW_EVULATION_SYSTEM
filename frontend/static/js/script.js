console.log("AI Interview System Loaded");

function startPractice(){
    const loggedIn = "{{ 'true' if logged_in else 'false' }}";

    if(loggedIn === "false"){
        alert("⚠ Please login first!");
    } 
    else {
        window.location.href = "/dashboard";
    }
}