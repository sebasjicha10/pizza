document.addEventListener('DOMContentLoaded', () => {

    // Mobile Menu - False for off, True for on
    let mobile_menu = false

    const hideMobileMenu = () => {
        mobile_menu = false
        document.querySelector("#mobile_nav_menu").style.display = "none";
        document.querySelector("#sandwich_menu").style.opacity = "0.95";
        document.querySelector("body").style.overflow = "scroll";
    }

    const renderMobileMenu = () => {
        mobile_menu = true
        document.querySelector("#mobile_nav_menu").style.display = "initial";
        document.querySelector("#sandwich_menu").style.opacity = "0.5";
        document.querySelector("body").style.overflow = "hidden";
    }

    // Toggle mobile nav menu
    document.querySelector("#sandwich_menu").onclick = () => {
        mobile_menu == false ?
            renderMobileMenu() :
            hideMobileMenu()
    }

    document.querySelectorAll('.menu_link_mobile').forEach(element => {
        element.onclick = () => {
            hideMobileMenu()
        }
    })

    // Regular Pizza Submission
    document.querySelector("#regular_pizza_form").onsubmit = () => {
        const dish = document.querySelector("#main_dish_regular").value
        const extras_selected = document.querySelectorAll("#extras_regular option:checked")
        const extras = Array.from(extras_selected).map(el => el.value).length

        // No toppings validator
        if ((dish == 1 || dish == 2) && extras != 0) {
            alert("Select a different pizza to add toppings")
        } 
        // 1 topping validator
        if ((dish == 3 || dish == 4) && extras != 1) {
            alert("Select 1 topping")
        }
        // 2 toppings validator
        if ((dish == 5 || dish == 6) && extras != 2) {
            alert("Select 2 toppings")
        }
        // 3 toppings validator
        if ((dish == 7 || dish == 8) && extras != 3) {
            alert("Select 3 toppings")
        }
        // Special Pizza Pizza validator
        if ((dish == 9 || dish == 10) && extras != 5) {
            alert("Select 5 toppings")
        }
    }

    // Sicilian Pizza Submission
    document.querySelector("#sicilian_pizza_form").onsubmit = () => {
        const dish = document.querySelector("#main_dish_sicilian").value
        const extras_selected = document.querySelectorAll("#extras_sicilian option:checked")
        const extras = Array.from(extras_selected).map(el => el.value).length

        // No toppings validator
        if ((dish == 11 || dish == 12) && extras != 0) {
            alert("Select a different pizza to add toppings")
        } 
        // 1 topping validator
        if ((dish == 13 || dish == 14) && extras != 1) {
            alert("Select 1 topping")
        }
        // 2 toppings validator
        if ((dish == 15 || dish == 16) && extras != 2) {
            alert("Select 2 toppings")
        }
        // 3 toppings validator
        if ((dish == 17 || dish == 18) && extras != 3) {
            alert("Select 3 toppings")
        }
        // Special Pizza Pizza validator
        if ((dish == 19 || dish == 20) && extras != 5) {
            alert("Select 5 toppings")
        }
    }

    // Select Multiple Extras Regular 
    document.querySelector("#extras_regular").onclick = () => {
        document.querySelector("#extras_regular").size = "6"
        document.querySelector("#control_command_regular").innerHTML = "Hold down the Ctrl (windows) or Command (Mac) button to select multiple options."
    
    }
    
    // Select Multiple Extras Sicilian 
    document.querySelector("#extras_sicilian").onclick = () => {
        document.querySelector("#extras_sicilian").size = "6"
        document.querySelector("#control_command_sicilian").innerHTML = "Hold down the Ctrl (windows) or Command (Mac) button to select multiple options."
    }

    // Select Multiple Extras Subs 
    document.querySelector("#extras_sub").onclick = () => {
        document.querySelector("#extras_sub").size = "4"
        document.querySelector("#control_command_subs").innerHTML = "Hold down the Ctrl (windows) or Command (Mac) button to select multiple options."
    }
})

