let N = parseInt(prompt("შეიყვანეთ რიცხვების რაოდენობა N:"));
let array = [];

for (let i = 0; i < N; i++) {
    let num = parseInt(prompt(`შეიყვანეთ ${i + 1}-ე რიცხვი:`));
    array.push(num);
}

console.log("კენტ ინდექსებზე მყოფი ელემენტები:");
for (let i = 1; i < array.length; i += 2) {
    console.log(array[i]);
}