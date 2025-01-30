let blackScreen = confirm("გსურთ შავი ეკრანი?")
let largeText = confirm("გსურთ დიდი ტექსტი?")
let longText = confirm("გსურთ გრძელი ტექსტი?")

let url = "https://example.com?"

if (blackScreen) {
    url += "blackScreen=true&"
}
if (largeText) {
    url += "largeText=true&"
}
if (longText) {
    url += "longText=true&"
}

window.location.href = url