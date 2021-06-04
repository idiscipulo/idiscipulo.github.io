var list_main_header = ""
var state = "top" //top, faction, list_main

function top_new_list_click() {
    state = "faction"

    document.getElementById("top").style.display = "none";
    document.getElementById("faction").style.display = "block";
}

function faction_hivespawn_drones_click() {
    state = "list_main"

    list_main_header = "=!= HYPERMAW SERVANTS =!=";
    document.getElementById("list_main_header").innerText = list_main_header

    document.getElementById("top").style.display = "none";
    document.getElementById("faction").style.display = "none";
    document.getElementById("list_main").style.display = "block";
}

function faction_walrus_collective_click() {
    state = "list_main"

    list_main_header = "=!= WALRUS COLLECTIVE =!=";
    document.getElementById("list_main_header").innerText = list_main_header

    document.getElementById("top").style.display = "none";
    document.getElementById("faction").style.display = "none";
    document.getElementById("list_main").style.display = "block";
}

function faction_servants_of_luna_click() {
    state = "list_main"

    list_main_header = "=!= SERVANTS OF LUNA =!=";
    document.getElementById("list_main_header").innerText = list_main_header

    document.getElementById("top").style.display = "none";
    document.getElementById("faction").style.display = "none";
    document.getElementById("list_main").style.display = "block";
}

function back_click() {
    if (state == "faction") {
        state = "top"

        document.getElementById("top").style.display = "block";
        document.getElementById("faction").style.display = "none";
        document.getElementById("list_main").style.display = "none"; 
    }else if (state == "list_main") {
        state = "faction"

        document.getElementById("top").style.display = "none";
        document.getElementById("faction").style.display = "block";
        document.getElementById("list_main").style.display = "none"; 
    } 
}