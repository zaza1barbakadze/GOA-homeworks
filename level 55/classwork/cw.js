function checkAge() {
    const firstName = document.getElementById("firstName").value;
    const lastName = document.getElementById("lastName").value;
    const age = parseInt(document.getElementById("age").value, 10);
    const messageElement = document.getElementById("message");

    if (!firstName || !lastName || isNaN(age)) {
        messageElement.textContent = "გთხოვთ შეავსოთ ყველა ველი!";
        messageElement.style.color = "red";
        return;
    }

    if (age >= 18) {
        messageElement.textContent = `გამარჯობა, ${firstName} ${lastName}! თქვენ სრულწლოვანი ხართ.`;
        messageElement.style.color = "green";
    } else {
        messageElement.textContent = "ბოდიში, მაგრამ თქვენ არ შეგიძლიათ ამ პროგრამის გამოყენება.";
        messageElement.style.color = "red";
    }
}