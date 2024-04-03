
var currentTab = 0;
document.addEventListener("DOMContentLoaded", function () { 
    showTab(getCurrentTab());
});

function getCurrentTab() {
    // Get all steps
    let steps = document.querySelectorAll(".step");
    // Iterate through steps to find the one with the 'active' class
    for (let i = 0; i < steps.length; i++) {
        if (steps[i].classList.contains("active")) {
            return i;
        }
    }
    // Return 0 if no step has the 'active' class (default to first step)
    return 0;
}
function showTab(n) {
    // Get all steps
    let x = document.getElementsByClassName("step");
    if (x.length > 0) {
        // Hide all steps
        for (let i = 0; i < x.length; i++) {
            x[i].style.display = "none";
        }
        // Show the current step
        x[n].style.display = "block";
        // Update Previous/Next buttons and progress bar indicators
        let prevBtn = document.getElementById("prevBtn");
        let nextBtn = document.getElementById("nextBtn");
        if (n === 0) {
            prevBtn.style.display = "none";
        } else {
            prevBtn.style.display = "inline";
        }
        if (n === x.length - 1) {
            nextBtn.innerHTML = "Submit";
        } else {
            nextBtn.innerHTML = "Next";
        }
        // Update step indicator classes
        let steps = document.querySelectorAll(".steps");
        for (let j = 0; j < steps.length; j++) {
            if (j < n) {
                steps[j].classList.add("finish");
                steps[j].classList.remove("active");
            } else if (j === n) {
                steps[j].classList.add("active");
                steps[j].classList.remove("finish");
            } else {
                steps[j].classList.remove("active");
                steps[j].classList.remove("finish");
            }
        }
    }
}

function nextPrev(n) {
    // This function will figure out which tab to display
    let x = document.getElementsByClassName("step");
    // Exit the function if any field in the current tab is invalid:
    if (n == 1 && !validateForm()) return false;
    // Hide the current tab:
    x[currentTab].style.display = "none";
    // Increase or decrease the current tab by 1:
    currentTab = currentTab + n;
    // if you have reached the end of the form...
    if (currentTab >= x.length) {
        // ... the form gets submitted:
       // document.getElementById("msform").submit();
        window.location.href = "officalAccount";
        return false;
    }
    // Otherwise, display the correct tab:
    showTab(currentTab);
}

function validateForm() {
    // This function deals with validation of the form fields
    let x, y, i, valid = true;
    x = document.getElementsByClassName("step");
    y = x[currentTab].getElementsByTagName("input");
    // A loop that checks every input field in the current tab:
    for (i = 0; i < y.length; i++) {
        // If a field is empty...
        if (y[i].value == "") {
            // add an "invalid" class to the field:
            y[i].className += " invalid";
            // and set the current valid status to false
            valid = false;
        }
    }
      // If the valid status is true, mark the step as finished and valid:
      if (valid) {
        document.getElementsByClassName("steps")[currentTab].className += " finish";
    }
    return valid; // return the valid status
}
function fixStepIndicator(n) {
    // This function removes the "active" class of all steps...
    let i, x = document.getElementsByClassName("steps");
    for (i = 0; i < x.length; i++) {
        x[i].className = x[i].className.replace(" active", "");
    }
    //... and adds the "active" class on the current step:
    x[n].className += " active";
}
