const input = prompt("შეიყვანეთ ტექსტი:");
const x = parseInt(prompt("რამდენჯერ გავიმეორო?"), 10);

if (!isNaN(x) && x > 0) {
    console.log(input.repeat(x));
} else {
    console.log("გთხოვთ შეიყვანოთ პოზიტიური რიცხვი!");
}