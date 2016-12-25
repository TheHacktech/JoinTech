$("body").backstretch("/assets/img/moles-01-01.png");

var error = false;
function updatePage(data) {
    if(data.split(" ")[0] === "Thank") { // register success
        document.getElementById("form").innerHTML = '<div id="success" class="label" style="border: 2px; width: 95%">'+data+'</div>';
        $("html, body").animate({ scrollTop: 0 }, "slow");
    } else { // register failure
        if(error === false) {
            document.getElementById("registerForm").innerHTML = '<div><div id="failure" class="label" style="border: 2px; width: 95%; margin-bottom: 6px; margin-top: -6px">'+data+'</div></div>' +
                document.getElementById("registerForm").innerHTML; 
            error = true;
        } else {
            document.getElementById("failure").innerHTML = data;
        }
        $("html, body").animate({ scrollTop: 0 }, "slow");
        $("#failure").addClass("failure_flash");
    }
}

function constrain(amt, low, high){
    if(amt < low || amt === null){
        amt = low;
    } else if(amt > high){
        amt = high;
    }
    return amt;
}

function nonneg(amt){
    if(amt < 0 || amt === null){
        amt = 0;
    }
    return amt;
}

function validateEmail(email) {
    var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(email);
}

function validate_form() {
    if(document.getElementById("fname").value.length < 1 || document.getElementById("fname").value.length > 120) {
        updatePage("Your first name is invalid. Check your input and try again.");
        return false;
    }
    if(document.getElementById("lname").value.length < 1 || document.getElementById("lname").value.length > 120) {
        updatePage("Your last name is invalid. Check your input and try again.");
        return false;
    }
    if(document.getElementById("email").value.length < 6 || document.getElementById("email").value.length > 120 || validateEmail(document.getElementById("email").value) === false) {
        updatePage("Your email address is invalid. Check your input and try again.");
        return false;
    }
    if(document.getElementById("gradeDrop").value === "default" || (document.getElementById("gradeDrop").value === "other" && document.getElementById("formTextGrade").value.length < 1)) {
        updatePage("Your grade is invalid. Check your input and try again.");
        return false;
    }
    if(document.getElementById("school").value.length < 1) {
        updatePage("Your school is invalid. Check your input and try again.");
        return false;
    }
    if(document.getElementById("formSelectBus").value === "default") {
        updatePage("Your selected bus is invalid. Check your input and try again.\nIf you don't need or want a bus, select 'No Bus Needed'.");
        return false;
    }
    if(document.getElementById("poem").value.length < 1) {
        updatePage("Your acrostic poem is invalid. Check your input and try again.");
        return false;
    }
    if(document.getElementById("techsimplify").value.length < 1) {
        updatePage("Your response to the second free-response question is invalid. Check your input and try again.");
        return false;
    }
    if(document.getElementById("hacktechsuggest").value.length < 1) {
        updatePage("Your input for what you'd like to see at Hacktech is invalid. Check your input and try again.");
        return false;
    }
    if(document.getElementById("accept_tos").checked === false) {
        updatePage("You must accept the MLH Code of Conduct to participate at Hacktech.");
        return false;
    }
    return true;
}

var frm = $('#registerForm');
frm.submit(function (ev) {
    if(validate_form() === true) {
        $.ajax({
            type: frm.attr('method'),
            url: frm.attr('action'),
            data: new FormData(this),
            //data: frm.serialize(),
            cache: false,
            contentType: false,
            processData: false,
            success: function (data) {
                updatePage(data);
            }
        });
    }
    ev.preventDefault();
});

function checkOther() {
    if(document.getElementById('gradeDrop').value==="other") {
        document.getElementById('gradeDrop').name = "gradeSelect";
        document.getElementById('formTextGrade').name = "grade";
        document.getElementById('formTextGrade').style="width: 30%";
        document.getElementById('gradeDrop').style="width: 30%";
        document.getElementById('school').style="width: 30%";
    } else {
        document.getElementById('gradeDrop').name = "grade";
        document.getElementById('formTextGrade').name = "gradeOther";
        document.getElementById('formTextGrade').style="display: none;";
        document.getElementById('gradeDrop').style="width: 45%";
        document.getElementById('school').style="width: 45%";
    }
}

function uploadResume() {
    document.getElementById("resumefileinput").click();
}

function updateBtnTxt() {
    var name = document.getElementById("resumefileinput").files[0].name;
    document.getElementById("resumeUploadBtn").innerHTML = document.getElementById("resumefileinput").files[0].name;
}
