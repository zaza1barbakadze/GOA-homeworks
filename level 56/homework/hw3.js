let N = parseInt(prompt("შეიყვანეთ რიცხვების რაოდენობა N:"));
let array = [];

for (let i = 0; i < N; i++) {
    let num = parseInt(prompt(`შეიყვანეთ ${i + 1}-ე რიცხვი:`));
    array.push(num);
}

console.log("შებრუნებული თანმიმდევრობით:");
for (let i = array.length - 1; i >= 0; i--) {
    console.log(array[i]);
}