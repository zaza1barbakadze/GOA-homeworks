document.addEventListener("DOMContentLoaded", function () {
    const container = document.body;
    
    for (let i = 1; i <= 10; i++) {
        let newDiv = document.createElement("div");
        newDiv.style.width = `${50 * (2 ** i)}px`;
        newDiv.style.height = `${50 * (2 ** i)}px`;
        newDiv.style.background = i % 2 === 0 ? "blue" : "red";
        newDiv.style.margin = "10px";
        newDiv.style.border = "1px solid black";
        
        if (i % 2 === 0) {
            container.appendChild(newDiv);
        } else {
            container.prepend(newDiv);
        }
    }
});
