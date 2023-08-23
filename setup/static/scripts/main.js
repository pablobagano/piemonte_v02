// When the user clicks on the button, toggle between hiding and showing the dropdown content
function menu() {
    var dropdown = document.getElementById("myDropdown");
    dropdown.classList.toggle("show");
};

// Close the dropdown menu if the user clicks outside of it
window.onclick = function (event) {
    if (!event.target.matches('.menu-btn')) {
        var dropdowns = document.getElementsByClassName("dropdownContent");
        for (var i = 0; i < dropdowns.length; i++) {
            var openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('show')) {
                openDropdown.classList.remove('show');
            }
        }
    }
};

document.addEventListener("DOMContentLoaded", function() {
    var contactButton = document.getElementById("contato");

    contactButton.addEventListener("click", function() {
        window.location.href = "{url 'contato'}";
    });
})
